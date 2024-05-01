import tkinter as tk

class TodoList:
    def __init__(self, listbox):
        self.items = []
        self.listbox = listbox

    def add(self, item):
        self.items.append(item)
        self.update_listbox()

    def remove(self, item):
        self.items.remove(item)
        self.update_listbox()

    def get_list(self):
        return self.items

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for item in self.items:
            self.listbox.insert(tk.END, item)

class TodoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")
        self.master.geometry("400x300")  

        self.listbox = tk.Listbox(master, width=50, height=15) 
        self.listbox.pack(pady=10)

        self.todo_list = TodoList(self.listbox)

        self.label = tk.Label(master, text="Enter task:")
        self.label.pack()

        self.entry = tk.Entry(master, width=40)
        self.entry.pack()

        self.add_button = tk.Button(master, text="Add", command=self.add_item, width=10, bg="#4CAF50", fg="white", relief=tk.GROOVE)
        self.add_button.pack(pady=5)

        self.remove_button = tk.Button(master, text="Remove", command=self.remove_item, width=10, bg="#f44336", fg="white", relief=tk.GROOVE)
        self.remove_button.pack()

        # Change color on hover for add button
        self.add_button.bind("<Enter>", lambda event: self.on_enter(event, self.add_button, "#45a049"))
        self.add_button.bind("<Leave>", lambda event: self.on_leave(event, self.add_button, "#4CAF50"))

        # Change color on hover for remove button
        self.remove_button.bind("<Enter>", lambda event: self.on_enter(event, self.remove_button, "#e57373"))
        self.remove_button.bind("<Leave>", lambda event: self.on_leave(event, self.remove_button, "#f44336"))

    def add_item(self):
        item = self.entry.get()
        if item:
            self.todo_list.add(item)
            self.entry.delete(0, tk.END)

    def remove_item(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            item = self.listbox.get(selected_index)
            self.todo_list.remove(item)

    def on_enter(self, event, widget, color):
        widget.config(bg=color)

    def on_leave(self, event, widget, color):
        widget.config(bg=color)

def main():
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
