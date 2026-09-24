from nonebot import on_message
from nonebot.adapters.qq import Bot, MessageEvent
from nonebot.rule import Rule

async def is_jun(bot: Bot, event: MessageEvent) -> bool:
    return event.get_plaintext().strip() == "君"

matcher = on_message(rule=Rule(is_jun), priority=5)

@matcher.handle()
async def handle_jun(bot: Bot, event: MessageEvent):
    await matcher.finish("！？君？！")
