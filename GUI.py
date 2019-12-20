import tkinter as tk
import Day3

root = tk.Tk()
#root.geometry("2000x2000")
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
canvas = tk.Canvas(root, width=1500, height=1500, bg='white')

A = Day3.clean_data(Day3.data[0])
B = Day3.clean_data(Day3.data[1])
A_Coords = Day3.coord(A)
B_Coords = Day3.coord(B)


def draw(coords, color):
    for i in range(1, len(coords)):
        canvas.create_line(coords[i - 1], coords[i], width=2, fill=color)


def main():
    draw(A_Coords, 'red')
    draw(B_Coords, 'blue')
    canvas.pack(fill=tk.BOTH, expand=True)
    root.mainloop()


if __name__ == '__main__':
    main()
