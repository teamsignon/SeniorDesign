import pygame
from datetime import datetime

pygame.init()

# ORDER OR IMAGES ====================
#   1 - Lock
#   1 - Fan
#   1 - Lamp
#   1 - Led
#   1 - Radio
#=====================================

# Initail State of Appliances
lockState = False
fanState = False
lampState = False
ledState = False
radioState = False

# Initial size constraints
display_width = 800
display_height = 600

imageWidth = display_width / 9  # size of icon images X
imageHeight = imageWidth  # size of icon images Y

# Change to int
imageWidth = int(imageWidth)
imageHeight = int(imageHeight)

gapSize = int(imageWidth/2)

edgegapSize = int(imageWidth)
spacer = gapSize + imageWidth

image_1_Start = edgegapSize
image_2_Start = image_1_Start + spacer
image_3_Start = image_2_Start + spacer
image_4_Start = image_3_Start + spacer
image_5_Start = image_4_Start + spacer

image_Y_Start = (display_height/2)-(imageHeight/2)
image_Y_Start = int(image_Y_Start)

userDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('User Interface')

black = (0, 0, 0)
white = (255, 255, 255)

clock = pygame.time.Clock()
crashed = False
carImg = pygame.image.load('racecar.png')


# COLORED IMAGES
cLock = pygame.image.load('C_Lock.png')
cRadio = pygame.image.load('C_Radio.png')
cFan = pygame.image.load('C_Fan.png')
cLamp = pygame.image.load('C_Lamp.png')
cLed = pygame.image.load('C_Led.png')

# BLACK and WHITE IMAGES
bLock = pygame.image.load('B_Lock.png')
bRadio = pygame.image.load('B_Radio.png')
bFan = pygame.image.load('B_Fan.png')
bLamp = pygame.image.load('B_Lamp.png')
bLed = pygame.image.load('B_Led.png')

# RESIZE IMAGES
cLock = pygame.transform.scale(cLock, (imageWidth,imageHeight))
cRadio = pygame.transform.scale(cRadio, (imageWidth,imageHeight))
cFan = pygame.transform.scale(cFan, (imageWidth,imageHeight))
cLamp = pygame.transform.scale(cLamp, (imageWidth,imageHeight))
cLed = pygame.transform.scale(cLed, (imageWidth,imageHeight))

bLock = pygame.transform.scale(bLock, (imageWidth,imageHeight))
bRadio = pygame.transform.scale(bRadio, (imageWidth,imageHeight))
bFan = pygame.transform.scale(bFan, (imageWidth,imageHeight))
bLamp = pygame.transform.scale(bLamp, (imageWidth,imageHeight))
bLed = pygame.transform.scale(bLed, (imageWidth,imageHeight))

# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# CLOCK CODE
digital_font = pygame.font.SysFont('Calibri', 32, False, False)
clock = pygame.time.Clock()


# Blit original images
#userDisplay.blit(cLock, (image_1_Start, image_Y_Start))
#userDisplay.blit(cFan, (image_2_Start, image_Y_Start))
#userDisplay.blit(cLamp, (image_3_Start, image_Y_Start))
#userDisplay.blit(cLed, (image_4_Start, image_Y_Start))
#userDisplay.blit(cRadio, (image_5_Start, image_Y_Start))



# --------------------------------------------------------------------------- LOCK functions
def lockOn():
    userDisplay.blit(cLock, (image_1_Start, image_Y_Start))

def lockOff():
    userDisplay.blit(bLock, (image_1_Start, image_Y_Start))

def toggleLock():
    global lockState
    lockState = not lockState

def updateLock():
    if lockState == True:
        lockOn()
    else:
        lockOff()
    pygame.display.update()
# --------------------------------------------------------------------------- FAN functions
def fanOn():
    userDisplay.blit(cFan, (image_2_Start, image_Y_Start))

def fanOff():
    userDisplay.blit(bFan, (image_2_Start, image_Y_Start))

def toggleFan():
    global fanState
    fanState = not fanState

def updateFan():
    if fanState == True:
        fanOn()
    else:
        fanOff()
    pygame.display.update()
# --------------------------------------------------------------------------- LAMP functions
def lampOn():
    userDisplay.blit(cLamp, (image_3_Start, image_Y_Start))

def lampOff():
    userDisplay.blit(bLamp, (image_3_Start, image_Y_Start))

def toggleLamp():
    global lampState
    lampState = not lampState

def updateLamp():
    if lampState == True:
        lampOn()
    else:
        lampOff()
    pygame.display.update()
# --------------------------------------------------------------------------- LED functions
def ledOn():
    userDisplay.blit(cLed, (image_4_Start, image_Y_Start))

def ledOff():
    userDisplay.blit(bLed, (image_4_Start, image_Y_Start))

def toggleLed():
    global ledState
    ledState = not ledState

def updateLed():
    if ledState == True:
        ledOn()
    else:
        ledOff()
    pygame.display.update()

# --------------------------------------------------------------------------- RADIO functions
def radioOn():
    userDisplay.blit(cRadio, (image_5_Start, image_Y_Start))

def radioOff():
    userDisplay.blit(bRadio, (image_5_Start, image_Y_Start))

def toggleRadio():
    global radioState
    radioState = not radioState

def updateRadio():
    if radioState == True:
        radioOn()
    else:
        radioOff()
    pygame.display.update()


# --------------------------------------------------------------------------- OTHER FUNCTIONS

def showAndTell():
    lockOn()
    fanOn()
    lampOn()
    ledOn()
    radioOn()

    pygame.time.delay(1000)
    pygame.display.update()


    lockOff()
    pygame.time.delay(1000)
    pygame.display.update()

    fanOff()
    pygame.time.delay(1000)
    pygame.display.update()

    lampOff()
    pygame.time.delay(1000)
    pygame.display.update()

    ledOff()
    pygame.time.delay(1000)
    pygame.display.update()

    radioOff()
    pygame.time.delay(1000)
    pygame.display.update()

def car(x, y):
    userDisplay.blit(carImg, (x, y))

def checkClick(x,y):
    global lockState
    maxY = image_Y_Start+imageHeight
    if y<image_Y_Start or y>maxY:
        return
    else:
        # LOCK CONDITIONS
        if x>image_1_Start and x<image_1_Start+imageWidth:
            toggleLock()
            updateLock()
        # FAN CONDITIONS
        elif x>image_2_Start and x<image_2_Start+imageWidth:
            toggleFan()
            updateFan()
        # LAMP CONDITIONS
        elif x>image_3_Start and x<image_3_Start+imageWidth:
            toggleLamp()
            updateLamp()
        # LED CONDITIONS
        elif x>image_4_Start and x<image_4_Start+imageWidth:
            toggleLed()
            updateLed()
        # RADIO CONDITIONS
        elif x>image_5_Start and x<image_5_Start+imageWidth:
            toggleRadio()
            updateRadio()
def clockFunction():

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)

    DIGITAL_H = 100  # height of digital clock
    W = display_width  # screen width
    H = display_height  # screen height

    digital_font = pygame.font.SysFont('Calibri', 128, False, False)

    clock = pygame.time.Clock()
    done = False

    now = datetime.now()

    # draw digital clock
    digital_text = now.strftime('%I:%M:%S')
    text = digital_font.render(digital_text, True, WHITE)

    # CLOCK POSITION
    fontX = int(W / 2 - digital_font.size(digital_text)[0] / 2)
    fontY = int((H/4) - digital_font.size(digital_text)[1] / 2)
    pygame.draw.rect(userDisplay, BLACK,
                     (fontX, fontY, digital_font.size(digital_text)[0], digital_font.size(digital_text)[1]), 0)
    userDisplay.blit(text, [fontX, fontY])
    pygame.display.flip()
    clock.tick(60)
## =============================================================================================================================

def main():
    # infinite loop
    updateLock()
    updateFan()
    updateLamp()
    updateLed()
    updateRadio()

    while True:
        clockFunction()

        # gets a single event from the event queue
        event = pygame.event.poll()

        # if the 'close' button of the window is pressed
        if event.type == pygame.QUIT:
            # stops the application
            break

        # if any mouse button is pressed
        if event.type == pygame.MOUSEBUTTONDOWN:
            # prints on the console the pressed button and its position at that moment
            x, y = pygame.mouse.get_pos()
            checkClick(x,y)

    # finalizes Pygame
    pygame.quit()


if __name__ == '__main__':
    main()
