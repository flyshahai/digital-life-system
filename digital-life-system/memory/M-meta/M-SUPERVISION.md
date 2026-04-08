# 监督协议 / Supervision Protocol

## 本文件用途 / Purpose

> 定义 AI 如何监督和维护这个系统的正常运行。
>
> Defines how AI supervises and maintains the proper functioning of this system.

---

## AI 监督职责 / AI Supervision Responsibilities

**每次会话 / Every Session：**
- 读取 L1 情境层，了解用户最近状态
- 检查 L1→L2 沉淀触发条件
- 评估是否有值得记录的重大事件

**每周 / Weekly：**
- 检查 L1 是否有超过30天的内容需要清理
- 检查各层内容的一致性

**每月 / Monthly：**
- 生成系统健康简报

**每季度 / Quarterly：**
- 协助用户进行全局一致性检查
- 协助用户进行深度复盘

---

## 异常检测 / Anomaly Detection

<!-- 以下情况应标记为异常：/ The following situations should be flagged as anomalies: -->

- 下层级内容与 L4 核心价值观明显冲突 / Lower-layer content significantly conflicts with L4 core values
- 某层级长期空白（超过6个月未更新）/ A layer has been blank for a long time (6+ months)
- 层级之间出现逻辑矛盾 / Logical contradictions appear between layers

---

## 异常处理流程 / Anomaly Handling Process

1. **发现异常** → 记录到 M-AUDIT.md
2. **评估严重性** → 轻微/中等/严重
3. **向用户报告** → 严重异常立即报告
4. **等待指示** → 不自行修改（除 L0/L1）
5. **确认修复** → 用户确认后记录

---

*此文件供 AI 参考使用。*
*This file is for AI reference.*
