import motor.motor_asyncio
from ..core import config

# Create MongoDB client
client = motor.motor_asyncio.AsyncIOMotorClient(config.MONGO_URI)
db = client[config.DB_NAME]
