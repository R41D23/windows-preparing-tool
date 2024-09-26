from sys import path
from importlib import import_module
from tkinter import messagebox

path.append("../")

from app.logic.lib.lib_install import install_lib

try:
    import_module("pyuac")
except ImportError:
    check_for_lib = messagebox.askquestion(
        "Windows Preparing Tool",
        "Wymagane jest pobranie dodatkowych bibliotek. Czy chcesz to zrobić teraz?"
    )
    if check_for_lib == "yes":
        install_lib()
    else:
        exit()
        
from pyuac import isUserAdmin, runAsAdmin

if not isUserAdmin():
    runAsAdmin()
else:

    from app.gui.main_window import MainWindow

    mainWindow = MainWindow()
    mainWindow.start()
