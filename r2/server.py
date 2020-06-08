import socket 
import threading
import sqlite3
from time import sleep
# myip = "113.182.56.233" 192.168.64.1
HEADER = 64
PORT = 4444
SERVER = socket.gethostbyname(socket.gethostname())
# SERVER = "192.168.64.1"
# SERVER = myip
# SERVER = socket.gethostname()
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(socket.gethostbyname(socket.gethostname()),socket.gethostname())
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(ADDR)
connections = {} # {id_user: (con, addr)}
# ds_ban_be = ''
# ds_ban_be_dang_online = ''



# users_connections = {} 



def handle_client(conn, addr):
    link = r'C:\Users\htjir\OneDrive\Máy tính\r2\db\info_user.db'
    # link = 'C:\Users\htjir\OneDrive\Máy tính\r2\db'
    connect_sql = sqlite3.connect(link)
    cursor = connect_sql.cursor()
    
    print(f"[NEW CONNECTION] {addr} connected.")
    global connections
    # id_user = ""
    # return_friend_is_on = []
    # return_friend_is_on = ''
    
    true = True
    while true:
        messuser = ""
        # while True :

        try :
            # lengh_msg = conn.recv(128).decode(FORMAT)
            # co the bug 
            # if lengh_msg == '': continue
            # lengh_msg = int(lengh_msg)
            messuser = conn.recv(128).decode(FORMAT)
            if messuser == None:
                try:
                    if messuser.split('-')[2] =='':
                        print('if messuser',messuser) 
                except :
                    continue
                
            messuser = messuser.split('-')
            print(messuser)
        except Exception as e:
            print(f'loi cmrn {e}')
            true = False
            # sys.exit()
            conn.close()
            break
            

       

        print(f"day la messuser: {type(messuser)}")
        
        # phan tich thanh list_- cua messuser
                    # messuser = messuser.split('-')
        # kiem tra dang nhap 
        if messuser[0] == 'dangnhap' or messuser[0] == 'kiemtradangnhap': # req-tk-mk
            # truy van trong db 
            # cursor.execute(f'select tai_khoan from User where tai_khoan ="tu" ')


            cursor.execute(f'select tai_khoan, mat_khau from User where tai_khoan = "{messuser[1]}" ')

            data = cursor.fetchone() # tuple (a,b)
            # co tai khoan

            if data != None :
                if (data[1] == messuser[2]):
                    conn.send(bytes(f'dangnhapthanhcong-{messuser[1]}-dang nhap thanh cong','utf-8'))
                    
                    # co the da luong cho nay 
                    # messuser[1] la id_user
                    connections[messuser[1]] = (conn, addr) # them vao dict
                    # truy van db tim ban be va tra lai ds ban be va ds ban be dang on
                    sleep(1)
                    cursor.execute(f'select tai_khoan_1, tai_khoan_2 from Friends where tai_khoan_1 = "{messuser[1]}" or tai_khoan_2 = "{messuser[1]}" ')
                    data_friends = cursor.fetchall()
                    list_friends = []
                    for colum1, colum2  in data_friends:
                        list_friends.append(colum1)
                        list_friends.append(colum2)
                    list_friends = set(list_friends)
                    list_friends = list(list_friends)
                    #kiem tra ban be online
                    ds_ban_be_dang_online = ''
                    for i in list_friends:
                        if i in connections.keys():
                            ds_ban_be_dang_online += i +','
                     #format lai ds_ban_be_dang_online
                    print(ds_ban_be_dang_online)
                    # ds_ban_be_dang_online = ds_ban_be_dang_online[:-1]
                    
                    # gui string '[a,b];[c,d]', tui muon gui 'dsbanbe-a,b;a,b,c,d'
                    # ds_ban_be = f'{ds_ban_be_dang_online};'
                    # tra ve ds ban be 
                    ds_ban_be = ','.join(list_friends) + ';' + ds_ban_be_dang_online
                    print(f'dsbanbe-{ds_ban_be}')
                    conn.send(bytes(f'dsbanbe-{ds_ban_be}','utf-8'))
                else :
                    conn.send(bytes(f'dangnhapthatbai-{messuser[1]}-sai mat khau','utf-8'))
            else :
                 conn.send(bytes(f'tai khoan {messuser[1]} khong ton tai', 'utf-8'))

        # messuser[0] = 'dangky'
        if messuser[0] == 'dangky': 
            # truy van tk toi db, neu ko ton tai tk trong db => dang ky dc <=> cursor.fetchone = None
            cursor.execute(f'select tai_khoan from User where tai_khoan = "{messuser[1]}"')
            data  = cursor.fetchone()
            if data == None: # dang ky dc
                # truy van insert vao db va thong bao dk thanh cong
                cursor.execute(f"INSERT INTO Friends VALUES ('{messuser[1]}','{messuser[2]}')")
                conn.send(bytes('thanhcong-dang ky thanh cong','utf-8'))
                connections[messuser[1]] = (conn, addr)
            else: # ton tai tai khoan trong db
                conn.send('thatbai-tai khoan da ton tai-dang ky khong thanh cong')

        # yeu cau dang xuat messuser[0] == 'dangxuat'
        if messuser[0] == 'dangxuat':
        #gui thong diep cho tat ca ban be dang online
        # for i in : #duyet ds ban be dang online cua user
            connections.pop(messuser[1])
            conn.send(bytes(f'dadangxuat-{messuser[1]}','utf-8'))
            print('da dang xuat')
            conn.close()
            true = False 


        if messuser[0] == 'chat': # yeu cau la chat => messuser = 'chat-ban1,ban2-noi dung chat'
            list_get_msg = messuser[1].split(',')
            if len(list_get_msg) == 2:
                try :
                    messerver = f'chat-{list_get_msg[0]}-{messuser[2]}'
                    a = list_get_msg[0]
                    # connections[a].send(bytes(messerver),'utf-8')
                    connections[a][0].send(bytes(messerver,'utf-8'),)
                    a = list_get_msg[1]
                    messerver = f'chat-{list_get_msg[0]}-{messuser[2]}'
                    connections[a][0].send(bytes(messerver,'utf-8'),)
                    print(messerver)
                except Exception as e:
                    print(f'loi ko gui dc {e}') # co the continue
    
            else:
                for i in list_get_msg:
                    value = connections.get(i)
                    if value != None: #(con, addr)
                        con = value[0]
                        try :
                            messerver = f'chat-{i}-{messuser[2]}'
                            con.send(bytes(messerver,'utf-8'))
                            print(messerver)
                        except Exception as e:
                            print(f'loi ko gui dc {e}') # co the continue
            
            print(f'dang trong leng chat {list_get_msg}')

        if messuser[0] == 'themban':
            cursor.execute(f"select tai_khoan from User where tai_khoan = '{messuser[1]}'")
            data = cursor.fetchone()
            if data != None :
                
                pass

        if messuser[0] == 'xoaban':
            pass


# cap nhat ds ban be 
"""
lay ds ban be kiem tra trong connection 
    neu i in ds ban be ton tai thi them vao ds_ban_be_dang_on; 
    ds_ban_be_dang_on la 1 list nen chuyen thanh set de loc du lieu va chuyen lai thanh list
    su dung ','.join(ds_ban_be_dang_on) de chuyen thanh str co dang = 'a,b,c,d'
    dong goi yeu cau = 'ds_ban_be_dang_on-a,b,c,d'
    gui yeu cau = conn.send(bytes())
"""
    # conn.close()
        

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        # global connections
        # connections.append((conn,addr))
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")

start()

