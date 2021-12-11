from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from ftplib import FTP

ftp = FTP()

class MainApp(Tk):
    def __init__(self):
        super(MainApp, self).__init__()

        self.label0 = Label(text="Đăng Nhập", font = 2).grid(row=0, column=1, columnspan=2)

        self.lable1 = Label(text = 'IP Sever').grid(row = 1, column = 0,columnspan=2)
        self.entry1 = Entry()
        self.entry1.grid(row=1, column=2, sticky= E )

        self.lable2 = Label(text='Tài Khoản').grid(row=2, column=0, columnspan=2)
        self.entry2 = Entry()
        self.entry2.grid(row=2, column=2, sticky=E)

        self.lable3 = Label(text='Mật Khẩu').grid(row=3, column=0, columnspan=2)
        self.entry3 = Entry(show = '*')
        self.entry3.grid(row=3, column=2, sticky=E)

        self.group1 = LabelFrame(self, text="Các chức năng:", font=('Times', 20), padx=10, pady=5, width = 20, height = 10)
        self.group1.grid(row=0, column = 3, rowspan = 5, padx=20, pady=10, sticky=E)

        self.lbl_test = Label(self.group1, text="""
                0.Hiển thị File/Folder trong Server
                1.Mở một Folder              
                2.Download File
                3.Upload File
                4.Kiểm tra dung lượng File
                5.Xóa File
                6.Đổi tên File
                7.Tạo Folder mới
                8.Xóa Folder
                9.Quay lại Folder trước
                00.Thoát khỏi
                
                """)
        self.lbl_test.grid(row=0, column=3, sticky = E)

        self.lable4 = Label(text= 'Chọn chức năng').grid(row=4, column=0)
        list_data = [ 'lựa chọn 0', 'lựa chọn 1', 'lựa chọn 2',
                     'lựa chọn 3', 'lựa chọn 4', 'lựa chọn 5',
                      'lựa chọn 6', 'lựa chọn 7', 'lựa chọn 8',
                      'lựa chọn 9', 'lựa chọn 00'
                     ]
        self.cbx_test = ttk.Combobox(self, values=list_data)
        self.cbx_test.current(0)
        self.cbx_test.grid(row=4, column=2, sticky=E)

        self.btn_test = Button(self, text="Đăng Nhập", command=lambda: dangnhap(self), height=2, width=15)
        self.btn_test.grid(row=6, column=2, padx=20, pady=20, sticky=E)

        self.btn_test1 = Button(self, text="Xác Nhận", command=  lambda : handbuton(self)  , height=2, width=15)
        self.btn_test1.grid(row=6, column=3, padx=100, pady=20, sticky=W )



def dangnhap(self):
    try:
        ip_sever = str(self.entry1.get())
        user1 = str(self.entry2.get())
        password = str(self.entry3.get())

        ftp.connect(ip_sever, 2121)
        ftp.login(user=user1, passwd=password)
        print(ftp.getwelcome())
        messagebox.showinfo('Thông Báo', 'Đăng nhập thành công ')
    except Exception as e:
        if e:
            messagebox.showinfo('Lỗi', e)


def handbuton(self):
    try:
        if  str(self.cbx_test.get()) == 'lựa chọn 0':
            print("Hiển thị file/folder :")
            file = ftp.dir()
            print(file)
            messagebox.showinfo('Thông Báo', 'Xác nhận thành công ')

        elif str(self.cbx_test.get()) == 'lựa chọn 1':
            # mở 1 thư mục
            file2 = input('Folder cần vào: ')
            ftp.cwd(file2)
            print('Folder ' + file2 + ' có: ')
            ftp.pwd()
            print(ftp.dir())
            messagebox.showinfo('Thông Báo', 'Xác nhận thành công ')

        elif str(self.cbx_test.get()) == 'lựa chọn 2':
            #    download file về máy
            filename_dow = input("File cần download: ")
            localfile = open(filename_dow, 'wb')
            ftp.retrbinary('RETR ' + filename_dow, localfile.write, 1024)
            ftp.pwd()
            print('Download thành công')
            localfile.close()
            messagebox.showinfo('Thông Báo', 'Xác nhận thành công ')

        elif str(self.cbx_test.get()) == 'lựa chọn 3':
            # upload file len sever
            filename_up = input('File cần Upload: ')
            ftp.storbinary('STOR ' + filename_up, open(filename_up, 'rb'))
            print('Sau khi upload file: ')
            print(ftp.dir())
            messagebox.showinfo('Thông Báo', 'Xác nhận thành công ')

        elif str(self.cbx_test.get()) == 'lựa chọn 4':
            file_size = input('File cần kiểm tra dung lượng: ')
            print(ftp.size(file_size) ,'KB')
            messagebox.showinfo('Thông Báo', 'Xác nhận thành công ')

        elif str(self.cbx_test.get()) == 'lựa chọn 5':
            # xoa file
            ftp.delete(input('File cần xóa: '))
            print('Sau khi xóa file:')
            print(ftp.dir())
            messagebox.showinfo('Thông Báo', 'Xác nhận thành công ')

        elif str(self.cbx_test.get()) == 'lựa chọn 6':
            oldname = input('Tên File cũ: ')
            newname = input('Tên File mới: ')
            ftp.rename(oldname, newname)
            print('Sau khi đổi tên file:')
            print(ftp.dir())
            messagebox.showinfo('Thông Báo', 'Xác nhận thành công ')

        elif str(self.cbx_test.get()) == 'lựa chọn 7':
            folder_new = input('Tên Folder mới:')
            ftp.mkd(folder_new)
            print('Sau khi tạo folder :')
            print(ftp.dir())
            messagebox.showinfo('Thông Báo', 'Xác nhận thành công ')

        elif str(self.cbx_test.get()) == 'lựa chọn 8':
            folder_del = input('Tên Folder:')
            ftp.rmd(folder_del)
            print('Sau khi xóa folder :')
            print(ftp.dir())
            messagebox.showinfo('Thông Báo', 'Xác nhận thành công ')


        elif str(self.cbx_test.get()) == 'lựa chọn 9':
            print('Quay lại folder:')
            ftp.cwd('..')
            print(ftp.pwd())
            messagebox.showinfo('Thông Báo', 'Xác nhận thành công ')

        else:
            print('kt chuong trinh')
            ftp.quit()
            reset(self)
            messagebox.showinfo('Thông Báo', "Bạn đã đăng xuất thành công!Nếu muốn tiếp tục cần đăng nhập lần nữa.")

    except Exception as e:
        if e:
            messagebox.showinfo('Lỗi', e)

def reset(self):
    self.entry1.delete(0, 'end')
    self.entry2.delete(0, 'end')
    self.entry3.delete(0, 'end')


if __name__ == '__main__':
    main_app = MainApp()
    main_app.wm_title("FTP Server")
    main_app.mainloop()