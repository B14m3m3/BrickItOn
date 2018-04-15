from tkinter import *
from PIL import ImageTk, Image
import cv2
import webcam.camera as wb
import webcam.hand as vid
import queue
import threading


imgtk = None

class Interface:
    def __init__(self, master, q):
        self.master = master
        self.queue = q
        self.stop = False
        self.startCapture = False
        master.title("Brick-It-On!")

        self.video = vid.Hand()
        # Use webcam
        #cam = wb.Webcam()
        #cv2image = cam.takePicture()

        cv2image, countour = self.video.picture()

        # Setup camera
        img = Image.fromarray(cv2image)
        self.imgtk = ImageTk.PhotoImage(image=img)

        # Top-left window = camera
        self.cam = Label(master, image=self.imgtk)
        self.cam.imgtk = self.imgtk
        self.cam.grid(row=0)

        # Top-right window = instructions
        self.instructions = Label(master, text="Instructions")
        self.instructions.grid(row=0, column=1)

        # Bot-left window = player stats
        self.stats = Label(master, text="Player stats")
        self.stats.grid(row=1, column=0)

        # Bot-right window = buttons
        self.control = Label(master, text="Buttons for control")
        self.control.grid(row=1, column=1)


        self.greet_button = Button(self.master, text="Greet", command=self.capture)
        self.greet_button.grid(row=2)

        '''
        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()
        '''
        self.spawnThreads()

    def spawnThreads(self):
        # Spawn thread to generate images
        threading.Thread(target=self.worker).start()
        self.master.after(50,self.periodicLoop)

    def capture(self):
        print("Taking image")
        self.startCapture = True

    def worker(self):
        import time

        while not self.stop:
            cv2image, countour = self.video.picture()
            img = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image=img)
            self.clearQueue()
            self.queue.put(imgtk)
            time.sleep(0.025)

            if self.startCapture:
                self.startCapture = False
                cropped = self.video.crop_img(cv2image, countour)
                self.processImage(cropped)

        print("Killing thread")

    def processImage(self, imgdata):
        self.app.processFromGUI(imgdata)

    def clearQueue(self):
        try:
            self.queue.get_nowait()
        except:
            pass

    def periodicLoop(self):

        try:
            self.imgtk = self.queue.get(0)
            self.cam.configure(image=self.imgtk)
        except queue.Empty:
            pass

        self.master.after(25, self.periodicLoop)

    def closing(self):
        self.stop = True
        print("Stopping")
        self.master.destroy()

    @staticmethod
    def show(app):

        # Start a thread
        q = queue.Queue()

        root = Tk()
        my_gui = Interface(root, q)
        my_gui.app = app
        root.protocol("WM_DELETE_WINDOW", my_gui.closing)
        root.mainloop()
        print("Stoppig root.mainloop()...")



if __name__ == "__main__":
    Interface.show(None)