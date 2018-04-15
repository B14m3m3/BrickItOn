from tkinter import *
from PIL import ImageTk, Image
import cv2
import webcam.camera as wb
import webcam.hand as vid
import queue
import threading
import gui.builder as builder
import time

imgtk = None


class Interface:
    def __init__(self, master, q):
        self.master = master
        self.queue = q
        self.stop = False
        self.startCapture = False

        builder.ElementBuilder(self.master, self)

        self.cap_gest_button.configure(self.capture)
        self.next_button.configure(self.switchPlayer)
        '''
        self.greet_button = Button(self.master, text="Greet", command=self.capture)
        self.greet_button.grid(row=2)

        self.close_button = Button(master, text="Close", command=self.switchPlayer)
        self.close_button.grid(row=3)
        '''
        self.spawnThreads()

    def spawnThreads(self):
        # Spawn thread to generate images
        threading.Thread(target=self.worker).start()
        self.master.after(50, self.periodicLoop)

    def switchPlayer(self):
        if (self.app.game is not None):
            self.app.game.switchPlayer()

    def capture(self):
        self.startCapture = True

    def worker(self):
        self.video = vid.Hand()

        while not self.stop:
            cv2image, countour = self.video.picture()
            img = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image=img)
            self.clearQueue()
            self.queue.put(imgtk)

            if self.startCapture:
                self.startCapture = False
                cropped = self.video.crop_img(cv2image, countour)
                self.processImage(cropped)

            time.sleep(0.025)

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
            self.cam_window.configure(image=self.imgtk)

            if self.app.game is not None:
                self.player1_score.configure(text=self.app.game.getScore(0))
                self.player2_score.control.configure(text=self.app.game.getScore(1))
        except queue.Empty:
            pass

        self.master.after(25, self.periodicLoop)

    def quit(self):
        self.stop = True
        print("Stopping")
        self.master.quit()

    @staticmethod
    def show(app):

        # Start a thread
        q = queue.Queue()

        root = Tk()
        my_gui = Interface(root, q)
        my_gui.app = app
        root.protocol("WM_DELETE_WINDOW", my_gui.quit)
        root.mainloop()
        print("Stoppig root.mainloop()...")


if __name__ == "__main__":
    Interface.show(None)
