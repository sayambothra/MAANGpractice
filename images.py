from PIL import Image,ImageFilter
img=Image.open('./venv/images/Football.jpg')#To Open an Image and covert it an image object
print(img.format) # returns image format (Ex:JPEG,PNG etc)
print(img.size) # return image size in pixels
print(img.mode)#  returns image mode (RGB etc)
print(dir(img))
filtered_img=img.filter(ImageFilter.SMOOTH)
filtered_img.save("SMOOTH.png",'png')
img.thumbnail((300,300))
img.show()
box=(100,100,400,400)
region=img.crop(box) # crop an image by setting the  pixel size we want to crop
region.show()
filtered_img=img.convert('L') # converts image to grey scale image
resize=filtered_img.resize((300,300)) # to change the size of an image but it losses its aspect ratio
# aspect ratio is the relationship between the height and width of an image
img.thumbnail((300,300)) # resizes the image without affection the aspect ratio
resize.save("fr.png",'png')