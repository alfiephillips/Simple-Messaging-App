import sqlite3
from datetime import datetime
import time

# CONSTANTS

DB_FILE = "database.db"
MESSAGES_TABLE = "Messages"
USER_TABLE = "Users"

class Database:
    """
    Used to connect, write and read from a local sqlite3 database.
    """

    def __init__(self):

        """
        Initiate a connection to the database file 
        and create cursor to execute table queries.
        """

        self.conn = None
        self.tables = [MESSAGES_TABLE, USER_TABLE]

        try:
            self.conn = sqlite3.connect(DB_FILE)

        except sqlite3.Error as error:
            print(error)

        self.cursor = self.conn.cursor()
        self._create_tables()

    def close(self):
        """
        Close database connection
        :return: None
        """
        print("Closing connection...")
        self.conn.close()

    def _create_tables(self):
        """
        Create new tables in (self.tables) if they don't already exist
        :return: None
        """
        try:
            for table in self.tables:
                if table == MESSAGES_TABLE:
                    query = f"""CREATE TABLE IF NOT EXISTS {MESSAGES_TABLE}
                                (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, content TEXT, time DATE)"""

                    self.cursor.execute(query)

                elif table == USER_TABLE:
                    query = f"""CREATE TABLE IF NOT EXISTS {USER_TABLE}
                                (id INTEGER PRIMARY KEY, username TEXT, password TEXT, time_created DATE)"""

                    self.cursor.execute(query)
                    
        except sqlite3.Error as error:
            print(error)
            self.conn.rollback()

        self.conn.commit()
        print("Tables have been created successfully")

    def get_all_messages(self, limit=100, name=None):
        """
        Returns all messsages from Messages table
        :param limit: int
        :return: list[dict: Message<Object>]
        """

        try:
            if not name:
                query = f"SELECT * FROM {MESSAGES_TABLE}"
                self.cursor.execute(query)
            else:
                query = f"SELECT * FROM {MESSAGES_TABLE} WHERE NAME = ?"
                self.cursor.execute(query, (name))

        except sqlite3.Error as error:
            print(error)
            self.conn.rollback()

        result = self.cursor.fetchall()

        # Return message in a sorted order/

        results = []
        for r in sorted(result, key=lambda x: x[3], reverse=True)[:limit]:
            _id, name, content, date = r
            data = {"name": name, "message": content, "time": str(date)}

            results.append(data)

        return list(reversed(results))

    def get_messages_by_name(self, name, limit=100):
        """
        Gets a list of messages from a specific user
        :param name: str
        :param limit: int
        :return: list
        """

        return self.get_all_messages(limit, name)


    def save_message(self, name, msg):
        """
        Saves a specific message in the Messages table
        :param name: str
        :param msg: str
        :return: None
        """

        try:
            date = datetime.now()
            query = f"INSERT INTO {MESSAGES_TABLE} VALUES (?, ?, ?, ?)"
            self.cursor.execute(query, (None, name, msg, date))

        except sqlite3.Error as error:
            print(error)
            self.conn.rollback()

        self.conn.commit()