from psychopy import visual,core,event
import random as r

win = visual.Window(size=(600,600))
IntroText = visual.TextStim(win, 'You will see black faces and white faces. Press the z key if you see black and m key if you see white. You will also see positive and negative words. Press the z key if you see positive words, and the m key if you see negative words', color=(0, 1, 0), colorSpace='rgb')

imgArr = ["bface1.jpg", "wface1.jpg", "bface2.jpg", "wface2.jpg", "bface3.jpg", "wface3.jpg"]
wordArr = ["happy", "agony", "poison", "bliss", "love", "hate"]
#win.flip() #used to clear the window from the text... I think
data = [] #defines data as an empty list, to store values

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
        print("z")
    elif k[0] == "m":
        keyPressed = 'm'
        print("m")
    elif k[0] == "q":
        core.quit()
    data += [imgArr[i], str(round(rt, 4)), keyPressed]
    print(data)
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
        print("z")
    elif k[0] == "m":
        keyPressed = 'm'
        print("m")
    elif k[0] == "q":
        core.quit()
    data += [wordArr[i], str(round(rt, 4)), keyPressed]
    print(data)
    win.flip()

#TransitionToTest2
#TransitionText = visual.TextStim(win, 'Now, the commands will be inversed, press z if you see black faces and negative words, and m if you see white faces and positive words', color=(0, 1, 0), colorSpace='rgb')

#core.wait(10)
#win.flip() #used to clear the window from the text... I think

#Test2

#ExportToCSV

core.quit()
