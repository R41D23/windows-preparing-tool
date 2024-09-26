from tkinter import messagebox


class UserManagement:
    def __init__(self):
        self.user_add_list = []

    def append_user_to_list(
        self,
        root,
        user_list_label,
        user_name,
        user_pass,
        user_pass_again,
        pass_never_expires,
        user_can_change_pass,
        add_user_to_admin_group,
    ):

        self.root = root

        if user_name == "":
            messagebox.showerror(
                "Brak nazwy użytkownika", "Uzupełnij nazwę użytkownika!"
            )
        else:
            if user_pass != user_pass_again:
                messagebox.showerror("Błąd hasła", "Podane hasła nie pasują do siebie!")
            else:
                self.user = {
                    "user_name": user_name,
                    "user_pass": user_pass,
                    "pass_never_expires": pass_never_expires,
                    "user_can_change_pass": user_can_change_pass,
                    "add_user_to_admin_group": add_user_to_admin_group,
                }
                self.user_add_list.append(self.user)

                self.label_text = "Lista userów do dodania:\n"

                for user in self.user_add_list:
                    user_text = f'   Nazwa: {user["user_name"]}\n   Hasło nigdy nie wygasa: {user["pass_never_expires"]}\n   User może zmienić hasło: {user["user_can_change_pass"]}\n   User jest adminem: {user["add_user_to_admin_group"]}\n'
                    self.label_text = self.label_text + user_text

                user_list_label.config(text=self.label_text)

    def clear_user_add_list(self, user_list_label):

        self.clear_list_confirm = messagebox.askquestion(
            "Windows Preparing Tool",
            "Czy na pewno chcesz wyczyścić listę?",
        )

        if self.clear_list_confirm == "no":
            return

        self.user_add_list.clear()
        user_list_label.config(text="Lista userów do dodania:\n")
