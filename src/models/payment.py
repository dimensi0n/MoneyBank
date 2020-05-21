from datetime import datetime
import sqlite3

class Payment:
    def __init__(self, price = 0, database = sqlite3.connect('database.db')):
        self.conn = database
        self.price = price
        c = self.conn.cursor()
        c.execute('''
        CREATE TABLE IF NOT EXISTS payments (id INTEGER PRIMARY KEY, price decimal, date date)
        ''')
        self.conn.commit()

    def create(self):
        c = self.conn.cursor()
        c.execute('''
        INSERT INTO payments (price, date) VALUES (?,?)
        ''', (self.price, datetime.today().strftime('%d%m%Y')))
        self.conn.commit()

    def getGainOfToday(self):
        c = self.conn.cursor()
        c.execute('''
        SELECT SUM(price) FROM payments WHERE date="
        '''+ datetime.today().strftime('%d%m%Y') + "\"")
        return c.fetchone()
