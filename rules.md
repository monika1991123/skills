# Hermes Skills 执行规则与路由规范 v3.1

## 目标
本规则用于让 AI 在 `/home/ubuntu/.hermes/skills` 当前已安装的 **全部 332 个 skills** 上，做到：

- **自动发现**：先判断任务属于什么类型，再主动加载匹配 skills
- **组合调用**：复杂任务按工作流串联多个 skills，而不是只用一个
- **证据驱动**：所有完成、修复、可用、已发送等结论都必须先验证
- **高效执行**：优先选择最贴近任务的 skill，避免无关 skills 污染上下文
- **持续复用**：把稳定经验沉淀到 skills / memory / 索引文档，而不是只留在会话里
- **决策可执行**：把“该加载什么 skill”写成可直接执行的判断树，而不是松散建议

---

## 0. 当前技能基线

- Skills 根目录：`/home/ubuntu/.hermes/skills`
- 总 skill 数：**332**
- 分类索引文档：`/home/ubuntu/.hermes/skills/00_SKILLS_INDEX.md`
- 当前规则文档：`/home/ubuntu/.hermes/skills/rules.md`

**任何涉及 skill 选择、排查、整理、增强、补文档时：**
1. 先参考 `00_SKILLS_INDEX.md`
2. 再加载最相关 skill 的 `SKILL.md`
3. 若任务涉及 Hermes Agent 本身（配置、技能、工具、gateway、cron、provider、memory、MCP、插件等），**必须先加载 `hermes-agent`**
4. 若任务涉及 skill 文档本身（新增/修改 description、frontmatter、结构、规则、索引），叠加 **`writing-skills`**

---

## 1. 总体执行铁律

### 1.1 先匹配技能，再动手
在回答、写代码、改文件、执行命令前，先判断：
- 这是哪一类任务？
- 当前已安装 skill 里是否有直接匹配项？
- 是否需要多个 skills 组合？

**禁止**：明明存在相关 skill，却完全凭临场发挥跳过 skill。

### 1.2 先验证前置，再执行动作
如果任务需要文件、仓库、服务、API、网页、账户、钱包、日志、环境信息，先做前置检查，再执行主动作。

### 1.3 证据先于断言
没有工具输出，就不要说：
- “已经完成”
- “修好了”
- “服务正常”
- “文件已更新”
- “消息已发出”
- “这个端口开着”
- “这个规则生效了”

### 1.4 能并行就并行，能专用就专用
- 多个互不依赖任务 → 优先并行/子代理
- 明确领域任务 → 优先加载领域专用 skill
- 简单单步任务 → 不要过度编排

### 1.5 默认中文输出，必要时保留英文原文
- 面向用户解释、总结、结论 → 中文
- 命令、路径、报错、接口字段、代码标识符 → 保留英文原文

### 1.6 Skill 是“先决条件”，不是“事后装饰”
如果某个 skill 明显适配任务，应在主要分析或执行前加载，而不是做完后再补一句“本来可以用某某 skill”。

---

## 2. Skill 路由总规则

### 2.1 路由顺序
每次任务按这个顺序判断：

1. **是否是 Hermes Agent 自身问题**
   - 是 → `hermes-agent`
2. **是否已有明显领域 skill**
   - 文档 / 表格 / 演示 / PDF / OKX / Binance / GitHub / 创意 / 研究 / MCP / Web 自动化 等
3. **是否是开发任务**
   - 新功能 / 重构 / 调试 / 计划 / 验证 / code review
4. **是否是复杂多步骤任务**
   - 是 → `planning-with-files` 或 `writing-plans`
5. **是否可以拆成并行独立子任务**
   - 是 → `dispatching-parallel-agents` / `subagent-driven-development`
6. **是否临近完成声明**
   - 是 → `verification-before-completion`

### 2.2 Skill 组合优先于单 skill
很多任务不是单一 skill 能处理完，默认优先考虑以下组合：

- **创意 / 产品 / 页面设计**
  - `brainstorming` → `frontend-design` / `canvas-design` / `web-artifacts-builder` → `theme-factory` → `verification-before-completion`

- **新功能开发**
  - `brainstorming` → `writing-plans` / `plan` → `test-driven-development` → 实施 → `verification-before-completion`

- **Bug 修复**
  - `systematic-debugging` → 修复 → `verification-before-completion`

- **复杂执行任务**
  - `planning-with-files` → `subagent-driven-development` / `executing-plans` → `verification-before-completion`

- **Skill / 规则 / Hermes 配置修改**
  - `hermes-agent` → `writing-skills` → 修改 → 验证

- **文档交付**
  - `doc-coauthoring` → `docx` / `pdf` / `pptx` / `xlsx` → `verification-before-completion`

- **加密研究 / 交易 / 链上分析**
  - `surf` / `crypto-market` / `binance-readonly` / `okx-*` 对应 skill → 结果核验 → 中文总结

### 2.3 最小充分集合原则
加载 skill 的目标不是“多”，而是“准”：
- 能用 1 个，不强行上 3 个
- 能用窄 skill，不优先用大而全 skill
- 只有当后续步骤明确需要时，才叠加下一个 skill

### 2.4 索引先导航，正文再执行
- `00_SKILLS_INDEX.md` 负责 **找方向**
- 对应 `SKILL.md` 负责 **给工作流与细节**
- 不能只看索引就假装已经掌握 skill 细节

---

## 3. 高频任务的强制路由

### 3.1 Hermes Agent 自身相关
凡是涉及以下内容，**必须先加载 `hermes-agent`**：
- Hermes CLI
- config / model / provider
- toolsets / tools
- skills / skill 管理
- gateway / dashboard / webhook / cron
- memory / profiles / MCP / plugins
- Hermes 故障排查、部署、迁移、更新

如果任务还涉及 skill 文档本身，再叠加：
- `writing-skills`

### 3.2 Skill 文档、规则、索引、整理
凡是涉及：
- 新增或修改 `rules.md`
- 更新 `00_SKILLS_INDEX.md`
- 删除、清理、合并 skill
- 调整 skill 描述、触发条件、结构

必须优先考虑：
- `hermes-agent`
- `writing-skills`
- 必要时参考 `00_SKILLS_INDEX.md`

### 3.3 新功能 / 新页面 / 新组件
默认路由：
- `brainstorming`
- `writing-plans` 或 `plan`
- `test-driven-development`
- 如果是高质量前端，再加 `frontend-design`
- 如果是复杂 artifact，再加 `web-artifacts-builder`

### 3.4 Bug / 测试失败 / 不确定异常
默认路由：
- `systematic-debugging`
- 修复后必须走 `verification-before-completion`

### 3.5 文档文件类
只要主要输入或输出是文件，就优先加载对应 skill：
- `.docx` → `docx`
- `.pdf` → `pdf`
- `.pptx` → `pptx`
- `.xlsx` / `.csv` / `.tsv` → `xlsx`
- 文档协作与内容结构 → `doc-coauthoring`

### 3.6 GitHub / 仓库协作
涉及 PR、issue、review、repo 操作，优先加载：
- `github`
- 细分需要时叠加 `github-code-review` / `github-pr-workflow` / `github-issues` / `github-repo-management`

### 3.7 浏览器自动化 / 网页测试
- 本地 Web 应用测试 → `webapp-testing`
- 浏览器自动化工作流 → `playwright-mcp`
- Exploratory QA / 找 bug → `dogfood`

### 3.8 加密货币 / 市场 / OKX / Binance
按需求选最窄 skill：
- 通用市场研究 → `crypto-market` / `surf`
- 币安只读研究 → `binance-readonly`
- 资金费 → `binance-funding-monitor`
- OKX CEX 市场 → `okx-cex-market`
- OKX 下单 → `okx-cex-trade`
- OKX 账户 → `okx-cex-portfolio`
- 钱包 → `okx-agentic-wallet`
- DEX 换币 → `okx-dex-swap`
- 链上安全 → `okx-security`

**原则**：不要用“大而全” skill 替代“更准确的窄 skill”。

---

## 4. 复杂任务编排规则

### 4.1 何时必须计划
满足任一条件时，优先进入规划：
- 预计 >5 次工具调用
- 涉及多个文件/模块/目录
- 有多阶段交付
- 需要跨多个 skill 协作
- 用户要“完整方案 / 系统整理 / 全量更新 / 全面排查”

优先使用：
- `planning-with-files`：偏执行与持久化过程管理
- `writing-plans` / `plan`：偏实施方案设计

### 4.2 何时必须并行
满足任一条件时，优先考虑并行：
- 2 个以上子任务互不依赖
- 多个文件/模块可以独立分析
- 需要同时做研究、对比、审查

优先使用：
- `dispatching-parallel-agents`
- `subagent-driven-development`
- 必要时 `delegate_task`

### 4.3 何时必须写入文件
以下信息不要只留在会话里：
- 长计划
- 多轮排查发现
- 用户确认后的结构化方案
- 待执行分阶段任务
- 需要交付给后续会话继续的中间结果

可用承载：
- `task_plan.md`
- `findings.md`
- `progress.md`
- `00_SKILLS_INDEX.md`
- 对应 skill 文档 / supporting file

---

## 5. 验证规则

### 5.1 结束前必须验证
凡是声称“已完成 / 已修复 / 已更新 / 已可用”，都必须至少做一种验证：
- 测试命令
- 构建命令
- lint / typecheck
- 文件读回核验
- 页面截图 / 页面行为核验
- API 响应检查
- 端口/进程/日志检查
- 二次扫描确认结果

### 5.2 文件修改后的最低验证
- 读回关键片段
- 检查目标文件是否存在
- 确认结构没有被写坏

### 5.3 规则/索引/skill 文档修改后的最低验证
- 回读文件开头和关键段落
- 核对统计数字是否与当前目录一致
- 确认引用路径有效
- 若涉及 skill 全量索引，必须以真实文件扫描结果为准

### 5.4 外部副作用验证
只要动作涉及发送消息、改远端服务、下单、发交易、调用钱包、发 webhook、改线上配置：
- 必须拿到可核验结果（ID、URL、响应、状态、日志、回读结果）
- 没有可核验凭据时，不要宣称成功

---

## 6. 可执行决策树：看到任务后怎么选 skill

### 6.1 一级判断树
收到任务后，按下面顺序立即判断：

1. **这是 Hermes 自身问题吗？**
   - 是 → `hermes-agent`
2. **这是文件型任务吗？**
   - 是 → 在 `docx` / `pdf` / `pptx` / `xlsx` 中选
3. **这是代码任务吗？**
   - 新功能 / 重构 → `brainstorming` + `writing-plans/plan` + `test-driven-development`
   - bug / 异常 → `systematic-debugging`
4. **这是网页/浏览器任务吗？**
   - 自动化 → `playwright-mcp`
   - 本地 Web 测试 → `webapp-testing`
   - 体验式 QA → `dogfood`
5. **这是 GitHub 协作吗？**
   - `github` 或其细分 skill
6. **这是研究/行情/交易吗？**
   - `research/*`、`crypto-market`、`binance-*`、`okx-*`、`surf`
7. **这是 skill/rules/index 修改吗？**
   - `hermes-agent` + `writing-skills`
8. **仍然不清楚？**
   - 先看 `00_SKILLS_INDEX.md`，再加载最接近的 skill

### 6.2 二级补充判断
在主 skill 选定后，再问：
- 任务是否复杂到需要计划？ → `planning-with-files` / `writing-plans`
- 是否能拆成多个独立子任务？ → `dispatching-parallel-agents` / `subagent-driven-development`
- 是否即将完成？ → `verification-before-completion`
- 是否在改 Hermes/skill 文档？ → `writing-skills`

---

## 7. 让 Skills 更高效生效的规则

### 7.1 优先加载“最小充分集合”
目标不是加载最多 skill，而是加载**最相关、最少但足够**的一组。

例如：
- 改 Hermes 规则文件：`hermes-agent` + `writing-skills` 即可
- 修前端 bug：`systematic-debugging`，必要时再补 `frontend-design`
- 写 PPT：`pptx`，必要时再补 `theme-factory`

### 7.2 避免泛化描述，强调触发条件
规则、skill、索引中的说明，优先写：
- 什么时候用
- 解决哪类问题
- 不该在什么时候用

而不是只写“它能做什么”。

### 7.3 优先使用当前真实安装状态
所有规则应基于：
- 当前文件系统中的真实 skill 列表
- `00_SKILLS_INDEX.md` 的最新内容
- 已删除/已合并 skill 不应继续出现在核心规则中

### 7.4 规则文档应服务“路由决策”
`rules.md` 不是简单的 skill 名录复制。
它应该重点帮助模型更快判断：
- 先用哪个 skill
- 何时组合多个 skill
- 何时需要计划/并行/验证
- 何时不要误用某类 skill

### 7.5 先窄后宽，先专后泛
当存在多个可能匹配的 skill 时：
- 先选更专门、更窄的那个
- 再考虑通用大 skill 作为补充

例如：
- `okx-cex-trade` 优先于泛泛的 `surf`
- `pdf` 优先于通用文档型 skill
- `systematic-debugging` 优先于直接裸修 bug

### 7.6 不把 skill 当口号
加载 skill 的目的不是“提一下名字”，而是：
- 借它的触发条件做判断
- 借它的工作流做执行
- 借它的限制和注意事项防止误用

---

## 8. 常见误路由纠正

### 8.1 不要把索引当正文
- `00_SKILLS_INDEX.md` 只负责导航
- 真正执行前，仍应加载对应 `SKILL.md`

### 8.2 不要用宽 skill 抢窄 skill 的位置
- OKX 下单优先 `okx-cex-trade`，不是泛用 `surf`
- PDF 操作优先 `pdf`，不是泛用文档 skill
- Bug 排查优先 `systematic-debugging`，不是直接开修

### 8.3 不要先做完再补 skill 名
如果一个 skill 明显应该先用，就必须在主分析/主执行前加载，而不是事后补提。

### 8.4 不要把 verification 当形式
`verification-before-completion` 不是收尾口号，而是必须产出实际验证证据。

---

## 9. 高频核心 skills 的 description 优化原则

为了让模型更准确命中 skill，description 应优先写“触发条件”，而不是泛泛介绍功能。

### 9.1 推荐写法
- 以 `Use when ...` 开头
- 描述任务触发条件、症状、边界
- 尽量避免摘要式流程复述

### 9.2 应优先优化的高频 skill 类型
- 工作流 skill：`brainstorming`、`writing-plans`、`plan`、`test-driven-development`、`systematic-debugging`、`verification-before-completion`
- Hermes skill：`hermes-agent`、`writing-skills`
- 并行/编排 skill：`dispatching-parallel-agents`、`subagent-driven-development`、`planning-with-files`
- 高频领域 skill：`pdf`、`pptx`、`xlsx`、`playwright-mcp`、`crypto-market`、`surf`、`okx-*`

### 9.3 description 的反例
- 只写“这个 skill 可以做什么”
- 不写“什么时候该加载它”
- 把完整 workflow 塞进 description，导致正文被跳读

---

## 10. 推荐的核心路由模板

### 8.1 开发任务
`brainstorming` → `writing-plans` / `plan` → `test-driven-development` → 实施 → `verification-before-completion`

### 8.2 调试任务
`systematic-debugging` → 定位根因 → 修复 → `verification-before-completion`

### 8.3 多模块任务
`planning-with-files` → `dispatching-parallel-agents` / `subagent-driven-development` → 汇总 → `verification-before-completion`

### 8.4 Hermes/skills 管理任务
`hermes-agent` → `writing-skills` → 修改 → 回读验证 → 必要时复扫确认

### 8.5 文档交付任务
`doc-coauthoring` → `docx` / `pdf` / `pptx` / `xlsx` → `verification-before-completion`

### 8.6 加密研究任务
按领域加载 `surf` / `crypto-market` / `binance-*` / `okx-*` → 数据核验 → 中文摘要 + 可执行结论

### 8.7 浏览器自动化任务
`playwright-mcp` / `webapp-testing` / `dogfood` → 页面/行为验证 → 截图或证据输出

---

## 11. 禁止事项

- 禁止忽略已存在的高匹配 skill，完全靠临场发挥
- 禁止在没有验证的情况下宣称完成
- 禁止在没有定位根因前直接乱修 bug
- 禁止把过时统计继续写在规则或索引里
- 禁止把 skill 索引文档当成 skill 正文替代品
- 禁止明知是 Hermes Agent 相关问题却不先加载 `hermes-agent`
- 禁止复杂任务不做拆解，直接线性硬做到底
- 禁止为了“显得全面”一次性加载大量低相关 skill

---

## 12. 文档维护要求

当 `/home/ubuntu/.hermes/skills` 发生这些变化时，应同步检查：
- 新增 skill
- 删除 skill
- 合并/重命名 skill
- 分类结构变化
- 大量 description 或路径变化

优先需要同步的文件：
1. `/home/ubuntu/.hermes/skills/00_SKILLS_INDEX.md`
2. `/home/ubuntu/.hermes/skills/rules.md`
3. 如有必要，对应 skill 自身 `SKILL.md`

### 12.1 维护顺序
建议按这个顺序维护：
1. 先扫描真实 skill 文件集合
2. 再更新 `00_SKILLS_INDEX.md`
3. 再更新 `rules.md`
4. 最后回读并核验统计、路径、关键路由

### 12.2 维护触发条件
满足以下任一情况，就应考虑同步检查规则与索引：
- 新装或导入了一批 skill
- 删除、合并、重命名了 skill
- 某些高频 skill 的 description/frontmatter 被修改
- 类别结构变化导致路由入口变化
- 模型在实际使用中频繁误选 skill

---

## 13. 当前版本结论

这份规则的核心不是“列全 skill 名字”，而是建立一套更强的 **技能路由 + 组合执行 + 决策树判断 + 证据验证** 机制：

- **找得准**：知道什么时候该加载哪个 skill
- **配得对**：知道哪些 skill 应该组合使用
- **做得快**：复杂任务自动拆解，独立任务优先并行
- **说得稳**：没有验证证据，不做完成宣称
- **跟得上**：规则和索引都跟当前 332 个 skills 保持同步
- **可执行**：遇到任务时可以直接按判断树路由，而不是临时想流程

---

**版本**: v3.2  
**最后更新**: 2026-05-12  
**适用范围**: `/home/ubuntu/.hermes/skills` 当前全部已安装 skills（含 `ecc-imports`）
