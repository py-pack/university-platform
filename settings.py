from dotenv import load_dotenv
from envparse import env

load_dotenv()

DB_HOST = env.str("DB_HOST", default="0.0.0.0")
DB_PORT = env.int("DB_PORT", default="5432")

DB_DATABASE = env.str("DB_DATABASE", default="postgres")
DB_USERNAME = env.str("DB_USERNAME", default="postgres")
DB_PASSWORD = env.str("DB_PASSWORD", default="postgres")

DB_URL = env.str(
    "DB_URL",
    default=f"postgresql+asyncpg://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}",
)


DB_HOST_TEST = env.str("DB_HOST_TEST", default="0.0.0.0")
DB_PORT_TEST = env.int("DB_PORT_TEST", default="5432")

DB_DATABASE_TEST = env.str("DB_DATABASE_TEST", default="postgres_test")
DB_USERNAME_TEST = env.str("DB_USERNAME_TEST", default="postgres_test")
DB_PASSWORD_TEST = env.str("DB_PASSWORD_TEST", default="postgres_test")

DB_URL_TEST = env.str(
    "DB_URL_TEST",
    default=f"postgresql+asyncpg://{DB_USERNAME_TEST}:{DB_PASSWORD_TEST}@{DB_HOST_TEST}:{DB_PORT_TEST}/{DB_DATABASE_TEST}",
)
