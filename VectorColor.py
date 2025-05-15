from Vec3 import *
from PIL import Image
R = 0; G = 0; B = 0;
global WriteImageData2

with open("FinalImageFile.ppm", "w") as ImageFile:
    ImageFile.write("")
    ImageFile.close()

def color(e0, e1, e2):
    PixelColor = Vec3(e0, e1, e2)
    R = PixelColor.x()
    G = PixelColor.y()
    B = PixelColor.z()

    Rbyte = int(255.999 * R)
    Gbyte = int(255.999 * G)
    Bbyte = int(255.999 * B)
    return str(Rbyte) + " " + str(Gbyte) + " " + str(Bbyte) + "\n"
#color(100, 10, 50)

def SaveImage(Width, Heigth, ImageData):
    with open("FinalImageFile.ppm", "a") as ImageFile:
        ImageFile.write(ImageData)
    ImageFile = Image.open("FinalImageFile.ppm")
    ImageFile.save("FinalImageFile" + ".bmp", "BMP")


#with open("FinalImageFile.ppm", "a") as ImageFile:
#ImageFile.write(str(Rbyte) + " " + str(Gbyte) + " " + str(Bbyte) + "\n")