from psychopy import visual,core,event
import random as r

win = visual.Window(size=(600,600))
IntroText = visual.TextStim(win, 'You will see black faces and white faces. Press the z key if you see black and m key if you see white. You will also see positive and negative words. Press the z key if you see positive words, and the m key if you see negative words', color=(0, 1, 0), colorSpace='rgb')

core.wait(10)
win.flip() #used to clear the window from the text... I think
data = [] #defines data as an empty list, to store values

#Test1
core.wait(1)
image = visual.ImageStim(win, image='face1.jpg') #displays image stimulus
rtClock = core.Clock()
rtClock.reset()
k = event.waitKeys(keyList=["z", "m"])
rt = rtClock.getTime()
if k[0]=="z":
    keyPressed = 'z'
elif k[0]=="m":
    keyPressed = 'm'
data += ['face1', str(round(rt, 4)), keyPressed]
win.flip() #used to clear the window from the image... I think

core.wait(1)
IntroText = visual.TextStim(win, 'Happy', color=(0, 1, 0), colorSpace='rgb') #displays text stimulus
rtClock = core.Clock()
rtClock.reset()
k = event.waitKeys(keyList=["z", "m"])
rt = rtClock.getTime()
if k[0]=="z":
    keyPressed = 'z'
elif k[0]=="m":
    keyPressed = 'm'
data += ['face1', str(round(rt, 4)), keyPressed]
win.flip()  #used to clear the window from the text... I think



#TransitionToTest2
TransitionText = visual.TextStim(win, 'Now, the commands will be inversed, press z if you see black faces and negative words, and m if you see white faces and positive words', color=(0, 1, 0), colorSpace='rgb')

core.wait(10)
win.flip() #used to clear the window from the text... I think

#Test2

#ExportToCSV

core.quit()
