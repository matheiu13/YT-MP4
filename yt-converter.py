from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def downloadVideo(url, save_path):
    if url and save_path:
        try:
            yt = YouTube(url)
            streams = yt.streams.filter(progressive=True, file_extension="mp4")
            highest_res_stream = streams.get_highest_resolution()
            highest_res_stream.download(output_path=save_path)
            print("Video Downloaded Successfully!")
            success = tk.Label(root, text="Download Successfully!", font=("Arial 16"))
            success.pack(pady=30)

        except Exception as e:
            print("Download failed.")
            print(e)

dialog_open = False
def select_sav_dir(event):
    global dialog_open
    if not dialog_open:
        folder = filedialog.askdirectory()
        if folder:
            dialog_open = True
            folder_dir_var.set(folder)
            print(f"Your selected folder: {folder_dir_entry.get()}")
            
        else:
            print("invalid folder directory.")
    dialog_open = False
    
def convert_to_string():
    url = yt_url_entry.get()
    sav_dir = folder_dir_entry.get()
    downloadVideo(url, sav_dir)


root = tk.Tk()
root.geometry("750x425")
root.title("YT downloader (pytube)")

label = tk.Label(root, text="Enter YT url:", font=("Arial 18"))
dir_label = tk.Label(root, text="Select Folder:", font=("Arial 18"))

yt_url_var = tk.StringVar()
yt_url_entry = tk.Entry(root, textvariable=yt_url_var, font=("Arial 16"))

folder_dir_var = tk.StringVar()
folder_dir_entry = tk.Entry(root, textvariable=folder_dir_var, font=("Arial 16"))
folder_dir_entry.bind("<Button-1>", lambda event: root.after(100, select_sav_dir, event))

downloadButton = tk.Button(root, text="download video", command=convert_to_string)

label.pack()
yt_url_entry.pack(fill="x", padx=90, pady=10)

dir_label.pack()
folder_dir_entry.pack(fill="x", padx=90, pady=10)
downloadButton.pack()

root.mainloop()