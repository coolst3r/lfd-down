import os
import sys
import subprocess
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import threading

def check_dependencies():
    try:
        subprocess.run(["which", "aria2c"], check=True)
    except subprocess.CalledProcessError:
        subprocess.run(["sudo", "pacman", "-S", "aria2"])

def download_file(link, save_path):
    subprocess.run(["aria2c", "-d", save_path, link])

def download_thread(link, save_path, progress_bar):
    download_file(link, save_path)
    progress_bar.step(100)

def main():
    root = tk.Tk()
    root.withdraw()
    save_path = filedialog.askdirectory()

    check_dependencies()

    links = []
    links_input = tk.Text(root)
    links_input.pack()

    download_button = tk.Button(root, text="Start Download", command=lambda: start_download(links_input, save_path))
    download_button.pack()

    root.mainloop()

def start_download(links_input, save_path):
    links = links_input.get("1.0", "end-1c").split("\n")

    progress_bar = ttk.Progressbar(root, length=len(links))
    progress_bar.pack()

    for link in links:
        thread = threading.Thread(target=download_thread, args=(link, save_path, progress_bar))
        thread.start()

if __name__ == "__main__":
    main()
