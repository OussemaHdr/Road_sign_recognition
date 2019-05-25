# Self driving car Project "Mercury"
## Raspberry Pi comand    
### 1. Model loading  
###### NB : This may take arround 2-3 mins  
```python
from keras.models import load_model
classifier = load_model('/home/pi/SignRec-CNN_3.h5')
```  
### 2. GPIO setup  
```python
camera= PiCamera()
camera.resolution =(1024,768)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(15, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(32, GPIO.OUT, initial=GPIO.LOW)

GPIO.setup(3, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(5, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(29, GPIO.OUT)
pwmL=GPIO.PWM(12,100)
pwmR=GPIO.PWM(32,100)

GPIO.setup(40, GPIO.IN)
GPIO.setup(19, GPIO.IN)  
```  
### 3. Control functions  
```python
def Forward():
    GPIO.output(5,GPIO.HIGH)
    GPIO.output(3,GPIO.LOW)
    GPIO.output(12,GPIO.HIGH)

    GPIO.output(15,GPIO.HIGH)
    GPIO.output(13,GPIO.LOW)
    GPIO.output(32,GPIO.HIGH)

def Back():
    pwmL.start(70)
    GPIO.output(5,GPIO.LOW)
    GPIO.output(3,GPIO.HIGH)
    GPIO.output(12,GPIO.HIGH)
    pwmR.start(70)
    GPIO.output(15,GPIO.LOW)
    GPIO.output(13,GPIO.HIGH)
    GPIO.output(32,GPIO.HIGH)

def rotRight():
    GPIO.output(5,GPIO.HIGH)
    GPIO.output(3,GPIO.LOW)
    GPIO.output(12,GPIO.HIGH)

    GPIO.output(15,GPIO.LOW)
    GPIO.output(13,GPIO.HIGH)
    GPIO.output(32,GPIO.HIGH)

def rotLeft():
    GPIO.output(5,GPIO.LOW)
    GPIO.output(3,GPIO.HIGH)
    GPIO.output(12,GPIO.HIGH)

    GPIO.output(15,GPIO.HIGH)
    GPIO.output(13,GPIO.LOW)
    GPIO.output(32,GPIO.HIGH)

def sstop():
    GPIO.output(12,GPIO.LOW)
    GPIO.output(32, GPIO.LOW)
    pwmL.stop()
    pwmR.stop()

def cap():
    CLeft=GPIO.input(40)
    CRight=GPIO.input(19)
```  
### 4. Line tracker  
```python
def LineFollow():
    L1=[]
    if((GPIO.input(40)== False) and (GPIO.input(19)==False)):
        Forward()
    elif((GPIO.input(40)== False) and (GPIO.input(19)== True)):
        rotLeft()
    elif((GPIO.input(40)== True) and (GPIO.input(19)== False)):
        rotRight()
    if((GPIO.input(40)== True) and (GPIO.input(19)==True)):
        ImgCapture()
        prepare('/home/pi/sign.jpg')
        L1=predictt('/home/pi/sign.jpg')
        if(L1[0]==4):
            sstop()
            sleep(5)
        elif(L1[0]==3):
            rotRight()
            sleep(1.5)
            Forward()
            sleep(0.5)
        elif(L1[0]==2):
            rotLeft()
            sleep(1.5)
            Forward()
            sleep(0.5)
        else :
        	sstop()
        	sleep(3)
```  
### 5. Image capture 
```python
def ImgCapture():
    sleep(0.1)
    camera.capture('/home/pi/sign.jpg')
```  
### 6. Preparing the captured image  
```python  
def prepare(path):
    img = Image.open(path)
    img_reshaped = img.resize((32, 32))
    img_rotated = img_reshaped.rotate(180)
    img_rotated.save(path)
    img = Image.open(path)
    img = np.expand_dims(img, axis = 0)
    img = img/255
    return img
```  
### 7. Predict function 
```python
def predictt(path):
	prediction = classifier.predict([prepare(path)])
	L1=[]
	prediction
	n=(np.argmax(prediction))
	X=prediction[0][n]
	#print(np.argmax(prediction))
	L1.append(n)
	L1.append(X)
	return L1
```  
### 8. Loop
```python
screen=curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)
try:
    while True:
        char= screen.getch()
        if char== ord('q'):
            break
        if char== ord('S'):
            os.system("sudo shutdown now")
        if char == ord('a'):
            while True:
               LineFollow()
        elif char== curses.KEY_DOWN:
            Back()
        elif char== curses.KEY_RIGHT:
            rotRight()
        elif char== curses.KEY_LEFT:
            rotLeft()
        elif char== curses.KEY_UP:
            Forward()
        elif char== 10:
            sstop()

finally:
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    GPIO.cleanup()
```    
          
