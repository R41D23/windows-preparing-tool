from tkinter import BOTH, Canvas, PhotoImage


class CreateBackground:
    def __init__(self, root, bg_image_path, logo_image_path):
        self.root = root

        self.canvas = Canvas(
            root, bg="pink", width=200, height=200, highlightthickness=0
        )
        self.bg_img = PhotoImage(file=bg_image_path)
        self.lg_img = PhotoImage(file=logo_image_path)
        self.canvas.pack(fill=BOTH, expand=True)
        self.canvas.create_image(0, 0, image=self.bg_img, anchor="nw")
        self.canvas.create_image(930, 630, image=self.lg_img, anchor="se")
        self.canvas.create_rectangle(20, 20, 500, 360, width=2)
        self.canvas.create_text(
            130,
            35,
            anchor="n",
            width=200,
            fill="white",
            text="DODAJ UŻYTKOWNIKA",
            justify="center",
        )
        self.canvas.create_text(
            30, 65, anchor="nw", width=200, fill="white", text="Nazwa użytkownika:"
        )
        self.canvas.create_text(
            30, 115, anchor="nw", width=200, fill="white", text="Hasło:"
        )
        self.canvas.create_text(
            30, 165, anchor="nw", width=200, fill="white", text="Powtórz hasło:"
        )
        self.canvas.create_rectangle(20, 380, 305, 535, width=2)
        self.canvas.create_text(
            163,
            400,
            anchor="n",
            width=200,
            fill="white",
            text="USTAWIENIA BITLOCKERA",
            justify="center",
        )
