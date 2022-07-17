#!/usr/bin/env python3

import tkinter as tk

HEIGHT = 800
WIDTH = 1200
FONT = ('Arial', 20, 'normal')
FONT_BOLD = ('Arial', 20, 'bold')

root = tk.Tk()
root.minsize(width=WIDTH, height=HEIGHT)
root.title('Diabetes Manager')
root.grid_columnconfigure((0, 1, 2, 3), weight=1)

title_label = tk.Label(root, text='Diabetes Manager', font=FONT_BOLD)
record_btn = tk.Button(root, text='Record')
trend_btn = tk.Button(root, text='Trends')

title_label.grid(column=1, row=0, columnspan=2)
record_btn.grid(column=1, row=1)
trend_btn.grid(column=2, row=1)


root.mainloop()
