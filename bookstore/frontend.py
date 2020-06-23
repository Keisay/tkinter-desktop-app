from tkinter import *
import backend

def get_selected_row(event):
    global selected_tuple
    index = list1.curselection()
    selected_tuple = list1.get(index)
    entry_1.delete(0, END)
    entry_1.insert(END, selected_tuple[1])
    entry_2.delete(0, END)
    entry_2.insert(END, selected_tuple[2])
    entry_3.delete(0, END)
    entry_3.insert(END, selected_tuple[3])
      

def view_command():
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row)
    
def search_command():
    list1.delete(0, END)
    for row in backend.search(title_text.get(), author_text.get(), year_text.get()):
        list1.insert(END, row)
        
def add_command():
    backend.insert(title_text.get(), author_text.get(), year_text.get())
    list1.delete(0, END)
    list1.insert(END, (title_text.get(), author_text.get(), year_text.get()))
    
def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get())
    

window = Tk()

label_1 = Label(window, text="Title")
label_1.grid(row=0,column=0)

label_2 = Label(window, text="Author")
label_2.grid(row=0,column=2)

label_3 = Label(window, text="Year")
label_3.grid(row=1,column=0)

title_text = StringVar()
entry_1 = Entry(window, textvariable=title_text)
entry_1.grid(row=0,column=1)

author_text = StringVar()
entry_2 = Entry(window, textvariable=author_text)
entry_2.grid(row=0,column=3)

year_text = StringVar()
entry_3 = Entry(window, textvariable=year_text)
entry_3.grid(row=1,column=1)

list1 = Listbox(window, height=6, width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

b1 = Button(window, text="View all", width=12, command=view_command)
b1.grid(row=2,column=3)

b2 = Button(window, text="Search entry", width=12, command=search_command)
b2.grid(row=3,column=3)

b3 = Button(window, text="Add entry", width=12, command=add_command)
b3.grid(row=4,column=3)

b4 = Button(window, text="Update selected", width=12, command=update_command)
b4.grid(row=5,column=3)

b5 = Button(window, text="Delete selected", width=12, command=delete_command)
b5.grid(row=6,column=3)

b6 = Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7,column=3)

window.mainloop()


