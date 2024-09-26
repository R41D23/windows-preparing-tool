from subprocess import check_output
from tkinter import StringVar


class BitlockerManagement:
    def __init__(self, root):
        self.root = root

        self.bitl_set_state = StringVar(self.root, "deactivate")

    def check_on_startup(self):
        self.mbde_output = check_output(["manage-bde", "-status", "C:"]).decode("utf-8")

        for line in self.mbde_output.splitlines():
            if "Fully Decrypted" in line:
                self.bitl_set_state.set("deactivate")
            elif "Used Space Only Encrypted" in line:
                self.bitl_set_state.set("activate")
            elif "Fully Encrypted" in line:
                self.bitl_set_state.set("activate")
            elif "Encryption in Progress" in line:
                self.bitl_set_state.set("activate")
        print(self.bitl_set_state)
