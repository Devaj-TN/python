import tkinter as tk

def show_text():
    entered_text = entry.get()
    label.config(text=entered_text)

root = tk.Tk()
root.title("Display Input Text")
root.geometry("400x200")

entry = tk.Entry(root, width=30)
entry.pack(pady=20)

button = tk.Button(root, text="Show Text", command=show_text)
button.pack(pady=10)

label = tk.Label(root, text="", font=("Arial", 14))
label.pack(pady=20)

root.mainloop()
