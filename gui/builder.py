from tkinter import *
from PIL import ImageTk, Image
import cv2
import webcam.camera as wb

class ElementBuilder:
    def __init__(self, master, window):
        master.title("Brick-It-On!")
        master.config(background="#FFFFFF")

        # Top-left window = camera
        window.cam_window = Label(master, image=None)
        window.cam_window.grid(row=0, column=0)

        # Top-right window = instructions
        nav_img = ImageTk.PhotoImage(Image.open('gui/nav.png'))
        window.instructions_window = Label(master, text="Instructions", image=nav_img)
        window.instructions_window.imgtk = nav_img
        window.instructions_window.grid(row=0, column=1, padx=50)

        # Bot-left window = player stats
        window.stats_window = Label(master)
        window.stats_window.grid(row=1, column=0)

        # Bot-right window = buttons
        window.control_window = Label(master)
        window.control_window.grid(row=1, column=1)

        # Player stats setup
        window.player_frame = Frame(window.stats_window)
        window.player_frame.grid(row=0, column=0)
        window.player1_label = Label(window.player_frame, text='Player 1 score:', font=25)
        window.player1_label.grid(row=0, column=0, sticky='W', padx=75, pady=20)
        window.player1_score = Label(window.player_frame, text='Player1 score placeholder')
        window.player1_score.grid(row=1, column=0)
        window.player2_label = Label(window.player_frame, text='Player 2 score:', font=25)
        window.player2_label.grid(row=0, column=1, sticky='E', padx=75, pady=10)
        window.player2_score = Label(window.player_frame, text='Player2 score placeholder')
        window.player2_score.grid(row=1, column=1)

        # Control buttons setup
        window.cap_gest_button = Button(window.control_window, text='capture gesture')
        window.cap_gest_button.pack(side='left', padx=10)
        #window.start_button_label = Label(window.instructions_window)
        #window.start_button_label.grid(row=0, column=0, sticky='w')
        window.start_button = Button(window.control_window, text='start')
        window.start_button.pack(side='left', padx=10)
        #window.next_button_label = Label(window.instructions_window)
        #window.next_button_label.grid(row=0, column=1)
        window.next_button = Button(window.control_window, text='next')
        window.next_button.pack(side='left', padx=10)