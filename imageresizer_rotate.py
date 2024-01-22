from PIL import Image

Original_Image = Image.open(r"path2originalpic.jpg")
  
rotated_image2 = Original_Image.transpose(Image.ROTATE_90)
  
rotated_image2.save(r"path2newpic.jpg")
