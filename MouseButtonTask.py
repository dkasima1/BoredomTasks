#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.90.2),
    on July 16, 2018, at 12:54
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""
from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
# import numpy as np  # whole numpy lib is available, prepend 'np.'
# from numpy import (sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray)
# from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding
import random
import ctypes

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session

expName = u'FirstExperiment'  # from the Builder filename that created this script
expInfo = {'session': '001', 'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK is False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
# Sets up initial GUI

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'MouseButtonTaskData/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
                                 extraInfo=expInfo, runtimeInfo=None,
                                 originPath=None,
                                 savePickle=True, saveWideText=True,
                                 dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 720), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[1, 1, 1], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] is not None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "Welcome"
WelcomeClock = core.Clock()

# Welcome Text
welcomeText = visual.TextStim(win=win, name='welcomeText',
                              text=u'Welcome to the experiment.\n\nIn this task we ask you to click the buttons on the '
                                   u'screen until all the shapes they correspond '
                                   u'to disappear.\n\nPress space to continue.',
                              font=u'Arial',
                              pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
                              color=u'black', colorSpace='rgb', opacity=1,
                              depth=0.0)

# Initialize components for Routine "section1"
section1Clock = core.Clock()
polygonNum = 6
posit = [(-2/3, 2/3), (0, 2/3), (2/3, 2/3), (-2/3, 0), (0, 0), (2/3, 0)]
positK = [(-0.675, -0.5333), (-0.525, -0.5333), (-0.375, -0.5333), (-0.225, -0.5333), (-0.075, -0.5333),
          (0.075, -0.5333), (0.225, -0.5333), (0.375, -0.5333), (0.525, -0.5333), (0.675, -0.5333),
          (-0.6, -0.6833), (-0.45, -0.6833), (-0.3, -0.6833), (-0.15, -0.6833), (0, -0.6833),
          (0.15, -0.6833), (0.3, -0.6833), (0.45, -0.6833), (0.6, -0.6833), (-0.45, -0.8333),
          (-0.3, -0.8333), (-0.15, -0.8333), (0, -0.8333), (0.15, -0.8333), (0.3, -0.8333),
          (0.45, -0.8333)]
textK = ['q', 'w', 'e', 'r', 't',
         'y', 'u', 'i', 'o', 'p',
         'a', 's', 'd', 'f', 'g',
         'h', 'j', 'k', 'l', 'z',
         'x', 'c', 'v', 'b', 'n',
         'm']
iterText = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

# Initialize components for Routine "Blank"

totalTime = 20
totalCredits = 0.5
continueTXT2 = visual.TextStim(win=win, name='continueTXT',
                               text=u'We ask that you complete the entire next 20 minutes.\n'
                                    u'Are you sure you want to continue?\n\n'
                                    u'Press y for Yes or n for No.',
                               font=u'Arial',
                               pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
                               color=u'black', colorSpace='rgb', opacity=1,
                               depth=0.0)
BlankClock = core.Clock()
textBlank = visual.TextStim(win=win, name='textBlank',
                            text=None,
                            font=u'Arial',
                            pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
                            color=u'black', colorSpace='rgb', opacity=1,
                            depth=0.0)

# Initialize components for Routine "End"
EndClock = core.Clock()
endTXT = visual.TextStim(win=win, name='endTXT',
                         text=u'Press Space to Exit.\n '
                              u'Please go see the Instructor.',
                         font=u'Arial',
                         pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
                         color=u'black', colorSpace='rgb', opacity=1,
                         depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine

# ------Prepare to start Routine "Welcome"-------
t = 0
WelcomeClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
keyboardPress = event.BuilderKeyResponse()
# keep track of which components have finished
WelcomeComponents = [welcomeText, keyboardPress]
for thisComponent in WelcomeComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Welcome"-------
while continueRoutine:
    # get current time
    t = WelcomeClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *welcomeText* updates
    if t >= 0.0 and welcomeText.status == NOT_STARTED:
        # keep track of start time/frame for later
        welcomeText.tStart = t
        welcomeText.frameNStart = frameN  # exact frame index
        welcomeText.setAutoDraw(True)

    # *keyboardPress* updates
    if t >= 0.0 and keyboardPress.status == NOT_STARTED:
        # keep track of start time/frame for later
        keyboardPress.tStart = t
        keyboardPress.frameNStart = frameN  # exact frame index
        keyboardPress.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(keyboardPress.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    for i in range(polygonNum):
        if keyboardPress.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])

            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                keyboardPress.keys = theseKeys[-1]  # just the last key pressed
                keyboardPress.rt = keyboardPress.clock.getTime()
                # a response ends the routine
                continueRoutine = False

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Welcome"-------
for thisComponent in WelcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if keyboardPress.keys in ['', [], None]:  # No response was made
    keyboardPress.keys = None
thisExp.addData('keyboardPress.keys', keyboardPress.keys)
if keyboardPress.keys is not None:  # we had a response
    thisExp.addData('keyboardPress.rt', keyboardPress.rt)
thisExp.nextEntry()
# the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=100000, method='random',
                           extraInfo=expInfo, originPath=-1,
                           trialList=[None],
                           seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial is not None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))
counter = 1
compTrials = -1
usableTrials = -1
mouse = event.Mouse(win=win)
timer = core.Clock()
timer.reset()
for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial is not None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    print(timer)
    #while timer.getTime() >= 10:
    #    trials.finished = True
    # ------Prepare to start Routine "section1"-------
    pText = []  # Stores the Text boxes for each square
    rText = []  # Keys that can be Pressed
    correctKeys = []
    allKeys = []
    keyResp = []
    polygons = []
    buttons = []
    keyText = []
    count = 0
    randomChar = random.sample(xrange(0, 25), polygonNum)
    # Creates the Nine Boxes as well as places the letters in each box.
    for i in range(26):
        keyboardButtons = visual.Rect(  # Generates the Keyboard Buttons
            win=win, name='keyboardButtons',
            width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
            ori=0, pos=(positK[i]),
            lineWidth=1, lineColor='black', lineColorSpace='rgb',
            fillColor=[255, 255, 0], fillColorSpace='rgb',
            opacity=1, depth=0.0, interpolate=True)
        buttons.append(keyboardButtons)
        textButtons = visual.TextStim(  # Generates Text boxes per polygon.
            win=win, name='iteratedText',
            text=textK[i].upper(),
            font=u'Arial',
            pos=(positK[i]), height=0.05, wrapWidth=None, ori=0,
            color=u'black', colorSpace='rgb', opacity=1,
            depth=-2.0)
        keyText.append(textButtons)  # Adds text box letters to list.
    for i in range(polygonNum):
        iteratedSquare = visual.Rect(  # Generates the Polygons
            win=win, name='iteratedSquare',
            width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
            ori=0, pos=(posit[i]),
            lineWidth=1, lineColor='black', lineColorSpace='rgb',
            fillColor=[0, 255, 255], fillColorSpace='rgb',
            opacity=1, depth=0.0, interpolate=True)
        polygons.append(iteratedSquare)  # Generates the polygons.
        # Centers text box in same position as polygons generated above.
        iText = iterText[randomChar[i]]  # Takes random letters from iterText and stores them within same iteration.
        iteratedText = visual.TextStim(  # Generates Text boxes per polygon.
            win=win, name='iteratedText',
            text=iText.upper(),
            font=u'Arial',
            pos=(posit[i]), height=0.05, wrapWidth=None, ori=0,
            color=u'black', colorSpace='rgb', opacity=1,
            depth=-2.0)
        pText.append(iteratedText)  # Adds text box letters to list.
        rText.append(iText)  # Takes key stored from iText and appends to rText for key selection.

    t = 0
    section1Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    section1Components = [polygons, keyText, pText, buttons, mouse]
    for thisComponent in section1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # -------Start Routine "section1"-------
    compTrials += 1
    usableTrials += 1
    buttonStates = [True, True, True, True, True, True]
    while continueRoutine:
        # get current time
        t = section1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # polygons* updates
        for i in range(26):
            if t >= 0.0 and buttons[i].status == NOT_STARTED:
                # keep track of start time/frame for later
                buttons[i].tStart = t
                buttons[i].frameNStart = frameN  # exact frame index
                buttons[i].setAutoDraw(True)
            if t >= 0.0 and keyText[i].status == NOT_STARTED:
                # keep track of start time/frame for later
                keyText[i].tStart = t
                keyText[i].frameNStart = frameN  # exact frame index
                keyText[i].setAutoDraw(True)

        for i in range(polygonNum):
            if t >= 0.0 and polygons[i].status == NOT_STARTED:
                # keep track of start time/frame for later
                polygons[i].tStart = t
                polygons[i].frameNStart = frameN  # exact frame index
                polygons[i].setAutoDraw(True)
            # *iteratedText* updates
            if t >= 0.0 and pText[i].status == NOT_STARTED:
                # keep track of start time/frame for later
                pText[i].tStart = t
                pText[i].frameNStart = frameN  # exact frame index
                pText[i].setAutoDraw(True)
            if t >= 0.0 and mouse.status == NOT_STARTED:
                # keep track of start time/frame for later
                mouse.tStart = t
                mouse.frameNStart = frameN  # exact frame index
                mouse.status = STARTED


                # keyboard checking is just starting
                # win.callOnFlip(mouse.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='space')
            if mouse.status == STARTED:
                for x in range(26):
                    if mouse.isPressedIn(buttons[x]):
                        mouse.clickReset()
                        if textK[x] == rText[i]:
                            polygons[i].setAutoDraw(False)
                            pText[i].setAutoDraw(False)
                            buttonStates[i] = False
                            win.flip()
                if sum(buttonStates) == 0:
                    polygons[i].setAutoDraw(False)
                    pText[i].setAutoDraw(False)
                    continueRoutine = False

        # a response ends the routine
            # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        for thisComponent in section1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            print('You have completed %d trial(s)! Only %d however are(is) usable!' % (compTrials, usableTrials))
            core.quit()
        # refresh the screen
        # if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    # -------Ending Routine "section1"-------
    # check responses
    """for i in range(polygonNum):
        if keyResp[i] in ['', [], None]:  # No response was made
            keyResp[i].keys = None
        trials.addData('keyResp.keys', keyResp[i].keys)
        if keyResp[i].keys is not None:  # we had a response
            trials.addData('keyResp.rt', keyResp[i].rt)
        # the Routine "section1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()"""
    for i in range(26):
        buttons[i].setAutoDraw(False)
        keyText[i].setAutoDraw(False)

    # ------Prepare to start Routine "Blank"-------
    t = 0
    BlankClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    if timer.getTime() > 1200:
        if counter == 4:
            trials.finished = True
            break
        continueTXT = visual.TextStim(win=win, name='continueTXT',
                                      text=u'You have completed ' + str(totalTime) + ' minutes. \n'
                                           u'For ' + str(totalCredits) + ' credits. \n'
                                           u'Would you like to continue?\n\n'
                                           u'Press y for Yes or n for No.',
                                      font=u'Arial',
                                      pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
                                      color=u'black', colorSpace='rgb', opacity=1,
                                      depth=0.0)
        continueTXT.setAutoDraw(True)
        win.flip()
        contKeys = event.waitKeys(keyList=['y', 'n', 'escape'])
        if contKeys[0] == 'n':
            trials.finished = True
            continueTXT.setAutoDraw(False)
        elif contKeys[0] == 'y':
            continueTXT.setAutoDraw(False)
            continueTXT2.setAutoDraw(True)
            win.flip()
            cont2Keys = event.waitKeys(keyList=['y', 'n', 'escape'])
            if cont2Keys[0] == 'n':
                continueTXT2.setAutoDraw(False)
                trials.finished = True
            elif cont2Keys[0] == 'y':
                continueTXT2.setAutoDraw(False)
                trials.finished = False
                timer.reset()
                counter += 1
                totalCredits += 0.5
                totalTime += 20
            else:
                core.quit()
        else:
            core.quit()
    BlankComponents = [textBlank]
    for thisComponent in BlankComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "Blank"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = BlankClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *textBlank* updates
        if t >= 0.0 and textBlank.status == NOT_STARTED:
            # keep track of start time/frame for later
            textBlank.tStart = t
            textBlank.frameNStart = frameN  # exact frame index
            textBlank.setAutoDraw(True)
        frameRemains = 0.0 + 1.0 - win.monitorFramePeriod * 0.75  # most of one frame period left
        if textBlank.status == STARTED and t >= frameRemains:
            textBlank.setAutoDraw(False)

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BlankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            rText = []
            polygons = []

    # -------Ending Routine "Blank"-------
    for thisComponent in BlankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()


# completed 2 repeats of 'trials'


# ------Prepare to start Routine "End"-------
for i in range(26):
    buttons[i].setAutoDraw(False)

t = 0
EndClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()
# keep track of which components have finished
EndComponents = [endTXT, key_resp_2]
for thisComponent in EndComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "End"-------
while continueRoutine:
    # get current time
    t = EndClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *endTXT* updates
    if t >= 0.0 and endTXT.status == NOT_STARTED:
        # keep track of start time/frame for later
        endTXT.tStart = t
        endTXT.frameNStart = frameN  # exact frame index
        endTXT.setAutoDraw(True)
    frameRemains = 0.0 + 1.0 - win.monitorFramePeriod * 0.75  # most of one frame period left
    if endTXT.status == STARTED and t >= frameRemains:
        endTXT.setAutoDraw(True)

    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])

        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_2.keys = theseKeys[-1]  # just the last key pressed
            key_resp_2.rt = key_resp_2.clock.getTime()
            # a response ends the routine
            continueRoutine = False

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "End"-------
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys', key_resp_2.keys)
if key_resp_2.keys is not None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('Minutes_x30', counter)
thisExp.nextEntry()
# the Routine "End" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
