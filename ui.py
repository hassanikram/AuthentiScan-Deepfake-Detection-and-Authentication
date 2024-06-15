import tkinter as tk
from tkinter import filedialog, Label, Button, Canvas
import threading
import time
import datetime
import cv2
from PIL import Image, ImageTk

class VideoUploaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DEEP FAKE DETECTION")
        self.root.geometry("800x600")
        self.root.configure(bg="#e0f7fa")

        # Date and time display
        self.date_time_label = Label(root, text="", bg="#e0f7fa", font=("Helvetica", 12))
        self.date_time_label.place(x=10, y=10)
        self.update_time()

        # Upload section
        self.label = Label(root, text="Please upload a video", bg="#e0f7fa", font=("Helvetica", 16, "bold"))
        self.label.pack(pady=10)

        self.upload_button = Button(root, text="Upload Video", command=self.upload_video, bg="#00796b", fg="white", font=("Helvetica", 12))
        self.upload_button.pack(pady=10)

        self.file_path_label = Label(root, text="", bg="#e0f7fa", font=("Helvetica", 12))
        self.file_path_label.pack(pady=10)

        # Video preview
        self.video_preview_label = Label(root, bg="black")
        self.video_preview_label.pack(pady=10)

        # Process section
        self.process_button = Button(root, text="Process Video", command=self.process_video, bg="#004d40", fg="white", font=("Helvetica", 12))
        self.process_button.pack(pady=10)

        self.progress_label = Label(root, text="", bg="#e0f7fa", font=("Helvetica", 12))
        self.progress_label.pack(pady=10)

        self.canvas = Canvas(root, width=400, height=30, bg="white")
        self.canvas.pack(pady=10)
        self.progress_bar = self.canvas.create_rectangle(0, 0, 0, 30, fill="blue")

        self.result_label = Label(root, text="", bg="#e0f7fa", font=("Helvetica", 14, "bold"))
        self.result_label.pack(pady=20)

    def update_time(self):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.date_time_label.config(text=now)
        self.root.after(1000, self.update_time)  # Update the time every second

    def upload_video(self):
        file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi;*.mkv;*.mov")])
        if file_path:
            self.file_path_label.config(text=f"Selected file: {file_path}")
            self.show_video_preview(file_path)
            self.file_path = file_path

    def show_video_preview(self, file_path):
        cap = cv2.VideoCapture(file_path)
        if not cap.isOpened():
            return

        def update_preview():
            ret, frame = cap.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = cv2.resize(frame, (400, 300))  # Resize frame for display
                img = Image.fromarray(frame)
                img = ImageTk.PhotoImage(image=img)
                self.video_preview_label.img = img  # Keep a reference
                self.video_preview_label.config(image=img)
                self.video_preview_label.after(10, update_preview)  # Update every 10 milliseconds
            else:
                cap.release()

        update_preview()

    def process_video(self):
        self.progress_label.config(text="Processing video...")
        self.root.update()  # Update the UI to show progress label

        def run_processing():
            for i in range(1, 101):
                time.sleep(0.05)  # Simulating processing time
                self.canvas.coords(self.progress_bar, 0, 0, 4*i, 30)
                self.progress_label.config(text=f"Processing... {i}%")
                self.root.update()  # Update the UI to show progress

            # After processing completes
            result = "The uploaded video is a real video."
            self.progress_label.config(text="")
            self.result_label.config(text=result)

        threading.Thread(target=run_processing).start()

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoUploaderApp(root)
    root.mainloop()
