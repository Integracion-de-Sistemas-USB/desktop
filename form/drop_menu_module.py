import tkinter as tk
from tkinter import ttk

def create_drop_menu_frame(parent_frame):
    frame = ttk.Frame(parent_frame, padding="10")

    # Create a label for the percentage dropdown
    percentage_label = ttk.Label(frame, text="Percentage:")
    percentage_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)

    # Variable to hold the selected percentage
    percentage_var = tk.StringVar(value="0%")

    # Create and place the percentage dropdown menu
    percentage_combobox = ttk.Combobox(frame, values=["0%", "20%", "40%", "60%", "80%", "100%"], textvariable=percentage_var)
    percentage_combobox.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

    return frame, percentage_var
