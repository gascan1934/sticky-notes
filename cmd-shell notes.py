import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os

# Create the main application window
root = tk.Tk()
root.title("Quick NotePad")
root.geometry("600x400")

# Default theme and font size settings
dark_mode = False
default_font_size = 12

# Create a frame for the toolbar
toolbar = tk.Frame(root)
toolbar.pack(side="top", fill="x")

# Create a text area with a scrollbar
text_area = tk.Text(root, wrap="word", undo=True, font=("Arial", default_font_size))
scrollbar = tk.Scrollbar(root, command=text_area.yview)
text_area.config(yscrollcommand=scrollbar.set)
text_area.pack(expand=True, fill="both", side="left")
scrollbar.pack(side="right", fill="y")

# Function to open a persistent CMD window (this keeps it open)
def open_cmd():
    os.system("start cmd")  # Opens CMD and keeps it open

# Function to open PowerShell inside the already open CMD window
def switch_to_powershell():
    os.system("start cmd /k powershell")  # Opens CMD and switches to PowerShell inside

# Function to switch back to CMD inside the same window
def switch_to_cmd():
    os.system("start cmd /k cmd")  # Opens CMD and keeps it open in CMD mode

# Function to save the note
def save_note():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text_area.get(1.0, tk.END))
        messagebox.showinfo("Saved", "Note saved successfully!")

# Function to open a file
def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file.read())

# Function to toggle dark mode
def toggle_dark_mode():
    global dark_mode
    if dark_mode:
        root.config(bg="white")
        text_area.config(bg="white", fg="black", insertbackground="black")
        dark_mode_button.config(text="Enable Dark Mode", bg="lightgray", fg="black")
    else:
        root.config(bg="black")
        text_area.config(bg="black", fg="white", insertbackground="white")
        dark_mode_button.config(text="Disable Dark Mode", bg="gray", fg="white")
    dark_mode = not dark_mode

# Function to change font size
def change_font_size(size_change):
    global default_font_size
    default_font_size += size_change
    text_area.config(font=("Arial", default_font_size))

# Add buttons to the toolbar
cmd_button = tk.Button(toolbar, text="Open CMD", command=open_cmd)
cmd_button.pack(side="left", padx=5, pady=5)

ps_button = tk.Button(toolbar, text="Switch to PowerShell", command=switch_to_powershell)
ps_button.pack(side="left", padx=5, pady=5)

back_to_cmd_button = tk.Button(toolbar, text="Switch to CMD", command=switch_to_cmd)
back_to_cmd_button.pack(side="left", padx=5, pady=5)

open_button = tk.Button(toolbar, text="Open File", command=open_file)
open_button.pack(side="left", padx=5, pady=5)

save_button = tk.Button(toolbar, text="Save Note", command=save_note)
save_button.pack(side="left", padx=5, pady=5)

dark_mode_button = tk.Button(toolbar, text="Enable Dark Mode", command=toggle_dark_mode)
dark_mode_button.pack(side="left", padx=5, pady=5)

font_increase_button = tk.Button(toolbar, text="Increase Font Size", command=lambda: change_font_size(2))
font_increase_button.pack(side="left", padx=5, pady=5)

font_decrease_button = tk.Button(toolbar, text="Decrease Font Size", command=lambda: change_font_size(-2))
font_decrease_button.pack(side="left", padx=5, pady=5)

# Run the application
root.mainloop()
