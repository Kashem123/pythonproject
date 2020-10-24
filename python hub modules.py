import tkinter
import random

#list of possible colour

colour = ["Red","Blue","Green","Pink","Black","Yellow","Orange","White","Purple","Brown"]
score = 0
#the game time left, initially 30 second
timeleft = 60

#function that will start the game.
def startGame(event):
    if timeleft == 60:
        #start the countdown timer.
        countdown()

    # run the function to
    # choose the next colour.
    nextColour()
#Function to choose and
#display the next colour.
def nextColour():
    # use the globally declared 'score'
    # and 'play' variables above.
    global score
    global timeleft
    #if a game is currently in play
    if timeleft>0:
        # make the text entry box active.
        e.focus_set()
        # if the colour typed is equal
        # to the colour of the text
        if e.get().lower()==colour[1].lower():
            score += 1
        #clear the text entry box.
        e.delete(0,tkinter.END)
        random.shuffle(colour)
        #change the colour to type,by changing the
        #text _and_ the colour to random colour value
        label.config(fg = str(colour[1]),text = str(colour[0]))
        #update the score
        scoreLabel.config(text="Score: "+str(score))

def countdown():
    global timeleft
    # if a game is in play

    if timeleft>0:
        # decrement the timer
        timeleft -= 1
        # update the time left label
        timeLabel.config(text="Time left: " + str(timeleft))

        # run the function again after 1 second
        timeLabel.after(1000,countdown)

# Driver Code
# create a GUI window
root = tkinter.Tk()
# set the title
root.title("COLORGAME")

# set the size

root.geometry("375x200")
# add an instructions label

instructions = tkinter.Label(root,text="Type the colour of the words,the word text!", font=('Helvetica', 12))
instructions.pack()

scoreLable = tkinter.Label(root,text="Press enter to start",font=('Helvetica',12))
scoreLable.pack()

timeLabel = tkinter.Label(root,text = "Time left: "+ str(timeleft),font=('Helvetica',12))
timeLabel.pack()

Label = tkinter.Label(root,font='Helvetica')
Label.pack()

e = tkinter.Entry(root)
root.bind("<Return>",startGame)
e.pack()

e.focus_set()

root.mainloop()