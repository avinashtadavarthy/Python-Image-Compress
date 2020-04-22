import os
import cv2

os.mkdir("compressed")

i=0
for filename in os.listdir("./"):
    if os.path.isfile(filename):
        img = cv2.imread(filename)
        filesize = os.stat(filename).st_size / 1000.0
        print("file", i+1)
        print("details:", filename, filesize, img.shape)

        # decide image size scaling percentage
        scale_percent = None
        if img.shape[1] < 1500:
            scale_percent = 100
        elif 2000 > img.shape[1] >= 1500:
            scale_percent = 70
        elif 3000 > img.shape[1] >= 2000:
            scale_percent = 50
        elif 4000 >= img.shape[1] >= 3000:
            scale_percent = 30
        else: 
            scale_percent = 20

        print("scale percent:", scale_percent, img.shape[1] * scale_percent/100.0)
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)

        # resize image
        resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

        # save image
        savedfilename = filename.split(".")[0]+"-min.jpg"
        cv2.imwrite("compressed/"+savedfilename, resized, [int(cv2.IMWRITE_JPEG_QUALITY), 85])
        print("file saved as:", savedfilename)

        print()
        i = i+1
