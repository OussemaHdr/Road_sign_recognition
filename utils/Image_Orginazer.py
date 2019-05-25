import pandas as pd
import os
from tqdm import tqdm
from PIL import Image
data = pd.read_csv('C:/Users/SBS/Desktop/GT-final_test.csv', sep=';')

pictures_folder = 'C:/Users/SBS/Desktop/Final_Test/Images'
target = 'Test_full'

#creating multiple folders inside the main folder (tsawer) 
for i in range (0,43):
        os.mkdir('C:/Users/SBS/Desktop/Test_full/' + str(i))

#puting every picture in its associated class folder
for item in tqdm(range(0, data.shape[0])):
    picture_name = data['Filename'][item]
    picture = Image.open(pictures_folder + '/' + picture_name)
    picture_class = data['ClassId'][item]
    picture.save('Test_full/' + str(picture_class) + '/' + picture_name)
