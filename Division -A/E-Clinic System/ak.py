from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry


def calendar_view():
    def print_sel():
        e2 = Entry(mainframe, width=50)
        e2.insert(END, cal.selection_get())
        e2.grid(row=2, column=1)

    top = Toplevel(root)

    cal = Calendar(top, font="Arial 14", selectmode='day', cursor="hand1", year=2018, month=2, day=5)
    cal.pack(fill="both", expand=True)
    ttk.Button(top, text="ok", command=print_sel).pack()
    return "pk"


# widow properties...............................................................................

root = Tk()
root.geometry('640x480')
root.title("Student Managment System")

# frames...........................................................................................

mainframe = ttk.Frame(root, padding="10 10 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
Label(mainframe, text="USER NAME/EMAIL").grid(row=0, column=0, sticky='E')
e1 = Entry(mainframe, width=50).grid(row=0, column=1)
Label(mainframe, text="PASSWORD").grid(row=1, column=0, sticky='E')
e2 = Entry(mainframe, width=50, ).grid(row=1, column=1, )
Label(mainframe, text="DOB").grid(row=2, column=0, sticky='E')

b1 = Button(mainframe, text='Select DOB', width=10, command=calendar_view)
b1.grid(row=3, column=1, sticky='E')

root.mainloop()