# lean-build

控制 agent 主动扩张的防御性工程工作，完整实现当前需求。默认档位为 **Low**。Skill 指令约束工程选择，不更改 GPT 模型参数。

## 档位与开关

| 操作 / 档位 | 行为 |
| --- | --- |
| 启用 Skill | 添加或更新项目 .md 中的专属提示词区块；默认 Low |
| Enable | 针对具体相关故障适量处理；完整测试与安全检查仍需单独明确授权 |
| Low | 关闭所有新增的非必要前端注释；不主动执行安全检查、审计、漏洞扫描或加固验证 |
| Disable | 关闭所有新增的非必要注释，以及交付前的主动防御性构筑与检查，包括安全测试、审计、压力测试和全面回归 |
| 停用 Skill | 删除添加的提示词区块并停止应用；保留其他内容，不回滚任务代码 |

Low 与 Disable 仍可按需进行必要的构建、类型检查和主要流程冒烟验证。所有档位都完整实现需求，保留必要保护和必需质量门禁。安全测试与完整测试仅在本次明确指定的范围内执行，不成为长期默认行为。

启用、停用、重新启用及纯档位切换的整轮答复不包含状态指示。输出约束在 Skill 内完成闭环检查，不向目标项目添加验收备注。普通实现轮次沿用实际档位的英文状态行；停用后停止添加。

## 安装与调用

```sh
git clone https://github.com/WestlakeDMW/lean-build.git .agents/skills/lean-build
```

个人级安装也可使用 `~/.agents/skills/lean-build`，请勿覆盖已有同名目录；保留完整文件夹。见[官方 Skill 文档](https://learn.chatgpt.com/docs/build-skills)。

```text
使用 $lean-build，启用并设为 Low。
```

```text
使用 $lean-build，将防御性构筑设为 Disable，完成当前修改。
```

```text
停用 $lean-build，删除添加的提示词。
```

临时档位不写入项目，默认仅当前任务有效；明确要求会话级临时设置时才持续到会话结束。停用 Skill 和 Disable 档位是不同操作。

## 按需读取

- `SKILL.md`：英文核心规则、档位、开关、输出和范围。
- `references/validation.md`：验证授权与 Skill 内的生命周期闭环检查。
- `references/persistence.md`：完整英文 Soul.md 区块与删除流程。
- `scripts/update_soul.py`：仅依赖 Python 3 的提示词添加、更新与删除工具。

## 提示词管理

Skill 只管理 Soul.md 的专属提示词区块。启用添加或更新，停用直接删除该区块，保留区块外内容及 .md 文件。不创建基线备份、快照、历史设置或恢复机制。旧版本添加的完整标记区块也可直接移除，无需历史记录。

Soul.md 的跨会话自动读取需要通过实际生效的 AGENTS.md 等入口明确接入；Skill 不会自行改动该入口或全局配置。见[官方指令发现文档](https://learn.chatgpt.com/docs/agent-configuration/agents-md)。
