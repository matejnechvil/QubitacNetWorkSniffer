
import sqlite3

DATABASE = "qubitac.db"


def init_database():

    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS packets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            captured_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            src_ip TEXT,
            dst_ip TEXT,
            protocol TEXT,
            src_port INTEGER,
            dst_port INTEGER,
            size INTEGER
        )
    """)

    connection.commit()
    connection.close()


def save_packet(data):

    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO packets (
            src_ip,
            dst_ip,
            protocol,
            src_port,
            dst_port,
            size
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        data["src_ip"],
        data["dst_ip"],
        data["protocol"],
        data["src_port"],
        data["dst_port"],
        data["size"]
    ))

    connection.commit()
    connection.close()


def get_packets(limit=100):

    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM packets
        ORDER BY id DESC
        LIMIT ?
    """, (limit,))

    packets = [dict(row) for row in cursor.fetchall()]

    connection.close()

    return packets
