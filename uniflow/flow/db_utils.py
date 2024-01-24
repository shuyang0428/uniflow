import sqlite3
from sqlite3 import Connection
from threading import Lock

# Ensuring thread-safe database access with a lock
db_lock = Lock()

def get_db_connection(db_path: str) -> Connection:
    """Create a new database connection."""
    connection = sqlite3.connect(db_path, check_same_thread=False)
    return connection

def init_db(db_path: str) -> None:
    """Initialize the database and create required tables."""
    with db_lock, get_db_connection(db_path) as conn:
        conn.execute('''
        CREATE TABLE IF NOT EXISTS flow_output (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            key TEXT NOT NULL,
            value TEXT NOT NULL
        );
        ''')

def insert_flow_output(db_path: str, key: str, value: str) -> None:
    """Insert a key-value pair into the flow_output table."""
    with db_lock, get_db_connection(db_path) as conn:
        conn.execute('INSERT INTO flow_output (key, value) VALUES (?, ?)', (key, value))
        conn.commit()
