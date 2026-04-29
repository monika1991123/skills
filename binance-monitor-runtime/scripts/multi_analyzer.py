#!/usr/bin/env python3
"""多币种评分分析（精简版）"""

import json
import sys
from pathlib import Path
from datetime import datetime, timedelta

class Analyzer:
    def __init__(self, data_dir: Path):
        self.data_dir = data_dir
        self.hist_file = data_dir / "multi_snapshot_history.jsonl"

    def load_recent_snapshots(self, hours=24, limit=None):
        """加载最近 N 小时快照"""
        if not self.hist_file.exists():
            return []
        
        snapshots, cutoff = [], datetime.utcnow() - timedelta(hours=hours)
        with open(self.hist_file) as f:
            for line in f:
                try:
                    s = json.loads(line)
                    t = datetime.fromisoformat(s['timestamp'].replace('Z', '+00:00'))
                    if t >= cutoff:
                        snapshots.append(s)
                except:
                    pass
        return snapshots[-limit:] if limit else snapshots

    def calc_scores(self, sym, curr, snaps):
        """计算单币种评分"""
        c24h = curr.get('change_24h_pct', 0)
        c4h = curr.get('change_4h_pct', 0)
        oi = curr.get('oi_usdt', 0)
        vol = curr.get('volume_24h', 0)
        whale_net = curr.get('whale_net', 0)
        
        # 简单打分：动能25% + 共振25% + 成交量20% + 大户20% + 波动10%
        momentum = 50 + (c24h + c4h) / 2 * 5
        momentum = max(0, min(100, momentum))
        
        # OI共振：最近快照对比
        resonance = 50
        if len(snaps) >= 2:
            prev_oi = snaps[-2].get('symbols', {}).get(sym, {}).get('oi_usdt', 0)
            if prev_oi > 0 and oi > 0:
                oi_chg = (oi - prev_oi) / prev_oi
                price_chg = (curr.get('price', 0) - snaps[-2].get('symbols', {}).get(sym, {}).get('price', 1)) / snaps[-2].get('symbols', {}).get(sym, {}).get('price', 1)
                if oi_chg > 0 and price_chg > 0:
                    resonance = 50 + min(50, (oi_chg + abs(price_chg)) / 2 * 100)
        
        # 成交量倍数
        vol_score = 50
        if len(snaps) >= 2:
            avg_vol = sum(s.get('symbols', {}).get(sym, {}).get('volume_24h', 0) for s in snaps[:-1]) / (len(snaps)-1)
            if avg_vol > 0:
                ratio = vol / avg_vol
                vol_score = 50 + min(50, (ratio - 1) * 33)
        
        # 大户反手
        whale_score = 50 + abs(whale_net) * 100
        whale_score = max(0, min(100, whale_score))
        
        # 波动率
        volatility = 50 + min(50, abs(c24h) * 5)
        
        # 加权综合
        composite = (momentum * 0.25 + resonance * 0.25 + vol_score * 0.20 +
                     whale_score * 0.20 + volatility * 0.10)
        
        return {
            'composite_score': round(composite, 1),
            'momentum_score': round(momentum, 1),
            'resonance_score': round(resonance, 1),
            'volume_score': round(vol_score, 1),
            'whale_score': round(whale_score, 1),
            'volatility_score': round(volatility, 1)
        }

    def run(self):
        latest = self.data_dir / "multi_snapshot_latest.json"
        if not latest.exists():
            return {"error": "无最新快照"}
        
        snap = json.loads(latest.read_text())
        snaps = self.load_recent_snapshots(limit=24)
        if not snaps:
            snaps = [snap]
        
        report = {
            'generated_at': datetime.utcnow().isoformat() + 'Z',
            'snapshot_time': snap['timestamp'],
            'symbols': {}
        }
        
        for sym, data in snap.get('symbols', {}).items():
            scores = self.calc_scores(sym, data, snaps)
            report['symbols'][sym] = {
                'price': data.get('price'),
                'change_24h_pct': data.get('change_24h_pct'),
                'change_4h_pct': data.get('change_4h_pct'),
                'oi_usdt': data.get('oi_usdt'),
                'volume_24h': data.get('volume_24h'),
                'whale_long_ratio': data.get('whale_long_ratio'),
                'whale_short_ratio': data.get('whale_short_ratio'),
                **scores
            }
        
        ranked = sorted(report['symbols'].items(),
                       key=lambda x: x[1]['composite_score'], reverse=True)
        report['ranking'] = [{
            'rank': i+1, 'symbol': sym,
            'score': data['composite_score'],
            'change_24h': data['change_24h_pct'],
            'price': data['price']
        } for i, (sym, data) in enumerate(ranked)]
        
        return report

if __name__ == "__main__":
    data_dir = Path(__file__).parent.parent / "data"
    analyzer = Analyzer(data_dir)
    report = analyzer.run()
    
    report_file = data_dir / "analysis_report_latest.json"
    report_file.parent.mkdir(parents=True, exist_ok=True)
    report_file.write_text(json.dumps(report, indent=2, ensure_ascii=False) + '\n')
    
    print(json.dumps(report, indent=2, ensure_ascii=False))
