import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

def plot_graph():
    # Get data from entry widgets
    x_data = list(map(float, entry_x.get().split(',')))
    y_data = list(map(float, entry_y.get().split(',')))

    # Create a new figure
    fig = Figure(figsize=(5, 4), dpi=100)
    plot = fig.add_subplot(1, 1, 1)

    # Plot the data
    plot.plot(x_data, y_data, marker='o')

    # Embed the figure into the Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=3, column=0, columnspan=2)

# Create the main window
window = tk.Tk()
window.title("Data Entry and Plotting")

# Create entry widgets for x and y data
label_x = ttk.Label(window, text="X Data:")
label_x.grid(row=0, column=0)
entry_x = ttk.Entry(window)
entry_x.grid(row=0, column=1)

label_y = ttk.Label(window, text="Y Data:")
label_y.grid(row=1, column=0)
entry_y = ttk.Entry(window)
entry_y.grid(row=1, column=1)

# Button to trigger the plot
plot_button = ttk.Button(window, text="Plot", command=plot_graph)
plot_button.grid(row=2, column=0, columnspan=2)

# Start the Tkinter event loop
window.mainloop()
