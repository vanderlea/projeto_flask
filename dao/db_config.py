import pg8000

def get_connection():
    
    return pg8000.connect(
        user="neondb_owner",
        password="npg_eTgiMwpX5Yx3",
        host="ep-proud-glitter-b7sfoqm1-pooler.c-13.us-east-1.aws.neon.tech",
        port=5432,
        database="neondb",
        ssl_context=True
        )
