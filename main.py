import cv2
import numpy
import math
import matplotlib.pyplot as plt
import os

class Image:
    def __init__(self, name):
        self.__imagename = name
        self.__width = 0
        self.__height = 0
        self.__image = ''
        self.__channel = 0

    def GetName(self):
        return self.__imagename

    def Setsize(self, image):
        height, width, channel = image.shape
        self.__height = int(height/8)
        if self.__height < 72:
            self.__height = 72
        elif self.__height > 144:
            self.__height = 144

        while self.__height % 8 != 0:
            self.__height -= 1

        print(self.__height)
        self.__channel = channel
        self.__width = self.__height

    def resize(self, image):
        self.__image = cv2.resize(image, (self.__width,self.__height), interpolation = cv2.INTER_AREA)

    def Ascii(self, final, sprites):
        indexrow = 0
        self.__image = cv2.imread(self.__imagename)
        cv2.imshow("raw", self.__image)
        cv2.waitKey(0)
        self.Setsize(self.__image)
        self.resize(self.__image)
        cv2.imshow("Scaled", self.__image)
        cv2.waitKey(0)

        for i in self.__image:
            columnindex = 0
            row = []
            for j in i:
                temp = self.Luminance(indexrow, columnindex)
                if 0 <= temp < 21:
                    row.append(sprites[0])
                elif 21 <= temp < 42:
                    row.append(sprites[1])
                elif 42 <= temp < 63:
                    row.append(sprites[2])
                elif 63 <= temp < 84:
                    row.append(sprites[3])
                elif 84 <= temp < 105:
                    row.append(sprites[4])
                elif 105 <= temp < 126:
                    row.append(sprites[5])
                elif 126 <= temp < 147:
                    row.append(sprites[6])
                elif 147 <= temp < 168:
                    row.append(sprites[7])
                elif 168 <= temp < 189:
                    row.append(sprites[8])
                elif 189 <= temp < 210:
                    row.append(sprites[9])
                else:
                    row.append(sprites[9])
                columnindex += 1
            final.append(row)
            indexrow += 1



    def Luminance(self, row, column):
        r,g,b = self.__image[row][column]
        return math.floor(0.2126 * r + 0.7152 * g + 0.0722 * b) * 10/ 10

sprites = [" ", ".", ":", "-", "=", "+", "*", "#", "%", "@"]
final = []

def DrawImage(array):
    for i in array:
        temp = ""
        for j in i:
            temp += " " + j + " "

        print(temp)

def SaveImage(array):
    try:
        os.remove(f"{ascii.GetName()}Ascii.txt")
    except FileNotFoundError:
        print("Cant delete file")
    textpad = open(f"{ascii.GetName()}Ascii.txt", "a")
    for i in array:
        temp = ""
        for j in i:
            temp += j + " "
        textpad.write(f"{temp}\n")


if __name__ == '__main__':
    sprite = str(input("What is the name of the file you would like to be ascii?: "))
    ascii = Image(sprite)
    ascii.Ascii(final, sprites)
    DrawImage(final)
    SaveImage(final)

