
import os
import psycopg
from dotenv import load_dotenv

load_dotenv()


DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "dbname": "qubitac",
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD")
}


def get_connection():
    return psycopg.connect(**DB_CONFIG)


def save_flow(src_ip, dst_ip, src_port, dst_port, protocol, packets, bytes_sent):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO flows
                (src_ip, dst_ip, src_port, dst_port, protocol, packets, bytes_sent)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """,
                (src_ip, dst_ip, src_port, dst_port, protocol, packets, bytes_sent)
            )


def get_flows(limit=100):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT *
                FROM flows
                ORDER BY id DESC
                LIMIT %s
                """,
                (limit,)
            )

            return cursor.fetchall()


def get_flow(flow_id):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM flows WHERE id = %s",
                (flow_id,)
            )

            return cursor.fetchone()
