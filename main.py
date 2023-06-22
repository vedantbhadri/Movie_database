# pip install PyMySQL
import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk


# connection for phpmyadmin
def connection():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='vedant5121',
        db='mydata',
    )
    return conn


def refreshTable():
    for data in my_tree.get_children():
        my_tree.delete(data)

    for array in read():
        my_tree.insert(parent='', index='end', iid=array, text="", values=(array), tag="orow")

    my_tree.tag_configure('orow', background='#EEEEEE', font=('Arial', 12))
    my_tree.grid(row=8, column=0, columnspan=5, rowspan=11, padx=10, pady=20)


root = Tk()
root.title("Movie Database")
root.geometry("1080x720")
my_tree = ttk.Treeview(root)

# placeholders for entry
ph1 = tk.StringVar()
ph2 = tk.StringVar()
ph3 = tk.StringVar()
ph4 = tk.StringVar()
ph5 = tk.StringVar()


# placeholder set value function
def setph(word, num):
    if num == 1:
        ph1.set(word)
    if num == 2:
        ph2.set(word)
    if num == 3:
        ph3.set(word)
    if num == 4:
        ph4.set(word)
    if num == 5:
        ph5.set(word)


def read():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM movies")
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results


def add():
    movie_id = str(movieidEntry.get())
    movie_name = str(movie_nameEntry.get())
    streaming_company = str(Streaming_companyEntry.get())
    date_watched = str(date_watchedEntry.get())
    rating = str(ratingEntry.get())

    if (movie_id == "" or movie_id == " ") or (movie_name == "" or movie_name == " ") or (
            streaming_company == "" or streaming_company == " ") or (date_watched == "" or date_watched == " ") or (
            rating == "" or rating == " "):
        messagebox.showinfo("Error", "Please fill up the blank entry")
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO movies VALUES ('" + movie_id + "','" + movie_name + "','" + streaming_company + "','" + date_watched + "','" + rating + "') ")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "movie ID already exist")
            return

    refreshTable()


def reset():
    decision = messagebox.askquestion("Warning!!", "Delete all data?")
    if decision != "yes":
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM movies")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Sorry an error occured")
            return

        refreshTable()


def delete():
    decision = messagebox.askquestion("Warning!!", "Delete the selected data?")
    if decision != "yes":
        return
    else:
        selected_item = my_tree.selection()[0]
        deleteData = str(my_tree.item(selected_item)['values'][0])
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM movies WHERE movie_id='" + str(deleteData) + "'")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Sorry an error occured")
            return

        refreshTable()


def select():
    try:
        selected_item = my_tree.selection()[0]
        movie_id = str(my_tree.item(selected_item)['values'][0])
        movie_name = str(my_tree.item(selected_item)['values'][1])
        streaming_company = str(my_tree.item(selected_item)['values'][2])
        data_watched = str(my_tree.item(selected_item)['values'][3])
        rating = str(my_tree.item(selected_item)['values'][4])

        setph(movie_id, 1)
        setph(movie_name, 2)
        setph(streaming_company, 3)
        setph(data_watched, 4)
        setph(rating, 5)
    except:
        messagebox.showinfo("Error", "Please select a data row")


def search():
    movie_id = str(movieidEntry.get())
    movie_name = str(movie_nameEntry.get())
    streaming_company = str(Streaming_companyEntry.get())
    date_watched = str(date_watchedEntry.get())
    rating = str(ratingEntry.get())

    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM movies WHERE movie_name='" +
                   movie_id + "' or movie_name='" +
                   movie_name + "' or streaming_company='" +
                   streaming_company + "' or date_watched='" +
                   date_watched + "' or rating='" +
                   rating + "' ")

    try:
        result = cursor.fetchall()

        for num in range(0, 5):
            setph(result[0][num], (num + 1))

        conn.commit()
        conn.close()
    except:
        messagebox.showinfo("Error", "No data found")


def update():
    selectedMovieId = ""

    try:
        selected_item = my_tree.selection()[0]
        selectedMovieId = str(my_tree.item(selected_item)['values'][0])
    except:
        messagebox.showinfo("Error", "Please select a data row")

    movie_id = str(movieidEntry.get())
    movie_name = str(movie_nameEntry.get())
    streaming_company = str(Streaming_companyEntry.get())
    date_watched = str(date_watchedEntry.get())
    rating = str(ratingEntry.get())

    if (movie_id == "" or movie_id == " ") or (movie_name == "" or movie_id == " ") or (
            streaming_company == "" or streaming_company == " ") or (date_watched == "" or date_watched == " ") or (
            rating == "" or rating == " "):
        messagebox.showinfo("Error", "Please fill up the blank entry")
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE students SET STUDID='" +
                           movie_id + "', FNAME='" +
                           movie_name + "', LNAME='" +
                           streaming_company + "', ADDRESS='" +
                           date_watched + "', PHONE='" +
                           rating + "' WHERE STUDID='" +
                           selectedMovieId + "' ")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Stud ID already exist")
            return

    refreshTable()


label = Label(root, text="Movie Database", font=('Arial Bold', 30))
label.grid(row=0, column=0, columnspan=8, rowspan=2, padx=50, pady=40)

movieidLabel = Label(root, text="Movie ID", font=('Arial', 15))
nameLabel = Label(root, text="Movie Name", font=('Arial', 15))
streamingLabel = Label(root, text="Streaming Site", font=('Arial', 15))
dateLabel = Label(root, text="Watched Date", font=('Arial', 15))
ratingLabel = Label(root, text="Rating", font=('Arial', 15))

movieidLabel.grid(row=3, column=0, columnspan=1, padx=50, pady=5)
nameLabel.grid(row=4, column=0, columnspan=1, padx=50, pady=5)
streamingLabel.grid(row=5, column=0, columnspan=1, padx=50, pady=5)
dateLabel.grid(row=6, column=0, columnspan=1, padx=50, pady=5)
ratingLabel.grid(row=7, column=0, columnspan=1, padx=50, pady=5)

movieidEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable=ph1)
movie_nameEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable=ph2)
Streaming_companyEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable=ph3)
date_watchedEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable=ph4)
ratingEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable=ph5)

movieidEntry.grid(row=3, column=1, columnspan=4, padx=5, pady=0)
movie_nameEntry.grid(row=4, column=1, columnspan=4, padx=5, pady=0)
Streaming_companyEntry.grid(row=5, column=1, columnspan=4, padx=5, pady=0)
date_watchedEntry.grid(row=6, column=1, columnspan=4, padx=5, pady=0)
ratingEntry.grid(row=7, column=1, columnspan=4, padx=5, pady=0)

addBtn = Button(
    root, text="Add", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#84F894", command=add)
updateBtn = Button(
    root, text="Update", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#84E8F8", command=update)
deleteBtn = Button(
    root, text="Delete", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#FF9999", command=delete)
searchBtn = Button(
    root, text="Search", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#F4FE82", command=search)
resetBtn = Button(
    root, text="Reset", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#F398FF", command=reset)
selectBtn = Button(
    root, text="Select", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#EEEEEE", command=select)

addBtn.grid(row=3, column=5, columnspan=1, rowspan=2)
updateBtn.grid(row=5, column=5, columnspan=1, rowspan=2)
deleteBtn.grid(row=7, column=5, columnspan=1, rowspan=2)
searchBtn.grid(row=9, column=5, columnspan=1, rowspan=2)
resetBtn.grid(row=11, column=5, columnspan=1, rowspan=2)
selectBtn.grid(row=13, column=5, columnspan=1, rowspan=2)

style = ttk.Style()
style.configure("Treeview.Heading", font=('Arial Bold', 15))

my_tree['columns'] = ("Movie ID", "Movie Name", "Streaming Site", "Watched Date", "Rating")

my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Movie ID", anchor=W, width=170)
my_tree.column("Movie Name", anchor=W, width=150)
my_tree.column("Streaming Site", anchor=W, width=150)
my_tree.column("Watched Date", anchor=W, width=165)
my_tree.column("Rating", anchor=W, width=150)

my_tree.heading("Movie ID", text="Movie ID", anchor=W)
my_tree.heading("Movie Name", text="Movie Name", anchor=W)
my_tree.heading("Streaming Site", text="Streaming Site", anchor=W)
my_tree.heading("Watched Date", text="Watched Date", anchor=W)
my_tree.heading("Rating", text="Rating", anchor=W)

refreshTable()

root.mainloop()