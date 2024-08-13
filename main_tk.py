import tkinter as tk
import os
root = tk.Tk()
root.geometry("400x600")
root.title("Main Window")
menubar_color = "blue"
local = os.getcwd()
page_frame = tk.Frame(root)
page_frame.place(relwidth=1.0, relheight=1.0, x=50)

menubar_frame = tk.Frame(root,  bg=menubar_color)
toggle_icon  = tk.PhotoImage(file = f"{local}/images/toggle_btn_icon.png")
home_icon  = tk.PhotoImage(file = f"{local}/images/home_icon.png")
about_icon  = tk.PhotoImage(file = f"{local}/images/about_icon.png")
close_icon  = tk.PhotoImage(file = f"{local}/images/close_btn_icon.png")
services_icon  = tk.PhotoImage(file = f"{local}/images/services_icon.png")
update_icon  = tk.PhotoImage(file = f"{local}/images/updates_icon.png")
contact_icon  = tk.PhotoImage(file = f"{local}/images/contact_icon.png")
close_icon  = tk.PhotoImage(file = f"{local}/images/close_btn_icon.png")
def switch_indicator(indicator_label, page):
    home_bt_indicator.config(bg=menubar_color)
    services_bt_indicator.config(bg=menubar_color)
    update_bt_indicator.config(bg=menubar_color)
    contact_bt_indicator.config(bg=menubar_color)
    about_bt_indicator.config(bg=menubar_color)
    indicator_label.config(bg="white")
    if menubar_frame.winfo_width() > 45:
        flod_menubar()
    for frame in page_frame.winfo_children():
        frame.destroy()
    page()

def extennd_animation():
    current_width = menubar_frame.winfo_width()
    if current_width < 200:
        current_width += 10
        menubar_frame.config(width=current_width)
        root.after(15, extennd_animation)
def extend_menubar():
    # menubar_frame.config(width=200)
    extennd_animation()
    btn_toggle.config(image=close_icon)
    btn_toggle.config(command=flod_menubar)

def flod_menubar_animation():
    current_width = menubar_frame.winfo_width()
    if current_width > 45:
        current_width -= 10
        menubar_frame.config(width=current_width)
        root.after(15, flod_menubar_animation)
def flod_menubar():
    # menubar_frame.config(width=45)
    flod_menubar_animation()
    btn_toggle.config(image=toggle_icon)
    btn_toggle.config(command=extend_menubar)
def home_page():
    home_page_frame = tk.Frame(page_frame)
    home_page_frame.pack(fill=tk.BOTH, expand=True)
    lable = tk.Label(home_page_frame, text="Home Page", bg="red")
    lable.place(x=100, y=100, width=100, height=100)

def services_page():
    services_page_frame = tk.Frame(page_frame)
    services_page_frame.pack(fill=tk.BOTH, expand=True)
    lable = tk.Label(services_page_frame, text="Services Page", bg="red")
    lable.place(x=100, y=100, width=100, height=100)
def update_page():
    update_page_frame = tk.Frame(page_frame)
    update_page_frame.pack(fill=tk.BOTH, expand=True)
    lable = tk.Label(update_page_frame, text="Update Page", bg="red")
    lable.place(x=100, y=100, width=100, height=100)
def contact_page():
    contact_page_frame = tk.Frame(page_frame)
    contact_page_frame.pack(fill=tk.BOTH, expand=True)
    lable = tk.Label(contact_page_frame, text="Contact Page", bg="red")
    lable.place(x=100, y=100, width=100, height=100)
def about_page():
    about_page_frame = tk.Frame(page_frame)
    about_page_frame.pack(fill=tk.BOTH, expand=True)
    lable = tk.Label(about_page_frame, text="About Page", bg="red")
    lable.place(x=100, y=100, width=100, height=100)
home_page()
btn_toggle = tk.Button(menubar_frame,image=toggle_icon, bg = menubar_color, bd=0, activebackground=menubar_color, command=extend_menubar)
btn_toggle.place(x=4, y=10)
home_bt = tk.Button(menubar_frame,image=home_icon, bg = menubar_color, bd=0, activebackground=menubar_color,\
                     command=lambda: switch_indicator(indicator_label=home_bt_indicator,page=home_page))
home_bt.place(x=9, y=130, width=30, height=40)
home_bt_indicator = tk.Label(menubar_frame, bg = "white")
home_bt_indicator.place(x=3, y=130, width=3, height=40)
home_page_lb = tk.Label(menubar_frame, text="Home", bg = menubar_color, fg="white", font=("Arial", 15, "bold"), anchor=tk.W)
home_page_lb.place(x=45, y=130, width=100, height=40)
home_page_lb.bind("<Button-1>", lambda e: switch_indicator(indicator_label=home_bt_indicator,page=home_page))

services_bt = tk.Button(menubar_frame,image=services_icon, bg = menubar_color, bd=0, activebackground=menubar_color,\
                         command=lambda: switch_indicator(services_bt_indicator,page=services_page))
services_bt.place(x=9, y=190, width=30, height=40)
services_bt_indicator = tk.Label(menubar_frame, bg = menubar_color)
services_bt_indicator.place(x=3, y=190, width=3, height=40)
services_page_lb = tk.Label(menubar_frame, text="Services", bg = menubar_color, fg="white", font=("Arial", 15, "bold"), anchor=tk.W)
services_page_lb.place(x=45, y=190, width=100, height=40)
services_page_lb.bind("<Button-1>", lambda e: switch_indicator(services_bt_indicator, page=services_page))

update_bt = tk.Button(menubar_frame,image=update_icon, bg = menubar_color, bd=0, activebackground=menubar_color,\
                       command=lambda: switch_indicator(update_bt_indicator,page=update_page))
update_bt.place(x=9, y=250, width=30, height=40)
update_bt_indicator = tk.Label(menubar_frame, bg = menubar_color)
update_bt_indicator.place(x=3, y=250, width=3, height=40)
update_page_lb = tk.Label(menubar_frame, text="Updates", bg = menubar_color, fg="white", font=("Arial", 15, "bold"), anchor=tk.W)
update_page_lb.place(x=45, y=250, width=100, height=40)
update_page_lb.bind("<Button-1>", lambda e: switch_indicator(update_bt_indicator, page=update_page))

contact_bt = tk.Button(menubar_frame,image=contact_icon, bg = menubar_color, bd=0, activebackground=menubar_color,\
                        command=lambda: switch_indicator(contact_bt_indicator,page=contact_page))
contact_bt.place(x=9, y=310, width=30, height=40)
contact_bt_indicator = tk.Label(menubar_frame, bg = menubar_color)
contact_bt_indicator.place(x=3, y=310, width=3, height=40)
contact_page_lb = tk.Label(menubar_frame, text="Contact", bg = menubar_color, fg="white", font=("Arial", 15, "bold"), anchor=tk.W)
contact_page_lb.place(x=45, y=310, width=100, height=40)
contact_page_lb.bind("<Button-1>", lambda e: switch_indicator(contact_bt_indicator, page=contact_page))

about_bt = tk.Button(menubar_frame,image=about_icon, bg = menubar_color, bd=0, activebackground=menubar_color,
                      command=lambda: switch_indicator(about_bt_indicator, page=about_page))
about_bt.place(x=9, y=370, width=30, height=40)
about_bt_indicator = tk.Label(menubar_frame, bg = menubar_color)
about_bt_indicator.place(x=3, y=370, width=3, height=40)
about_page_lb = tk.Label(menubar_frame, text="About", bg = menubar_color, fg="white", font=("Arial", 15, "bold"), anchor=tk.W)
about_page_lb.place(x=45, y=370, width=100, height=40)
about_page_lb.bind("<Button-1>", lambda e: switch_indicator(about_bt_indicator, page=about_page))



menubar_frame.pack(side=tk.LEFT, fill=tk.Y, padx=3, pady=4)
menubar_frame.pack_propagate(flag=False)
menubar_frame.config(width=45)

root.mainloop()