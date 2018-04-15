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
        master.config(background="#FFFFFF")

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
        nav_img = ImageTk.PhotoImage(Image.open('nav.png'))
        self.instructions_window = Label(master, text="Instructions", image=nav_img)
        self.instructions_window.imgtk = nav_img
        self.instructions_window.grid(row=0, column=1, padx=50)

        # Bot-left window = player stats
        self.stats_window = Label(master)
        self.stats_window.grid(row=1, column=0)

        # Bot-right window = buttons
        self.control_window = Label(master)
        self.control_window.grid(row=1, column=1)

        # Player stats setup
        self.player_frame = Frame(self.stats_window)
        self.player_frame.grid(row=0, column=0)
        self.player1_label = Label(self.player_frame, text='Player 1 score:', font=25)
        self.player1_label.grid(row=0, column=0, sticky='W', padx=75, pady=20)
        self.player1_score = Label(self.player_frame, text='Player1 score placeholder')
        self.player1_score.grid(row=1, column=0)
        self.player2_label = Label(self.player_frame, text='Player 2 score:', font=25)
        self.player2_label.grid(row=0, column=1, sticky='E', padx=75, pady=10)
        self.player2_score = Label(self.player_frame, text='Player2 score placeholder')
        self.player2_score.grid(row=1, column=1)

        # Control buttons setup
        self.cap_gest_button = Button(self.control_window, text='capture gesture')
        self.cap_gest_button.pack(side='left', padx=10)
        #self.start_button_label = Label(self.instructions_window)
        #self.start_button_label.grid(row=0, column=0, sticky='w')
        self.start_button = Button(self.control_window, text='start')
        self.start_button.pack(side='left', padx=10)
        #self.next_button_label = Label(self.instructions_window)
        #self.next_button_label.grid(row=0, column=1)
        self.next_button = Button(self.control_window, text='next')
        self.next_button.pack(side='left', padx=10)

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