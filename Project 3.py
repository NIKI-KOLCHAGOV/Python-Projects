import Vec3
from Vec3 import *
from VectorColor import *
from CreateRay import *

ImageWidth = 256
ImageHeight = 256

#WriteImageData = "P3\n" + str(ImageWidth) + " " + str(ImageHeight) + "\n255\n"
#print("P3\n" + str(ImageWidth) + " " + str(ImageHeight) + "\n255\n")

def RayColor(r):
    UnitDirection = Vec3.unit_vector(r)
    a = 0.5 * (UnitDirection.y() + 1.0)
    return (1.0 - a) * color(1.0, 1.0, 1.0) + a * color(0.5, 0.7, 1)

#Screen Size And Image
AspectRatio = 16.0 / 9.0
ImageWidth = 400; int(ImageWidth)
ImageHeight = int(ImageWidth / AspectRatio)
#Calculate the image height, and ensure that it's at least 1.
if ImageHeight < 1 == True:
    ImageHeight = 1
#print(ImageWidth, ImageHeight)

#Camera
FocalLenght = 1.0
ViewportHeight = 2.0
ViewportWidth = ViewportHeight * (float(ImageWidth) / ImageHeight)
CameraCenter = point3(0, 0, 0).length()
#Calculate the vectors across the horizontal and down the vertical viewport edges.
#Basically Make The Pixels
ViewportU = Vec3(ViewportWidth, 0, 0).length()
ViewportV = Vec3(0, -ViewportHeight, 0).length()
#Calculate the horizontal and vertical delta vectors from pixel to pixel.
PixelDeltaU = ViewportU / ImageWidth
PixelDeltaV = ViewportV / ImageHeight
#Calculate the location of the upper left pixel.
ViewportUpperLeft = CameraCenter - Vec3(0, 0, FocalLenght).length() - ViewportU / 2 - ViewportV / 2
StartPixelLocation = ViewportUpperLeft + 0.5 * (PixelDeltaV + PixelDeltaV)

#Render

WriteImageData = "P3\n" + str(ImageWidth) + " " + str(ImageHeight) + "\n255\n"
print("P3\n" + str(ImageWidth) + " " + str(ImageHeight) + "\n255\n")

#Counter1 = ImageWidth
R = 0; G = 0; B = 0
R = float(R); G = float(G); B = float(B)
for Counter1 in range(0, ImageHeight, 1):
    print("\rScanlines Remaining: " + str(ImageHeight - Counter1), end="")
    for Counter2 in range(0, ImageWidth, 1):
        #R = float(Counter2) / float(ImageWidth) G = float(Counter1) / float(ImageHeight) B = 0.0 IR = (255.99 * R); IR = int(IR) IG = (255.99 * G); IG = int(IG) IB = (255.99 * B); IB = int(IB) print(str(IR) + " " + str(IG) + " " + str(IB) + "\n") WriteImageData = WriteImageData + str(IR) + " " + str(IG) + " " + str(IB) + "\n"
        PixelCenter = StartPixelLocation + (Counter2 * PixelDeltaU) + (Counter1 * PixelDeltaV)
        RayDirection = PixelCenter - CameraCenter
        r = Ray(CameraCenter, RayDirection)
        #ImageWidth2 = Counter2 / ImageWidth
        #ImageHeight2 = Counter1 / ImageHeight
        #PixelColor2 = color(ImageWidth2, ImageHeight2, 0)
        PixelColor2 = RayColor(r)
        WriteImageData = WriteImageData + str(PixelColor2)
SaveImage(ImageWidth, ImageHeight, WriteImageData)