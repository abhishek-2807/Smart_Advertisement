import mysql.connector
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import matplotlib.pyplot as plt
from tkinter.font import Font
mt=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="abhishek")
h=mt.cursor()


def action():
    va=c.get()
    if va=="Hour Wise":
        number = []
        dur = ["00:00 to 2:00", "2:00 to 4:00", "4:00 to 6:00", "6:00 to 8:00", "8:00 to 10:00", "10:00 to 12:00",
               "12:00 to 14:00", "14:00 to 16:00", "16:00 to 18:00", "18:00 to 20:00", "20:00 to 22:00",
               "22:00 to 00:00"]
        q = 'SELECT COUNT(SNo) from camera WHERE TIME(Start_Time) BETWEEN TIME("00:00:00") AND TIME("02:00:01")'
        h.execute(q)
        a = h.fetchall()
        for i in a:
            for j in i:
                print(j)
                number.append(j)
        q = 'SELECT COUNT(SNo) from camera WHERE TIME(Start_Time) BETWEEN TIME("02:00:00") AND TIME("04:00:01")'
        h.execute(q)
        a = h.fetchall()
        for i in a:
            for j in i:
                print(j)
                number.append(j)
        q = 'SELECT COUNT(SNo) from camera WHERE TIME(Start_Time) BETWEEN TIME("04:00:00") AND TIME("06:00:01")'
        h.execute(q)
        a = h.fetchall()
        for i in a:
            for j in i:
                print(j)
                number.append(j)
        q = 'SELECT COUNT(SNo) from camera WHERE TIME(Start_Time) BETWEEN TIME("06:00:00") AND TIME("08:00:01")'
        h.execute(q)
        a = h.fetchall()
        for i in a:
            for j in i:
                print(j)
                number.append(j)
        q = 'SELECT COUNT(SNo) from camera WHERE TIME(Start_Time) BETWEEN TIME("08:00:00") AND TIME("10:00:01")'
        h.execute(q)
        a = h.fetchall()
        for i in a:
            for j in i:
                print(j)
                number.append(j)
        q = 'SELECT COUNT(SNo) from camera WHERE TIME(Start_Time) BETWEEN TIME("10:00:00") AND TIME("12:00:01")'
        h.execute(q)
        a = h.fetchall()
        for i in a:
            for j in i:
                print(j)
                number.append(j)
        q = 'SELECT COUNT(SNo) from camera WHERE TIME(Start_Time) BETWEEN TIME("12:00:00") AND TIME("14:00:01")'
        h.execute(q)
        a = h.fetchall()
        for i in a:
            for j in i:
                print(j)
                number.append(j)
        q = 'SELECT COUNT(SNo) from camera WHERE TIME(Start_Time) BETWEEN TIME("14:00:00") AND TIME("16:00:01")'
        h.execute(q)
        a = h.fetchall()
        for i in a:
            for j in i:
                print(j)
                number.append(j)
        q = 'SELECT COUNT(SNo) from camera WHERE TIME(Start_Time) BETWEEN TIME("16:00:00") AND TIME("18:00:01")'
        h.execute(q)
        a = h.fetchall()
        for i in a:
            for j in i:
                print(j)
                number.append(j)
        q = 'SELECT COUNT(SNo) from camera WHERE TIME(Start_Time) BETWEEN TIME("18:00:00") AND TIME("20:00:01")'
        h.execute(q)
        a = h.fetchall()
        for i in a:
            for j in i:
                print(j)
                number.append(j)
        q = 'SELECT COUNT(SNo) from camera WHERE TIME(Start_Time) BETWEEN TIME("20:00:00") AND TIME("22:00:01")'
        h.execute(q)
        a = h.fetchall()
        for i in a:
            for j in i:
                print(j)
                number.append(j)
        q = 'SELECT COUNT(SNo) from camera WHERE TIME(Start_Time) BETWEEN TIME("22:00:00") AND TIME("0:00:01")'
        h.execute(q)
        a = h.fetchall()
        for i in a:
            for j in i:
                print(j)
                number.append(j)
        print(number)
        plt.bar(dur, number)
        plt.title("Bar plot of Number of vieweres in different time interval")
        plt.xlabel("Time Intervals")
        plt.ylabel("Number of Viewers")
        plt.xticks(dur, rotation=45)
        plt.get_current_fig_manager().window.state('zoomed')
        plt.show()


    elif va=="Day Wise":
        messagebox.showerror("Error","Not enough data available for Date Wise comparison")
        # dur=[]
        # number=[]
        # h.execute("SELECT DISTINCT Date from camera")
        # a = h.fetchall()
        # for i in a:
        #     for j in i:
        #         j = j.strftime("%Y-%m-%d")
        #         dur.append(j)
        #         print(dur)
        # for i in dur:
        #     print(i)
        #     h.execute("SELECT COUNT(SNo) from camera WHERE DATE(Date)=DATE(temp)")
        #     a=h.fetchall()
        #     for j in a:
        #         for k in j:
        #             number.append(k)

    elif va=="Week Wise":
        messagebox.showerror("Error","Not enough data available for weekly comparison")

    else:
        messagebox.showerror("Error","Please Select an option")

root=Tk()
root.title("Visualise Data")
root.geometry("400x250+450+225")
my = Font(family="Helvetica", size=16, weight="bold", slant="italic")
l1=Label(root,text="Please enter details below to log in")
l1.config(font=my)
l1.pack()
Label(root,text="").pack()
my = Font(family="Helvetica", size=14, weight="bold")
l2=Label(root,text="Enter the category according to which")
l2.config(font=my)
l2.pack()
l2=Label(root,text="data will be presented")
l2.config(font=my)
l2.pack()
Label(root,text="").pack()
v=["Hour Wise","Day Wise","Week Wise"]
c=Combobox(root,values=v,height=3,width=15)
c.set("select")
c.pack()
Label(root,text="").pack()
b=Button(root,text="Go",command=action).pack()
root.mainloop()
