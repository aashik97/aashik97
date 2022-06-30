#Import the required libraries
from tkinter import *
from tkinter import ttk

#Create an instance of Tkinter Frame
win = Tk()
win.title('FCSKU Master')
#Set the geometry
win.geometry("300x300")

# Define a function to return the Input data
def get_data():
 label.config(text= entry.get(), font= ('Helvetica 13'))
 label.place(relx=.5, rely=.5, anchor=N)


#Create an Entry Widget
entry = Entry(win, width= 20)
entry.place(relx= .5, rely= .5, anchor= CENTER)

#Inititalize a Label widget
label= Label(win, text="ASIN", font=('Helvetica 13'), width=50)
label.pack()

#Create a Button to get the input data
ttk.Button(win, text= "Click to Show", command= get_data).place(relx= .7, rely= .5, anchor= CENTER)
win.mainloop()