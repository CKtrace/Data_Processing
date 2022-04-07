import glob
from PIL import Image
import os

# 0 ~ 99 folder exist
for a in range(1, 100) :
    a = str(a)
    # glob() return path & filename
    files = glob.glob('./' + a + '/*')
    
    for f in files:
        # Seprate title & extension
        title, ext = os.path.splitext(f)
        if ext in ['.png']:
            img = Image.open(f)
            # Image resize -> width = 299, height = 299
            img_resize = img.resize((299, 299))
            # Resized image save
            img_resize.save(title + ext)
