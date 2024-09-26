from tkinter import Entry, Label

from app.gui.inputs.button import DefaultButton, DefaultCheckButton
from app.logic.user.user_management import UserManagement


class CreateUserManagementSection:
    def __init__(self, root):

        self.root = root
        self.user_management = UserManagement()

        self.user_name = Entry(self.root)
        self.user_name.place(x=30, y=85, width=200, height=20)

        self.user_pass = Entry(self.root, show="*")
        self.user_pass.place(x=30, y=135, width=200, height=20)

        self.user_pass_again = Entry(self.root, show="*")
        self.user_pass_again.place(x=30, y=185, width=200, height=20)

        self.pass_never_expires = DefaultCheckButton(
            self.root,
            text="Hasło nigdy nie wygasa",
            x=30,
            y=220,
        )

        self.user_can_change_pass = DefaultCheckButton(
            self.root,
            text="Użytkownik może zmienić hasło",
            x=30,
            y=250,
        )

        self.add_user_to_admin_group = DefaultCheckButton(
            self.root,
            text="Dodaj do grupy Administratorzy",
            x=30,
            y=280,
        )

        self.user_list_label = Label(
            self.root, text="Lista userów do dodania:", anchor="nw", justify="left"
        )
        self.user_list_label.place(x=240, y=30, width=250, height=320)

        self.add_user_to_list = DefaultButton(
            self.root,
            text="Dodaj do listy",
            command=lambda: self.user_management.append_user_to_list(
                self.root,
                self.user_list_label,
                user_name=self.user_name.get(),
                user_pass=self.user_pass.get(),
                user_pass_again=self.user_pass_again.get(),
                pass_never_expires=self.pass_never_expires.variable.get(),
                user_can_change_pass=self.user_can_change_pass.variable.get(),
                add_user_to_admin_group=self.add_user_to_admin_group.variable.get(),
            ),
            x=30,
            y=320,
        )

        self.clear_add_user_list = DefaultButton(
            self.root,
            text="Wyczyść listę",
            command=lambda: self.user_management.clear_user_add_list(
                user_list_label=self.user_list_label
            ),
            x=120,
            y=320,
        )
