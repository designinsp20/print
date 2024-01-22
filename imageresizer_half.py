from PIL import Image
 
# Opens a image in RGB mode
im = Image.open(r"path2originalpic.jpg")
 
resized_im = im.resize((round(im.size[0]*0.5), round(im.size[1]*0.5)))
 
resized_im.save(r"path2newpic.jpg")
