# Contributing Guide

感谢你对 vllm-ascend-harness 的关注！本文档描述如何参与本项目贡献。

## 上游溯源声明

**本项目在 OpenHarness 基础上演进**，保留上游开源声明与 MIT License。感谢 OpenHarness 社区提供的基础架构与设计思想。

## 架构变更与 RFC

**重大架构变更需要社区 RFC 讨论。** 如果你的贡献涉及以下方面，请先在 [Issues](https://github.com/vllm-ascend/vllm-ascend-harness/issues) 发起 RFC 讨论，获得社区共识后再开始实现：

- 核心微内核（AgentLoop / EventBus / PluginManager）接口变更
- 模块间通信契约变更
- 新增核心依赖
- 沙箱隔离策略变更
- 评测指标体系变更

不影响公共接口的内部重构、Bug 修复、文档改进无需 RFC。

## 开发环境

```bash
git clone https://github.com/vllm-ascend/vllm-ascend-harness.git
cd vllm-ascend-harness
pip install -e ".[dev]"
```

## 代码规范

- 遵循 **vLLM-Ascend 社区 Python 编码规范**。
- 使用 **ruff** 进行 lint：`ruff check src tests`
- 使用 **flake8** 进行补充 lint：`flake8 src tests`
- 类型标注：公共接口必须包含类型标注，使用 `from __future__ import annotations`。
- 代码风格：行宽 99，4 空格缩进。

## 提交前检查

```bash
ruff check src tests
flake8 src tests
pytest tests -q
```

所有检查通过后方可提交 PR。

## 提交规范

- Commit message 使用 Conventional Commits 格式：`feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `ci:`
- PR 标题应简洁描述变更内容。
- PR 描述应包含：变更动机、实现方式、测试方式。

## 测试

- 单元测试位于 `tests/` 目录，按模块组织。
- 新增功能必须附带单元测试。
- 运行测试：`pytest tests -q`

## 目录结构

```
src/vllm_ascend_harness/
├── core/        # 微内核
├── adapters/    # 模型后端适配器
├── sandbox/     # 任务沙箱
├── evaluator/   # 评测模块
├── telemetry/   # 遥测
└── skills/      # 内置技能
tests/
├── test_core/
├── test_adapters/
├── test_sandbox/
└── test_evaluator/
```

## 许可证

贡献的代码将在 [MIT License](../LICENSE) 下发布。提交即表示同意以该许可证发布。
