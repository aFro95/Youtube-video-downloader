from pytube import YouTube
from tkinter import *

def download():
    link = website_entry.get()  # Get the URL from the entry widget
    try:
        youtubeObject = YouTube(link)
        youtubeObject = youtubeObject.streams.get_highest_resolution()
        youtubeObject.download()
        status_label.config(text="Download is completed successfully")
    except Exception as e:
        status_label.config(text=f"An error has occurred: {e}")


# UI SETUP
window = Tk()
window.title("Youtube Video Downloader")
window.config(padx=50, pady=50)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

# Entries
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()

download_button = Button(text="Download", width=13, command=download)
download_button.grid(row=1, column=2)

# Status Label
status_label = Label(text="")
status_label.grid(row=2, column=1)

window.mainloop()
