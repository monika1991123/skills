# Hermes Skills 全量索引与使用指引

这个文档用于汇总 `/home/ubuntu/.hermes/skills` 下 **全部已安装 skills**，包括 `ecc-imports` 子目录中的扩展 skills。

它的目标不是替代每个 skill 自己的 `SKILL.md`，而是提供：

- 快速总览：当前到底装了哪些 skills
- 分类导航：不同任务该先看哪一组
- 触发提示：什么时候应该优先加载某个 skill
- 路径索引：方便你直接去对应目录查看源码或文档

---

## 一、总览

- **Skills 总数**: 332
- **分类数**: 26
- **包含 `ecc-imports`**: 是（共 184 个）
- **索引范围**: 仅统计存在 `SKILL.md` 的技能目录

### 建议使用方式

1. **先按任务类型找分类**：比如开发、研究、文档、OKX、创意。
2. **再看 skill 名和简述**：确定最贴近当前任务的 skill。
3. **最后打开对应 `SKILL.md`**：看完整 workflow、命令、限制和注意事项。

---

## 二、分类目录

- [根目录通用 Skills](#根目录通用-skills)（43）
- [软件开发与调试](#软件开发与调试)（8）
- [OKX 交易与链上操作](#okx-交易与链上操作)（21）
- [创意与设计](#创意与设计)（19）
- [办公与生产力](#办公与生产力)（8）
- [GitHub 工作流](#github-工作流)（6）
- [研究与信息检索](#研究与信息检索)（5）
- [自治代理与多代理](#自治代理与多代理)（4）
- [DevOps 与自动化](#devops-与自动化)（3）
- [MCP 集成](#mcp-集成)（1）
- [媒体与音视频](#媒体与音视频)（5）
- [Apple 生态](#apple-生态)（4）
- [邮件](#邮件)（1）
- [社交媒体](#社交媒体)（1）
- [笔记与知识库](#笔记与知识库)（1）
- [智能家居](#智能家居)（1）
- [数据科学](#数据科学)（1）
- [游戏相关](#游戏相关)（2）
- [MLOps 与模型工程](#mlops-与模型工程)（1）
- [安全对抗](#安全对抗)（1）
- [ECC Imports 扩展技能库](#ecc-imports-扩展技能库)（184）
- [mlops/evaluation](#mlopsevaluation)（2）
- [mlops/inference](#mlopsinference)（4）
- [mlops/models](#mlopsmodels)（2）
- [mlops/research](#mlopsresearch)（1）
- [mlops/training](#mlopstraining)（3）

---

## 三、核心优先级建议

如果你不确定先看哪个 skill，可以优先从下面这些“高频入口”开始：

- **通用入口**：`using-superpowers`、`writing-skills`、`verification-before-completion`
- **开发流程**：`brainstorming` → `writing-plans` / `plan` → `test-driven-development` → `systematic-debugging`
- **多代理/自动化**：`dispatching-parallel-agents`、`subagent-driven-development`、`hermes-agent`
- **文档与办公**：`docx`、`pdf`、`pptx`、`xlsx`、`google-workspace`、`notion`
- **加密与交易**：`surf`、`crypto-market`、`binance-readonly`、`okx-*` 系列
- **研究检索**：`arxiv`、`blogwatcher`、`llm-wiki`、`summarize`

---

## 四、全量 Skills 索引

## 根目录通用 Skills

> 根目录通常放的是高频通用 skills，很多会作为默认工作流入口。

### 1. `algorithmic-art`
- **标题**: algorithmic-art
- **路径**: `algorithmic-art/SKILL.md`
- **用途**: Creating algorithmic art using p5.js with seeded randomness and interactive parameter exploration. Use this when users request creating art using code, gener...

### 2. `binance-funding-monitor`
- **标题**: Binance Funding Monitor
- **路径**: `binance-funding-monitor/SKILL.md`
- **用途**: monitor binance usdⓈ-m usdt perpetual funding rates and present a sorted watchlist when the user asks to check funding, rank symbols below a threshold, compa...

### 3. `binance-monitor-runtime`
- **标题**: Binance Monitor Runtime
- **路径**: `binance-monitor-runtime/SKILL.md`
- **用途**: Binance USDⓈ-M USDT 永续合约市场监控运行时 - 自动扫描价格、资金费、成交量异常，生成评分报告并推送 Telegram

### 4. `binance-readonly`
- **标题**: Binance Read-Only
- **路径**: `binance-readonly/SKILL.md`
- **用途**: Use installed Binance tooling for read-only market/account research. Activate when the user asks for Binance prices, klines, order book, balances, open order...

### 5. `brainstorming`
- **标题**: Brainstorming Ideas Into Designs
- **路径**: `brainstorming/SKILL.md`
- **用途**: You MUST use this before any creative work - creating features, building components, adding functionality, or modifying behavior. Explores user intent, requi...

### 6. `brand-guidelines`
- **标题**: Anthropic Brand Styling
- **路径**: `brand-guidelines/SKILL.md`
- **用途**: Applies Anthropic's official brand colors and typography to any sort of artifact that may benefit from having Anthropic's look-and-feel. Use it when brand co...

### 7. `canvas-design`
- **标题**: canvas-design
- **路径**: `canvas-design/SKILL.md`
- **用途**: Create beautiful visual art in .png and .pdf documents using design philosophy. You should use this skill when the user asks to create a poster, piece of art...

### 8. `code-simplifier`
- **标题**: code-simplifier
- **路径**: `code-simplifier/SKILL.md`
- **用途**: Simplifies and refines code for clarity, consistency, and maintainability while preserving all functionality. Focuses on recently modified code unless instru...

### 9. `crypto-market`
- **标题**: Crypto Market Research
- **路径**: `crypto-market/SKILL.md`
- **用途**: Use installed crypto market tooling for general market research, trend checks, and historical price analysis. Activate when the user asks for crypto prices,...

### 10. `dispatching-parallel-agents`
- **标题**: Dispatching Parallel Agents
- **路径**: `dispatching-parallel-agents/SKILL.md`
- **用途**: 适用于：facing 2+ independent tasks that can be worked on without shared state or sequential dependencies

### 11. `doc-coauthoring`
- **标题**: Doc Co-Authoring Workflow
- **路径**: `doc-coauthoring/SKILL.md`
- **用途**: Guide users through a structured workflow for co-authoring documentation. Use when user wants to write documentation, proposals, technical specs, decision do...

### 12. `docx`
- **标题**: DOCX creation, editing, and analysis
- **路径**: `docx/SKILL.md`
- **用途**: Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files). Triggers include: any mention of 'Word doc', 'word...

### 13. `dogfood`
- **标题**: Dogfood: Systematic Web Application QA Testing
- **路径**: `dogfood/SKILL.md`
- **用途**: Exploratory QA of web apps: find bugs, evidence, reports.

### 14. `executing-plans`
- **标题**: Executing Plans
- **路径**: `executing-plans/SKILL.md`
- **用途**: 适用于：you have a written implementation plan to execute in a separate session with review checkpoints

### 15. `find-skills`
- **标题**: Find Skills Skill
- **路径**: `find-skills/SKILL.md`
- **用途**: Search and discover OpenClaw skills from various sources. Use when: user wants to find available skills, search for specific functionality, or discover new s...

### 16. `finishing-a-development-branch`
- **标题**: Finishing a Development Branch
- **路径**: `finishing-a-development-branch/SKILL.md`
- **用途**: 适用于：implementation is complete, all tests pass, and you need to decide how to integrate the work - guides completion of development work by presenting struct...

### 17. `frontend-design`
- **标题**: frontend-design
- **路径**: `frontend-design/SKILL.md`
- **用途**: Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, or appli...

### 18. `github`
- **标题**: GitHub Skill
- **路径**: `github/SKILL.md`
- **用途**: Interact with GitHub using the `gh` CLI. Use `gh issue`, `gh pr`, `gh run`, and `gh api` for issues, PRs, CI runs, and advanced queries.

### 19. `internal-comms`
- **标题**: internal-comms
- **路径**: `internal-comms/SKILL.md`
- **用途**: A set of resources to help me write all kinds of internal communications, using the formats that my company likes to use. Claude should use this skill whenev...

### 20. `mcp-builder`
- **标题**: MCP Server Development Guide
- **路径**: `mcp-builder/SKILL.md`
- **用途**: Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. Use whe...

### 21. `notebooklm-skill`
- **标题**: NotebookLM Research Assistant Skill
- **路径**: `notebooklm-skill/SKILL.md`
- **用途**: Use this skill to query your Google NotebookLM notebooks directly from Claude Code for source-grounded, citation-backed answers from Gemini. Browser automati...

### 22. `openclaw-backup`
- **标题**: OpenClaw Backup
- **路径**: `openclaw-backup/SKILL.md`
- **用途**: Backup and restore OpenClaw data. Use when user asks to create backups, set up automatic backup schedules, restore from backup, or manage backup rotation. Ha...

### 23. `pdf`
- **标题**: PDF Processing Guide
- **路径**: `pdf/SKILL.md`
- **用途**: Use this skill whenever the user wants to do anything with PDF files. This includes reading or extracting text/tables from PDFs, combining or merging multipl...

### 24. `planning-with-files`
- **标题**: Planning with Files
- **路径**: `planning-with-files/SKILL.md`
- **用途**: Implements Manus-style file-based planning to organize and track progress on complex tasks. Creates task_plan.md, findings.md, and progress.md. Use when aske...

### 25. `playwright-mcp`
- **标题**: Playwright MCP Skill
- **路径**: `playwright-mcp/SKILL.md`
- **用途**: Browser automation via Playwright MCP server. Navigate websites, click elements, fill forms, extract data, take screenshots, and perform full browser automat...

### 26. `pptx`
- **标题**: PPTX Skill
- **路径**: `pptx/SKILL.md`
- **用途**: Use this skill any time a .pptx file is involved in any way — as input, output, or both. This includes: creating slide decks, pitch decks, or presentations;...

### 27. `receiving-code-review`
- **标题**: Code Review Reception
- **路径**: `receiving-code-review/SKILL.md`
- **用途**: 适用于：receiving code review feedback, before implementing suggestions, especially if feedback seems unclear or technically questionable - requires technical ri...

### 28. `self-improving`
- **标题**: self-improving
- **路径**: `self-improving/SKILL.md`
- **用途**: Self-reflection + Self-criticism + Self-learning + Self-organizing memory. Agent evaluates its own work, catches mistakes, and improves permanently. Use when...

### 29. `skill-creator`
- **标题**: Skill Creator
- **路径**: `skill-creator/SKILL.md`
- **用途**: Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, update or optimize...

### 30. `slack-gif-creator`
- **标题**: Slack GIF Creator
- **路径**: `slack-gif-creator/SKILL.md`
- **用途**: Knowledge and utilities for creating animated GIFs optimized for Slack. Provides constraints, validation tools, and animation concepts. Use when users reques...

### 31. `summarize`
- **标题**: Summarize
- **路径**: `summarize/SKILL.md`
- **用途**: Summarize URLs or files with the summarize CLI (web, PDFs, images, audio, YouTube).

### 32. `surf`
- **标题**: Surf — One Skill, All Crypto Data
- **路径**: `surf/SKILL.md`
- **用途**: 暂无 frontmatter 描述，建议直接查看该 skill 的 SKILL.md 获取完整用法。

### 33. `systematic-debugging`
- **标题**: Systematic Debugging
- **路径**: `systematic-debugging/SKILL.md`
- **用途**: 适用于：encountering any bug, test failure, or unexpected behavior, before proposing fixes

### 34. `test-driven-development`
- **标题**: Test-Driven Development (TDD)
- **路径**: `test-driven-development/SKILL.md`
- **用途**: 适用于：implementing any feature or bugfix, before writing implementation code

### 35. `theme-factory`
- **标题**: Theme Factory Skill
- **路径**: `theme-factory/SKILL.md`
- **用途**: Toolkit for styling artifacts with a theme. These artifacts can be slides, docs, reportings, HTML landing pages, etc. There are 10 pre-set themes with colors...

### 36. `using-git-worktrees`
- **标题**: Using Git Worktrees
- **路径**: `using-git-worktrees/SKILL.md`
- **用途**: 适用于：starting feature work that needs isolation from current workspace or before executing implementation plans - creates isolated git worktrees with smart di...

### 37. `using-superpowers`
- **标题**: Using Skills
- **路径**: `using-superpowers/SKILL.md`
- **用途**: 适用于：starting any conversation - establishes how to find and use skills, requiring Skill tool invocation before ANY response including clarifying questions

### 38. `verification-before-completion`
- **标题**: Verification Before Completion
- **路径**: `verification-before-completion/SKILL.md`
- **用途**: 适用于：about to claim work is complete, fixed, or passing, before committing or creating PRs - requires running verification commands and confirming output befo...

### 39. `web-artifacts-builder`
- **标题**: Web Artifacts Builder
- **路径**: `web-artifacts-builder/SKILL.md`
- **用途**: Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui). Use...

### 40. `webapp-testing`
- **标题**: Web Application Testing
- **路径**: `webapp-testing/SKILL.md`
- **用途**: Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend functionality, debugging UI behavior, capturing...

### 41. `writing-skills`
- **标题**: Writing Skills
- **路径**: `writing-skills/SKILL.md`
- **用途**: 适用于：creating new skills, editing existing skills, or verifying skills work before deployment

### 42. `xlsx`
- **标题**: Requirements for Outputs
- **路径**: `xlsx/SKILL.md`
- **用途**: Use this skill any time a spreadsheet file is the primary input or output. This means any task where the user wants to: open, read, edit, or fix an existing...

### 43. `yuanbao`
- **标题**: Yuanbao Group Interaction
- **路径**: `yuanbao/SKILL.md`
- **用途**: Yuanbao (元宝) groups: @mention users, query info/members.

---

## 软件开发与调试

> 这一组偏“工程工作流增强版”，适合计划、调试、实验和 repo 内开发。

### 1. `debugging-hermes-tui-commands`
- **标题**: Debugging Hermes TUI Slash Commands
- **路径**: `software-development/debugging-hermes-tui-commands/SKILL.md`
- **用途**: Debug Hermes TUI slash commands: Python, gateway, Ink UI.

### 2. `hermes-agent-skill-authoring`
- **标题**: Authoring Hermes-Agent Skills (in-repo)
- **路径**: `software-development/hermes-agent-skill-authoring/SKILL.md`
- **用途**: Author in-repo SKILL.md: frontmatter, validator, structure.

### 3. `node-inspect-debugger`
- **标题**: Node.js Inspect Debugger
- **路径**: `software-development/node-inspect-debugger/SKILL.md`
- **用途**: Debug Node.js via --inspect + Chrome DevTools Protocol CLI.

### 4. `plan`
- **标题**: Plan Mode
- **路径**: `software-development/plan/SKILL.md`
- **用途**: Plan mode: write markdown plan to .hermes/plans/, no exec.

### 5. `python-debugpy`
- **标题**: Python Debugger (pdb + debugpy)
- **路径**: `software-development/python-debugpy/SKILL.md`
- **用途**: Debug Python: pdb REPL + debugpy remote (DAP).

### 6. `spike`
- **标题**: Spike
- **路径**: `software-development/spike/SKILL.md`
- **用途**: Throwaway experiments to validate an idea before build.

### 7. `subagent-driven-development`
- **标题**: Subagent-Driven Development
- **路径**: `software-development/subagent-driven-development/SKILL.md`
- **用途**: Execute plans via delegate_task subagents (2-stage review).

### 8. `writing-plans`
- **标题**: Writing Implementation Plans
- **路径**: `software-development/writing-plans/SKILL.md`
- **用途**: Write implementation plans: bite-sized tasks, paths, code.

---

## OKX 交易与链上操作

### 1. `okx-agentic-wallet`
- **标题**: Onchain OS Wallet
- **路径**: `okx/okx-agentic-wallet/SKILL.md`
- **用途**: AUTHORITATIVE source for OKX Agentic Wallet and its Gas Station feature. Gas Station = OKX's stablecoin-gas feature via EIP-7702 + third-party Relayer — NOT...

### 2. `okx-audit-log`
- **标题**: Onchain OS Audit Log
- **路径**: `okx/okx-audit-log/SKILL.md`
- **用途**: Use this skill when the user asks to export audit logs, find audit log location, view command history, 导出日志, 查看日志, 日志路径, 操作记录, 调用记录, 命令历史. Do NOT use for wal...

### 3. `okx-cex-bot`
- **标题**: OKX CEX Bot Trading
- **路径**: `okx/okx-cex-bot/SKILL.md`
- **用途**: Manage Grid bots (spot/contract/coin-margined) and DCA Martingale bots (Spot DCA 现货马丁 / Contract DCA 合约马丁) on OKX. Covers create, stop, amend, monitor P&L, T...

### 4. `okx-cex-earn`
- **标题**: OKX CEX Earn CLI
- **路径**: `okx/okx-cex-earn/SKILL.md`
- **用途**: Manages OKX Simple Earn (flexible savings/lending), Flash Earn, On-chain Earn (staking/DeFi), Dual Investment (DCD/双币赢), and AutoEarn (自动赚币) via the okx CLI....

### 5. `okx-cex-market`
- **标题**: OKX CEX Market Data CLI
- **路径**: `okx/okx-cex-market/SKILL.md`
- **用途**: Use this skill when the user asks for: price of any asset, ticker, order book, market depth, candles, OHLCV, funding rate, open interest, open interest histo...

### 6. `okx-cex-portfolio`
- **标题**: OKX CEX Portfolio & Account CLI
- **路径**: `okx/okx-cex-portfolio/SKILL.md`
- **用途**: This skill should be used when the user asks about 'account balance', 'how much USDT do I have', 'my funding account', 'show my positions', 'open positions',...

### 7. `okx-cex-skill-mp`
- **标题**: OKX Skills Marketplace
- **路径**: `okx/okx-cex-skill-mp/SKILL.md`
- **用途**: Use this skill when the user asks to: 'find a trading skill', 'search for skills', 'install a skill', 'add a skill', 'download a skill', 'browse skill market...

### 8. `okx-cex-trade`
- **标题**: OKX CEX Trading CLI
- **路径**: `okx/okx-cex-trade/SKILL.md`
- **用途**: This skill should be used when the user asks to 'buy BTC', 'sell ETH', 'place a limit order', 'place a market order', 'cancel my order', 'amend my order', 'l...

### 9. `okx-defi-invest`
- **标题**: OKX DeFi Invest
- **路径**: `okx/okx-defi-invest/SKILL.md`
- **用途**: Use this skill to 'invest in DeFi', 'earn yield on USDC', 'deposit into Aave', 'stake ETH on Lido', 'search DeFi products', 'find best APY', 'redeem my DeFi...

### 10. `okx-defi-portfolio`
- **标题**: OKX DeFi Portfolio
- **路径**: `okx/okx-defi-portfolio/SKILL.md`
- **用途**: Use this skill to 'check my DeFi positions', 'view DeFi holdings', 'show my DeFi portfolio', 'what DeFi am I invested in', 'show my staking positions', 'show...

### 11. `okx-dex-market`
- **标题**: Onchain OS DEX Market
- **路径**: `okx/okx-dex-market/SKILL.md`
- **用途**: Use this skill for on-chain market data: token prices/价格, K-line/OHLC charts, index prices, and wallet PnL/盈亏分析 (win rate, my wallet's DEX trade history, rea...

### 12. `okx-dex-signal`
- **标题**: Onchain OS DEX Signal & Leaderboard
- **路径**: `okx/okx-dex-signal/SKILL.md`
- **用途**: Use this skill for smart-money/whale/KOL/大户 activity tracking, aggregated buy signal/信号 alerts, and leaderboard/牛人榜 rankings. Covers: (1) address tracker — r...

### 13. `okx-dex-swap`
- **标题**: Onchain OS DEX Swap
- **路径**: `okx/okx-dex-swap/SKILL.md`
- **用途**: Use this skill to 'swap tokens', 'trade OKB for USDC', 'buy tokens', 'sell tokens', 'exchange crypto', 'convert tokens', 'swap SOL for USDC', 'get a swap quo...

### 14. `okx-dex-token`
- **标题**: Onchain OS DEX Token
- **路径**: `okx/okx-dex-token/SKILL.md`
- **用途**: Use this skill for token-level data: search tokens, trending/hot tokens (热门, 代币榜单), liquidity pools, holder distribution (whale/巨鲸, sniper, bundler-tagged ho...

### 15. `okx-dex-trenches`
- **标题**: Onchain OS DEX Trenches
- **路径**: `okx/okx-dex-trenches/SKILL.md`
- **用途**: Use this skill for meme/打狗/alpha token research on pump.fun and similar launchpads: scanning new token launches, checking developer reputation/开发者信息/dev laun...

### 16. `okx-dex-ws`
- **标题**: Onchain OS DEX WebSocket — Unified Skill
- **路径**: `okx/okx-dex-ws/SKILL.md`
- **用途**: Use this skill when the user mentions 'onchainos ws', 'ws start', 'ws poll', 'ws stop', 'ws channels', 'ws session', 'ws channel-info', 'idle-timeout', 'idle...

### 17. `okx-onchain-gateway`
- **标题**: Onchain OS Gateway
- **路径**: `okx/okx-onchain-gateway/SKILL.md`
- **用途**: Use this skill to 'broadcast transaction', 'send tx', 'estimate gas', 'simulate transaction', 'check tx status', 'track my transaction', 'get gas price', 'ga...

### 18. `okx-security`
- **标题**: Onchain OS Security
- **路径**: `okx/okx-security/SKILL.md`
- **用途**: Use this skill for security scanning: check transaction safety, is this transaction safe, pre-execution check, security scan, token risk scanning, honeypot d...

### 19. `okx-sentiment-tracker`
- **标题**: OKX News & Sentiment
- **路径**: `okx/okx-sentiment-tracker/SKILL.md`
- **用途**: Use this skill when the user asks about: 'any crypto news', 'what happened recently', 'latest news', 'any big news today', 'catch me up', 'market update', 'd...

### 20. `okx-wallet-portfolio`
- **标题**: Onchain OS Portfolio
- **路径**: `okx/okx-wallet-portfolio/SKILL.md`
- **用途**: Use this skill when the user provides a specific wallet address and wants to check its balance, token holdings, portfolio value, or DeFi positions. Typical t...

### 21. `okx-x402-payment`
- **标题**: Onchain OS x402 Payment
- **路径**: `okx/okx-x402-payment/SKILL.md`
- **用途**: This skill should be used when the user encounters an HTTP 402 Payment Required response, wants to pay for a payment-gated API or resource, or mentions 'x402...

---

## 创意与设计

### 1. `architecture-diagram`
- **标题**: Architecture Diagram Skill
- **路径**: `creative/architecture-diagram/SKILL.md`
- **用途**: Dark-themed SVG architecture/cloud/infra diagrams as HTML.

### 2. `ascii-art`
- **标题**: ASCII Art Skill
- **路径**: `creative/ascii-art/SKILL.md`
- **用途**: ASCII art: pyfiglet, cowsay, boxes, image-to-ascii.

### 3. `ascii-video`
- **标题**: ASCII Video Production Pipeline
- **路径**: `creative/ascii-video/SKILL.md`
- **用途**: ASCII video: convert video/audio to colored ASCII MP4/GIF.

### 4. `baoyu-comic`
- **标题**: Knowledge Comic Creator
- **路径**: `creative/baoyu-comic/SKILL.md`
- **用途**: Knowledge comics (知识漫画): educational, biography, tutorial.

### 5. `baoyu-infographic`
- **标题**: Infographic Generator
- **路径**: `creative/baoyu-infographic/SKILL.md`
- **用途**: Infographics: 21 layouts x 21 styles (信息图, 可视化).

### 6. `claude-design`
- **标题**: Claude Design for CLI/API Agents
- **路径**: `creative/claude-design/SKILL.md`
- **用途**: Design one-off HTML artifacts (landing, deck, prototype).

### 7. `comfyui`
- **标题**: ComfyUI
- **路径**: `creative/comfyui/SKILL.md`
- **用途**: Generate images, video, and audio with ComfyUI — install, launch, manage nodes/models, run workflows with parameter injection. Uses the official comfy-cli fo...

### 8. `creative-ideation`
- **标题**: Creative Ideation
- **路径**: `creative/creative-ideation/SKILL.md`
- **用途**: Generate project ideas via creative constraints.

### 9. `design-md`
- **标题**: DESIGN.md Skill
- **路径**: `creative/design-md/SKILL.md`
- **用途**: Author/validate/export Google's DESIGN.md token spec files.

### 10. `excalidraw`
- **标题**: Excalidraw Diagram Skill
- **路径**: `creative/excalidraw/SKILL.md`
- **用途**: Hand-drawn Excalidraw JSON diagrams (arch, flow, seq).

### 11. `humanizer`
- **标题**: Humanizer: Remove AI Writing Patterns
- **路径**: `creative/humanizer/SKILL.md`
- **用途**: Humanize text: strip AI-isms and add real voice.

### 12. `manim-video`
- **标题**: Manim Video Production Pipeline
- **路径**: `creative/manim-video/SKILL.md`
- **用途**: Manim CE animations: 3Blue1Brown math/algo videos.

### 13. `p5js`
- **标题**: p5.js Production Pipeline
- **路径**: `creative/p5js/SKILL.md`
- **用途**: p5.js sketches: gen art, shaders, interactive, 3D.

### 14. `pixel-art`
- **标题**: Pixel Art
- **路径**: `creative/pixel-art/SKILL.md`
- **用途**: Pixel art w/ era palettes (NES, Game Boy, PICO-8).

### 15. `popular-web-designs`
- **标题**: Popular Web Designs
- **路径**: `creative/popular-web-designs/SKILL.md`
- **用途**: 54 real design systems (Stripe, Linear, Vercel) as HTML/CSS.

### 16. `pretext`
- **标题**: Pretext Creative Demos
- **路径**: `creative/pretext/SKILL.md`
- **用途**: 适用于：building creative browser demos with @chenglou/pretext — DOM-free text layout for ASCII art, typographic flow around obstacles, text-as-geometry games, k...

### 17. `sketch`
- **标题**: Sketch
- **路径**: `creative/sketch/SKILL.md`
- **用途**: Throwaway HTML mockups: 2-3 design variants to compare.

### 18. `songwriting-and-ai-music`
- **标题**: Songwriting & AI Music Generation
- **路径**: `creative/songwriting-and-ai-music/SKILL.md`
- **用途**: Songwriting craft and Suno AI music prompts.

### 19. `touchdesigner-mcp`
- **标题**: TouchDesigner Integration (twozero MCP)
- **路径**: `creative/touchdesigner-mcp/SKILL.md`
- **用途**: Control a running TouchDesigner instance via twozero MCP — create operators, set parameters, wire connections, execute Python, build real-time visuals. 36 na...

---

## 办公与生产力

### 1. `airtable`
- **标题**: Airtable — Bases, Tables & Records
- **路径**: `productivity/airtable/SKILL.md`
- **用途**: Airtable REST API via curl. Records CRUD, filters, upserts.

### 2. `google-workspace`
- **标题**: Google Workspace
- **路径**: `productivity/google-workspace/SKILL.md`
- **用途**: Gmail, Calendar, Drive, Docs, Sheets via gws CLI or Python.

### 3. `linear`
- **标题**: Linear — Issue & Project Management
- **路径**: `productivity/linear/SKILL.md`
- **用途**: Linear: manage issues, projects, teams via GraphQL + curl.

### 4. `maps`
- **标题**: Maps Skill
- **路径**: `productivity/maps/SKILL.md`
- **用途**: Geocode, POIs, routes, timezones via OpenStreetMap/OSRM.

### 5. `nano-pdf`
- **标题**: nano-pdf
- **路径**: `productivity/nano-pdf/SKILL.md`
- **用途**: Edit PDF text/typos/titles via nano-pdf CLI (NL prompts).

### 6. `notion`
- **标题**: Notion API
- **路径**: `productivity/notion/SKILL.md`
- **用途**: Notion API via curl: pages, databases, blocks, search.

### 7. `ocr-and-documents`
- **标题**: PDF & Document Extraction
- **路径**: `productivity/ocr-and-documents/SKILL.md`
- **用途**: Extract text from PDFs/scans (pymupdf, marker-pdf).

### 8. `powerpoint`
- **标题**: Powerpoint Skill
- **路径**: `productivity/powerpoint/SKILL.md`
- **用途**: Create, read, edit .pptx decks, slides, notes, templates.

---

## GitHub 工作流

### 1. `codebase-inspection`
- **标题**: Codebase Inspection with pygount
- **路径**: `github/codebase-inspection/SKILL.md`
- **用途**: Inspect codebases w/ pygount: LOC, languages, ratios.

### 2. `github-auth`
- **标题**: GitHub Authentication Setup
- **路径**: `github/github-auth/SKILL.md`
- **用途**: GitHub auth setup: HTTPS tokens, SSH keys, gh CLI login.

### 3. `github-code-review`
- **标题**: GitHub Code Review
- **路径**: `github/github-code-review/SKILL.md`
- **用途**: Review PRs: diffs, inline comments via gh or REST.

### 4. `github-issues`
- **标题**: GitHub Issues Management
- **路径**: `github/github-issues/SKILL.md`
- **用途**: Create, triage, label, assign GitHub issues via gh or REST.

### 5. `github-pr-workflow`
- **标题**: GitHub Pull Request Workflow
- **路径**: `github/github-pr-workflow/SKILL.md`
- **用途**: GitHub PR lifecycle: branch, commit, open, CI, merge.

### 6. `github-repo-management`
- **标题**: GitHub Repository Management
- **路径**: `github/github-repo-management/SKILL.md`
- **用途**: Clone/create/fork repos; manage remotes, releases.

---

## 研究与信息检索

### 1. `arxiv`
- **标题**: arXiv Research
- **路径**: `research/arxiv/SKILL.md`
- **用途**: Search arXiv papers by keyword, author, category, or ID.

### 2. `blogwatcher`
- **标题**: Blogwatcher
- **路径**: `research/blogwatcher/SKILL.md`
- **用途**: Monitor blogs and RSS/Atom feeds via blogwatcher-cli tool.

### 3. `llm-wiki`
- **标题**: Karpathy's LLM Wiki
- **路径**: `research/llm-wiki/SKILL.md`
- **用途**: Karpathy's LLM Wiki: build/query interlinked markdown KB.

### 4. `polymarket`
- **标题**: Polymarket — Prediction Market Data
- **路径**: `research/polymarket/SKILL.md`
- **用途**: Query Polymarket: markets, prices, orderbooks, history.

### 5. `research-paper-writing`
- **标题**: Research Paper Writing Pipeline
- **路径**: `research/research-paper-writing/SKILL.md`
- **用途**: Write ML papers for NeurIPS/ICML/ICLR: design→submit.

---

## 自治代理与多代理

### 1. `claude-code`
- **标题**: Claude Code — Hermes Orchestration Guide
- **路径**: `autonomous-ai-agents/claude-code/SKILL.md`
- **用途**: Delegate coding to Claude Code CLI (features, PRs).

### 2. `codex`
- **标题**: Codex CLI
- **路径**: `autonomous-ai-agents/codex/SKILL.md`
- **用途**: Delegate coding to OpenAI Codex CLI (features, PRs).

### 3. `hermes-agent`
- **标题**: Hermes Agent
- **路径**: `autonomous-ai-agents/hermes-agent/SKILL.md`
- **用途**: Configure, extend, or contribute to Hermes Agent.

### 4. `opencode`
- **标题**: OpenCode CLI
- **路径**: `autonomous-ai-agents/opencode/SKILL.md`
- **用途**: Delegate coding to OpenCode CLI (features, PR review).

---

## DevOps 与自动化

### 1. `kanban-orchestrator`
- **标题**: Kanban Orchestrator — Decomposition Playbook
- **路径**: `devops/kanban-orchestrator/SKILL.md`
- **用途**: Decomposition playbook + specialist-roster conventions + anti-temptation rules for an orchestrator profile routing work through Kanban. The "don't do the wor...

### 2. `kanban-worker`
- **标题**: Kanban Worker — Pitfalls and Examples
- **路径**: `devops/kanban-worker/SKILL.md`
- **用途**: Pitfalls, examples, and edge cases for Hermes Kanban workers. The lifecycle itself is auto-injected into every worker's system prompt as KANBAN_GUIDANCE (fro...

### 3. `webhook-subscriptions`
- **标题**: Webhook Subscriptions
- **路径**: `devops/webhook-subscriptions/SKILL.md`
- **用途**: Webhook subscriptions: event-driven agent runs.

---

## MCP 集成

### 1. `native-mcp`
- **标题**: Native MCP Client
- **路径**: `mcp/native-mcp/SKILL.md`
- **用途**: MCP client: connect servers, register tools (stdio/HTTP).

---

## 媒体与音视频

### 1. `gif-search`
- **标题**: GIF Search (Tenor API)
- **路径**: `media/gif-search/SKILL.md`
- **用途**: Search/download GIFs from Tenor via curl + jq.

### 2. `heartmula`
- **标题**: HeartMuLa - Open-Source Music Generation
- **路径**: `media/heartmula/SKILL.md`
- **用途**: HeartMuLa: Suno-like song generation from lyrics + tags.

### 3. `songsee`
- **标题**: songsee
- **路径**: `media/songsee/SKILL.md`
- **用途**: Audio spectrograms/features (mel, chroma, MFCC) via CLI.

### 4. `spotify`
- **标题**: Spotify
- **路径**: `media/spotify/SKILL.md`
- **用途**: Spotify: play, search, queue, manage playlists and devices.

### 5. `youtube-content`
- **标题**: YouTube Content Tool
- **路径**: `media/youtube-content/SKILL.md`
- **用途**: YouTube transcripts to summaries, threads, blogs.

---

## Apple 生态

### 1. `apple-notes`
- **标题**: Apple Notes
- **路径**: `apple/apple-notes/SKILL.md`
- **用途**: Manage Apple Notes via memo CLI: create, search, edit.

### 2. `apple-reminders`
- **标题**: Apple Reminders
- **路径**: `apple/apple-reminders/SKILL.md`
- **用途**: Apple Reminders via remindctl: add, list, complete.

### 3. `findmy`
- **标题**: Find My (Apple)
- **路径**: `apple/findmy/SKILL.md`
- **用途**: Track Apple devices/AirTags via FindMy.app on macOS.

### 4. `imessage`
- **标题**: iMessage
- **路径**: `apple/imessage/SKILL.md`
- **用途**: Send and receive iMessages/SMS via the imsg CLI on macOS.

---

## 邮件

### 1. `himalaya`
- **标题**: Himalaya Email CLI
- **路径**: `email/himalaya/SKILL.md`
- **用途**: Himalaya CLI: IMAP/SMTP email from terminal.

---

## 社交媒体

### 1. `xurl`
- **标题**: xurl — X (Twitter) API via the Official CLI
- **路径**: `social-media/xurl/SKILL.md`
- **用途**: Interact with X/Twitter via xurl, the official X API CLI. Use for posting, replying, quoting, searching, timelines, mentions, likes, reposts, bookmarks, foll...

---

## 笔记与知识库

### 1. `obsidian`
- **标题**: Obsidian Vault
- **路径**: `note-taking/obsidian/SKILL.md`
- **用途**: Read, search, and create notes in the Obsidian vault.

---

## 智能家居

### 1. `openhue`
- **标题**: OpenHue CLI
- **路径**: `smart-home/openhue/SKILL.md`
- **用途**: Control Philips Hue lights, scenes, rooms via OpenHue CLI.

---

## 数据科学

### 1. `jupyter-live-kernel`
- **标题**: Jupyter Live Kernel (hamelnb)
- **路径**: `data-science/jupyter-live-kernel/SKILL.md`
- **用途**: Iterative Python via live Jupyter kernel (hamelnb).

---

## 游戏相关

### 1. `minecraft-modpack-server`
- **标题**: Minecraft Modpack Server Setup
- **路径**: `gaming/minecraft-modpack-server/SKILL.md`
- **用途**: Host modded Minecraft servers (CurseForge, Modrinth).

### 2. `pokemon-player`
- **标题**: Pokemon Player
- **路径**: `gaming/pokemon-player/SKILL.md`
- **用途**: Play Pokemon via headless emulator + RAM reads.

---

## MLOps 与模型工程

### 1. `huggingface-hub`
- **标题**: Hugging Face CLI (`hf`) Reference Guide
- **路径**: `mlops/huggingface-hub/SKILL.md`
- **用途**: HuggingFace hf CLI: search/download/upload models, datasets.

---

## 安全对抗

### 1. `godmode`
- **标题**: G0DM0D3 Jailbreaking Skill
- **路径**: `red-teaming/godmode/SKILL.md`
- **用途**: Jailbreak LLMs: Parseltongue, GODMODE, ULTRAPLINIAN.

---

## ECC Imports 扩展技能库

> 这一组是从 ECC 导入的扩展技能库，覆盖大量工程、架构、安全、测试、运维、行业流程场景。

### 1. `accessibility`
- **标题**: Accessibility (WCAG 2.2)
- **路径**: `ecc-imports/accessibility/SKILL.md`
- **用途**: Design, implement, and audit inclusive digital products using WCAG 2.2 Level AA

### 2. `agent-eval`
- **标题**: Agent Eval Skill
- **路径**: `ecc-imports/agent-eval/SKILL.md`
- **用途**: Head-to-head comparison of coding agents (Claude Code, Aider, Codex, etc.) on custom tasks with pass rate, cost, time, and consistency metrics

### 3. `agent-harness-construction`
- **标题**: Agent Harness Construction
- **路径**: `ecc-imports/agent-harness-construction/SKILL.md`
- **用途**: Design and optimize AI agent action spaces, tool definitions, and observation formatting for higher completion rates.

### 4. `agent-introspection-debugging`
- **标题**: Agent Introspection Debugging
- **路径**: `ecc-imports/agent-introspection-debugging/SKILL.md`
- **用途**: Structured self-debugging workflow for AI agent failures using capture, diagnosis, contained recovery, and introspection reports.

### 5. `agent-payment-x402`
- **标题**: Agent Payment Execution (x402)
- **路径**: `ecc-imports/agent-payment-x402/SKILL.md`
- **用途**: Add x402 payment execution to AI agents — per-task budgets, spending controls, and non-custodial wallets via MCP tools. Use when agents need to pay for APIs,...

### 6. `agent-sort`
- **标题**: Agent Sort
- **路径**: `ecc-imports/agent-sort/SKILL.md`
- **用途**: Build an evidence-backed ECC install plan for a specific repo by sorting skills, commands, rules, hooks, and extras into DAILY vs LIBRARY buckets using paral...

### 7. `agentic-engineering`
- **标题**: Agentic Engineering
- **路径**: `ecc-imports/agentic-engineering/SKILL.md`
- **用途**: Operate as an agentic engineer using eval-first execution, decomposition, and cost-aware model routing.

### 8. `ai-first-engineering`
- **标题**: AI-First Engineering
- **路径**: `ecc-imports/ai-first-engineering/SKILL.md`
- **用途**: Engineering operating model for teams where AI agents generate a large share of implementation output.

### 9. `ai-regression-testing`
- **标题**: AI Regression Testing
- **路径**: `ecc-imports/ai-regression-testing/SKILL.md`
- **用途**: Regression testing strategies for AI-assisted development. Sandbox-mode API testing without database dependencies, automated bug-check workflows, and pattern...

### 10. `android-clean-architecture`
- **标题**: Android Clean Architecture
- **路径**: `ecc-imports/android-clean-architecture/SKILL.md`
- **用途**: Clean Architecture patterns for Android and Kotlin Multiplatform projects — module structure, dependency rules, UseCases, Repositories, and data layer patterns.

### 11. `api-connector-builder`
- **标题**: API Connector Builder
- **路径**: `ecc-imports/api-connector-builder/SKILL.md`
- **用途**: Build a new API connector or provider by matching the target repo's existing integration pattern exactly. Use when adding one more integration without invent...

### 12. `api-design`
- **标题**: API Design Patterns
- **路径**: `ecc-imports/api-design/SKILL.md`
- **用途**: REST API design patterns including resource naming, status codes, pagination, filtering, error responses, versioning, and rate limiting for production APIs.

### 13. `architecture-decision-records`
- **标题**: Architecture Decision Records
- **路径**: `ecc-imports/architecture-decision-records/SKILL.md`
- **用途**: Capture architectural decisions made during Claude Code sessions as structured ADRs. Auto-detects decision moments, records context, alternatives considered,...

### 14. `article-writing`
- **标题**: Article Writing
- **路径**: `ecc-imports/article-writing/SKILL.md`
- **用途**: Write articles, guides, blog posts, tutorials, newsletter issues, and other long-form content in a distinctive voice derived from supplied examples or brand...

### 15. `automation-audit-ops`
- **标题**: Automation Audit Ops
- **路径**: `ecc-imports/automation-audit-ops/SKILL.md`
- **用途**: Evidence-first automation inventory and overlap audit workflow for ECC. Use when the user wants to know which jobs, hooks, connectors, MCP servers, or wrappe...

### 16. `autonomous-agent-harness`
- **标题**: Autonomous Agent Harness
- **路径**: `ecc-imports/autonomous-agent-harness/SKILL.md`
- **用途**: Transform Claude Code into a fully autonomous agent system with persistent memory, scheduled operations, computer use, and task queuing. Replaces standalone...

### 17. `autonomous-loops`
- **标题**: Autonomous Loops Skill
- **路径**: `ecc-imports/autonomous-loops/SKILL.md`
- **用途**: Patterns and architectures for autonomous Claude Code loops — from simple sequential pipelines to RFC-driven multi-agent DAG systems.

### 18. `backend-patterns`
- **标题**: Backend Development Patterns
- **路径**: `ecc-imports/backend-patterns/SKILL.md`
- **用途**: Backend architecture patterns, API design, database optimization, and server-side best practices for Node.js, Express, and Next.js API routes.

### 19. `benchmark`
- **标题**: Benchmark — Performance Baseline & Regression Detection
- **路径**: `ecc-imports/benchmark/SKILL.md`
- **用途**: Use this skill to measure performance baselines, detect regressions before/after PRs, and compare stack alternatives.

### 20. `blueprint`
- **标题**: Blueprint — Construction Plan Generator
- **路径**: `ecc-imports/blueprint/SKILL.md`
- **用途**: 暂无 frontmatter 描述，建议直接查看该 skill 的 SKILL.md 获取完整用法。

### 21. `brand-voice`
- **标题**: Brand Voice
- **路径**: `ecc-imports/brand-voice/SKILL.md`
- **用途**: Build a source-derived writing style profile from real posts, essays, launch notes, docs, or site copy, then reuse that profile across content, outreach, and...

### 22. `browser-qa`
- **标题**: Browser QA — Automated Visual Testing & Interaction
- **路径**: `ecc-imports/browser-qa/SKILL.md`
- **用途**: Use this skill to automate visual testing and UI interaction verification using browser automation after deploying features.

### 23. `bun-runtime`
- **标题**: Bun Runtime
- **路径**: `ecc-imports/bun-runtime/SKILL.md`
- **用途**: Bun as runtime, package manager, bundler, and test runner. When to choose Bun vs Node, migration notes, and Vercel support.

### 24. `canary-watch`
- **标题**: Canary Watch — Post-Deploy Monitoring
- **路径**: `ecc-imports/canary-watch/SKILL.md`
- **用途**: Use this skill to monitor a deployed URL for regressions after deploys, merges, or dependency upgrades.

### 25. `carrier-relationship-management`
- **标题**: Carrier Relationship Management
- **路径**: `ecc-imports/carrier-relationship-management/SKILL.md`
- **用途**: >

### 26. `ck`
- **标题**: ck — Context Keeper
- **路径**: `ecc-imports/ck/SKILL.md`
- **用途**: Persistent per-project memory for Claude Code. Auto-loads project context on session start, tracks sessions with git activity, and writes to native memory. C...

### 27. `claude-devfleet`
- **标题**: Claude DevFleet Multi-Agent Orchestration
- **路径**: `ecc-imports/claude-devfleet/SKILL.md`
- **用途**: Orchestrate multi-agent coding tasks via Claude DevFleet — plan projects, dispatch parallel agents in isolated worktrees, monitor progress, and read structur...

### 28. `click-path-audit`
- **标题**: /click-path-audit — Behavioural Flow Audit
- **路径**: `ecc-imports/click-path-audit/SKILL.md`
- **用途**: Trace every user-facing button/touchpoint through its full state change sequence to find bugs where functions individually work but cancel each other out, pr...

### 29. `clickhouse-io`
- **标题**: ClickHouse Analytics Patterns
- **路径**: `ecc-imports/clickhouse-io/SKILL.md`
- **用途**: ClickHouse database patterns, query optimization, analytics, and data engineering best practices for high-performance analytical workloads.

### 30. `code-tour`
- **标题**: Code Tour
- **路径**: `ecc-imports/code-tour/SKILL.md`
- **用途**: Create CodeTour `.tour` files — persona-targeted, step-by-step walkthroughs with real file and line anchors. Use for onboarding tours, architecture walkthrou...

### 31. `codebase-onboarding`
- **标题**: Codebase Onboarding
- **路径**: `ecc-imports/codebase-onboarding/SKILL.md`
- **用途**: Analyze an unfamiliar codebase and generate a structured onboarding guide with architecture map, key entry points, conventions, and a starter CLAUDE.md. Use...

### 32. `coding-standards`
- **标题**: Coding Standards & Best Practices
- **路径**: `ecc-imports/coding-standards/SKILL.md`
- **用途**: Baseline cross-project coding conventions for naming, readability, immutability, and code-quality review. Use detailed frontend or backend skills for framewo...

### 33. `compose-multiplatform-patterns`
- **标题**: Compose Multiplatform Patterns
- **路径**: `ecc-imports/compose-multiplatform-patterns/SKILL.md`
- **用途**: Compose Multiplatform and Jetpack Compose patterns for KMP projects — state management, navigation, theming, performance, and platform-specific UI.

### 34. `configure-ecc`
- **标题**: Configure Everything Claude Code (ECC)
- **路径**: `ecc-imports/configure-ecc/SKILL.md`
- **用途**: Interactive installer for Everything Claude Code — guides users through selecting and installing skills and rules to user-level or project-level directories,...

### 35. `connections-optimizer`
- **标题**: Connections Optimizer
- **路径**: `ecc-imports/connections-optimizer/SKILL.md`
- **用途**: Reorganize the user's X and LinkedIn network with review-first pruning, add/follow recommendations, and channel-specific warm outreach drafted in the user's...

### 36. `content-engine`
- **标题**: Content Engine
- **路径**: `ecc-imports/content-engine/SKILL.md`
- **用途**: Create platform-native content systems for X, LinkedIn, TikTok, YouTube, newsletters, and repurposed multi-platform campaigns. Use when the user wants social...

### 37. `content-hash-cache-pattern`
- **标题**: Content-Hash File Cache Pattern
- **路径**: `ecc-imports/content-hash-cache-pattern/SKILL.md`
- **用途**: Cache expensive file processing results using SHA-256 content hashes — path-independent, auto-invalidating, with service layer separation.

### 38. `context-budget`
- **标题**: Context Budget
- **路径**: `ecc-imports/context-budget/SKILL.md`
- **用途**: Audits Claude Code context window consumption across agents, skills, MCP servers, and rules. Identifies bloat, redundant components, and produces prioritized...

### 39. `continuous-agent-loop`
- **标题**: Continuous Agent Loop
- **路径**: `ecc-imports/continuous-agent-loop/SKILL.md`
- **用途**: Patterns for continuous autonomous agent loops with quality gates, evals, and recovery controls.

### 40. `continuous-learning`
- **标题**: Continuous Learning Skill - DEPRECATED
- **路径**: `ecc-imports/continuous-learning/SKILL.md`
- **用途**: [DEPRECATED - use continuous-learning-v2] Legacy v1 stop-hook skill extractor. v2 is a strict superset with instinct-based, project-scoped, hook-reliable lea...

### 41. `continuous-learning-v2`
- **标题**: Continuous Learning v2.1 - Instinct
- **路径**: `ecc-imports/continuous-learning-v2/SKILL.md`
- **用途**: Instinct-based learning system that observes sessions via hooks, creates atomic instincts with confidence scoring, and evolves them into skills/commands/agen...

### 42. `cost-aware-llm-pipeline`
- **标题**: Cost-Aware LLM Pipeline
- **路径**: `ecc-imports/cost-aware-llm-pipeline/SKILL.md`
- **用途**: Cost optimization patterns for LLM API usage — model routing by task complexity, budget tracking, retry logic, and prompt caching.

### 43. `council`
- **标题**: Council
- **路径**: `ecc-imports/council/SKILL.md`
- **用途**: Convene a four-voice council for ambiguous decisions, tradeoffs, and go/no-go calls. Use when multiple valid paths exist and you need structured disagreement...

### 44. `cpp-coding-standards`
- **标题**: C++ Coding Standards (C++ Core Guidelines)
- **路径**: `ecc-imports/cpp-coding-standards/SKILL.md`
- **用途**: C++ coding standards based on the C++ Core Guidelines (isocpp.github.io). Use when writing, reviewing, or refactoring C++ code to enforce modern, safe, and i...

### 45. `cpp-testing`
- **标题**: C++ Testing (Agent Skill)
- **路径**: `ecc-imports/cpp-testing/SKILL.md`
- **用途**: Use only when writing/updating/fixing C++ tests, configuring GoogleTest/CTest, diagnosing failing or flaky tests, or adding coverage/sanitizers.

### 46. `crosspost`
- **标题**: Crosspost
- **路径**: `ecc-imports/crosspost/SKILL.md`
- **用途**: Multi-platform content distribution across X, LinkedIn, Threads, and Bluesky. Adapts content per platform using content-engine patterns. Never posts identica...

### 47. `csharp-testing`
- **标题**: C# Testing Patterns
- **路径**: `ecc-imports/csharp-testing/SKILL.md`
- **用途**: C# and .NET testing patterns with xUnit, FluentAssertions, mocking, integration tests, and test organization best practices.

### 48. `customer-billing-ops`
- **标题**: Customer Billing Ops
- **路径**: `ecc-imports/customer-billing-ops/SKILL.md`
- **用途**: Operate customer billing workflows such as subscriptions, refunds, churn triage, billing-portal recovery, and plan analysis using connected billing tools lik...

### 49. `customs-trade-compliance`
- **标题**: Customs & Trade Compliance
- **路径**: `ecc-imports/customs-trade-compliance/SKILL.md`
- **用途**: >

### 50. `dart-flutter-patterns`
- **标题**: Dart/Flutter Patterns
- **路径**: `ecc-imports/dart-flutter-patterns/SKILL.md`
- **用途**: Production-ready Dart and Flutter patterns covering null safety, immutable state, async composition, widget architecture, popular state management frameworks...

### 51. `dashboard-builder`
- **标题**: Dashboard Builder
- **路径**: `ecc-imports/dashboard-builder/SKILL.md`
- **用途**: Build monitoring dashboards that answer real operator questions for Grafana, SigNoz, and similar platforms. Use when turning metrics into a working dashboard...

### 52. `data-scraper-agent`
- **标题**: Data Scraper Agent
- **路径**: `ecc-imports/data-scraper-agent/SKILL.md`
- **用途**: Build a fully automated AI-powered data collection agent for any public source — job boards, prices, news, GitHub, sports, anything. Scrapes on a schedule, e...

### 53. `database-migrations`
- **标题**: Database Migration Patterns
- **路径**: `ecc-imports/database-migrations/SKILL.md`
- **用途**: Database migration best practices for schema changes, data migrations, rollbacks, and zero-downtime deployments across PostgreSQL, MySQL, and common ORMs (Pr...

### 54. `deep-research`
- **标题**: Deep Research
- **路径**: `ecc-imports/deep-research/SKILL.md`
- **用途**: Multi-source deep research using firecrawl and exa MCPs. Searches the web, synthesizes findings, and delivers cited reports with source attribution. Use when...

### 55. `defi-amm-security`
- **标题**: DeFi AMM Security
- **路径**: `ecc-imports/defi-amm-security/SKILL.md`
- **用途**: Security checklist for Solidity AMM contracts, liquidity pools, and swap flows. Covers reentrancy, CEI ordering, donation or inflation attacks, oracle manipu...

### 56. `deployment-patterns`
- **标题**: Deployment Patterns
- **路径**: `ecc-imports/deployment-patterns/SKILL.md`
- **用途**: Deployment workflows, CI/CD pipeline patterns, Docker containerization, health checks, rollback strategies, and production readiness checklists for web appli...

### 57. `design-system`
- **标题**: Design System — Generate & Audit Visual Systems
- **路径**: `ecc-imports/design-system/SKILL.md`
- **用途**: Use this skill to generate or audit design systems, check visual consistency, and review PRs that touch styling.

### 58. `django-patterns`
- **标题**: Django Development Patterns
- **路径**: `ecc-imports/django-patterns/SKILL.md`
- **用途**: Django architecture patterns, REST API design with DRF, ORM best practices, caching, signals, middleware, and production-grade Django apps.

### 59. `django-security`
- **标题**: Django Security Best Practices
- **路径**: `ecc-imports/django-security/SKILL.md`
- **用途**: Django security best practices, authentication, authorization, CSRF protection, SQL injection prevention, XSS prevention, and secure deployment configurations.

### 60. `django-tdd`
- **标题**: Django Testing with TDD
- **路径**: `ecc-imports/django-tdd/SKILL.md`
- **用途**: Django testing strategies with pytest-django, TDD methodology, factory_boy, mocking, coverage, and testing Django REST Framework APIs.

### 61. `django-verification`
- **标题**: Django Verification Loop
- **路径**: `ecc-imports/django-verification/SKILL.md`
- **用途**: Verification loop for Django projects: migrations, linting, tests with coverage, security scans, and deployment readiness checks before release or PR.

### 62. `dmux-workflows`
- **标题**: dmux Workflows
- **路径**: `ecc-imports/dmux-workflows/SKILL.md`
- **用途**: Multi-agent orchestration using dmux (tmux pane manager for AI agents). Patterns for parallel agent workflows across Claude Code, Codex, OpenCode, and other...

### 63. `docker-patterns`
- **标题**: Docker Patterns
- **路径**: `ecc-imports/docker-patterns/SKILL.md`
- **用途**: Docker and Docker Compose patterns for local development, container security, networking, volume strategies, and multi-service orchestration.

### 64. `documentation-lookup`
- **标题**: Documentation Lookup (Context7)
- **路径**: `ecc-imports/documentation-lookup/SKILL.md`
- **用途**: Use up-to-date library and framework docs via Context7 MCP instead of training data. Activates for setup questions, API references, code examples, or when th...

### 65. `dotnet-patterns`
- **标题**: .NET Development Patterns
- **路径**: `ecc-imports/dotnet-patterns/SKILL.md`
- **用途**: Idiomatic C# and .NET patterns, conventions, dependency injection, async/await, and best practices for building robust, maintainable .NET applications.

### 66. `e2e-testing`
- **标题**: E2E Testing Patterns
- **路径**: `ecc-imports/e2e-testing/SKILL.md`
- **用途**: Playwright E2E testing patterns, Page Object Model, configuration, CI/CD integration, artifact management, and flaky test strategies.

### 67. `ecc-tools-cost-audit`
- **标题**: ECC Tools Cost Audit
- **路径**: `ecc-imports/ecc-tools-cost-audit/SKILL.md`
- **用途**: Evidence-first ECC Tools burn and billing audit workflow. Use when investigating runaway PR creation, quota bypass, premium-model leakage, duplicate jobs, or...

### 68. `email-ops`
- **标题**: Email Ops
- **路径**: `ecc-imports/email-ops/SKILL.md`
- **用途**: Evidence-first mailbox triage, drafting, send verification, and sent-mail-safe follow-up workflow for ECC. Use when the user wants to organize email, draft o...

### 69. `energy-procurement`
- **标题**: Energy Procurement
- **路径**: `ecc-imports/energy-procurement/SKILL.md`
- **用途**: >

### 70. `enterprise-agent-ops`
- **标题**: Enterprise Agent Ops
- **路径**: `ecc-imports/enterprise-agent-ops/SKILL.md`
- **用途**: Operate long-lived agent workloads with observability, security boundaries, and lifecycle management.

### 71. `eval-harness`
- **标题**: Eval Harness Skill
- **路径**: `ecc-imports/eval-harness/SKILL.md`
- **用途**: Formal evaluation framework for Claude Code sessions implementing eval-driven development (EDD) principles

### 72. `evm-token-decimals`
- **标题**: EVM Token Decimals
- **路径**: `ecc-imports/evm-token-decimals/SKILL.md`
- **用途**: Prevent silent decimal mismatch bugs across EVM chains. Covers runtime decimal lookup, chain-aware caching, bridged-token precision drift, and safe normaliza...

### 73. `exa-search`
- **标题**: Exa Search
- **路径**: `ecc-imports/exa-search/SKILL.md`
- **用途**: Neural search via Exa MCP for web, code, and company research. Use when the user needs web search, code examples, company intel, people lookup, or AI-powered...

### 74. `fal-ai-media`
- **标题**: fal.ai Media Generation
- **路径**: `ecc-imports/fal-ai-media/SKILL.md`
- **用途**: Unified media generation via fal.ai MCP — image, video, and audio. Covers text-to-image (Nano Banana), text/image-to-video (Seedance, Kling, Veo 3), text-to-...

### 75. `finance-billing-ops`
- **标题**: Finance Billing Ops
- **路径**: `ecc-imports/finance-billing-ops/SKILL.md`
- **用途**: Evidence-first revenue, pricing, refunds, team-billing, and billing-model truth workflow for ECC. Use when the user wants a sales snapshot, pricing compariso...

### 76. `flox-environments`
- **标题**: Flox Environments
- **路径**: `ecc-imports/flox-environments/SKILL.md`
- **用途**: Create reproducible, cross-platform development environments with Flox — a declarative environment manager built on Nix. ALWAYS use this skill when the user...

### 77. `flutter-dart-code-review`
- **标题**: Flutter/Dart Code Review Best Practices
- **路径**: `ecc-imports/flutter-dart-code-review/SKILL.md`
- **用途**: Library-agnostic Flutter/Dart code review checklist covering widget best practices, state management patterns (BLoC, Riverpod, Provider, GetX, MobX, Signals)...

### 78. `foundation-models-on-device`
- **标题**: FoundationModels: On-Device LLM (iOS 26)
- **路径**: `ecc-imports/foundation-models-on-device/SKILL.md`
- **用途**: Apple FoundationModels framework for on-device LLM — text generation, guided generation with @Generable, tool calling, and snapshot streaming in iOS 26+.

### 79. `frontend-patterns`
- **标题**: Frontend Development Patterns
- **路径**: `ecc-imports/frontend-patterns/SKILL.md`
- **用途**: Frontend development patterns for React, Next.js, state management, performance optimization, and UI best practices.

### 80. `frontend-slides`
- **标题**: Frontend Slides
- **路径**: `ecc-imports/frontend-slides/SKILL.md`
- **用途**: Create stunning, animation-rich HTML presentations from scratch or by converting PowerPoint files. Use when the user wants to build a presentation, convert a...

### 81. `gan-style-harness`
- **标题**: GAN-Style Harness Skill
- **路径**: `ecc-imports/gan-style-harness/SKILL.md`
- **用途**: GAN-inspired Generator-Evaluator agent harness for building high-quality applications autonomously. Based on Anthropic's March 2026 harness design paper.

### 82. `gateguard`
- **标题**: GateGuard — Fact-Forcing Pre-Action Gate
- **路径**: `ecc-imports/gateguard/SKILL.md`
- **用途**: Fact-forcing gate that blocks Edit/Write/Bash (including MultiEdit) and demands concrete investigation (importers, data schemas, user instruction) before all...

### 83. `git-workflow`
- **标题**: Git Workflow Patterns
- **路径**: `ecc-imports/git-workflow/SKILL.md`
- **用途**: Git workflow patterns including branching strategies, commit conventions, merge vs rebase, conflict resolution, and collaborative development best practices...

### 84. `github-ops`
- **标题**: GitHub Operations
- **路径**: `ecc-imports/github-ops/SKILL.md`
- **用途**: GitHub repository operations, automation, and management. Issue triage, PR management, CI/CD operations, release management, and security monitoring using th...

### 85. `golang-patterns`
- **标题**: Go Development Patterns
- **路径**: `ecc-imports/golang-patterns/SKILL.md`
- **用途**: Idiomatic Go patterns, best practices, and conventions for building robust, efficient, and maintainable Go applications.

### 86. `golang-testing`
- **标题**: Go Testing Patterns
- **路径**: `ecc-imports/golang-testing/SKILL.md`
- **用途**: Go testing patterns including table-driven tests, subtests, benchmarks, fuzzing, and test coverage. Follows TDD methodology with idiomatic Go practices.

### 87. `google-workspace-ops`
- **标题**: Google Workspace Ops
- **路径**: `ecc-imports/google-workspace-ops/SKILL.md`
- **用途**: Operate across Google Drive, Docs, Sheets, and Slides as one workflow surface for plans, trackers, decks, and shared documents. Use when the user needs to fi...

### 88. `healthcare-cdss-patterns`
- **标题**: Healthcare CDSS Development Patterns
- **路径**: `ecc-imports/healthcare-cdss-patterns/SKILL.md`
- **用途**: Clinical Decision Support System (CDSS) development patterns. Drug interaction checking, dose validation, clinical scoring (NEWS2, qSOFA), alert severity cla...

### 89. `healthcare-emr-patterns`
- **标题**: Healthcare EMR Development Patterns
- **路径**: `ecc-imports/healthcare-emr-patterns/SKILL.md`
- **用途**: EMR/EHR development patterns for healthcare applications. Clinical safety, encounter workflows, prescription generation, clinical decision support integratio...

### 90. `healthcare-eval-harness`
- **标题**: Healthcare Eval Harness — Patient Safety Verification
- **路径**: `ecc-imports/healthcare-eval-harness/SKILL.md`
- **用途**: Patient safety evaluation harness for healthcare application deployments. Automated test suites for CDSS accuracy, PHI exposure, clinical workflow integrity,...

### 91. `healthcare-phi-compliance`
- **标题**: Healthcare PHI/PII Compliance Patterns
- **路径**: `ecc-imports/healthcare-phi-compliance/SKILL.md`
- **用途**: Protected Health Information (PHI) and Personally Identifiable Information (PII) compliance patterns for healthcare applications. Covers data classification,...

### 92. `hermes-imports`
- **标题**: Hermes Imports
- **路径**: `ecc-imports/hermes-imports/SKILL.md`
- **用途**: Convert local Hermes operator workflows into sanitized ECC skills and release-pack artifacts. Use when preparing a Hermes workflow for public ECC reuse witho...

### 93. `hexagonal-architecture`
- **标题**: Hexagonal Architecture
- **路径**: `ecc-imports/hexagonal-architecture/SKILL.md`
- **用途**: Design, implement, and refactor Ports & Adapters systems with clear domain boundaries, dependency inversion, and testable use-case orchestration across TypeS...

### 94. `hipaa-compliance`
- **标题**: HIPAA Compliance
- **路径**: `ecc-imports/hipaa-compliance/SKILL.md`
- **用途**: HIPAA-specific entrypoint for healthcare privacy and security work. Use when a task is explicitly framed around HIPAA, PHI handling, covered entities, BAAs,...

### 95. `hookify-rules`
- **标题**: Writing Hookify Rules
- **路径**: `ecc-imports/hookify-rules/SKILL.md`
- **用途**: This skill should be used when the user asks to create a hookify rule, write a hook rule, configure hookify, add a hookify rule, or needs guidance on hookify...

### 96. `inventory-demand-planning`
- **标题**: Inventory Demand Planning
- **路径**: `ecc-imports/inventory-demand-planning/SKILL.md`
- **用途**: >

### 97. `investor-materials`
- **标题**: Investor Materials
- **路径**: `ecc-imports/investor-materials/SKILL.md`
- **用途**: Create and update pitch decks, one-pagers, investor memos, accelerator applications, financial models, and fundraising materials. Use when the user needs inv...

### 98. `investor-outreach`
- **标题**: Investor Outreach
- **路径**: `ecc-imports/investor-outreach/SKILL.md`
- **用途**: Draft cold emails, warm intro blurbs, follow-ups, update emails, and investor communications for fundraising. Use when the user wants outreach to angels, VCs...

### 99. `ios-icon-gen`
- **标题**: iOS Icon Generator
- **路径**: `ecc-imports/ios-icon-gen/SKILL.md`
- **用途**: Generate iOS app icons as PNG imagesets for Xcode asset catalogs from SF Symbols (5000+ Apple-native) or Iconify API (275k+ open source icons from 200+ colle...

### 100. `iterative-retrieval`
- **标题**: Iterative Retrieval Pattern
- **路径**: `ecc-imports/iterative-retrieval/SKILL.md`
- **用途**: Pattern for progressively refining context retrieval to solve the subagent context problem

### 101. `java-coding-standards`
- **标题**: Java Coding Standards
- **路径**: `ecc-imports/java-coding-standards/SKILL.md`
- **用途**: Java coding standards for Spring Boot services: naming, immutability, Optional usage, streams, exceptions, generics, and project layout.

### 102. `jira-integration`
- **标题**: Jira Integration Skill
- **路径**: `ecc-imports/jira-integration/SKILL.md`
- **用途**: Use this skill when retrieving Jira tickets, analyzing requirements, updating ticket status, adding comments, or transitioning issues. Provides Jira API patt...

### 103. `jpa-patterns`
- **标题**: JPA/Hibernate Patterns
- **路径**: `ecc-imports/jpa-patterns/SKILL.md`
- **用途**: JPA/Hibernate patterns for entity design, relationships, query optimization, transactions, auditing, indexing, pagination, and pooling in Spring Boot.

### 104. `knowledge-ops`
- **标题**: Knowledge Operations
- **路径**: `ecc-imports/knowledge-ops/SKILL.md`
- **用途**: Knowledge base management, ingestion, sync, and retrieval across multiple storage layers (local files, MCP memory, vector stores, Git repos). Use when the us...

### 105. `kotlin-coroutines-flows`
- **标题**: Kotlin Coroutines & Flows
- **路径**: `ecc-imports/kotlin-coroutines-flows/SKILL.md`
- **用途**: Kotlin Coroutines and Flow patterns for Android and KMP — structured concurrency, Flow operators, StateFlow, error handling, and testing.

### 106. `kotlin-exposed-patterns`
- **标题**: Kotlin Exposed Patterns
- **路径**: `ecc-imports/kotlin-exposed-patterns/SKILL.md`
- **用途**: JetBrains Exposed ORM patterns including DSL queries, DAO pattern, transactions, HikariCP connection pooling, Flyway migrations, and repository pattern.

### 107. `kotlin-ktor-patterns`
- **标题**: Ktor Server Patterns
- **路径**: `ecc-imports/kotlin-ktor-patterns/SKILL.md`
- **用途**: Ktor server patterns including routing DSL, plugins, authentication, Koin DI, kotlinx.serialization, WebSockets, and testApplication testing.

### 108. `kotlin-patterns`
- **标题**: Kotlin Development Patterns
- **路径**: `ecc-imports/kotlin-patterns/SKILL.md`
- **用途**: Idiomatic Kotlin patterns, best practices, and conventions for building robust, efficient, and maintainable Kotlin applications with coroutines, null safety,...

### 109. `kotlin-testing`
- **标题**: Kotlin Testing Patterns
- **路径**: `ecc-imports/kotlin-testing/SKILL.md`
- **用途**: Kotlin testing patterns with Kotest, MockK, coroutine testing, property-based testing, and Kover coverage. Follows TDD methodology with idiomatic Kotlin prac...

### 110. `laravel-patterns`
- **标题**: Laravel Development Patterns
- **路径**: `ecc-imports/laravel-patterns/SKILL.md`
- **用途**: Laravel architecture patterns, routing/controllers, Eloquent ORM, service layers, queues, events, caching, and API resources for production apps.

### 111. `laravel-plugin-discovery`
- **标题**: Laravel Plugin Discovery
- **路径**: `ecc-imports/laravel-plugin-discovery/SKILL.md`
- **用途**: Discover and evaluate Laravel packages via LaraPlugins.io MCP. Use when the user wants to find plugins, check package health, or assess Laravel/PHP compatibi...

### 112. `laravel-security`
- **标题**: Laravel Security Best Practices
- **路径**: `ecc-imports/laravel-security/SKILL.md`
- **用途**: Laravel security best practices for authn/authz, validation, CSRF, mass assignment, file uploads, secrets, rate limiting, and secure deployment.

### 113. `laravel-tdd`
- **标题**: Laravel TDD Workflow
- **路径**: `ecc-imports/laravel-tdd/SKILL.md`
- **用途**: Test-driven development for Laravel with PHPUnit and Pest, factories, database testing, fakes, and coverage targets.

### 114. `laravel-verification`
- **标题**: Laravel Verification Loop
- **路径**: `ecc-imports/laravel-verification/SKILL.md`
- **用途**: Verification loop for Laravel projects: env checks, linting, static analysis, tests with coverage, security scans, and deployment readiness.

### 115. `lead-intelligence`
- **标题**: Lead Intelligence
- **路径**: `ecc-imports/lead-intelligence/SKILL.md`
- **用途**: AI-native lead intelligence and outreach pipeline. Replaces Apollo, Clay, and ZoomInfo with agent-powered signal scoring, mutual ranking, warm path discovery...

### 116. `liquid-glass-design`
- **标题**: Liquid Glass Design System (iOS 26)
- **路径**: `ecc-imports/liquid-glass-design/SKILL.md`
- **用途**: iOS 26 Liquid Glass design system — dynamic glass material with blur, reflection, and interactive morphing for SwiftUI, UIKit, and WidgetKit.

### 117. `llm-trading-agent-security`
- **标题**: LLM Trading Agent Security
- **路径**: `ecc-imports/llm-trading-agent-security/SKILL.md`
- **用途**: Security patterns for autonomous trading agents with wallet or transaction authority. Covers prompt injection, spend limits, pre-send simulation, circuit bre...

### 118. `logistics-exception-management`
- **标题**: Logistics Exception Management
- **路径**: `ecc-imports/logistics-exception-management/SKILL.md`
- **用途**: >

### 119. `market-research`
- **标题**: Market Research
- **路径**: `ecc-imports/market-research/SKILL.md`
- **用途**: Conduct market research, competitive analysis, investor due diligence, and industry intelligence with source attribution and decision-oriented summaries. Use...

### 120. `mcp-server-patterns`
- **标题**: MCP Server Patterns
- **路径**: `ecc-imports/mcp-server-patterns/SKILL.md`
- **用途**: Build MCP servers with Node/TypeScript SDK — tools, resources, prompts, Zod validation, stdio vs Streamable HTTP. Use Context7 or official MCP docs for lates...

### 121. `messages-ops`
- **标题**: Messages Ops
- **路径**: `ecc-imports/messages-ops/SKILL.md`
- **用途**: Evidence-first live messaging workflow for ECC. Use when the user wants to read texts or DMs, recover a recent one-time code, inspect a thread before replyin...

### 122. `nanoclaw-repl`
- **标题**: NanoClaw REPL
- **路径**: `ecc-imports/nanoclaw-repl/SKILL.md`
- **用途**: Operate and extend NanoClaw v2, ECC's zero-dependency session-aware REPL built on claude -p.

### 123. `nestjs-patterns`
- **标题**: NestJS Development Patterns
- **路径**: `ecc-imports/nestjs-patterns/SKILL.md`
- **用途**: NestJS architecture patterns for modules, controllers, providers, DTO validation, guards, interceptors, config, and production-grade TypeScript backends.

### 124. `nextjs-turbopack`
- **标题**: Next.js and Turbopack
- **路径**: `ecc-imports/nextjs-turbopack/SKILL.md`
- **用途**: Next.js 16+ and Turbopack — incremental bundling, FS caching, dev speed, and when to use Turbopack vs webpack.

### 125. `nodejs-keccak256`
- **标题**: Node.js Keccak-256
- **路径**: `ecc-imports/nodejs-keccak256/SKILL.md`
- **用途**: Prevent Ethereum hashing bugs in JavaScript and TypeScript. Node's sha3-256 is NIST SHA3, not Ethereum Keccak-256, and silently breaks selectors, signatures,...

### 126. `nutrient-document-processing`
- **标题**: Nutrient Document Processing
- **路径**: `ecc-imports/nutrient-document-processing/SKILL.md`
- **用途**: Process, convert, OCR, extract, redact, sign, and fill documents using the Nutrient DWS API. Works with PDFs, DOCX, XLSX, PPTX, HTML, and images.

### 127. `nuxt4-patterns`
- **标题**: Nuxt 4 Patterns
- **路径**: `ecc-imports/nuxt4-patterns/SKILL.md`
- **用途**: Nuxt 4 app patterns for hydration safety, performance, route rules, lazy loading, and SSR-safe data fetching with useFetch and useAsyncData.

### 128. `openclaw-persona-forge`
- **标题**: 龙虾灵魂锻造炉
- **路径**: `ecc-imports/openclaw-persona-forge/SKILL.md`
- **用途**: 为 OpenClaw AI Agent 锻造完整的龙虾灵魂方案。根据用户偏好或随机抽卡， 输出身份定位、灵魂描述(SOUL.md)、角色化底线规则、名字和头像生图提示词。 如当前环境提供已审核的生图 skill，可自动生成统一风格头像图片。 当用户需要创建、设计或定制 OpenClaw 龙虾灵魂时使用。 不适用于...

### 129. `opensource-pipeline`
- **标题**: Open-Source Pipeline Skill
- **路径**: `ecc-imports/opensource-pipeline/SKILL.md`
- **用途**: Open-source pipeline: fork, sanitize, and package private projects for safe public release. Chains 3 agents (forker, sanitizer, packager). Triggers: '/openso...

### 130. `perl-patterns`
- **标题**: Modern Perl Development Patterns
- **路径**: `ecc-imports/perl-patterns/SKILL.md`
- **用途**: Modern Perl 5.36+ idioms, best practices, and conventions for building robust, maintainable Perl applications.

### 131. `perl-security`
- **标题**: Perl Security Patterns
- **路径**: `ecc-imports/perl-security/SKILL.md`
- **用途**: Comprehensive Perl security covering taint mode, input validation, safe process execution, DBI parameterized queries, web security (XSS/SQLi/CSRF), and perlc...

### 132. `perl-testing`
- **标题**: Perl Testing Patterns
- **路径**: `ecc-imports/perl-testing/SKILL.md`
- **用途**: Perl testing patterns using Test2::V0, Test::More, prove runner, mocking, coverage with Devel::Cover, and TDD methodology.

### 133. `plankton-code-quality`
- **标题**: Plankton Code Quality Skill
- **路径**: `ecc-imports/plankton-code-quality/SKILL.md`
- **用途**: Write-time code quality enforcement using Plankton — auto-formatting, linting, and Claude-powered fixes on every file edit via hooks.

### 134. `postgres-patterns`
- **标题**: PostgreSQL Patterns
- **路径**: `ecc-imports/postgres-patterns/SKILL.md`
- **用途**: PostgreSQL database patterns for query optimization, schema design, indexing, and security. Based on Supabase best practices.

### 135. `product-capability`
- **标题**: Product Capability
- **路径**: `ecc-imports/product-capability/SKILL.md`
- **用途**: Translate PRD intent, roadmap asks, or product discussions into an implementation-ready capability plan that exposes constraints, invariants, interfaces, and...

### 136. `product-lens`
- **标题**: Product Lens — Think Before You Build
- **路径**: `ecc-imports/product-lens/SKILL.md`
- **用途**: Use this skill to validate the "why" before building, run product diagnostics, and pressure-test product direction before the request becomes an implementati...

### 137. `production-scheduling`
- **标题**: Production Scheduling
- **路径**: `ecc-imports/production-scheduling/SKILL.md`
- **用途**: >

### 138. `project-flow-ops`
- **标题**: Project Flow Ops
- **路径**: `ecc-imports/project-flow-ops/SKILL.md`
- **用途**: Operate execution flow across GitHub and Linear by triaging issues and pull requests, linking active work, and keeping GitHub public-facing while Linear rema...

### 139. `prompt-optimizer`
- **标题**: Prompt Optimizer
- **路径**: `ecc-imports/prompt-optimizer/SKILL.md`
- **用途**: 暂无 frontmatter 描述，建议直接查看该 skill 的 SKILL.md 获取完整用法。

### 140. `python-patterns`
- **标题**: Python Development Patterns
- **路径**: `ecc-imports/python-patterns/SKILL.md`
- **用途**: Pythonic idioms, PEP 8 standards, type hints, and best practices for building robust, efficient, and maintainable Python applications.

### 141. `python-testing`
- **标题**: Python Testing Patterns
- **路径**: `ecc-imports/python-testing/SKILL.md`
- **用途**: Python testing strategies using pytest, TDD methodology, fixtures, mocking, parametrization, and coverage requirements.

### 142. `pytorch-patterns`
- **标题**: PyTorch Development Patterns
- **路径**: `ecc-imports/pytorch-patterns/SKILL.md`
- **用途**: PyTorch deep learning patterns and best practices for building robust, efficient, and reproducible training pipelines, model architectures, and data loading.

### 143. `quality-nonconformance`
- **标题**: Quality & Non-Conformance Management
- **路径**: `ecc-imports/quality-nonconformance/SKILL.md`
- **用途**: >

### 144. `ralphinho-rfc-pipeline`
- **标题**: Ralphinho RFC Pipeline
- **路径**: `ecc-imports/ralphinho-rfc-pipeline/SKILL.md`
- **用途**: RFC-driven multi-agent DAG execution pattern with quality gates, merge queues, and work unit orchestration.

### 145. `regex-vs-llm-structured-text`
- **标题**: Regex vs LLM for Structured Text Parsing
- **路径**: `ecc-imports/regex-vs-llm-structured-text/SKILL.md`
- **用途**: Decision framework for choosing between regex and LLM when parsing structured text — start with regex, add LLM only for low-confidence edge cases.

### 146. `remotion-video-creation`
- **标题**: remotion-video-creation
- **路径**: `ecc-imports/remotion-video-creation/SKILL.md`
- **用途**: Best practices for Remotion - Video creation in React. 29 domain-specific rules covering 3D, animations, audio, captions, charts, transitions, and more.

### 147. `repo-scan`
- **标题**: repo-scan
- **路径**: `ecc-imports/repo-scan/SKILL.md`
- **用途**: Cross-stack source code asset audit — classifies every file, detects embedded third-party libraries, and delivers actionable four-level verdicts per module w...

### 148. `research-ops`
- **标题**: Research Ops
- **路径**: `ecc-imports/research-ops/SKILL.md`
- **用途**: Evidence-first current-state research workflow for ECC. Use when the user wants fresh facts, comparisons, enrichment, or a recommendation built from current...

### 149. `returns-reverse-logistics`
- **标题**: Returns & Reverse Logistics
- **路径**: `ecc-imports/returns-reverse-logistics/SKILL.md`
- **用途**: >

### 150. `rules-distill`
- **标题**: Rules Distill
- **路径**: `ecc-imports/rules-distill/SKILL.md`
- **用途**: Scan skills to extract cross-cutting principles and distill them into rules — append, revise, or create new rule files

### 151. `rust-patterns`
- **标题**: Rust Development Patterns
- **路径**: `ecc-imports/rust-patterns/SKILL.md`
- **用途**: Idiomatic Rust patterns, ownership, error handling, traits, concurrency, and best practices for building safe, performant applications.

### 152. `rust-testing`
- **标题**: Rust Testing Patterns
- **路径**: `ecc-imports/rust-testing/SKILL.md`
- **用途**: Rust testing patterns including unit tests, integration tests, async testing, property-based testing, mocking, and coverage. Follows TDD methodology.

### 153. `safety-guard`
- **标题**: Safety Guard — Prevent Destructive Operations
- **路径**: `ecc-imports/safety-guard/SKILL.md`
- **用途**: Use this skill to prevent destructive operations when working on production systems or running agents autonomously.

### 154. `santa-method`
- **标题**: Santa Method
- **路径**: `ecc-imports/santa-method/SKILL.md`
- **用途**: Multi-agent adversarial verification with convergence loop. Two independent review agents must both pass before output ships.

### 155. `search-first`
- **标题**: /search-first — Research Before You Code
- **路径**: `ecc-imports/search-first/SKILL.md`
- **用途**: Research-before-coding workflow. Search for existing tools, libraries, and patterns before writing custom code. Invokes the researcher agent.

### 156. `security-bounty-hunter`
- **标题**: Security Bounty Hunter
- **路径**: `ecc-imports/security-bounty-hunter/SKILL.md`
- **用途**: Hunt for exploitable, bounty-worthy security issues in repositories. Focuses on remotely reachable vulnerabilities that qualify for real reports instead of n...

### 157. `security-review`
- **标题**: Security Review Skill
- **路径**: `ecc-imports/security-review/SKILL.md`
- **用途**: Use this skill when adding authentication, handling user input, working with secrets, creating API endpoints, or implementing payment/sensitive features. Pro...

### 158. `security-scan`
- **标题**: Security Scan Skill
- **路径**: `ecc-imports/security-scan/SKILL.md`
- **用途**: Scan your Claude Code configuration (.claude/ directory) for security vulnerabilities, misconfigurations, and injection risks using AgentShield. Checks CLAUD...

### 159. `seo`
- **标题**: SEO
- **路径**: `ecc-imports/seo/SKILL.md`
- **用途**: Audit, plan, and implement SEO improvements across technical SEO, on-page optimization, structured data, Core Web Vitals, and content strategy. Use when the...

### 160. `skill-comply`
- **标题**: skill-comply: Automated Compliance Measurement
- **路径**: `ecc-imports/skill-comply/SKILL.md`
- **用途**: Visualize whether skills, rules, and agent definitions are actually followed — auto-generates scenarios at 3 prompt strictness levels, runs agents, classifie...

### 161. `skill-stocktake`
- **标题**: skill-stocktake
- **路径**: `ecc-imports/skill-stocktake/SKILL.md`
- **用途**: 适用于：auditing Claude skills and commands for quality. Supports Quick Scan (changed skills only) and Full Stocktake modes with sequential subagent batch evalua...

### 162. `social-graph-ranker`
- **标题**: Social Graph Ranker
- **路径**: `ecc-imports/social-graph-ranker/SKILL.md`
- **用途**: Weighted social-graph ranking for warm intro discovery, bridge scoring, and network gap analysis across X and LinkedIn. Use when the user wants the reusable...

### 163. `springboot-patterns`
- **标题**: Spring Boot Development Patterns
- **路径**: `ecc-imports/springboot-patterns/SKILL.md`
- **用途**: Spring Boot architecture patterns, REST API design, layered services, data access, caching, async processing, and logging. Use for Java Spring Boot backend w...

### 164. `springboot-security`
- **标题**: Spring Boot Security Review
- **路径**: `ecc-imports/springboot-security/SKILL.md`
- **用途**: Spring Security best practices for authn/authz, validation, CSRF, secrets, headers, rate limiting, and dependency security in Java Spring Boot services.

### 165. `springboot-tdd`
- **标题**: Spring Boot TDD Workflow
- **路径**: `ecc-imports/springboot-tdd/SKILL.md`
- **用途**: Test-driven development for Spring Boot using JUnit 5, Mockito, MockMvc, Testcontainers, and JaCoCo. Use when adding features, fixing bugs, or refactoring.

### 166. `springboot-verification`
- **标题**: Spring Boot Verification Loop
- **路径**: `ecc-imports/springboot-verification/SKILL.md`
- **用途**: Verification loop for Spring Boot projects: build, static analysis, tests with coverage, security scans, and diff review before release or PR.

### 167. `strategic-compact`
- **标题**: Strategic Compact Skill
- **路径**: `ecc-imports/strategic-compact/SKILL.md`
- **用途**: Suggests manual context compaction at logical intervals to preserve context through task phases rather than arbitrary auto-compaction.

### 168. `swift-actor-persistence`
- **标题**: Swift Actors for Thread-Safe Persistence
- **路径**: `ecc-imports/swift-actor-persistence/SKILL.md`
- **用途**: Thread-safe data persistence in Swift using actors — in-memory cache with file-backed storage, eliminating data races by design.

### 169. `swift-concurrency-6-2`
- **标题**: Swift 6.2 Approachable Concurrency
- **路径**: `ecc-imports/swift-concurrency-6-2/SKILL.md`
- **用途**: Swift 6.2 Approachable Concurrency — single-threaded by default, @concurrent for explicit background offloading, isolated conformances for main actor types.

### 170. `swift-protocol-di-testing`
- **标题**: Swift Protocol-Based Dependency Injection for Testing
- **路径**: `ecc-imports/swift-protocol-di-testing/SKILL.md`
- **用途**: Protocol-based dependency injection for testable Swift code — mock file system, network, and external APIs using focused protocols and Swift Testing.

### 171. `swiftui-patterns`
- **标题**: SwiftUI Patterns
- **路径**: `ecc-imports/swiftui-patterns/SKILL.md`
- **用途**: SwiftUI architecture patterns, state management with @Observable, view composition, navigation, performance optimization, and modern iOS/macOS UI best practi...

### 172. `tdd-workflow`
- **标题**: Test-Driven Development Workflow
- **路径**: `ecc-imports/tdd-workflow/SKILL.md`
- **用途**: Use this skill when writing new features, fixing bugs, or refactoring code. Enforces test-driven development with 80%+ coverage including unit, integration,...

### 173. `team-builder`
- **标题**: Team Builder
- **路径**: `ecc-imports/team-builder/SKILL.md`
- **用途**: Interactive agent picker for composing and dispatching parallel teams

### 174. `terminal-ops`
- **标题**: Terminal Ops
- **路径**: `ecc-imports/terminal-ops/SKILL.md`
- **用途**: Evidence-first repo execution workflow for ECC. Use when the user wants a command run, a repo checked, a CI failure debugged, or a narrow fix pushed with exa...

### 175. `tinystruct-patterns`
- **标题**: tinystruct Development Patterns
- **路径**: `ecc-imports/tinystruct-patterns/SKILL.md`
- **用途**: 适用于：developing application modules or microservices with the tinystruct Java framework. Covers routing, context management, JSON handling with Builder, and C...

### 176. `token-budget-advisor`
- **标题**: Token Budget Advisor (TBA)
- **路径**: `ecc-imports/token-budget-advisor/SKILL.md`
- **用途**: 暂无 frontmatter 描述，建议直接查看该 skill 的 SKILL.md 获取完整用法。

### 177. `ui-demo`
- **标题**: UI Demo Video Recorder
- **路径**: `ecc-imports/ui-demo/SKILL.md`
- **用途**: Record polished UI demo videos using Playwright. Use when the user asks to create a demo, walkthrough, screen recording, or tutorial video of a web applicati...

### 178. `unified-notifications-ops`
- **标题**: Unified Notifications Ops
- **路径**: `ecc-imports/unified-notifications-ops/SKILL.md`
- **用途**: Operate notifications as one ECC-native workflow across GitHub, Linear, desktop alerts, hooks, and connected communication surfaces. Use when the real proble...

### 179. `verification-loop`
- **标题**: Verification Loop Skill
- **路径**: `ecc-imports/verification-loop/SKILL.md`
- **用途**: A comprehensive verification system for Claude Code sessions.

### 180. `video-editing`
- **标题**: Video Editing
- **路径**: `ecc-imports/video-editing/SKILL.md`
- **用途**: AI-assisted video editing workflows for cutting, structuring, and augmenting real footage. Covers the full pipeline from raw capture through FFmpeg, Remotion...

### 181. `videodb`
- **标题**: VideoDB Skill
- **路径**: `ecc-imports/videodb/SKILL.md`
- **用途**: See, Understand, Act on video and audio. See- ingest from local files, URLs, RTSP/live feeds, or live record desktop; return realtime context and playable st...

### 182. `visa-doc-translate`
- **标题**: visa-doc-translate
- **路径**: `ecc-imports/visa-doc-translate/SKILL.md`
- **用途**: Translate visa application documents (images) to English and create a bilingual PDF with original and translation

### 183. `workspace-surface-audit`
- **标题**: Workspace Surface Audit
- **路径**: `ecc-imports/workspace-surface-audit/SKILL.md`
- **用途**: Audit the active repo, MCP servers, plugins, connectors, env surfaces, and harness setup, then recommend the highest-value ECC-native skills, hooks, agents,...

### 184. `x-api`
- **标题**: X API
- **路径**: `ecc-imports/x-api/SKILL.md`
- **用途**: X/Twitter API integration for posting tweets, threads, reading timelines, search, and analytics. Covers OAuth auth patterns, rate limits, and platform-native...

---

## mlops/evaluation

### 1. `lm-evaluation-harness`
- **标题**: lm-evaluation-harness - LLM Benchmarking
- **路径**: `mlops/evaluation/lm-evaluation-harness/SKILL.md`
- **用途**: lm-eval-harness: benchmark LLMs (MMLU, GSM8K, etc.).

### 2. `weights-and-biases`
- **标题**: Weights & Biases: ML Experiment Tracking & MLOps
- **路径**: `mlops/evaluation/weights-and-biases/SKILL.md`
- **用途**: W&B: log ML experiments, sweeps, model registry, dashboards.

---

## mlops/inference

### 1. `llama-cpp`
- **标题**: llama.cpp + GGUF
- **路径**: `mlops/inference/llama-cpp/SKILL.md`
- **用途**: llama.cpp local GGUF inference + HF Hub model discovery.

### 2. `obliteratus`
- **标题**: OBLITERATUS Skill
- **路径**: `mlops/inference/obliteratus/SKILL.md`
- **用途**: OBLITERATUS: abliterate LLM refusals (diff-in-means).

### 3. `outlines`
- **标题**: Outlines: Structured Text Generation
- **路径**: `mlops/inference/outlines/SKILL.md`
- **用途**: Outlines: structured JSON/regex/Pydantic LLM generation.

### 4. `vllm`
- **标题**: vLLM - High-Performance LLM Serving
- **路径**: `mlops/inference/vllm/SKILL.md`
- **用途**: vLLM: high-throughput LLM serving, OpenAI API, quantization.

---

## mlops/models

### 1. `audiocraft`
- **标题**: AudioCraft: Audio Generation
- **路径**: `mlops/models/audiocraft/SKILL.md`
- **用途**: AudioCraft: MusicGen text-to-music, AudioGen text-to-sound.

### 2. `segment-anything`
- **标题**: Segment Anything Model (SAM)
- **路径**: `mlops/models/segment-anything/SKILL.md`
- **用途**: SAM: zero-shot image segmentation via points, boxes, masks.

---

## mlops/research

### 1. `dspy`
- **标题**: DSPy: Declarative Language Model Programming
- **路径**: `mlops/research/dspy/SKILL.md`
- **用途**: DSPy: declarative LM programs, auto-optimize prompts, RAG.

---

## mlops/training

### 1. `axolotl`
- **标题**: Axolotl Skill
- **路径**: `mlops/training/axolotl/SKILL.md`
- **用途**: Axolotl: YAML LLM fine-tuning (LoRA, DPO, GRPO).

### 2. `trl-fine-tuning`
- **标题**: TRL - Transformer Reinforcement Learning
- **路径**: `mlops/training/trl-fine-tuning/SKILL.md`
- **用途**: TRL: SFT, DPO, PPO, GRPO, reward modeling for LLM RLHF.

### 3. `unsloth`
- **标题**: Unsloth Skill
- **路径**: `mlops/training/unsloth/SKILL.md`
- **用途**: Unsloth: 2-5x faster LoRA/QLoRA fine-tuning, less VRAM.

---

## 五、怎么继续用这个索引

- 如果你已经知道 skill 名：直接去对应目录看 `SKILL.md`。
- 如果你只知道任务：先告诉我任务目标，我可以按这个索引帮你筛出最合适的 3~5 个 skills。
- 如果你想继续治理 skills：我也可以基于这个索引继续帮你做“重名检查 / 低质量 skill 筛查 / 分类重组 / 中英文说明统一”。

---

**文档版本**: 2.0
**最后更新**: 2026-05-12
**Skills 总数**: 332
**统计口径**: `/home/ubuntu/.hermes/skills/**/SKILL.md`
