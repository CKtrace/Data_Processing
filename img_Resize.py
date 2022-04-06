import glob
from PIL import Image
import os

# folder name (0~99)
for a in range(0, 99) :
    a = str(a)
    files = glob.glob('./' + a + '/*')

    for f in files:
        title, ext = os.path.splitext(f) # image name and extension split & save
        if ext in ['.png']:
            img = Image.open(f)
            img_resize = img.resize((299, 299)) # resize to (299, 299)
            img_resize.save(title+ext)
