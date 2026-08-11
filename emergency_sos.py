import tkinter as tk
from tkinter import ttk, messagebox


# Create main window
root = tk.Tk()
root.title("Emergency SOS System")
root.geometry("500x600")


# Heading
title_label = tk.Label(
    root,
    text="EMERGENCY SOS SYSTEM",
    font=("Arial", 20, "bold")
)
title_label.pack(pady=20)


# User Name
tk.Label(root, text="User Name").pack()
user_name_entry = tk.Entry(root, width=40)
user_name_entry.pack(pady=5)


# Phone Number
tk.Label(root, text="Phone Number").pack()
phone_entry = tk.Entry(root, width=40)
phone_entry.pack(pady=5)


# Emergency Type
tk.Label(root, text="Emergency Type").pack()

emergency_type = ttk.Combobox(
    root,
    values=["Accident", "Medical", "Fire", "Crime", "Other"],
    width=37
)
emergency_type.pack(pady=5)
emergency_type.set("Select Emergency Type")


# Location
tk.Label(root, text="Location").pack()
location_entry = tk.Entry(root, width=40)
location_entry.pack(pady=5)


# Latitude
tk.Label(root, text="Latitude").pack()
latitude_entry = tk.Entry(root, width=40)
latitude_entry.pack(pady=5)


# Longitude
tk.Label(root, text="Longitude").pack()
longitude_entry = tk.Entry(root, width=40)
longitude_entry.pack(pady=5)


# Description
tk.Label(root, text="Description").pack()
description_entry = tk.Entry(root, width=40)
description_entry.pack(pady=5)


# Priority
tk.Label(root, text="Priority").pack()

priority = ttk.Combobox(
    root,
    values=["Low", "Medium", "High", "Critical"],
    width=37
)
priority.pack(pady=5)
priority.set("Select Priority")


# Send SOS function
def send_sos():
    user_name = user_name_entry.get()
    phone = phone_entry.get()
    emergency = emergency_type.get()
    location = location_entry.get()
    latitude = latitude_entry.get()
    longitude = longitude_entry.get()
    description = description_entry.get()
    selected_priority = priority.get()

    if not user_name or not phone or not location:
        messagebox.showwarning(
            "Missing Information",
            "Please enter User Name, Phone Number and Location."
        )
        return

    messagebox.showinfo(
        "SOS Alert",
        "SOS request prepared successfully!"
    )


# SOS Button
sos_button = tk.Button(
    root,
    text="SEND SOS",
    command=send_sos,
    font=("Arial", 14, "bold"),
    padx=30,
    pady=10
)
sos_button.pack(pady=20)


# Start application
root.mainloop()