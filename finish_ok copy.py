import tkinter as tk
import os

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x600")
        self.root.title("Main Window")
        self.menubar_color = "blue"
        self.local = os.getcwd()

        # Tạo frame cho nội dung chính và thanh menu
        self.page_frame = tk.Frame(self.root, bg='lightgray')
        self.page_frame.place(relwidth=1.0, relheight=1.0, x=50, y=0)
        self.page_frame_width = 355  # Kích thước bắt đầu của page_frame

        self.menubar_frame = tk.Frame(self.root, bg=self.menubar_color)

        self.toggle_icon = tk.PhotoImage(file=f"{self.local}/images/toggle_btn_icon.png")
        self.home_icon = tk.PhotoImage(file=f"{self.local}/images/home_icon.png")
        self.about_icon = tk.PhotoImage(file=f"{self.local}/images/about_icon.png")
        self.close_icon = tk.PhotoImage(file=f"{self.local}/images/close_btn_icon.png")
        self.services_icon = tk.PhotoImage(file=f"{self.local}/images/services_icon.png")
        self.update_icon = tk.PhotoImage(file=f"{self.local}/images/updates_icon.png")
        self.contact_icon = tk.PhotoImage(file=f"{self.local}/images/contact_icon.png")

        self.create_menubar_buttons()
        self.switch_indicator(self.home_bt, self.home_page)  # Hiển thị trang "Home" và bật sáng indicator

        self.menubar_frame.pack(side=tk.LEFT, fill=tk.Y, padx=3, pady=4)
        self.menubar_frame.pack_propagate(flag=False)
        self.menubar_frame.config(width=45)

    def create_menubar_buttons(self):
        self.btn_toggle = tk.Button(self.menubar_frame, image=self.toggle_icon, bg=self.menubar_color, bd=0, 
                                    activebackground=self.menubar_color, command=self.extend_menubar)
        self.btn_toggle.place(x=4, y=10)

        self.home_bt, self.home_bt_indicator, self.home_page_lb = self.create_menu_button(
            130, self.home_icon, "Home", self.home_page, indicator=True
        )
        self.services_bt, self.services_bt_indicator, self.services_page_lb = self.create_menu_button(
            190, self.services_icon, "Services", self.services_page, indicator=True
        )
        self.update_bt, self.update_bt_indicator, self.update_page_lb = self.create_menu_button(
            250, self.update_icon, "Updates", self.update_page, indicator=True
        )
        self.contact_bt, self.contact_bt_indicator, self.contact_page_lb = self.create_menu_button(
            310, self.contact_icon, "Contact", self.contact_page, indicator=True
        )
        self.about_bt, self.about_bt_indicator, self.about_page_lb = self.create_menu_button(
            370, self.about_icon, "About", self.about_page, indicator=True
        )

    def create_menu_button(self, y, icon, text, command, indicator=False):
        btn = tk.Button(self.menubar_frame, image=icon, bg=self.menubar_color, bd=0, 
                        activebackground=self.menubar_color, command=lambda: self.switch_indicator(btn, command))
        btn.place(x=9, y=y, width=30, height=40)

        if indicator:
            indicator_label = tk.Label(self.menubar_frame, bg=self.menubar_color)
            indicator_label.place(x=3, y=y, width=3, height=40)
        else:
            indicator_label = None

        lb = tk.Label(self.menubar_frame, text=text, bg=self.menubar_color, fg="white", 
                      font=("Arial", 15, "bold"), anchor=tk.W)
        lb.place(x=45, y=y, width=100, height=40)
        lb.bind("<Button-1>", lambda e: self.switch_indicator(btn, command))

        return btn, indicator_label, lb

    def switch_indicator(self, btn, page):
        indicators = [self.home_bt_indicator, self.services_bt_indicator, self.update_bt_indicator, 
                      self.contact_bt_indicator, self.about_bt_indicator]
        for indicator in indicators:
            indicator.config(bg=self.menubar_color)

        if btn == self.home_bt:
            self.home_bt_indicator.config(bg="white")
        elif btn == self.services_bt:
            self.services_bt_indicator.config(bg="white")
        elif btn == self.update_bt:
            self.update_bt_indicator.config(bg="white")
        elif btn == self.contact_bt:
            self.contact_bt_indicator.config(bg="white")
        elif btn == self.about_bt:
            self.about_bt_indicator.config(bg="white")

        for frame in self.page_frame.winfo_children():
            frame.destroy()
        page()

        # Gấp lại menubar nếu đang mở rộng
        if self.menubar_frame.winfo_width() > 45:
            self.flod_menubar()

    def extennd_animation(self):
        current_width = self.menubar_frame.winfo_width()
        if current_width < 200:
            current_width += 10
            self.menubar_frame.config(width=current_width)
            self.page_frame.config(width=self.page_frame_width - (current_width - 45))
            self.root.after(15, self.extennd_animation)

    def extend_menubar(self):
        self.extennd_animation()
        self.btn_toggle.config(image=self.close_icon)
        self.btn_toggle.config(command=self.flod_menubar)

    def flod_menubar_animation(self):
        current_width = self.menubar_frame.winfo_width()
        if current_width > 45:
            current_width -= 10
            self.menubar_frame.config(width=current_width)
            self.page_frame.config(width=self.page_frame_width - (current_width - 45))
            self.root.after(15, self.flod_menubar_animation)

    def flod_menubar(self):
        self.flod_menubar_animation()
        self.btn_toggle.config(image=self.toggle_icon)
        self.btn_toggle.config(command=self.extend_menubar)

    def home_page(self):
        self.create_page_frame("Home Page")

    def services_page(self):
        self.create_page_frame("Services Page")

    def update_page(self):
        self.create_page_frame("Update Page")

    def contact_page(self):
        self.create_page_frame("Contact Page")

    def about_page(self):
        self.create_page_frame("About Page")

    def create_page_frame(self, text):
        page_frame = tk.Frame(self.page_frame)
        page_frame.pack(fill=tk.BOTH, expand=True)
        label = tk.Label(page_frame, text=text, bg="red")
        label.place(x=100, y=100, width=100, height=100)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
