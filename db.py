import sqlite3

class DatabaseActivity:
    def __init__(self):
        self.conn = sqlite3.connect('telegram_cli.db')
        self.cursor = self.conn.cursor()

    def create_chats_table(self):
        try:
            self.conn.execute('''CREATE TABLE IF NOT EXISTS chats(
                id INTEGER PRIMARY KEY,
                chat_id INTEGER,
                name TEXT);''')
            self.conn.commit()
        except sqlite3.Error as e:
            print(f'Error occured: {e}')
        finally:
            if self.conn:
                self.conn.close()

    def verify_chat_db(self):
        try:
            print(self.cursor)
        except sqlite3.Error as e:
            print('Error occurred - ', e)
        finally:
            if self.conn:
                self.conn.close()
                print("DB Closed")

    def insert_chat(self, chat_id, name):
        try:
            self.cursor.execute(
                'INSERT INTO chats (chat_id, name) VALUES (?, ?)', (chat_id, name))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f'Error occured: {e}')
        finally:
            self.conn.close()

    def get_all_chats(self):
        try:
            self.cursor.execute('SELECT * FROM chats')
            result = self.cursor.fetchall()
            self.conn.commit()
            print(result)
        except sqlite3.Error as e:
            print(f'Error occured: {e}')
        finally:
            if self.conn:
                self.conn.close()
                print("DB Closed")

if __name__ == '__main__':
    db_conn = DatabaseActivity()
    db_conn.get_all_chats()
