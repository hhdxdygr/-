import os

from nonebot import on_message
from nonebot.adapters.onebot.v11 import Bot, MessageEvent
from nonebot.rule import Rule


TARGET_QQ = os.getenv("TARGET_QQ", "2193585663")


async def is_target_user(bot: Bot, event: MessageEvent) -> bool:
    return event.get_user_id() == TARGET_QQ


matcher = on_message(rule=Rule(is_target_user), priority=10, block=True)


@matcher.handle()
async def handle_hello(bot: Bot, event: MessageEvent):
    raw_text = event.get_plaintext().strip()

    if not raw_text:
        await matcher.finish("hello？你倒是说点啥呀")

    await matcher.finish(f"hello{raw_text[:2]}")