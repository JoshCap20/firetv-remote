# GUI FOR FIRE TV REMOTE
import tkinter as tk
from tkinter import ttk

from ttkthemes import ThemedTk

from remote.main import Remote


class RemoteApp:
    def __init__(self, root, remote):
        self.root = root
        self.remote = remote
        self.root.title("TV Remote Control")
        self.root.geometry("350x300")
        self.create_buttons()

    def create_buttons(self):
        style = ttk.Style()
        style.configure("TButton", font=("Arial", 14),
                        background="black", foreground="white")

        ttk.Button(self.root, text='Power', style='TButton',
                   command=self.remote.power).grid(row=0, column=1)

        ttk.Button(self.root, text='Up', style='TButton',
                   command=self.remote.up).grid(row=1, column=1)

        ttk.Button(self.root, text='Left', style='TButton',
                   command=self.remote.left).grid(row=2, column=0)
        ttk.Button(self.root, text='Enter', style='TButton',
                   command=self.remote.enter).grid(row=2, column=1)
        ttk.Button(self.root, text='Right', style='TButton',
                   command=self.remote.right).grid(row=2, column=2)

        ttk.Button(self.root, text='Down', style='TButton',
                   command=self.remote.down).grid(row=3, column=1)

        ttk.Button(self.root, text='Home', style='TButton',
                   command=self.remote.home).grid(row=4, column=0)
        ttk.Button(self.root, text='Back', style='TButton',
                   command=self.remote.back).grid(row=4, column=2)

        ttk.Button(self.root, text='Volume Up', style='TButton',
                   command=self.remote.volume_up).grid(row=5, column=0)
        ttk.Button(self.root, text='Volume Down', style='TButton',
                   command=self.remote.volume_down).grid(row=5, column=2)
        ttk.Button(self.root, text='Mute', style='TButton',
                   command=self.remote.mute).grid(row=5, column=1)

        ttk.Button(self.root, text='Play/Pause', style='TButton',
                   command=self.remote.play).grid(row=6, column=1)

        ttk.Button(self.root, text='Previous', style='TButton',
                   command=self.remote.previous).grid(row=7, column=0)
        ttk.Button(self.root, text='Next', style='TButton',
                   command=self.remote.next).grid(row=7, column=2)


if __name__ == "__main__":
    remote = Remote("192.168.1.33")  # Replace with your device's IP address
    root = ThemedTk(theme="equilux")
    app = RemoteApp(root, remote)
    root.mainloop()
