import nonebot
from nonebot.log import logger
from nonebot.adapters.qq import Adapter as QQAdapter

nonebot.init(driver="~fastapi+~httpx")
driver = nonebot.get_driver()

logger.info(f"Driver type: {type(driver)}")
logger.info(f"Has HTTPClientMixin: {hasattr(driver, 'request') or hasattr(driver, '_request')}")
logger.info(f"Has ASGIMixin: {hasattr(driver, 'setup')}")

driver.register_adapter(QQAdapter)
nonebot.load_plugins("plugins")

app = nonebot.get_asgi()

if __name__ == "__main__":
    nonebot.run(app="bot:app")
