from tkinter import *
import tkinter as tk
import sqlite3
from tkinter.messagebox import showinfo
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import ttk
from voting_database import *
from PIL import Image, ImageTk
import sqlite3
import re

global State1
State1 = 0  # 0:normal 1:manager


def signup():
    new = Toplevel(frame)
    frame1 = tk.Frame(master=new, bg="midnightblue")
    frame1.pack(fill=tk.BOTH, expand=True)
    frame1.pack()
    new.title("SignUp Form")
    canvas1 = tk.Canvas(frame1, width=650, height=500, relief='raised', bg="midnightblue")
    canvas1.pack()

    label1 = tk.Label(frame1, text='Registration Form')
    label1.config(font=("bold", 18), bg="turquoise")

    canvas1.create_window(250, 30, window=label1)

    label2 = tk.Label(frame1, text='Fullname :')
    label2.config(font=('helvetica', 14), bg="turquoise")

    canvas1.create_window(65, 60, window=label2)
    # label2.pack()

    entry1 = tk.Entry(frame1, textvar=Fullname, font=(14), borderwidth=2, width=30)

    canvas1.create_window(320, 60, window=entry1)

    label3 = tk.Label(frame1, text='National Code :')
    label3.config(font=('helvetica', 14), bg="turquoise")
    canvas1.create_window(65, 100, window=label3)
    # label3.pack()
    entry2 = tk.Entry(frame1, textvar=NationalCode, font=(14), borderwidth=2, width=30)
    canvas1.create_window(320, 100, window=entry2)

    label4 = tk.Label(frame1, text='Email :')

    label4.config(font=('helvetica', 14), bg="turquoise")

    canvas1.create_window(65, 140, window=label4)
    # label4.pack()
    entry3 = tk.Entry(frame1, textvar=Email, font=(14), borderwidth=2, width=30)
    canvas1.create_window(320, 140, window=entry3)

    # rd2.pack()

    label6 = tk.Label(frame1, text='Password :')
    label6.config(font=('helvetica', 14), bg="turquoise")

    # label6.pack()

    canvas1.create_window(65, 180, window=label6)

    entry5 = tk.Entry(frame1, textvar=Password, font=(14), borderwidth=2, width=30, show="*")
    canvas1.create_window(320, 180, window=entry5)
    # entry5.pack()
    label7 = tk.Label(frame1, text='Confirm Pass :')
    label7.config(font=('helvetica', 14), bg="turquoise")
    label7.pack()
    canvas1.create_window(65, 220, window=label7)

    entry6 = tk.Entry(frame1, textvar=ConfirmPassword, font=(14), borderwidth=2, width=30, show="*")
    canvas1.create_window(320, 220, window=entry6)

    label5 = tk.Label(frame1, text='Select Role :')
    label5.config(font=('helvetica', 14), bg="turquoise")
    canvas1.create_window(65, 260, window=label5)

    vlist = ["Normal User", "Manager"]

    Combo = ttk.Combobox(frame1, values=vlist)
    Combo.set("Select an Option")
    Combo.pack(padx=5, pady=5)
    Combo.place(relx=0.25, rely=0.43, height=30, width=200)

    def check_Repeated():
        conn = None
        output = []
        try:
            conn = sqlite3.connect(DATABASE)
            cursor = conn.cursor()
            s = '''SELECT natural_code FROM User'''
            cursor.execute(s)
            rows = cursor.fetchall()
            cols = [col[0] for col in cursor.description]
            for row in rows:
                d = {}
                for i in range(len(cols)):
                    d[cols[i]] = row[i]
                output.append(d)
            conn.commit()
        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()
        i = 0
        find = 0
        for row in rows:
            i = i + 1
        for j in range(i):
            if (list(output[j].values())[0]) == entry2.get():
                find = 1
        return find

    # entry6.pack()
    def inserttable():
        choice = Combo.get()
        if choice == 'Normal User':
            role = "Normal User"
        elif choice == 'Manager':
            role = "Manager"
        else:
            role = "Normal User"
        entry1.pack()
        entry2.pack()
        entry3.pack()
        entry5.pack()
        entry6.pack()
        out = check_Repeated()
        if (out == 0):
            if entry5.get() == entry6.get() and entry6.get() != "" and entry2.get() != "":
                insert_into_User_table(entry1.get(), entry5.get(), entry2.get(), entry3.get(), role)
                new.destroy()
                showinfo(title="Sign Up", message="Thanks for signing up!")
            elif (entry6.get() == "" and entry5.get() == "") or entry2.get() == "":
                new.destroy()
                showinfo(title="Error", message="Passwords and National Code can not be Empty!")
            else:
                new.destroy()
                showinfo(title="Error", message="Passwords not matching!")

            new.destroy()
        else:
            new.destroy()
            showinfo(title="Error", message="National Code is Repeated!")

    Button(frame1, height=2,
           width=25, font=('Helvetica 17 bold'), fg="midnight blue", bg="turquoise", text="Submit",
           command=inserttable).pack()


def candidate():
    window2 = tk.Tk()

    frame2 = tk.Frame(master=window2, bg="midnight blue")
    window2.title("Candidate Form")

    frame2.pack()
    canvas1 = tk.Canvas(frame2, width=650, height=500, relief='raised', bg="midnightblue")
    canvas1.pack()

    label1 = tk.Label(frame2, text='Candidate Form')
    label1.config(font=("bold", 18), bg="turquoise")
    canvas1.create_window(250, 30, window=label1)

    label2 = tk.Label(frame2, text='Fullname :')
    label2.config(font=('helvetica', 14), bg="turquoise")
    canvas1.create_window(65, 60, window=label2)

    entry1 = tk.Entry(frame2, textvar=Fullname, font=(14), borderwidth=2, width=30)
    canvas1.create_window(320, 60, window=entry1)

    label3 = tk.Label(frame2, text='National Code :')
    label3.config(font=('helvetica', 14), bg="turquoise")
    canvas1.create_window(65, 100, window=label3)

    entry2 = tk.Entry(frame2, textvar=NationalCode, font=(14), borderwidth=2, width=30)
    canvas1.create_window(320, 100, window=entry2)

    label4 = tk.Label(frame2, text='Email :')
    label4.config(font=('helvetica', 14), bg="turquoise")
    canvas1.create_window(65, 140, window=label4)

    entry3 = tk.Entry(frame2, textvar=Email, font=(14), borderwidth=2, width=30)
    canvas1.create_window(320, 140, window=entry3)

    label6 = tk.Label(frame2, text='Phone Number :')
    label6.config(font=('helvetica', 14), bg="turquoise")
    canvas1.create_window(65, 180, window=label6)
    entry6 = tk.Entry(frame2, textvar='Phone Number', font=(14), borderwidth=2, width=30)
    canvas1.create_window(320, 180, window=entry6)

    # label6.pack()

    def insertvolunteer():
        entry1.pack()
        entry2.pack()
        entry6.pack()
        entry3.pack()
        if entry2.get() != "":
            insert_into_Volunteer_table(entry1.get(), entry2.get(), entry6.get(), entry3.get())
            window2.destroy()
            showinfo(title="Registeration", message="Thanks for Register!")
        else:
            window2.destroy()
            showinfo(title="Error", message="National Code can not be Empty!")

    Button(frame2, height=2,
           width=25, font=('Helvetica 17 bold'), fg="midnight blue", bg="turquoise", text="Submit",
           command=insertvolunteer).pack()


# -----VOTING---------------------------------------
def vote():
    window2 = tk.Tk()

    frame2 = Frame(master=window2, bg="midnight blue")
    window2.title("Voting Form")

    frame2.pack()
    canvas1 = Canvas(frame2, width=600, height=500, relief='raised', bg="midnightblue")
    canvas1.pack()

    label1 = Label(frame2, text='Please Click on your desired candidate')
    label1.config(font=("bold", 13), bg="turquoise", compound=tk.CENTER)
    canvas1.create_window(320, 30, window=label1)

    lb = Listbox(frame2)
    lb.pack()
    lb.place(relx=0.35, rely=0.1, height=400, width=200)

    bt = Button(frame2, height=2, width=25, font=('Helvetica 17 bold'), fg="midnight blue", bg="turquoise",
                text="Submit")
    canvas1.create_window(320, 520, window=bt)

    db_Candidates = search_into_Candidate_table()
    candidates_list = []
    for i in db_Candidates:
        candidates_list.append((str(i['candidate_ID']) + ' - ' + i['fullname']))

    for i, cand in enumerate(candidates_list):
        lb.insert(i, cand)

    def insertVote():
        res = lb.get(lb.curselection())

        if res != "":
            increase_vote(int(res.split(' ')[0]))

            window2.destroy()
            showinfo(title="Voting", message="Thanks for Your Vote!")
        else:
            window2.destroy()
            showinfo(title="Error", message="Vote can not be Empty!")

    bt.config(command=insertVote)
    bt.pack()


# -----RESULTS---------------------------------------
def show_result():
    window2 = tk.Tk()

    frame2 = Frame(master=window2, bg="midnight blue")
    window2.title("Result Form")

    frame2.pack()
    canvas1 = Canvas(frame2, width=600, height=500, relief='raised', bg="midnightblue")
    canvas1.pack()

    label1 = Label(frame2, text='Final Result of Election')
    label1.config(font=("bold", 13), bg="turquoise", compound=tk.CENTER)
    canvas1.create_window(320, 30, window=label1)

    set = ttk.Treeview(frame2)
    set.pack()
    set.place(relx=0.27, rely=0.1, height=300, width=300)

    set['columns'] = ('full_Name', 'n_votes')
    set.column("#0", width=0, stretch=NO)
    set.column("full_Name", anchor=CENTER, width=150)
    set.column("n_votes", anchor=CENTER, width=150)

    set.heading("#0", text="", anchor=CENTER)
    set.heading("full_Name", text="Full_Name", anchor=CENTER)
    set.heading("n_votes", text="Number of votes", anchor=CENTER)

    db_Candidates = search_into_Candidate_table()
    db_Candidates = sorted(db_Candidates, key=lambda k: k['number_of_votes'], reverse=True)
    for candidate in db_Candidates:
        set.insert(parent='', index='end', text='',
                   values=(candidate['fullname'], candidate['number_of_votes']))


# ----REJECT-ACCEPT---------------------------
def reject_accept():
    global State1
    if State1 == 1:
        print(search_into_Volunteer_table())

        window2 = tk.Tk()

        frame2 = tk.Frame(master=window2, bg="midnight blue")

        window2.title("Confirmation of Volunteers")

        frame2.pack()
        canvas1 = tk.Canvas(frame2, width=650, height=500, relief='raised', bg="midnightblue")
        canvas1.pack()

        label1 = tk.Label(frame2, text='Volunteers Acceptance')
        label1.config(font=("bold", 18), bg="turquoise")
        canvas1.create_window(320, 30, window=label1)

        label1 = Label(frame2, text='Please click on all accepted candidates')
        label1.config(font=("bold", 13), bg="turquoise", compound=tk.CENTER)
        canvas1.create_window(320, 60, window=label1)

        lb = Listbox(frame2)
        lb.config(selectmode='multiple')
        lb.pack()
        lb.place(relx=0.25, rely=0.2, height=350, width=350)

        bt = Button(frame2, height=2, width=25, font=('Helvetica 17 bold'), fg="midnight blue", bg="turquoise",
                    text="Submit")
        canvas1.create_window(320, 520, window=bt)

        db_Volunteers = search_into_Volunteer_table()
        Volunteers_list = []
        for i in db_Volunteers:
            Volunteers_list.append((str(i['volunteer_ID']) + '  ' + i['fullname'] + '  ' + i['natural_code'] + '  ' + i[
                'phone_number'] + '  ' + i['email']))

        for i, vol in enumerate(Volunteers_list):
            lb.insert(i, vol)

        def insertcandidate():
            values = [lb.get(i) for i in lb.curselection()]

            if values != []:
                for v in values:
                    insert_into_Candidate_table(v.split('  ')[1], v.split('  ')[2], v.split('  ')[3], v.split('  ')[4])
                    delete_from_Volunteer_table(v.split('  ')[2])

                window2.destroy()
                showinfo(title="Voting", message="Thanks for Your Vote!")

        bt.config(command=insertcandidate)
        bt.pack()

    else:
        showinfo(title="Error", message="Not Accessible by Normal User!")


# --------------------------------------------


def open_win():
    new = tk.Tk()

    frame4 = tk.Frame(master=new, bg="midnight blue")
    frame4.pack()
    new.title("Menu Form")

    # call databasefunc(username,password)
    # if output!=0
    conn = sqlite3.connect('Form.sql')

    cursor = conn.cursor()
    username = entry1.get()
    password = entry2.get()
    # cursor.execute('execute u_p_check ' + str(username) +
    #               ', ' + str(password) + ';')
    # check and read from db

    # enter to page of services
    Label(frame4, text="", bg="midnight blue",
          font=('Helvetica 17 bold')).pack(pady=15)
    Label(frame4, text="Choose the service from check list",
          fg="turquoise", bg="midnight blue", font=('Helvetica 20 bold')).pack(pady=30)
    Label(frame4, text="", bg="midnight blue",
          font=('Helvetica 17 bold')).pack(pady=17)
    Button(frame4, height=2,
           width=25, font=('Helvetica 17 bold'), fg="midnight blue", bg="turquoise", text="Voting",
           command=vote).pack()
    Label(frame4, text="", bg="midnight blue",
          font=('Helvetica 10 bold')).pack(pady=1)
    Button(frame4, height=2,
           width=25, font=('Helvetica 17 bold'), fg="midnight blue", bg="turquoise", text="Show Results",
           command=show_result).pack()
    Label(frame4, text="", bg="midnight blue",
          font=('Helvetica 10 bold')).pack(pady=1)
    Button(frame4, height=2,
           width=25, font=('Helvetica 17 bold'), fg="midnight blue", bg="turquoise", text="Candidate",
           command=candidate).pack()
    Label(frame4, text="", bg="midnight blue",
          font=('Helvetica 10 bold')).pack(pady=1)
    Button(frame4, height=2,
           width=25, font=('Helvetica 17 bold'), fg="midnight blue", bg="turquoise",
           text="Volunteers Acceptance", command=reject_accept).pack()
    Label(frame4, text="", bg="midnight blue",
          font=('Helvetica 10 bold')).pack(pady=1)

    # else:
    # tk.messagebox.showinfo(None, "wrong username or password :(")
    conn.close()


def submit():
    fullname = Fullname.get()
    password = Password.get()

    print("Your Username is {} ".format(fullname))
    print("Your password is {} ".format(password))

    fullname.set("")
    Password.set("")


def invalid():
    invalid = Tk()
    invalid.title("Invalid Password")
    T = tk.Text(invalid, height=10, width=50)
    T.pack()
    T.insert(tk.END, """Invalid Password/n Include characters:
             numbers
             lowercase
             UPPERCASE
             Special Characters""")


def validate():
    while True:
        password = Password.get()
        if password < '8':
            invalid()
            break
        elif re.search('[0-9]', password) is None:
            invalid()
            break
        elif re.search('[A-Z]', password) is None:
            invalid()
            break
        else:
            window2 = Tk()
            window2.title("Confirmation")
            T = tk.Text(window2, height=2, width=30)
            T.pack()
            T.insert(tk.END, "Your Username and Password\nhas been set")
            break


window = tk.Tk()
frame = tk.Frame(master=window, bg="midnight blue")

window.title("Election system")
frame.pack(fill=tk.BOTH, expand=True)
frame.pack()

# root.title("Registration Form")

# reg = Frame(root)

Fullname = StringVar()
NationalCode = StringVar()
Email = StringVar()
Password = StringVar()
ConfirmPassword = StringVar()

conn = sqlite3.connect('Form.sql')
with conn:
    cursor = conn.cursor()

Label(frame, text="", bg="midnight blue",
      font=('Helvetica 17 bold')).pack(pady=17)
label1 = Label(frame, text="National Code",
               fg="turquoise", bg="midnight blue", font=('Helvetica 17 bold'))
label2 = tk.Label(frame, text="Password", width=20, font=(
    'Helvetica 17 bold'), fg="turquoise", bg="midnight blue")
entry2 = tk.Entry(frame, show="*", fg="midnight blue", bg="white",
                  width=20, font=('Helvetica 17 bold'))
entry1 = tk.Entry(frame, fg="midnight blue", bg="white",
                  width=20, font=('Helvetica 17 bold'))
label1.pack()
entry1.pack()
username = entry1.get()  # username get from user
label2.pack()
entry2.pack()
password = entry2.get()  # pass get from user


def check_USER_PASS():
    global State1
    conn = None
    output = []
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        s = '''SELECT natural_code, password, role FROM User'''
        cursor.execute(s)
        rows = cursor.fetchall()
        cols = [col[0] for col in cursor.description]
        for row in rows:
            d = {}
            for i in range(len(cols)):
                d[cols[i]] = row[i]
            output.append(d)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
    i = 0
    find = 0
    for row in rows:
        i = i + 1
    for j in range(i):
        if (list(output[j].values())[0]) == entry1.get() and (list(output[j].values())[1]) == entry2.get():
            find = 1
            if (list(output[j].values())[2]) == "Manager":
                State1 = 1
            else:
                State1 = 0
            print()
            print(list(output[j].values())[2])
            showinfo(title="Login", message="Login Successfully!")
            open_win()
            break
    if find == 0:
        showinfo(title="Error", message="Wrong NationalCode/Password!")


tk.Button(frame, text="Login", width=20, font=(
    'Helvetica 17 bold'), fg="midnight blue", bg="turquoise", command=check_USER_PASS).pack(pady=17)

tk.Button(frame, text="Sign Up", width=20, font=(
    'Helvetica 17 bold'), fg="midnight blue", bg="turquoise", command=signup).pack(pady=17)


def showMsg():
    # read from db

    tk.messagebox.showinfo(None, " Login successfuly ")


def database():
    fullname = Fullname.get()
    nationalCode = NationalCode.get()
    email = Email.get()
    role = var.get()
    password = Password.get()
    confirmpassword = ConfirmPassword.get()
    if (password == confirmpassword):
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS Student ( Fullname TEXT,NationalCode TEXT,Email TEXT,Role TEXT,Password TEXT)')
        cursor.execute('INSERT INTO Student (Fullname,NationalCode,Email,Role,Password) VALUES(?,?,?,?,?)',
                       (fullname, nationalCode, email, role, password))
        conn.commit()
        showinfo(title="Sign Up", message="Thanks for signing up!")


def main():
    fullname = Fullname.get()
    nationalCode = NationalCode.get()
    email = Email.get()
    role = var.get()
    password = Password.get()
    confirmpassword = ConfirmPassword.get()
    # branch = c.get()
    # prog = var1.get() + var2.get() + var3.get()
    tk.update(fullname, nationalCode, email, role, password)


def delete_task():
    database = r"Form.db"
    conn = sqlite3.connect(database)
    fullname = Fullname.get()
    password = Password.get()
    with conn:
        delete_task(conn, fullname)


# button2 = tk.Button(text='   Log in   ', command=database, bg='black', fg='white', font=('helvetica', 12, 'bold'))

# canvas1.create_window(300, 400, window=button2)

# window = tk.Tk()
# frame = tk.Frame(master=window, bg="midnight blue")


# frame.title("Login /Sign Up to voting system")
# frame.pack(fill=tk.BOTH, expand=True)


def iExit():
    iExit = tk.messagebox.askyesno("Scientific Calculator", "Do you want to exit ?")
    if iExit > 0:
        frame.destroy()
        return


def Data():
    frame.resizable(width=False, height=False)
    frame.geometry("1000x500+0+0")


def Form():
    frame.resizable(width=False, height=False)
    frame.geometry("500x500+0+0")


menubar = Menu(frame)

filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label="Form", command=Form)
filemenu.add_command(label="Data", command=Data)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=iExit)
# frame.config(menubar)

create_tables()

mainloop()
