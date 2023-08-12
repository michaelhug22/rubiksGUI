import tkinter as tk
from rubik_solver import utils
from tkinter import simpledialog, messagebox

# Constants
FACE_SIZE = 3
FACES = ['Up', 'Left', 'Front', 'Right', 'Back', 'Down']
COLORS = ["yellow", "blue", "red", "green", "orange", "white"]
LIGHT_COLORS = {
    "yellow": "#F0E2B6",  # Cream
    "blue": "#81D4FA",   # Light Blue
    "red": "#FFA07A",    # Light Salmon
    "green": "#98FB98",  # Pale Green
    "orange": "#FFDAB9", # Peach Puff
    "white": "#ededed"   # Light Grey
}

BUTTON_SIZE = 60


class RubiksCubeApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Rubik's Cube GUI")
        self.iconbitmap('rubiks_cube_15542.ico')
        self.configure(bg="lightblue")

        # Create a main frame for better layout control
        main_frame = tk.Frame(self, bg="lightblue")

        main_frame.pack(pady=20, padx=20)
        header_label = tk.Label(main_frame, bg="lightblue", text="Cube Solver",
                                font=("Arial", 24))  # You can change the font and size to your preference
        header_label.grid(row=0, columnspan=3)

        self.face_frames = {}
        self.tiles = []

        for index, face in enumerate(FACES):
            frame, face_tiles = self.create_face_frame(face, main_frame)
            self.face_frames[face] = frame
            self.tiles.extend(face_tiles)

            # Layout frames in a 2x3 grid
            row = (index // 3) + 1
            col = index % 3
            frame.grid(row=row, column=col, padx=10, pady=10)

        self.enter_button = tk.Button(main_frame, text="Enter", command=self.display_colors)
        self.enter_button.grid(row=3, columnspan=3)

    def create_face_frame(self, face_name, parent):
        face_color = COLORS[FACES.index(face_name)]
        light_face_color = LIGHT_COLORS[face_color]

        frame = tk.Frame(parent, padx=10, pady=10, bg=light_face_color)

        label = tk.Label(frame, text=face_name, bg=light_face_color, fg=COLORS[FACES.index(face_name)], font=("Arial", 12, "bold"))
        label.grid(row=0, column=0, columnspan=3)

        face_tiles = []
        for i in range(FACE_SIZE):
            for j in range(FACE_SIZE):
                btn = tk.Button(frame, bg=face_color, width=BUTTON_SIZE // 5, height=BUTTON_SIZE // 10,
                                activebackground=light_face_color)
                btn.grid(row=i + 1, column=j, padx=5, pady=5)  # Offset by 1 row for the label
                btn.configure(command=lambda button=btn: self.change_color(button))
                face_tiles.append(btn)

        return frame, face_tiles

    def change_color(self, button):
        current_color = button.cget('bg')
        current_index = COLORS.index(current_color)
        new_index = (current_index + 1) % len(COLORS)
        button.config(bg=COLORS[new_index])

    def display_colors(self):
        tile_colors = [tile.cget('bg')[0:1] for tile in self.tiles]
        cube = ("".join(tile_colors))
        solution = utils.solve(cube, 'Kociemba')
        messagebox.showinfo("Solution", solution)


if __name__ == "__main__":
    app = RubiksCubeApp()
    app.mainloop()
