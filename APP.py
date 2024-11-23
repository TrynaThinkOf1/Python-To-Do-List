import customtkinter as ctk

to_dos = {}

app = ctk.CTk()
ctk.set_default_color_theme("themes/violet.json")
app.geometry("750x750")


def add():
    name = add_todo_name.get()
    desc = add_todo_desc.get()
    if name and desc:
        to_dos[name] = desc
        add_todo_name.delete(0, ctk.END)
        add_todo_desc.delete(0, ctk.END)
        reload_list()


def remove(name):
    to_dos.pop(name)
    reload_list()


def reload_list():
    for widget in list_frame.winfo_children():
        widget.destroy()

    for name, desc in to_dos.items():
        frame = ctk.CTkFrame(master=list_frame)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure(0, weight=1)

        label = ctk.CTkLabel(master=frame, text=name, anchor="w")
        label.grid(row=0, column=0, sticky="w", padx=10, pady=10)

        button = ctk.CTkButton(master=frame, text="Remove", command=lambda n=name: remove(n))
        button.grid(row=0, column=1, padx=10, pady=10)

        frame.grid(pady=5, sticky="ew")

        frame.bind("<Button-1>", lambda event, lbl=label, n=name, d=desc: toggle(event, lbl, n, d))


def toggle(event, label, name, desc):
    current_text = label.cget("text")
    if current_text == name:
        label.config(text=desc)
    else:
        label.config(text=name)


# Entry for name
add_todo_name = ctk.CTkEntry(master=app, placeholder_text="To Do...")
add_todo_name.grid(row=0, column=0, pady=10, padx=10, sticky="ew")

# Entry for description
add_todo_desc = ctk.CTkEntry(master=app, placeholder_text="Description...")
add_todo_desc.grid(row=0, column=1, pady=10, padx=10, sticky="ew")

# Add button
add_button = ctk.CTkButton(master=app, text="Add To Do", command=add)
add_button.grid(row=0, column=2, pady=10, padx=10)

# Scrollable list frame
list_frame_container = ctk.CTkFrame(master=app)
list_frame_container.grid(row=1, column=0, columnspan=3, pady=20, sticky="nsew")

canvas = ctk.CTkCanvas(list_frame_container)
scrollbar = ctk.CTkScrollbar(list_frame_container, command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)
scrollable_list_frame = ctk.CTkFrame(canvas)

scrollable_list_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_list_frame, anchor="nw")
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

list_frame = scrollable_list_frame

# Dynamic resizing
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)
app.grid_columnconfigure(2, weight=0)
app.grid_rowconfigure(1, weight=1)

app.mainloop()