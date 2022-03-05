from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
import os
from loguru import logger

# ####### 数据库链接

# 形如 mysql+pymysql://root:passwd@127.0.0.1:3306/MemoryCard?charset=utf8mb4
ASYNC_SQLALCHEMY_DATABASE_URL = ''

# ######### jwt
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"  # jwt加密算法
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 6  # 访问令牌过期分钟, 默认6小时

oauth2_schema = OAuth2PasswordBearer(tokenUrl="/user/token")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

if os.path.isfile("local_settings.py"):
    from local_settings import *
else:
    f = open("local_settings.py", mode="w", encoding="utf-8")
    f.close()
    raise Exception("请先配置local_settings, 详情见README")

# ######### 一些初始数据

OPERATION_DATA = {
    "delete_card": 1,
    "create_card": 2,
    "review_card": 3,
    "delete_category": 4,
    "create_category": 5,
    "delete_plan": 6,
    "create_plan": 7,
}
# #### 日志路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

LOG_FILE_PATH = os.path.join(BASE_DIR, "logs")
LOG_FILE_FORMATE = "MemoryCard_{time}.log"
# 日志配置
LOGGING_CONFIG = {
    "logger": {
        "path": LOG_FILE_PATH,
        "filename": LOG_FILE_FORMATE,
        "level": "info",
        "rotation": "1 MB",
        "retention": "1 months",
        "format": "<level>{level: <8}</level> <green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> request id: {extra[request_id]} - <cyan>{name}</cyan>:<cyan>{function}</cyan> - <level>{message}</level>"

    }
}
