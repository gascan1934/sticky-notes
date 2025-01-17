import tkinter as tk
from tkinter import filedialog, messagebox

# Create the main application window
root = tk.Tk()
root.title("Quick NotePad")
root.geometry("600x400")

# Create a text area with a scrollbar
text_area = tk.Text(root, wrap="word", undo=True)
scrollbar = tk.Scrollbar(root, command=text_area.yview)
text_area.config(yscrollcommand=scrollbar.set)
text_area.pack(expand=True, fill="both", side="left")
scrollbar.pack(side="right", fill="y")

# Function to create a new file
def new_file():
    text_area.delete(1.0, tk.END)

# Function to open a file
def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file.read())

# Function to save a file
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text_area.get(1.0, tk.END))
        messagebox.showinfo("Saved", "File saved successfully!")

# Create a menu bar
menu_bar = tk.Menu(root)

# Add "File" menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

menu_bar.add_cascade(label="File", menu=file_menu)

# Set the menu bar
root.config(menu=menu_bar)

# Run the application
root.mainloop()
