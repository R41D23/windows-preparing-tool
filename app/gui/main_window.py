from tkinter import PhotoImage, Tk

from app.gui.background import CreateBackground
from app.gui.bitlocker.bitlocker_management_section import \
    CreateBitlockerManagementSection
from app.gui.user.user_management_section import CreateUserManagementSection


class MainWindow:
    def __init__(self):
        self.root = Tk()

        self.icon = PhotoImage(file="static/images/icon.png")
        self.root.wm_title("Windows Preparing Tool")
        self.root.wm_resizable(width=False, height=False)
        self.root.wm_geometry("950x650")
        self.root.iconphoto(False, self.icon)

        self.background = CreateBackground(
            self.root,
            bg_image_path="static/images/bg.png",
            logo_image_path="static/images/logo.png",
        )

        self.user_management_section = CreateUserManagementSection(self.root)

        self.bitlocker_management_section = CreateBitlockerManagementSection(self.root)

    def start(self):
        self.root.mainloop()
