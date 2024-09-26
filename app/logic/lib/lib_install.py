from subprocess import CalledProcessError, check_call
from sys import executable
from tkinter import messagebox

def install_lib():
    try:
        check_call([executable, "-m", "pip", "install", "-r", "..\\requirements.txt"])
    except CalledProcessError:
        if CalledProcessError.returncode == 0:
            messagebox.showinfo("Biblioteki zostały poprawnie zainstalowane.")
        else:
            messagebox.showerror("Nie udało się zainstalować bibliotek!")
            exit()