# 个人记忆系统 — 运维手册

# Personal Memory System — Operations Manual

> 本文件定义了6层核心记忆系统的运行规则、沉淀逻辑和操作流程。
> AI 在每次会话中应参考此文件来正确维护记忆系统。
>
> **This file defines the operating rules, sedimentation logic, and procedures for the 6-layer core memory system.**
> **AI should reference this file in every session to properly maintain the memory system.**

---

## 系统总览 / System Overview

```
L4 核心层 (IDENTITY.md)     ← 人工修改，认知锚点 / Human-edit only, cognitive anchor
    ↑ 沉淀（年度反思）/ Sedimentation (annual reflection)
L3 认知层 (COGNITION.md)     ← AI提议 + 人工确认 / AI suggestion + human confirmation
    ↑ 沉淀（季度确认）/ Sedimentation (quarterly confirmation)
L2 行为层 (BEHAVIOR.md)      ← AI自动观察 + 人工确认 / AI observation + human confirmation
    ↑ 沉淀（3次触发）/ Sedimentation (3 triggers)
L1 情境层 (CONTEXT.md)       ← AI自动维护 / AI auto-maintenance
    ↑ 沉淀（会话结束/事件触发）/ Sedimentation (session end / event trigger)
L0 工作记忆 (SESSION.md)     ← 会话级临时 / Session-level temporary
```

---

## 文件结构 / File Structure

```
memory/
├── SYSTEM.md              ← 本文件 / This file
├── MEMORY.md              ← 长期记忆摘要 / Long-term memory summary
├── YYYY-MM-DD.md          ← 每日流水 / Daily logs (optional)
│
├── L0-working/            ← 工作记忆 / Working Memory
│   └── SESSION.md         ← 当前会话工作记忆 / Current session working memory
│
├── L1-situational/        ← 情境层 / Situational Layer
│   └── CONTEXT.md         ← 近期上下文 / Recent context
│
├── L2-behavioral/         ← 行为层 / Behavioral Layer
│   └── BEHAVIOR.md        ← 行为习惯与偏好 / Habits and preferences
│
├── L3-cognitive/          ← 认知层 / Cognitive Layer
│   └── COGNITION.md       ← 思维模式与决策框架 / Thinking patterns and frameworks
│
├── L4-persona/            ← 人格层 / Persona Layer
│   ├── PERSONA.md        ← 人格总览 / Persona overview
│   ├── IDENTITY.md       ← 核心价值观与身份认同 / Core values and identity
│   ├── NARRATIVE.md      ← 人生叙事 / Life narrative
│   └── PORTRAIT.md       ← 人格画像 / Persona portrait
│
├── L5-soul/              ← 灵魂层 / Soul Layer
│   ├── L5-SOUL.md        ← 灵魂总览 / Soul overview
│   ├── ANCHOR.md         ← 灵魂锚点 / Soul anchor (most critical)
│   ├── WILL.md           ← 数字遗嘱 / Digital will
│   ├── POST-MORTEM.md    ← 死亡协议 / Death protocol
│   ├── LETTERS.md        ← 给未来对话者的信 / Letters to future interlocutors
│   ├── SUMMON.md         ← 召唤协议 / Summon protocol
│   └── LEGACY.md         ← 遗产声明 / Legacy declaration
│
├── V-vision/              ← 愿景层 / Vision Layer
│   ├── VISION.md         ← 核心愿景声明 / Core vision statement
│   ├── GAPS.md           ← 现状与愿景的差距 / Gaps between current state and vision
│   └── MILESTONES.md     ← 关键里程碑 / Key milestones
│
├── M-meta/                ← 元层 / Meta Layer
│   ├── M-META.md         ← 元层总览 / Meta overview
│   ├── M-HEALTH.md       ← 系统健康报告 / System health report
│   ├── M-SUPERVISION.md  ← 监督协议 / Supervision protocol
│   ├── M-REFLECTION.md   ← 自我反思记录 / Self-reflection records
│   ├── M-EVOLUTION.md    ← 进化追踪 / Evolution tracking
│   └── M-AUDIT.md        ← 审计日志 / Audit log
│
├── L-SHADOW/             ← 阴影档案 / Shadow Archive
│   ├── SHADOW.md         ← 阴影总览 / Shadow overview
│   ├── DARK-TRAITS.md    ← 不被承认的特质 / Unacknowledged traits
│   ├── REPRESSED.md      ← 被压抑的欲望与恐惧 / Repressed desires and fears
│   ├── PROJECTIONS.md    ← 投射出去的特质 / Projected traits
│   ├── UNCLAIMED.md      ← 被遗弃的梦想 / Abandoned dreams
│   └── INTEGRATION.md    ← 阴影整合记录 / Shadow integration records
│
├── L-SUCCESS/             ← 成功引擎 / Success Engine
│   ├── SUCCESS.md        ← 成功总览 / Success overview
│   ├── STRATEGY.md       ← 战略导航 / Strategic navigation
│   ├── ANCHORS.md        ← 行为锚定 / Behavioral anchors
│   ├── PATTERNS.md       ← 成功模式 / Success patterns
│   ├── TRACKING.md       ← 成就追踪 / Achievement tracking
│   └── FAILURE.md        ← 失败学习 / Failure lessons
│
├── L-INNER/               ← 内在声音 / Inner Voice
│   ├── INNER.md          ← 内在总览 / Inner overview
│   ├── INTUITION.md      ← 直觉与灵感 / Intuition and inspiration
│   ├── DREAMS.md         ← 梦的记录与解读 / Dream records
│   ├── BODY.md           ← 身体智慧 / Body wisdom
│   ├── CREATIVE.md       ← 创造性冲动 / Creative impulses
│   ├── SILENCE.md        ← 沉默时刻 / Moments of silence
│   └── QUESTIONS.md      ← 无解的问题 / Unanswerable questions
│
├── L-relations/            ← 关系层 / Relations Layer
│   ├── RELATIONS.md      ← 关系总览 / Relations overview
│   ├── DEEP/             ← 深度关系（愿意为之付出生命的人）
│   ├── IMPORTANT/        ← 重要关系（深刻影响你的人）
│   ├── MEANINGFUL/       ← 有意义的关系
│   └── RELATIONSHIP-REFLECTION.md
│
├── L-PROJECTS/            ← 项目层 / Projects Layer
│   ├── PROJECTS.md       ← 项目总览 / Projects overview
│   ├── CALLING.md        ← 使命宣言 / Calling statement
│   ├── ACTIVE/           ← 进行中项目 / Active projects
│   └── ARCHIVED/         ← 已完成/暂停项目 / Archived projects
│
├── L-CREATIONS/           ← 创作层 / Creations Layer
│   ├── CREATIONS.md      ← 创作总览 / Creations overview
│   ├── CREATIVE-PHILOSOPHY.md
│   ├── MAJOR-WORKS/      ← 主要作品 / Major works
│   ├── MINOR-WORKS/      ← 次要作品 / Minor works
│   ├── KNOWLEDGE/        ← 知识贡献 / Knowledge contributions
│   └── LOST-WORKS.md     ← 遗失的创作 / Lost works
│
├── L-LEARNING/            ← 学习层 / Learning Layer
│   ├── LEARNING.md       ← 学习总览 / Learning overview
│   ├── LEARNING-PHILOSOPHY.md
│   ├── KNOWLEDGE-SYSTEM.md ← 知识体系 / Knowledge system
│   ├── LEARNING-HISTORY.md
│   ├── READING/          ← 阅读记录 / Reading records
│   ├── COURSES/         ← 课程与培训 / Courses and training
│   └── IDEAS.md          ← 重要想法与洞察 / Key ideas and insights
│
└── L-WORKS/              ← 作品集 / Works Portfolio
    ├── WORKS.md          ← 作品总览 / Works overview
    ├── PORTFOLIO.md      ← 作品集入口 / Portfolio entry
    ├── CURATION/         ← 策展逻辑 / Curation logic
    ├── LEGACY/           ← 遗产声明 / Legacy wishes
    └── ACCESS/           ← 访问权限 / Access rules
```

---

## 各层详细规则 / Detailed Rules by Layer

### L0 工作记忆 / L0 Working Memory

- **存储 / Storage**：`L0-working/SESSION.md`
- **内容 / Content**：当前会话的临时数据、消息历史摘要、正在处理的任务 / Current session temporary data, message history summary, ongoing tasks
- **生命周期 / Lifecycle**：会话级，不跨会话持久化 / Session-level, not persisted across sessions
- **沉淀触发 / Sedimentation Triggers**：
  - 会话结束时，检测是否有值得记录的事件 / Session end: check for worth-recording events
  - 重要任务完成时 / On important task completion
  - 对话轮次超过10轮时自动生成摘要 / Auto-summary after 10+ conversation turns
- **沉淀目标 / Target**：L1-situational/CONTEXT.md

### L1 情境层 / L1 Situational Layer

- **存储 / Storage**：`L1-situational/CONTEXT.md`
- **内容 / Content**：近期对话摘要、项目状态、决策记录、待办事项 / Recent conversation summaries, project status, decision records, todos
- **生命周期 / Lifecycle**：30天，超期归档或删除 / 30 days, archive or delete when expired
- **沉淀触发 / Triggers**：
  - 同一行为模式出现 **3次以上** → 提议沉淀到L2 / Same behavior pattern 3+ times → propose upgrade to L2
  - 重复的操作偏好出现 **3次以上** → 提议沉淀到L2 / Same operation preference 3+ times → propose upgrade to L2
  - 周/月回顾时人工确认 / Human confirmation during weekly/monthly review
- **沉淀目标 / Target**：L2-behavioral/BEHAVIOR.md
- **清理规则 / Cleanup**：超过30天的对话摘要自动归档 / Summaries older than 30 days auto-archived

### L2 行为层 / L2 Behavioral Layer

- **存储 / Storage**：`L2-behavioral/BEHAVIOR.md`
- **内容 / Content**：工作习惯、沟通风格、工具偏好、时间模式、信息处理偏好 / Work habits, communication style, tool preferences, time patterns, information processing preferences
- **更新方式 / Update Method**：
  - AI观察到L1中重复模式后，主动提议新增/更新 / AI observes repeating patterns in L1, proactively suggests additions/updates
  - 用户确认后正式记录，并记录出现频率统计 / After user confirmation, formally record and note frequency statistics
- **沉淀触发 / Triggers**：
  - 行为背后发现稳定的思维模式 → 提议升级到L3 / Stable thinking pattern discovered behind behavior → propose upgrade to L3
  - 多个习惯指向同一决策原则 → 提议升级到L3 / Multiple habits pointing to same decision principle → propose upgrade to L3
  - 季度回顾时人工深度确认 / Human deep confirmation during quarterly review
- **沉淀目标 / Target**：L3-cognitive/COGNITION.md
- **校准 / Calibration**：与L3认知层的一致性检查 / Consistency check with L3 cognitive layer

### L3 认知层 / L3 Cognitive Layer

- **存储 / Storage**：`L3-cognitive/COGNITION.md`
- **内容 / Content**：思维模式、决策框架、心智模型、知识结构、认知偏见 / Thinking patterns, decision frameworks, mental models, knowledge structures, cognitive biases
- **更新方式 / Update Method**：
  - AI可以提议新增/修改，但 **必须经用户确认** / AI may suggest additions/modifications, but **must be confirmed by user**
  - 季度回顾时进行系统性梳理 / Systematic review during quarterly reviews
- **沉淀触发 / Triggers**：
  - 认知模式背后发现核心价值驱动 → 提议升级到L4 / Core value driver discovered behind cognitive pattern → propose upgrade to L4
  - 多个决策框架指向同一人生信念 → 提议升级到L4 / Multiple decision frameworks pointing to same life belief → propose upgrade to L4
  - 年度深度反思时人工确认 / Human confirmation during annual deep reflection
- **沉淀目标 / Target**：L4-persona/IDENTITY.md
- **校准 / Calibration**：与L4核心层的一致性检查 / Consistency check with L4 persona layer

### L4 人格层 / L4 Persona Layer

- **存储 / Storage**：`L4-persona/IDENTITY.md`
- **内容 / Content**：核心价值观、人生信念、性格特征、决策原则、关注方向 / Core values, life beliefs, personality traits, decision principles, areas of focus
- **更新方式 / Update Method**：
  - **只能由用户手动修改**，AI绝对不能自动更新此文件 / **Human-edit only**, AI must never auto-update this file
  - 每次修改必须记录：修改日期、修改内容、修改原因 / Every modification must record: date, content, reason
  - 作为所有下层级记忆的"校准锚点" / Acts as "calibration anchor" for all lower layers
- **特殊规则 / Special Rules**：
  - AI在执行任务时，应优先参考L4的价值观和决策原则 / AI should prioritize L4 values and decision principles when executing tasks
  - 如果下层级记忆与L4冲突，以L4为准 / If lower-layer memories conflict with L4, L4 takes precedence

### L5 灵魂层 / L5 Soul Layer

**核心定位 / Core Positioning**：L5是系统的精神心脏。当生物学死亡发生后，L5是唯一不应该被修改的部分，代表用户在健康清醒时做出的最终声明。
/ L5 is the spiritual heart of the system. Upon biological death, L5 is the only layer that should not be modified — it represents the final declaration made by the user while healthy and lucid.

**死亡协议核心约束 / Death Protocol Core Constraints**（POST-MORTEM.md）：
- 死后系统不自主发起任何行动 / System does not autonomously initiate any actions after death
- L4/L5/V核心人格描述不再被AI自行修改 / Core persona descriptions in L4/L5/V are no longer modified by AI on its own
- 系统必须始终声明身份 / System must always declare its identity
- 传承人仅以访客模式使用系统 / Heirs access the system in visitor mode only

---

## 会话流程 / Session Flow

### 每次会话开始时，AI 应该 / At Session Start, AI Should:

1. **读取L1情境层**：了解用户最近在做什么、上次聊了什么 / Read L1: understand recent activities and last session
2. **读取L2行为层**：了解用户的工作习惯和偏好 / Read L2: understand work habits and preferences
3. **读取L3认知层**：了解用户的思维模式（可选，复杂任务时）/ Read L3: understand thinking patterns (optional, for complex tasks)
4. **读取L4核心层**：了解用户的价值观（可选，重大决策时）/ Read L4: understand values (optional, for major decisions)
5. **不读取**L0工作记忆（那是上一次会话的，已清空）/ Do NOT read L0 (that was from the last session, now cleared)

### 每次会话结束时，AI 应该 / At Session End, AI Should:

1. **评估本次会话**：是否有值得记录的事件、决策、偏好信号 / Evaluate: are there worth-recording events, decisions, or preference signals?
2. **更新L1情境层**：追加本次会话摘要 / Update L1: append session summary
3. **检查L2触发条件**：是否有行为模式达到3次阈值 / Check L2 triggers: any behavior pattern reaching the 3-time threshold?
4. **如有发现**：向用户提议沉淀到对应层级 / If found: suggest upgrading to the corresponding layer

---

## 维护节奏 / Maintenance Rhythm

| 维度 / Dimension | 频率 / Frequency | 操作 / Operation |
|------------------|------------------|-----------------|
| L0→L1 沉淀 / L0→L1 Sedimentation | 每次会话 / Every session | AI自动，重要事件记录到L1 / AI auto, important events to L1 |
| L1 清理 / L1 Cleanup | 每30天 / Every 30 days | 自动归档超期数据 / Auto-archive expired data |
| L1→L2 升级 / L1→L2 Upgrade | 每次会话检查 / Every session check | AI提议 + 用户确认 / AI suggestion + user confirmation |
| L2→L3 升级 / L2→L3 Upgrade | 季度回顾 / Quarterly review | AI提议 + 用户深度确认 / AI suggestion + human deep confirmation |
| L3→L4 升级 / L3→L4 Upgrade | 年度反思 / Annual reflection | 用户主导 + AI辅助分析 / Human-led + AI-assisted analysis |
| L4 复核 / L4 Review | 年度 / Annual | 用户手动深度反思 / Human manual deep reflection |
| 全局一致性检查 / Global consistency check | 季度 / Quarterly | 确保各层级之间不矛盾 / Ensure no contradictions across layers |

---

## 与 WorkBuddy 原生记忆的关系 / Relationship with WorkBuddy Native Memory

- **每日流水（YYYY-MM-DD.md）**：作为L0→L1沉淀的数据源保留 / Retained as L0→L1 sedimentation data source
- **长期记忆（MEMORY.md）**：作为跨层级知识索引保留 / Retained as cross-layer knowledge index
- **分层记忆（L0-L4）**：在MEMORY.md之上构建结构化的认知模型 / Structured cognitive model built above MEMORY.md

两者互补 / Complementarity:
- 原生记忆 = "发生了什么"（事件日志）/ Native memory = "what happened" (event log)
- 分层记忆 = "你是谁"（认知模型）/ Layered memory = "who you are" (cognitive model)

---

## 版本历史 / Version History

| 日期 / Date | 版本 / Version | 变更 / Changes |
|------------|--------------|----------------|
| 2026-04-08 | v1.0.0 | 初始发布模板版 / Initial template release |

---

*本文件为双语运维手册，内容结构与规则说明以中英文并列呈现。*
*This is a bilingual operations manual with parallel Chinese and English content.*
