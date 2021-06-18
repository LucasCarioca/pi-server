import sqlite3

conn = sqlite3.connect('/home/pi/apps/dht11/dht.db')
c = conn.cursor()

def get_humidity_and_temperature():
    conn = sqlite3.connect("/home/pi/apps/dht11/dht.db")
    c = conn.cursor()
    rows = c.execute("SELECT * FROM DHT ORDER BY time LIMIT 1").fetchall()
    print(rows)
    conn.close()
    return rows[0][1], rows[0][2]
