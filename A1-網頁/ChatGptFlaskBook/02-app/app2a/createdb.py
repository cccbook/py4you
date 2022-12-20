import sqlite3

connection = sqlite3.connect('user.db')
cursor = connection.cursor()

# 在 user 資料庫中創建 users 表
query = '''
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL
);
'''
cursor.execute(query)

# 提交變更
connection.commit()

# 關閉連接
connection.close()
