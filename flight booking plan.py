from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("600x600")
Label(root, text="which country you want to travel in?",font="lucida 19 bold").pack()
country = ["Australia", "japan", "U.S.A", "England"]
var = StringVar()
new_var = var.set("nowhere")
def travel():
    tmsg.showinfo("lets travel", f"so, we are booking our flight to{var.get()}\nWe wish youa happy journey")
    for x in range(6):
        Radiobutton(root, text=country[x], variable=var,value=country[x]).pack()
Button(root, text ="lets travel", command=travel).pack()
root.mainloop()
