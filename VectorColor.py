from Vec3 import *
R = 0; G = 0; B = 0;
global WriteImageData2
def WriteColor(out, PixelColor):
    R = PixelColor.x()
    G = PixelColor.y()
    B = PixelColor.z()

    Rbyte = int(255.999 * R)
    Gbyte = int(255.999 * G)
    Bbyte = int(255.999 * B)
    return (str(Rbyte) + " " + str(Gbyte) + " " + str(Bbyte) + "\n")
    #with open("FinalImageFile.ppm", "a") as ImageFile:
        #ImageFile.write(str(Rbyte) + " " + str(Gbyte) + " " + str(Bbyte) + "\n")