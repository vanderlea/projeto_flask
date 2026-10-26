import psycopg2

# path / url de conexão
DB_PATH = "DATABASE_URL_UNPOOLED=postgresql://neondb_owner:npg_Wox4p8yvbRtg@ep-little-hill-b7vug4vu.c-13.us-east-1.aws.neon.tech/neondb?sslmode=require"

def get_connection():
    return psycopg2.connect(DB_PATH)