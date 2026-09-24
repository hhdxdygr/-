from nonebot import on_message
from nonebot.adapters.qq import Bot, MessageEvent
from nonebot.rule import Rule

# ⚠️ 这里填写目标用户的 OpenID，不是 QQ 号
# 获取方式：让目标用户先给机器人发一条消息，然后在 Render 日志里查看
TARGET_OPENID = "你的目标用户OpenID"


async def is_target_user(bot: Bot, event: MessageEvent) -> bool:
    return event.get_user_id() == TARGET_OPENID


matcher = on_message(rule=Rule(is_target_user), priority=10)


@matcher.handle()
async def handle_hello(bot: Bot, event: MessageEvent):
    raw_text = event.get_plaintext().strip()

    if not raw_text:
        await matcher.finish("hello？你倒是说点啥呀")

    prefix = raw_text[:2]
    reply = f"hello{prefix}"

    await matcher.finish(reply)
