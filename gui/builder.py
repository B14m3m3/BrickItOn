from tkinter import *
from PIL import ImageTk, Image
import cv2
import webcam.camera as wb

class ElementBuilder:
    def __init__(self, master, window):
        master.title("Brick-It-On!")
        #master.config(background="#000000")


        window.background_image = ImageTk.PhotoImage(Image.open('gui/background_clean.png'))
        window.background_label = Label(master, image=window.background_image)
        window.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Top-left window = camera
        window.cam_window = Label(master, image=None)
        window.cam_window.grid(row=0, column=0, padx = 100, pady = 100)

        # Top-right window = instructions
        '''
        nav_img = ImageTk.PhotoImage(Image.open('gui/nav.png'))
        window.instructions_window = Label(master, text="Instructions", image=nav_img)
        window.instructions_window.imgtk = nav_img
        window.instructions_window.grid(row=0, column=1, padx=50)
        '''

        # Bot-left window = player stats
        window.stats_window = Label(master)
        window.stats_window.grid(row=1, column=0, sticky=N)

        # Bot-right window = buttons
        window.control_window = Frame(master, relief=RAISED)
        window.control_window.grid(row=0, column=1, sticky=S)

        # Player stats setup
        window.player_frame = Frame(window.stats_window)
        window.player_frame.grid(row=0, column=0)
        window.player1_label = Label(window.player_frame, text='Player 1 score:', font=25)
        window.player1_label.grid(row=0, column=0, sticky='W', padx=75, pady=0)
        window.player1_score = Label(window.player_frame, text='Player1 score placeholder')
        window.player1_score.grid(row=1, column=0)
        window.player2_label = Label(window.player_frame, text='Player 2 score:', font=25)
        window.player2_label.grid(row=0, column=1, sticky='E', padx=75, pady=0)
        window.player2_score = Label(window.player_frame, text='Player2 score placeholder')
        window.player2_score.grid(row=1, column=1)

        # Control buttons setup
        window.button_frame = Frame(window.control_window, relief=RAISED)

        #window.cap_gest_button = Button(window.control_window, text='capture gesture')
        #window.cap_gest_button.pack(side='left', padx=10)
        #window.start_button_label = Label(window.instructions_window)
        #window.start_button_label.grid(row=0, column=0, sticky='w')
        window.start_button_image = ImageTk.PhotoImage(Image.open("gui/restart.png"))
        window.start_button = Button(window.button_frame, image=window.start_button_image)
        window.start_button.grid(row=0)

        #window.start_button.pack(side='left', padx=10)
        #window.next_button_label = Label(window.instructions_window)
        #window.next_button_label.grid(row=0, column=1)

        window.next_button_image = ImageTk.PhotoImage(Image.open("gui/next.png"))
        window.next_button = Button(window.button_frame, image=window.next_button_image)
        window.next_button.grid(row=1)
        window.button_frame.pack(side=BOTTOM)
