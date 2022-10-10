## Import Pillow module first
from PIL import Image
import os

## Create a new folder of those images you want to add in the pdf
folder=input("Enter Folder Address   : ")
files=os.listdir(folder)

li=[]
for file in files:
    s=folder+"\\" + file
    
    ## Must check the images should have .jpg , .jpeg and .png format only
    
    if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
        i = Image.open(s)
        width , height = i.size
        m = i.convert("RGB")
        m = m.resize((width , height))
        
        li.append(m)
a=li.pop()

pdf_file=input("Enter PDF filename with .pdf extension   : ")
s=folder+"//"+pdf_file
m.save(s , save_all=True , append_images=li)
print("The pdf is saved in the same folder")