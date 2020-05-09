print ("Hello world")
if 3 > 2:
    print('Ca marche!')

if 5 > 2:
    print('5 est effectivement plus grand que 2')
else:
    print('5 est plus petit que 2')

name = "Corinne"
if name == "Josh":
    print("Salut Josh")
elif name == "Corinne":
    print("Salut Corinne")
else:
    print("Salut personne!")

volume = 57
if volume < 20:
    print("it is quiet")
elif 20 <= volume < 40:
    print("It is a nice background music")
elif 80 <= volume < 100:
    print("A bit too loud!")
else:
    print("My ears are hurting!!!")

def hi():
    print('Hello!')
    print('How are you?')
hi()

def hi(name):
    if name == "Corinne":
        print("Hi Corinne")
    elif name == "Josh":
        print("Hi Josh")
    else:
        print("Hello there!")
hi("Corinne")
hi("Josh")
hi("Benjamin")

def hi(name):
    print('Hi ' + name + '!')
hi("Rachel")


girls = ['C', 'M', 'P', 'R']
for name in girls:
    hi(name)
    print('Next girls')
for i in range(1, 6):
    print(i)


    

    
          
        
