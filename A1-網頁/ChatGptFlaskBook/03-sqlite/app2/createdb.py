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

# 向 users 表中插入新記錄
query = '''
INSERT INTO users (username, email) VALUES ("John", "john@example.com");
'''
cursor.execute(query)


# 更新 username 為 John 的記錄
query = '''
UPDATE users SET username="Johnny" WHERE username="John";
'''
cursor.execute(query)

# 刪除 email 為 john@example.com 的記錄
query = '''
DELETE FROM users WHERE email="john@example.com";
'''
cursor.execute(query)


# 提交變更
connection.commit()

# 關閉連接
connection.close()
