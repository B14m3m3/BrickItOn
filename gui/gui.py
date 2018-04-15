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
        self.cam_window = Label(master, image=imgtk)
        self.cam_window.imgtk = imgtk
        self.cam_window.grid(row=0, column=0)

        # Top-right window = instructions
        self.instructions_window = Label(master, text="Instructions")
        self.instructions_window.grid(row=0, column=1)

        # Bot-left window = player stats
        self.stats_window = Label(master)
        self.stats_window.grid(row=1, column=0)

        # Bot-right window = buttons
        self.control_window = Label(master)
        self.control_window.grid(row=1, column=1)

        # Player stats setup
        self.player1_label = Label(self.stats_window, text='Player1')
        self.player1_label.grid(row=0, column=0)
        self.player1_score = Label(self.stats_window, text='Player1 score')
        self.player1_score.grid(row=1, column=0)
        self.player2_label = Label(self.stats_window, text='Player2')
        self.player2_label.grid(row=0, column=1)
        self.player2_score = Label(self.stats_window, text='Player2 score')
        self.player2_score.grid(row=1, column=1)

        # Control buttons setup
        #self.start_button_label = Label(self.instructions_window)
        #self.start_button_label.grid(row=0, column=0, sticky='w')
        self.start_button = Button(self.control_window, text='start', justify='right')
        self.start_button.pack()
        #self.next_button_label = Label(self.instructions_window)
        #self.next_button_label.grid(row=0, column=1)
        self.next_button = Button(self.control_window, text='next', justify='center')
        self.next_button.pack()
        self.cap_gest_button = Button(self.control_window, text='capture gesture', justify='left')
        self.cap_gest_button.pack()

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