import tkinter as tk

window = tk.Tk()
window.geometry("300x300")


calendar = tk.Label(text = "CALENDAR", background = "white", fg="black")
calendar.place(x=140,y=20)

year = tk.Label(text = "Enter The Year:",background = "white", fg="black")
year.place(x=133,y=45)

box = tk.Entry(window,width=5)
box.place(x=146,y=70)

button = tk.Button(window, text = "Submit", background = "White")
button.place(x=140,y=90)















window.mainloop()