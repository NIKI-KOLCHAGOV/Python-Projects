from PIL import Image
nx = 200
ny = 100
ImageFile = open("FinalImageFile.ppm", "w")
with open("FinalImageFile.ppm", "w") as ImageFile:
  ImageFile.write("")
print("P3\n" + str(nx) + " " + str(ny) + "\n255\n")
with open("FinalImageFile.ppm", "a") as ImageFile:
    ImageFile.write("P3\n" + str(nx) + " " + str(ny) + "\n255\n")
Counter1 = ny
R = 0; G = 0; B = 0
R = float(R); G = float(G); B = float(B)
for Counter1 in range(ny, 0, -1):
    for Counter2 in range(0, nx, 1):
        R = float(Counter2) / float(nx)
        G = float(Counter1) / float(ny)
        B = 0.2
        IR = (255.99 * R); IR = int(IR)
        IG = (255.99 * G); IG = int(IG)
        IB = (255.99 * B); IB = int(IB)
        print(str(IR) + " " + str(IG) + " " + str(IB) + "\n")
        with open("FinalImageFile.ppm", "a") as ImageFile:
            ImageFile.write(str(IR) + " " + str(IG) + " " + str(IB) + "\n")
ImageFile = Image.open("FinalImageFile.ppm")
ImageFile.save("FinalImageFile" + ".bmp", "BMP")