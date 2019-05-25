# Self driving car Project "Mercury"
## Objectif: Building a traffic signs classifier  
### 1. Organizing test images  
Unlike the training images the data provided for the test is not organasied per class  
```python
data = pd.read_csv('.../GT-final_test.csv', sep=';')
pictures_folder = '...'
target = 'Test_full'

#creating multiple folders inside the main folder (tsawer) 
for i in range (0,43):
        os.mkdir('.../Test_full/' + str(i))

#puting every picture in its associated class folder
for item in tqdm(range(0, data.shape[0])):
    picture_name = data['Filename'][item]
    picture = Image.open(pictures_folder + '/' + picture_name)
    picture_class = data['ClassId'][item]
    picture.save('Test_full/' + str(picture_class) + '/' + picture_name)
```  
### 2. Picking the signs to work with
Since we plan to implement this model in a robot using RaspberryPi we decided to focuse on a small numbers of signs for better performance.    
  
| Num | Sign |  
| --- | --- |  
| 2 | Speed limit (50km/h) |  
| 8 | Speed limit (120km/h) |  
| 14 | Stop |  
| 33 | Turn right | 
| 34 | Turn left |    
