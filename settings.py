from envparse import Env

env = Env()

DB_HOST = env.str("DB_HOST", default="localhost")
DB_PORT = env.str("DB_PORT", default="5432")

DB_DATABASE = env.str("DB_DATABASE", default="postgres")
DB_USERNAME = env.str("DB_USERNAME", default="postgres")
DB_PASSWORD = env.str("DB_PASSWORD", default="postgres")

REAL_DATABASE_URL = env.str(
    "REAL_DATABASE_URL",
    default=f"postgresql+asyncpg://${DB_USERNAME}:${DB_PASSWORD}@${DB_HOST}:${DB_PORT}/${DB_DATABASE}",
)
