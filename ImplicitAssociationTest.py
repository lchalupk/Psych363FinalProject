from psychopy import visual,core,event
import random as r

imgArr = ["bface1.jpg", "wface1.jpg", "bface2.jpg", "wface2.jpg", "bface3.jpg", "wface3.jpg"]
wordArr = ["happy", "agony", "poison", "bliss", "love", "hate"]
data = [] #defines data as an empty list, to store values

win = visual.Window(size=(600,600))
IntroText = visual.TextStim(win, 'You will see black faces and white faces. Press the z key if you see black and m key if you see white. You will also see positive and negative words. Press the z key if you see positive words, and the m key if you see negative words', color=(0, 1, 0), colorSpace='rgb')
IntroText.draw()
win.flip()
core.wait(12)

ReadyText = visual.TextStim(win, 'Get Ready, The first stimuli will appear in 5 seconds', color=(0, 1, 0), colorSpace='rgb')
ReadyText.draw()
win.flip()
core.wait(5)

#Test1
for i in range(6):
    core.wait(1)
    rtClock = core.Clock()
    image = visual.ImageStim(win, image=imgArr[i])  # displays image stimulus
    image.draw()
    win.flip()
    rtClock.reset()
    k = event.waitKeys(keyList=["z", "m", "q"])
    rt = rtClock.getTime()
    if k[0] == "z":
        keyPressed = 'z'
        adjective = 'Black'
    elif k[0] == "m":
        keyPressed = 'm'
        adjective = 'White'
    elif k[0] == "q":
        core.quit()
    data.append([imgArr[i], str(round(rt, 4)), keyPressed, adjective])
    win.flip()  # used to clear the window from the image... I think

    core.wait(1)
    IntroText = visual.TextStim(win, wordArr[i], color=(0, 1, 0), colorSpace='rgb')  # displays text stimulus
    IntroText.draw()
    win.flip()
    rtClock.reset()
    k = event.waitKeys(keyList=["z", "m"])
    rt = rtClock.getTime()
    if k[0] == "z":
        keyPressed = 'z'
        adjective = 'Good'
    elif k[0] == "m":
        keyPressed = 'm'
        adjective = 'Bad'
    elif k[0] == "q":
        core.quit()
    data.append([wordArr[i], str(round(rt, 4)), keyPressed, adjective])
    win.flip()

#TransitionToTest2
TransitionText = visual.TextStim(win, 'Now, the commands will be inverted, press z if you see black faces and negative words, and m if you see white faces and positive words', color=(0, 1, 0), colorSpace='rgb')
TransitionText.draw()
win.flip()
core.wait(12)

ReadyText = visual.TextStim(win, 'Get Ready, The first stimuli will appear in 5 seconds', color=(0, 1, 0), colorSpace='rgb')
ReadyText.draw()
win.flip()
core.wait(5)

#Test2

for i in range(6):
    core.wait(1)
    rtClock = core.Clock()
    image = visual.ImageStim(win, image=imgArr[i])  # displays image stimulus
    image.draw()
    win.flip()
    rtClock.reset()
    k = event.waitKeys(keyList=["z", "m", "q"])
    rt = rtClock.getTime()
    if k[0] == "z":
        keyPressed = 'z'
        adjective = 'Black'
    elif k[0] == "m":
        keyPressed = 'm'
        adjective = 'White'
    elif k[0] == "q":
        core.quit()
    data.append([imgArr[i], str(round(rt, 4)), keyPressed, adjective])
    win.flip()  # used to clear the window from the image... I think

    core.wait(1)
    IntroText = visual.TextStim(win, wordArr[i], color=(0, 1, 0), colorSpace='rgb')  # displays text stimulus
    IntroText.draw()
    win.flip()
    rtClock.reset()
    k = event.waitKeys(keyList=["z", "m"])
    rt = rtClock.getTime()
    if k[0] == "z":
        keyPressed = 'z'
        adjective = 'Bad'
    elif k[0] == "m":
        keyPressed = 'm'
        adjective = 'Good'
    elif k[0] == "q":
        core.quit()
    data.append([wordArr[i], str(round(rt, 4)), keyPressed, adjective])
    win.flip()

#Test Print Data

for x in data:
    print(x)

#ExportToCSV

core.quit()
