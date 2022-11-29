
import sys
import os
from PIL import Image

# img=Image.open('./converted_StringupimagesToPNG/Aerobite-GW.png')
# resize=img.resize((300,300))
# resize.save('Aerobite-GW.png','png')
#grab first and second argument
imagefolder=sys.argv[1]
outputfolder=sys.argv[2]
print(imagefolder,outputfolder)
#check if new/ exists, if not create it.
if not os.path.exists(outputfolder):
    os.makedirs(outputfolder) # makedirs - it is used to create a directory
#loop through image folder,
for filename in os.listdir(imagefolder): #listdirs - list all the items in the directory
    img=Image.open(f'{imagefolder}{filename}') # open an image from the imagefolder
# convert images to png
    resizing=img.resize((300,300))
    resizing.save(f'{outputfolder}{filename}','png')