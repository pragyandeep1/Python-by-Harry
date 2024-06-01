import tkinter
import PIL.Image, PIL.ImageTk #pip install pillow
import cv2 #pip install opencv-python
import threading
import imutils
import time
from functools import partial

stream = cv2.VideoCapture("D://Bitan//DRS//clip.mp4")
flag = True
def play(speed):
    global flag
    print(f"Now playing the clip. Speed is {speed}")
    
    #play the video backward
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1+speed)

    grabbed, frame = stream.read()
    if not grabbed:
        exit()
    frame = imutils.resize(frame, height=SET_HEIGHT, width=SET_WIDTH)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    if flag:
        canvas.create_text(120, 30, fill='green', font='Times 20 italic bold', text="Decision Pending")
    else:
        flag = not flag

    #play the video forward

def pending(decision):
    #1. Show Decision Pending
    frame = cv2.cvtColor(cv2.imread("D://Bitan//DRS//pending.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, height=SET_HEIGHT, width=SET_WIDTH)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

    #2. Wait for 1 second
    time.sleep(1)

    #3. Show Sponsor
    frame = cv2.cvtColor(cv2.imread("D://Bitan//DRS//sponsor.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, height=SET_HEIGHT, width=SET_WIDTH)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

    #4. Wait for 2 seconds
    time.sleep(2)

    #5. Show Out/Not Out
    if decision == 'out':
        decisionImg = "D://Bitan//DRS//out.png"
    else:
        decisionImg = "D://Bitan//DRS//notout.png"
    frame = cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, height=SET_HEIGHT, width=SET_WIDTH)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

def out():
    thread = threading.Thread(target=pending, args=("out", ))
    thread.daemon = 1
    thread.start()
    print(f"The player is out.")

def not_out():
    thread = threading.Thread(target=pending, args=("not out", ))
    thread.daemon = 1
    thread.start()
    print(f"The player is not out.")

#Height and Width Settings
SET_HEIGHT = 365
SET_WIDTH = 600

#tkinter GUI begins
window = tkinter.Tk()
window.title("Prag Third Umpire DRS Tool")
cv_img = cv2.cvtColor(cv2.imread("D://Bitan//DRS//gallery.png"), cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, height=SET_HEIGHT, width=SET_WIDTH)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0, 0, anchor=tkinter.NW, image=photo)
canvas.pack()

#PlayBack Control Button
btn = tkinter.Button(window, text="<< Previous (fast)", width=50, command=partial (play, -30))
btn.pack()

btn = tkinter.Button(window, text="< Previous (slow)", width=50, command=partial (play, -3))
btn.pack()

btn = tkinter.Button(window, text="Next (slow) >", width=50, command=partial (play, 3))
btn.pack()

btn = tkinter.Button(window, text="Next (fast) >>", width=50, command=partial (play, 30))
btn.pack()

btn = tkinter.Button(window, text="Give Out", width=50, command=out)
btn.pack()

btn = tkinter.Button(window, text="Give Not Out", width=50, command=not_out)
btn.pack()

window.mainloop()