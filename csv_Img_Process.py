import pandas as pd
import os
import shutil


def clearUp(name, idv):    # Separate images to each folder according to the criteria
    img_Path = '/home/oem/cultivate_classification/cultivar_100/train_images/'
    new_Img_Path = '/home/oem/cultivate_classification/cultivar_100/'
    shutil.move(img_Path + name, new_Img_Path + idv)


# load a csv file & count
df_all = pd.read_csv("/home/oem/cultivate_classification/cultivar_100/train_cultivar_mapping.csv")
print(len(df_all))
df_all.dropna(inplace=True) # dropna() : delete empty data
print(len(df_all))
df_all.head()


# index count search
unique_cultivars = list(df_all["cultivar"].unique())
num_classes = len(unique_cultivars)
print(num_classes)


# making new csv file
df_all["file_path"] = df_all["image"].apply(lambda image: "train_images/" + image)
df_all["cultivar_index"] = df_all["cultivar"].map(lambda item: unique_cultivars.index(item))
df_all["is_exist"] = df_all["file_path"].apply(lambda file_path: os.path.exists(file_path))
df_all = df_all[df_all.is_exist==True]
df_all.head()
df_all.to_csv('DataSave.csv')


img_list = pd.read_csv('/home/oem/cultivate_classification/cultivar_100/DataSave.csv')


# Extract only the desired column
img_index = img_list[['image', 'cultivar_index']]


# Sort ascending by "cultivar_index" value
sort_img = img_index.sort_values(by='cultivar_index', axis=0)
sort_img.to_csv('SortDataSet.csv')


# Create file(0~99)
for i in range(100):
    i = str(i)
    os.mkdir(i)


# csv separation
for a in range(100):
    create_csv = sort_img.loc[(sort_img["cultivar_index"] == a), :]
    a = str(a)
    create_csv.to_csv(a + 'data')

    
# call a function after extracting the image_path and cultivar_index values
for t in range(100):
    t = str(t)
    need = pd.read_csv(t + 'data')
    for id in need['image']:
        clearUp(id, t)
        
        
