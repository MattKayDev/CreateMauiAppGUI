import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import subprocess
import os

# Create the main application window
root = tk.Tk()
root.title("Create .NET Maui App")
root.geometry("400x300")

# Label for the path input
label_path = tk.Label(root, text="Enter or select the path:")
label_path.pack(pady=5)

# Entry widget for the path input
path_entry = tk.Entry(root, width=50)
path_entry.pack(pady=5)

# Button to open file dialog
def browse_directory():
    path = filedialog.askdirectory()
    if path:
        path_entry.delete(0, tk.END)
        path_entry.insert(0, path)

browse_button = tk.Button(root, text="Browse", command=browse_directory)
browse_button.pack(pady=5)

# Label for the name input
label_name = tk.Label(root, text="Enter the name:")
label_name.pack(pady=5)

# Entry widget for the name input
name_entry = tk.Entry(root, width=50)
name_entry.pack(pady=5)

# Function to run the terminal command
def run_command():
    path = path_entry.get()
    name = name_entry.get()
    full_path = os.path.join(path, name)
    
    if not path:
        messagebox.showerror("Error", "Please enter a valid path.")
        return
    
    if not name:
        messagebox.showerror("Error", "Please enter a valid name.")
        return

    if os.path.exists(full_path):
        messagebox.showerror("Error", f"A project named '{name}' already exists at the specified path.")
        return
    
    try:
        # Change the working directory to the specified path
        command = ['dotnet', 'new', 'maui', '-o', name]
        result = subprocess.run(command, cwd=path, capture_output=True, text=True, check=True)
        
        if "created successfully" in result.stdout.lower():
            messagebox.showinfo("Success", f"Successfully created {name}")
        else:
            messagebox.showerror("Error", "An error occurred:\n" + result.stdout)
            
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"An error occurred:\n{e.stderr}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Button to run the command
run_button = tk.Button(root, text="Create .NET MAUI App", command=run_command)
run_button.pack(pady=20)

# Run the main event loop
root.mainloop()