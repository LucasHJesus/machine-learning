import customtkinter as ctk
import tkinter as tk
import numpy as np

class Perceptron:
    def __init__(self, input_size, learning_rate=0.01, epochs=1000):
        self.weights = np.zeros(input_size + 1)  # +1 for the bias weight
        self.learning_rate = learning_rate
        self.epochs = epochs

    def activate(self, x):
        return 1 if x >= 0 else -1

    def train(self, X, y):
        for _ in range(self.epochs):
            for inputs, target in zip(X, y):
                inputs = np.insert(inputs, 0, 1)  # Adding bias input
                prediction = self.activate(np.dot(self.weights, inputs))
                error = target - prediction
                self.weights += self.learning_rate * error * inputs

    def predict(self, X):
        predictions = []
        for inputs in X:
            inputs = np.insert(inputs, 0, 1)
            prediction = self.activate(np.dot(self.weights, inputs))
            predictions.append(prediction)
        return predictions


def convert_to_bipolar(input_grid):
    bipolar_output = []
    for line in input_grid:
        for item in line:
            if item == 0:
                bipolar_output.append(-1)
            else:
                bipolar_output.append(item)
    return bipolar_output


# ctk configs
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# app configs
app = ctk.CTk()
app.geometry("900x600")
app.title("Reconhecimento de Dígitos")


my_font_1 = ctk.CTkFont(family="Courier", size=35, weight="normal")
my_font_2 = ctk.CTkFont(family="Courier", size=30, weight="normal")
text_1 = ctk.CTkLabel(app, text="Trabalho 4 - Machine Learning", font=my_font_1)
text_2 = ctk.CTkLabel(app, text="Reconhecimento de Dígitos", font=my_font_2)
text_1.pack(padx=10, pady=20)
text_2.pack(padx=10, pady=0)



GRID_SIZE = 5
CELL_SIZE = 50

cels_used = []

def clear(event):
    global cels_used
    cels_used = []

def paint(event):

    col = event.x // CELL_SIZE
    row = event.y // CELL_SIZE

    if [row,col] not in cels_used:

        cels_used.append([row,col])
        # Toggle the state and update the grid
        grid[row][col] = 1 - grid[row][col]

        # Update the color of the pixel based on the state
        new_color = "black" if grid[row][col] == 1 else "white"
        canvas.itemconfig(pixel_items[row][col], fill=new_color)


    # print(grid)


# Initialize the grid with all zeros
grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

canvas = tk.Canvas(app, width=GRID_SIZE * CELL_SIZE, height=GRID_SIZE * CELL_SIZE)
canvas.pack(padx=10, pady=50)

pixel_items = []
for row in range(GRID_SIZE):
    row_items = []
    for col in range(GRID_SIZE):
        item = canvas.create_rectangle(col * CELL_SIZE, row * CELL_SIZE,
                                       (col + 1) * CELL_SIZE, (row + 1) * CELL_SIZE,
                                       fill="white")
        row_items.append(item)
    pixel_items.append(row_items)

canvas.bind("<Button-1>", clear)
canvas.bind("<B1-Motion>", paint)


text_box = ctk.CTkTextbox(app, activate_scrollbars=False, height=10, width=20, border_width=2, border_color="gray", font=("Courier", 30))


def custom_index(lst, value):
    try:
        return lst.index(value)
    except ValueError:
        return -1

def button_event():
    text_box.delete("1.0", "end")
    new_grid = []
    new_grid.append(convert_to_bipolar(grid))
    # print("\n")
    predictions_array = []
    for k in range(len(perceptron_array)):
        predictions_array.append(perceptron_array[k].predict(new_grid))
    match custom_index(predictions_array, [1]):
        case 0:
            text_box.insert(index=tk.INSERT, text="0")
        case 1:
            text_box.insert(index=tk.INSERT, text="1")
        case 2:
            text_box.insert(index=tk.INSERT, text="2")
        case 3:
            text_box.insert(index=tk.INSERT, text="3")
        case 4:
            text_box.insert(index=tk.INSERT, text="4")
        case 5:
            text_box.insert(index=tk.INSERT, text="5")
        case 6:
            text_box.insert(index=tk.INSERT, text="6")
        case 7:
            text_box.insert(index=tk.INSERT, text="7")
        case 8:
            text_box.insert(index=tk.INSERT, text="8")
        case 9:
            text_box.insert(index=tk.INSERT, text="9")
        case -1:
            text_box.insert(index=tk.INSERT, text=" ")


def button_clear_event():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            canvas.itemconfig(pixel_items[row][col], fill="white")
            grid[row][col] = 0


button_clear = ctk.CTkButton(app, text="CLEAR", command=button_clear_event, font=("Courier", 25))
button_clear.pack(padx=10, pady=10)

button = ctk.CTkButton(app, text="SUBMIT", command=button_event, font=("Courier", 25))
button.pack(padx=10, pady=10)
text_box.pack(padx=10, pady=20)


if __name__ == "__main__":
    # Training process
    num0 = [-1, 1, 1, -1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1, -1, -1, 1, 1, -1, -1]

    num1 = [-1, -1, 1, -1, -1, -1, 1, 1, -1, -1, -1, -1, 1, -1, -1, -1, -1, 1, -1, -1, -1, 1, 1, 1, -1]

    num2 = [-1, 1, 1, -1, -1, 1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1, 1, 1, 1, 1, -1]

    num3 = [1, 1, 1, -1, -1, -1, -1, -1, 1, -1, -1, 1, 1, -1, -1, -1, -1, -1, 1, -1, 1, 1, 1, -1, -1]

    num4 = [1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1, 1, 1, 1, -1, -1, -1, 1, -1, -1, -1, -1, 1, -1, -1]

    num5 = [1, 1, 1, 1, -1, 1, -1, -1, -1, -1, 1, 1, 1, -1, -1, -1, -1, -1, 1, -1, 1, 1, 1, -1, -1]

    num6 = [-1, 1, 1, 1, -1, 1, -1, -1, -1, -1, 1, 1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, 1, -1, -1]

    num7 = [1, 1, 1, 1, -1, -1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1, -1, 1, -1, -1, -1]

    num8 = [-1, 1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, 1, -1, -1]

    num9 = [-1, 1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, 1, 1, -1, -1, -1, -1, 1, -1, -1, 1, 1, -1, -1]

    X = [num0, num1, num2, num3, num4, num5, num6, num7, num8, num9]

    target_pattern = [[1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, 1, -1, -1, -1, -1, -1, -1, -1, -1],
                      [-1, -1, 1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, 1, -1, -1, -1, -1, -1, -1],
                      [-1, -1, -1, -1, 1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, 1, -1, -1, -1, -1],
                      [-1, -1, -1, -1, -1, -1, 1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, 1, -1, -1],
                      [-1, -1, -1, -1, -1, -1, -1, -1, 1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, 1]]

    perceptron0 = Perceptron(input_size=25)
    perceptron1 = Perceptron(input_size=25)
    perceptron2 = Perceptron(input_size=25)
    perceptron3 = Perceptron(input_size=25)
    perceptron4 = Perceptron(input_size=25)
    perceptron5 = Perceptron(input_size=25)
    perceptron6 = Perceptron(input_size=25)
    perceptron7 = Perceptron(input_size=25)
    perceptron8 = Perceptron(input_size=25)
    perceptron9 = Perceptron(input_size=25)

    perceptron_array = [perceptron0, perceptron1, perceptron2, perceptron3, perceptron4, perceptron5, perceptron6,
                        perceptron7, perceptron8, perceptron9]

    for i in range(len(perceptron_array)):
        perceptron_array[i].train(X, target_pattern[i])

    app.mainloop()


