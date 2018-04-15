from tkinter import *
from PIL import ImageTk, Image
import cv2
import webcam.camera as wb
import webcam.hand as vid
import queue
import threading
import gui.builder as builder
import time
import numpy as np

imgtk = None
stop = threading.Event()

class Interface:
    def __init__(self, master, q):
        self.master = master
        self.queue = q
        self.startCapture = False
        self.workerThread = threading.Thread(target=self.worker)
        self.video = vid.Hand()

        self.master.bind("<space>", self.capture)
        self.master.bind("r", self.restartGame)
        self.master.bind("p", self.switchPlayer)

        builder.ElementBuilder(self.master, self)

        #self.cap_gest_button.configure(command=self.capture)
        self.next_button.configure(command=self.switchPlayer)
        self.start_button.configure(command=self.restartGame)

        self.spawnThreads()

    def spawnThreads(self):
        # Spawn thread to generate images
        self.workerThread.start()
        self.master.after(50, self.periodicLoop)

    def switchPlayer(self, unused = None):
        if (self.app.game is not None):
            self.app.game.switchPlayer()

    def capture(self, unused):
        self.startCapture = True

    def restartGame(self, unused = None):
        if (self.app.game is not None):
            self.app.game.restartGame()

    def worker(self):
        try:
            while not stop.is_set():
                cv2image, countour = self.video.picture()
                self.img = Image.fromarray(cv2.cvtColor(cv2image, cv2.COLOR_BGR2RGB))
                imgtk = ImageTk.PhotoImage(self.img)
                self.clearQueue()
                self.queue.put(imgtk)

                if self.startCapture:
                    self.startCapture = False
                    cropped = self.video.crop_img(cv2image, countour)
                    self.processImage(cropped)

                time.sleep(0.025)
        except:
            pass

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
                self.player2_score.configure(text=self.app.game.getScore(1))
        except queue.Empty:
            pass

        self.master.after(25, self.periodicLoop)

    @staticmethod
    def show(app):

        # Start a thread
        q = queue.Queue()

        root = Tk()
        root.geometry("1280x720")
        my_gui = Interface(root, q)
        my_gui.app = app
        root.mainloop()
        stop.set()

if __name__ == "__main__":
    Interface.show(None)
