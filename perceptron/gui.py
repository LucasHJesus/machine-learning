from tkinter import Canvas
import customtkinter as ctk


square_size = 50
grid_size = 4
grid = []
grid_itens = []



def button_callback():
    print("button clicked")

app = ctk.CTk()
app.geometry("400x512")

canvas = Canvas(app, width = grid_size *square_size, height= grid_size *square_size)
canvas.pack()

button = ctk.CTkButton(app, text="my button", command=button_callback)
button.pack(padx=20, pady=20)

app.mainloop()
