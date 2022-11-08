

from PIL import Image, ImageEnhance, ImageFilter
import os

path = "./imgs" #file with images to edit
pathOut = "./editedImgs" #file with edited images

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    edit = img.filter(ImageFilter.SHARPEN).filter(ImageFilter.SMOOTH).convert('L')

    
    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)

    

    clean_name = os.path.splitext(filename)[0]

    edit.save(f'{pathOut}/{clean_name}_edited.jpg')