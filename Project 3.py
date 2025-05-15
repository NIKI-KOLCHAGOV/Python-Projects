from PIL import Image
from Vec3 import *
from VectorColor import *

ImageWidth = 256
ImageHeight = 256

WriteImageData = "P3\n" + str(ImageWidth) + " " + str(ImageHeight) + "\n255\n"
print("P3\n" + str(ImageWidth) + " " + str(ImageHeight) + "\n255\n")

Counter1 = ImageWidth
R = 0; G = 0; B = 0
R = float(R); G = float(G); B = float(B)
for Counter1 in range(0, ImageHeight, 1):
    print("\rScanlines Remaining: " + str(ImageHeight - Counter1), end="")
    for Counter2 in range(0, ImageWidth, 1):
        #R = float(Counter2) / float(ImageWidth) G = float(Counter1) / float(ImageHeight) B = 0.0 IR = (255.99 * R); IR = int(IR) IG = (255.99 * G); IG = int(IG) IB = (255.99 * B); IB = int(IB) print(str(IR) + " " + str(IG) + " " + str(IB) + "\n") WriteImageData = WriteImageData + str(IR) + " " + str(IG) + " " + str(IB) + "\n"
        PixelColor = Vec3(float(Counter2) / (ImageWidth - 1), float(Counter1) / (ImageHeight - 1), 0,)
        WriteColor("", PixelColor)
        WriteImageData = WriteImageData + str(WriteColor)
with open("FinalImageFile.ppm", "a") as ImageFile:
    ImageFile.write(WriteImageData)
ImageFile = Image.open("FinalImageFile.ppm")
ImageFile.save("FinalImageFile" + ".bmp", "BMP")