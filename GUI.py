import tkinter as tk
from captureImage import *

# Function to be called when the button is clicked
def on_button_click():
    open_capture(image_counter)
    print("Button was clicked!")

# Create the main window
root = tk.Tk()
root.title("JPG to PNG Converter")

# Create a button widget
button = tk.Button(root, text="Camera", command=on_button_click)

# Pack the button into the window (makes it visible)
button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
