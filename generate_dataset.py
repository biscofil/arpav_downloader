import colorsys
import csv
import random

import cv2
import numpy

windowSize = 5  # must be odd

x = 29
y = 43
h = 98
w = 98


def loadImg(idx: int):
    filename = "frames/target-{}.png".format(idx)
    img = cv2.imread(filename)
    return img[y:y + h, x:x + w]


def windowToHueTensor(img):
    out = []
    for aaa in range(0, img.shape[1]):
        for bbb in range(0, img.shape[0]):
            r, g, b = img[aaa, bbb] / 255.0
            h, s, v = colorsys.rgb_to_hsv(r, g, b)
            out.append(h)
    return out


images = []
for imageIdx in range(0, 33):  # 32 included
    images.append(loadImg(imageIdx))

with open('dataset.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

    for i in range(0, 100):

        windowX = random.randint(0, w - windowSize)
        windowY = random.randint(0, h - windowSize)

        for imageIdx in range(0, 32):  # 32 not included

            try:
                img1 = images[imageIdx]
                img2 = images[imageIdx + 1]

                # crop random square
                img1 = img1[windowY:windowY + windowSize, windowX:windowX + windowSize]

                # print(int(windowY + ((windowSize - 1) / 2)), int(windowX + ((windowSize - 1) / 2)))
                img2 = numpy.array(
                    img2[int(windowY + ((windowSize - 1) / 2)), int(windowX + ((windowSize - 1) / 2))]).reshape(
                    (1, 1, 3))
                # print(img2)

                # to tensor
                img1 = windowToHueTensor(img1)
                img2 = windowToHueTensor(img2)

                # only consider center pixel
                # print(len(img1))
                # print(len(img2))

                record = img1 + img2
                print(record)

                writer.writerow(record)

            except:
                pass
