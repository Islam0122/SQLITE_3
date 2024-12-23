import sqlite3
from x import x
base = sqlite3.connect('SQLITE_3.db')
cursor = base.cursor()

base.execute('CREATE TABLE  IF NOT EXISTS {} (login PRIMARY KEY,password)'.format('data'))
base.commit()

# cursor.execute('INSERT INTO {} VALUES (?,?)'.format('data'),('16','123456'))
# base.commit()
# cursor.execute('INSERT INTO {} VALUES (?,?)'.format('data'),('1ads6','1as23456'))
# base.commit()
# cursor.executemany('INSERT INTO {} VALUES (?,?)'.format('data'),(x))
# base.commit()
#
# r = cursor.execute('SELECT * FROM data').fetchall()
# print(r)
#
# r = cursor.execute('SELECT password FROM data WHERE login==?',('16',)).fetchone()
# print(r)
#
# r = cursor.execute('UPDATE data SET password==? WHERE login=?',('16','16'))
# base.commit()
#
# r = cursor.execute('SELECT * FROM data WHERE login==?',('16',)).fetchone()
# print(r)
#
# cursor.execute('DELETE FROM data WHERE login=?',('user2',))
# base.commit()
# print(r)
base.execute('DROP TABLE IF EXISTS data')
base.commit()
base.close()
