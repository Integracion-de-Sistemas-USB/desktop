import tkinter as tk
from tkinter import ttk

def create_name_entry_frame(parent_frame, label_text="Enter your name:"):
    frame = ttk.Frame(parent_frame, padding="1")

    name_label = ttk.Label(frame, text=label_text)
    name_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)

    name_entry = ttk.Entry(frame, width=15)
    name_entry.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
    name_entry.focus()

    return frame, name_entry
