from tkinter import *
from tkinter import ttk
from ftplib import FTP

ftp = FTP()

master = Tk()
master.geometry("650x200")  #kích thước khung

master.title ('FTP Server') #tiêu đề
master.resizable(0, 0)
my_frame = Frame(master,bg='green')
my_frame.place(height=600,width=650)

def login():            #đăng nhập
    ipadd = ip.get()    #địa chỉ ip
    username = tk.get() #tài khoản
    password = mk.get() #mật khẩu

    try:
        ftp.connect(ipadd, 2121)
        ftp.login(user=username, passwd=password)
        print(ftp.getwelcome())

    except:
        print('Lỗi')

def reset():        # xóa hết để đăng nhập cái khác
    ipE.delete(0, 'end')
    tkE.delete(0, 'end')
    mkE.delete(0, 'end')
    entry.delete(0, 'end')


def function():     #chức năng
    try:
        if str(cbx_test.get()) == 'Hiển thị File/Folder':
            print(ftp.dir())


        elif str(cbx_test.get()) == 'Mở Folder':
            # mở 1 thư mục
            file2 = entry.get()
            ftp.cwd(file2)
            print('Folder ' + file2 + ' có: ')
            ftp.pwd()
            print(ftp.dir())


        elif str(cbx_test.get()) == 'Download File':
            #    download file về máy
            filename_dow = entry.get()
            localfile = open(filename_dow, 'wb')
            ftp.retrbinary('RETR ' + filename_dow, localfile.write, 1024)
            ftp.pwd()
            print('Download thành công')
            localfile.close()


        elif str(cbx_test.get()) == 'Upload File':
            # upload file len sever
            filename_up = entry.get()
            ftp.storbinary('STOR ' + filename_up, open(filename_up, 'rb'))
            print('Sau khi upload file: ')
            print(ftp.dir())

#viết thêm chức năng nhá
    except Exception as e:
        if e:
            print('Lỗi')


#tạo các biến chuỗi
ip = StringVar()
tk = StringVar()
mk = StringVar()

#tạo các label
Label(master, text="IP:", font=('Times', 15)).place(x=10,y=30)
Label(master, text="User:", font=('Times', 15)).place(x=10,y=60)
Label(master, text="Password:", font=('Times', 15)).place(x=10,y=90)

#tạo các entry
ipE = Entry(master, textvariable=ip,font=12)
ipE.place(x=110,y=30,width=220,height=30)
tkE = Entry(master, textvariable=tk,font=12)
tkE.place(x=110,y=60,width=220,height=30)
mkE = Entry(master, show="*", textvariable=mk,font=12)
mkE.place(x=110,y=90,width=220,height=30)

Label(master, text= 'Chức năng:', font=('Times', 15)).place(x = 10, y = 120)
list_data = [ 'Hiển thị File/Folder', 'Mở Folder', 'Download File',
              'Upload File' ]

#tạo combobox có danh sách là list_data
cbx_test = ttk.Combobox(master, values=list_data)
cbx_test.current(0)
cbx_test.place(x=110,y=120,width=220,height=30)

entry = Entry(master,font=10)       #cái này đặc biệt vì nó là chỗ để điền tên file/folder thực hiện chức năng
entry.place(x=110,y=150,width=220,height=30)


#tạo các nút nhấn
Button(master, text="Login",font=('Times New Roman', 13),
       command=login).place(x=350,y=55,width=70,height=60)
Button(master, text="Confirm",font=('Times New Roman', 13),
       command=function).place(x=450,y=55,width=70,height=60)
Button(master, text="Refresh",font=('Times New Roman', 13),
       command=reset).place(x=550,y=55,width=70,height=60)

master.mainloop()