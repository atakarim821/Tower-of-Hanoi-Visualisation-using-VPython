
import sys
from vpython import *

###########################################################
POLE_LENGTH = 10
DISKS = []
COLORS = [color.red, color.green, color.blue, color.orange, color.yellow, color.magenta, color.cyan, color.purple, color.white, color.gray(0.5)]
deltaRadius = 0.1
j = 1
###############################################################
L = label( height = 10, pos = vector(0, POLE_LENGTH-2, 4), text='Beginning', color = color.green )
def setupDisks(numDisks, poleRadius=0.2):

    cylinder(color=color.white, pos=vector(-POLE_LENGTH, -4., -2),
             radius=poleRadius, length=POLE_LENGTH*2, axis=vector(1, 0, 0))

    cylinder(color=color.white, pos=vector(-POLE_LENGTH, -4, -2),
             radius=poleRadius, length=POLE_LENGTH, axis=vector(0, 1, 0))
    cylinder(color=color.white, pos=vector(0, -4, -2),
             radius=poleRadius, length=POLE_LENGTH, axis=vector(0, 1, 0))
    cylinder(color=color.white, pos=vector(POLE_LENGTH, -4, -2),
             radius=poleRadius, length=POLE_LENGTH, axis=vector(0, 1, 0))

    text(text="Source", height=0.8, pos=vector(-10.5, POLE_LENGTH - 4, -2), color = color.orange)
    text(text="Temp", height=0.8, pos=vector(-1, POLE_LENGTH - 4, -2), color = color.orange)
    text(text="Destination", height=0.8, pos=vector(8.5, POLE_LENGTH - 4, -2), color = color.orange)
    for i in range(numDisks):
        disk = ring(color=COLORS[i], radius=1-deltaRadius*i, thickness=0.3, pos=vector(-POLE_LENGTH, -3+i, -2),
                    axis=vector(0, -1, 0))
        DISKS.append(disk)


def toh(n, NUMBER_DISKS, source, temp, dest, sceneCapture):
    if n == 1:
        # print("Moving disk {} from  {} to  {}. ".format(n, source, dest))
        moveDisk(n, NUMBER_DISKS, dest, sceneCapture)
        return
    toh(n-1, NUMBER_DISKS, source, dest, temp, sceneCapture)
    # print("Moving disk {} from  {} to  {}. ".format(n, source, dest))
    moveDisk(n, NUMBER_DISKS, dest, sceneCapture)
    toh(n-1, NUMBER_DISKS, temp, source, dest, sceneCapture)


# Actual moving and visualization of the movement of the disk.

def moveDisk(n, NUMBER_DISKS, end, sceneCapture, dT=0.5):
    sleep(dT)
    global j

    if end == 'destination':
        DISKS[NUMBER_DISKS-n].pos = vector(POLE_LENGTH, -0.8*n, -2)
        L.text = f"Step No. : {j}"
        j += 1
        if sceneCapture:
            scene.capture("image" + str(j).zfill(2))

    elif end == 'temp':
        DISKS[NUMBER_DISKS-n].pos = vector(0, -0.8*n, -2)
        L.text = f"Step No. : {j}"
        j += 1
        if sceneCapture:
            scene.capture("image" + str(j).zfill(2))

    elif end == 'source':
        DISKS[NUMBER_DISKS-n].pos = vector(-POLE_LENGTH, -0.8*n, -2)

        L.text = f"Step No. : {j}"
        j += 1
        if sceneCapture:
            scene.capture("image" + str(j).zfill(2))

def main():
    numberofdisks = 4 # Don't use more than 6
    setupDisks(numberofdisks)
    sceneCapture = False # Set to True to save images
    if sceneCapture:
        scene.capture("image0")# Starting Image
    dt = 0.4 # change this speed up or slow down animation
    keepRunning = False # Change it to True to keep going
    text(text = f"n = {numberofdisks}", pos = vector(-1, POLE_LENGTH -2, -2), color = color.orange)
    while True:
        rate(100)
        sleep(dt)
        l = label(text = "Arranging...",pos = vector(0, -4, 5), color = color.red)
        toh(numberofdisks, numberofdisks, 'source', 'temp',  'destination', sceneCapture)

        # print("Disk Transfer Completed. Swapping destination")
        # sleep(2.5)
        # toh(numberofdisks, numberofdisks, 'destination', 'temp', 'source', sceneCapture)# To move disks back to the original pole
        # sleep(dt)

        if not keepRunning:
            break
        # print("Disk Transfer Completed. Swapping destination")
    # print("All Done")
    l.text = "Done!!"
    # text(text = "Done", pos = vector(-1, -5.9, 3), color = color.red)

if __name__ == '__main__':
    main()

