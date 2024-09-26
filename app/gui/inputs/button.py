from tkinter import BooleanVar, Button, Checkbutton, Radiobutton


class DefaultButton:
    def __init__(self, root, text, command, x, y):
        self.root = root

        self.default_button = Button(
            self.root,
            text=text,
            command=command,
        )
        self.default_button.place(x=x, y=y)


class DefaultCheckButton:
    def __init__(self, root, text, x, y):
        self.root = root

        self.variable = BooleanVar(self.root)
        self.default_check_button = Checkbutton(
            self.root,
            text=text,
            variable=self.variable,
            onvalue=True,
            offvalue=False,
            anchor="n",
        )
        self.default_check_button.place(x=x, y=y)


class DefaultRadioButton:
    def __init__(self, root, text, variable, value, x, y):
        self.root = root

        self.default_radio_button = Radiobutton(
            self.root,
            text=text,
            variable=variable,
            value=value,
        )
        self.default_radio_button.place(x=x, y=y)
