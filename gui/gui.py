from tkinter import *
from PIL import ImageTk, Image
import cv2
import webcam.camera as wb

root = Tk()
imgtk = None

class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Brick-It-On!")

        # Setup camera
        cap = cv2.VideoCapture(1)
        _, frame = cap.read()
        frame = cv2.flip(frame, 1)
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)

        # Top-left window = camera
        self.cam = Label(master, image=imgtk)
        self.cam.imgtk = imgtk
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

        '''
        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()
        '''

    @staticmethod
    def show():
        my_gui = GUI(root)
        root.mainloop()

if __name__ == "__main__":
    GUI.show()