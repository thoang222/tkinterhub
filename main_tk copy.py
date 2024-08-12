import tkinter as tk
import os

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x600")
        self.title("Main Window")
        self.menubar_color = "blue"
        self.local = os.getcwd()

        self.toggle_icon = tk.PhotoImage(file=f"{self.local}/images/toggle_btn_icon.png")
        self.home_icon = tk.PhotoImage(file=f"{self.local}/images/home_icon.png")
        self.about_icon = tk.PhotoImage(file=f"{self.local}/images/about_icon.png")
        self.close_icon = tk.PhotoImage(file=f"{self.local}/images/close_btn_icon.png")
        self.services_icon = tk.PhotoImage(file=f"{self.local}/images/services_icon.png")
        self.update_icon = tk.PhotoImage(file=f"{self.local}/images/updates_icon.png")
        self.contact_icon = tk.PhotoImage(file=f"{self.local}/images/contact_icon.png")

        self.menubar_frame = tk.Frame(self, bg=self.menubar_color)
        self.page_frame = tk.Frame(self, bg="red")
        self.page_frame.place(relwidth=1.0, relheight=1.0, x=50)

        self.create_widgets()
        self.menubar_frame.pack(side=tk.LEFT, fill=tk.Y, padx=3, pady=4)
        self.menubar_frame.pack_propagate(flag=False)
        self.menubar_frame.config(width=45)

    def create_widgets(self):
        self.btn_toggle = tk.Button(self.menubar_frame, image=self.toggle_icon, bg=self.menubar_color,
                                    bd=0, activebackground=self.menubar_color, command=self.extend_menubar)
        self.btn_toggle.place(x=4, y=10)

        self.home_bt, self.home_bt_indicator, self.home_page_lb = self.create_menu_button(self.home_icon, "Home", 130, self.home_page)
        self.services_bt, self.services_bt_indicator, self.services_page_lb = self.create_menu_button(self.services_icon, "Services", 190, self.services_page)
        self.update_bt, self.update_bt_indicator, self.update_page_lb = self.create_menu_button(self.update_icon, "Updates", 250, self.update_page)
        self.contact_bt, self.contact_bt_indicator, self.contact_page_lb = self.create_menu_button(self.contact_icon, "Contact", 310, self.contact_page)
        self.about_bt, self.about_bt_indicator, self.about_page_lb = self.create_menu_button(self.about_icon, "About", 370, self.about_page)

        self.home_page()  # Load default home page

    def create_menu_button(self, icon, text, y, page):
        button = tk.Button(self.menubar_frame, image=icon, bg=self.menubar_color, bd=0,
                           activebackground=self.menubar_color, command=lambda: self.switch_indicator(page))
        button.place(x=9, y=y, width=30, height=40)
        indicator = tk.Label(self.menubar_frame, bg=self.menubar_color)
        indicator.place(x=3, y=y, width=3, height=40)
        label = tk.Label(self.menubar_frame, text=text, bg=self.menubar_color, fg="white",
                         font=("Arial", 15, "bold"), anchor=tk.W)
        label.place(x=45, y=y, width=100, height=40)
        label.bind("<Button-1>", lambda e: self.switch_indicator(page))
        return button, indicator, label

    def switch_indicator(self, page):
        self.reset_indicators()
        if self.menubar_frame.winfo_width() > 45:
            self.flod_menubar()
        self.load_page(page)

    def reset_indicators(self):
        for widget in self.menubar_frame.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(bg=self.menubar_color)

    def load_page(self, page):
        for frame in self.page_frame.winfo_children():
            frame.destroy()
        page()

    def extend_menubar(self):
        self.animate_menubar(200, self.close_icon, self.flod_menubar)

    def flod_menubar(self):
        self.animate_menubar(45, self.toggle_icon, self.extend_menubar)

    def animate_menubar(self, target_width, toggle_icon, toggle_command):
        current_width = self.menubar_frame.winfo_width()
        if (target_width > current_width and current_width < target_width) or (target_width < current_width and current_width > target_width):
            step = 10 if target_width > current_width else -10
            self.menubar_frame.config(width=current_width + step)
            self.after(15, lambda: self.animate_menubar(target_width, toggle_icon, toggle_command))
        else:
            self.btn_toggle.config(image=toggle_icon)
            self.btn_toggle.config(command=toggle_command)

    def home_page(self):
        self.create_page("Home Page")

    def services_page(self):
        self.create_page("Services Page")

    def update_page(self):
        self.create_page("Update Page")

    def contact_page(self):
        self.create_page("Contact Page")

    def about_page(self):
        self.create_page("About Page")

    def create_page(self, text):
        page_frame = tk.Frame(self.page_frame)
        page_frame.pack(fill=tk.BOTH, expand=True)
        label = tk.Label(page_frame, text=text, bg="red")
        label.place(x=100, y=100, width=100, height=100)

if __name__ == "__main__":
    app = Application()
    app.mainloop()
