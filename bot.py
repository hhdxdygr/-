import nonebot
from nonebot.log import logger
from nonebot.adapters.qq import Adapter as QQAdapter

nonebot.init()
driver = nonebot.get_driver()
driver.register_adapter(QQAdapter)
nonebot.load_plugins("plugins")

app = nonebot.get_asgi()


@driver.on_startup
async def debug_routes():
    raw = os.getenv("QQ_BOTS", "")
    logger.info(f"QQ_BOTS 原始值: {raw!r}")
    logger.info("=== 应用已启动，开始打印路由 ===")
    for route in app.routes:
        logger.info(f"Route: {getattr(route, 'path', route)}")
    logger.info("=== 路由打印完毕 ===")

if __name__ == "__main__":
    nonebot.run(app="bot:app")
