
import os, psycopg

DATABASE_URL = os.getenv("DATABASE_URL")

def get_conn():
    return psycopg.connect(DATABASE_URL, autocommit=True, row_factory=psycopg.rows.dict_row)

def create_schema():
    try:
        with get_conn() as conn, conn.cursor() as cur:
            # Create the schema
            cur.execute("""
                CREATE TABLE IF NOT EXISTS hotel_rooms (
                    id SERIAL PRIMARY KEY, -- primary key
                    room_number INT
                    type VARCHAR
                    price NUMERIC 
                    created_at TIMESTAMP DEFAULT now()
                );
            )
    except Exception as e:
        print(f"Error while creating schema: {e}")
