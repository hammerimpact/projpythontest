from tkinter import *
from PIL import ImageTk, Image
import sqlite3


root = Tk()
root.title("test database 01")


txt_f_name = Label(root, text="first name")
txt_f_name.grid(row=0, column=0, padx=20)
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)

txt_l_name = Label(root, text="last name")
txt_l_name.grid(row=1, column=0, padx=20)
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)

txt_adress = Label(root, text="adress")
txt_adress.grid(row=2, column=0, padx=20)
address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)

txt_state = Label(root, text="state")
txt_state.grid(row=3, column=0, padx=20)
state = Entry(root, width=30)
state.grid(row=3, column=1, padx=20)

txt_zipcode = Label(root, text="zipcode")
txt_zipcode.grid(row=4, column=0, padx=20)
zipcode = Entry(root, width=30)
zipcode.grid(row=4, column=1, padx=20)

txt_dbid = Label(root, text="dbid")
txt_dbid.grid(row=5, column=0, padx=20)
dbid = Entry(root, width=30)
dbid.grid(row=5, column=1, padx=20)

def createdb():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE t_addresses (
            dbid integer,
            first_name text,
            last_name text,
            address text,
            state text,
            zipcode integer
            )
            """)
    conn.commit()
    conn.close()


btnsubmit = Button(root, text="create db", command=createdb)
btnsubmit.grid(row=6, column=0, columnspan=2, padx=30, pady=10, ipadx=100)



def clearui():
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)
    dbid.delete(0, END)

def onclicksubmit():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    c.execute("INSERT INTO t_addresses VALUES (:dbid, :f_name, :l_name, :address, :state, :zipcode)",
                {
                    'dbid'      : dbid.get(),
                    'f_name'    : f_name.get(),
                    'l_name'    : l_name.get(),
                    'address'   : address.get(),
                    'state'     : state.get(),
                    'zipcode'   : zipcode.get()
                }
    )

    conn.commit()
    conn.close()
    clearui()
    pass

btnsubmit = Button(root, text="submit", command=onclicksubmit)
btnsubmit.grid(row=7, column=0, columnspan=2, padx=30, pady=10, ipadx=100)


lblresult = Label(root, text="ssss")
lblresult.grid(row=9, column= 0)

def onclickshowresult():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    c.execute("SELECT * FROM t_addresses")
    records = c.fetchall()
    
    print_text = ""
    for e in records:
        print_text += str(e) + "\n"

    conn.commit()
    conn.close()

    lblresult['text'] = print_text

btnshowresult = Button(root, text="show result", command=onclickshowresult)
btnshowresult.grid(row=8, column=0, columnspan=2, padx=30, pady=10, ipadx=100)


txt_deletedbid = Label(root, text="dbid")
txt_deletedbid.grid(row=10, column=0)
deletedbid = Entry(root, width=30)
deletedbid.grid(row=10, column=1, padx=20)

def onclickdeletedata():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    c.execute(f"DELETE from t_addresses where dbid={deletedbid.get()}")

    conn.commit()
    conn.close()

btndelete = Button(root, text="delete db data", command=onclickdeletedata)
btndelete.grid(row=11, column=0, columnspan=2, padx=30, pady=10, ipadx=100)


def onclickedit():
    global editor
    editor = Tk()
    editor.title("edit data")

    global f_name_editor
    txt_f_name_editor = Label(editor, text="first name")
    txt_f_name_editor.grid(row=0, column=0, padx=20)
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20)

    global l_name_editor
    txt_l_name_editor = Label(editor, text="last name")
    txt_l_name_editor.grid(row=1, column=0, padx=20)
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1, padx=20)

    global address_editor
    txt_adress_editor = Label(editor, text="adress")
    txt_adress_editor.grid(row=2, column=0, padx=20)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1, padx=20)

    global state_editor
    txt_state_editor = Label(editor, text="state")
    txt_state_editor.grid(row=3, column=0, padx=20)
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=3, column=1, padx=20)

    global zipcode_editor
    txt_zipcode_editor = Label(editor, text="zipcode")
    txt_zipcode_editor.grid(row=4, column=0, padx=20)
    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=4, column=1, padx=20)

    global dbid_editor
    txt_dbid_editor = Label(editor, text="dbid")
    txt_dbid_editor.grid(row=5, column=0, padx=20)
    dbid_editor = Entry(editor, width=30)
    dbid_editor.grid(row=5, column=1, padx=20)

    btnSetEdit = Button(editor, text="Update", command=onclickupdate)
    btnSetEdit.grid(row=6, column=0, columnspan=2, padx=30, pady=10, ipadx=100)

    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    c.execute(f"SELECT * from t_addresses where dbid={deletedbid.get()}")
    records = c.fetchall()

    for record in records:
        dbid_editor.insert(0, record[0])
        f_name_editor.insert(0, record[1])
        l_name_editor.insert(0, record[2])
        address_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])

    conn.close()



def onclickupdate():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    c.execute(f"""UPDATE t_addresses SET 
        first_name = :f_name,
        last_name = :l_name,
        address = :address,
        state = :state,
        zipcode = :zipcode

        where dbid = :dbid
    """,
    {
        'dbid' : dbid_editor.get(),
        'f_name': f_name_editor.get(),
        'l_name': l_name_editor.get(),
        'address': address_editor.get(),
        'state': state_editor.get(),
        'zipcode': zipcode_editor.get(),
    }
    )

    conn.commit()
    conn.close()
    editor.destroy()

btnEdit = Button(root, text="Edit data", command=onclickedit)
btnEdit.grid(row=12, column=0, columnspan=2, padx=30, pady=10, ipadx=100)


root.mainloop()
