import sqlite3

conn = sqlite3.connect('backend_python.sqlite3', check_same_thread=False)
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS lineups (PNumber INTEGER, Queue INTEGER, Status BOOLEAN)')

numberOfLines = 0

# cur.execute('INSERT INTO Data_Sheet (PNumber, Queue, Status) VALUES ( ?, ?, ? )', ( 12345678, 1, True ) )

def fulfilQueue(Number_of_people, Queue_number):
    total = 0
    cur.execute('SELECT PNumber FROM Data_Sheet WHERE Status = 0 AND Queue = %s' % Queue_number)
    for row in cur:
        total += 1
        return (list(row))
        if total >= Number_of_people:
            break
    cur.execute('UPDATE Data_Sheet SET Status = 1 WHERE Status = 0 AND Queue = %s' % Queue_number)
    cur.execute('DELETE FROM Data_Sheet WHERE Status = 1')

def addLine(x):
        numberOfLines = x
    
    
    
    