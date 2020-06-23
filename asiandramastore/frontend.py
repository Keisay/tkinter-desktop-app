from tkinter import *
import webbrowser
import backend

chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

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

def watch_drama(selected_drama):
    return selected_tuple[4]     

def view_command():
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row)
    
def search_command():
    list1.delete(0, END)
    for row in backend.search(drama_text.get(), episodes_text.get(), year_text.get(), link_text.get()):
        list1.insert(END, row)
        
def add_command():
    backend.insert(drama_text.get(), episodes_text.get(), year_text.get(), link_text.get())
    list1.delete(0, END)
    list1.insert(END, (drama_text.get(), episodes_text.get(), year_text.get()), link_text.get())
    
def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0], drama_text.get(), episodes_text.get(), year_text.get(), link_text.get())

def watch_command():
    webbrowser.get(chrome_path).open(selected_tuple[4], new=1)

window = Tk()

label_1 = Label(window, text="Drama")
label_1.grid(row=0,column=0)

label_2 = Label(window, text="Episodes")
label_2.grid(row=0,column=2)

label_3 = Label(window, text="Year")
label_3.grid(row=1,column=0)

label_4 = Label(window, text="Link")
label_4.grid(row=1,column=2)

drama_text = StringVar()
entry_1 = Entry(window, textvariable=drama_text)
entry_1.grid(row=0,column=1)

episodes_text = StringVar()
entry_2 = Entry(window, textvariable=episodes_text)
entry_2.grid(row=0,column=3)

year_text = StringVar()
entry_3 = Entry(window, textvariable=year_text)
entry_3.grid(row=1,column=1)

link_text = StringVar()
entry_4 = Entry(window, textvariable=link_text)
entry_4.grid(row=1,column=3)


list1 = Listbox(window, height=7, width=35)
list1.grid(row=2,column=0,rowspan=7,columnspan=2)

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

b6 = Button(window, text="Watch", width=12, command=watch_command)
b6.grid(row=7,column=3)

b7 = Button(window, text="Close", width=12, command=window.destroy)
b7.grid(row=8,column=3)

window.mainloop()


