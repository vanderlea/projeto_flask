import sqlite3
import psycopg2


DB_PATH = "postgresql://neondb_owner:npg_Wox4p8yvbRtg@ep-little-hill-b7vug4vu-pooler.c-13.us-east-1.aws.neon.tech/neondb?channel_binding=require&sslmode=require"

def get_connection():
    conn = psycopg2.connect(DB_PATH) 
    return conn