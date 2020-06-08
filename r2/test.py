import sqlite3

link = r'C:\Users\htjir\OneDrive\Máy tính\r2\db\info_user.db'
# link = 'C:\Users\htjir\OneDrive\Máy tính\r2\db'
connect_sql = sqlite3.connect(link)
cursor = connect_sql.cursor()
tu = 'tu'
cursor.execute(f'select tai_khoan_1, tai_khoan_2 from Friends where tai_khoan_1 = "{tu}" or tai_khoan_2 = "{tu}" ')
data_friends = cursor.fetchall()
print(data_friends)

# print(f'{type(data)}, du lieu la : {data}, rong = {data is None}/ {data != None}, thuc the: {data[0]}, type data[0]: {type(data[0])}')