from turtle import *
import json

halt = False
currentStatus = False
colormode(255)
bgcolor(0, 0, 0)

setworldcoordinates(0, 0, 1000, 1000)
penup()
pencolor(255, 255, 255)

title("Vector Display")

speed(0)

with open('savedFunctions.json', 'r') as openfile: json_object = json.load(openfile)
createdFunctions = json_object

with open('text.json', 'r') as openfile: json_object = json.load(openfile)
textFunctions = json_object

with open('var.json', 'r') as openfile: json_object = json.load(openfile)
tempVar= json_object

colorROM = [(255, 255, 255), (170, 170, 170), (85, 85, 85), (0, 0, 0), (255, 255, 85),
            (0, 170, 0), (85, 255, 85), (170, 0, 0), (255, 85, 85), (170, 85, 0), 
            (170, 0, 170), (255, 85, 255), (0, 170, 170), (85, 255, 255), (0, 0, 170), 
            (85, 85, 255)]

while True:
    colorType = str(input("Coloring type: (c)olor / (b)rightness\n"))
    if colorType == "c" or colorType == "b":
        break
    print(" Invalid argument: " + colorType)
    
class pointer:
    def __init__(self):
        pass
    
    def init(self):
        clearscreen()
        speed(0)
        penup()
        goto(0, 0)
        bgcolor("#000000")
        colormode(255)
        pencolor(255, 255, 255)
        createdFunctions = {}
    
    def startDraw(self):
        pendown()
            
    def endDraw(self):
        penup()
    
    def draw(self, drawFunction): 
        try:
            if colorType == "b":
                colorValue = int(drawFunction[3])
                brightnessValue = colorValue * 17
                colormode(255)
                pencolor(brightnessValue, brightnessValue, brightnessValue)
            elif colorType == "c":
                colormode(255)
                colorValue = int(drawFunction[3])
                pencolor(colorROM[colorValue])
            showturtle()
            goto(xcor() + int(drawFunction[1]), ycor() + int(drawFunction[2]))
            pencolor(255, 255, 255)
        except:
            print(" Invalid argument(s)")

    def drawStatus(self):
        print(" " + str(isdown()))
        
    def pos(self, posFunction):
        if len(posFunction) == 2:
            if posFunction[1] == "x":
                print(str(xcor()))
            elif posFunction[1] == "y":
                print(str(ycor()))
        elif len(posFunction) == 3:
            if posFunction[1] == "x" and posFunction[2] == "y": 
                print(str(xcor()) + ", " + str(ycor()))
                    
    def teleport(self, teleportFunction):
        currentSpeed = speed()
        currentStatus = isdown()
        penup()
        try:
            goto(int(teleportFunction[1]), int(teleportFunction[2]))
            if currentStatus == True:
                pendown()
            elif currentStatus == False:
                penup()
        except:
            print(" Invalid argument(s)")
    
    def color(self, colorFunction):
        try:
            if (int(colorFunction[1]) <= 15 and int(colorFunction[1]) >= 0):
                if colorType == "b":
                    colorValue = int(colorFunction[1])
                    brightnessValue = colorValue * 17
                    colormode(255)
                    pencolor(brightnessValue, brightnessValue, brightnessValue)
                elif colorType == "c":
                    colormode(255)
                    colorValue = int(colorFunction[1])
                    pencolor(colorROM[colorValue])
            else:
                print(" Color index out of range")
        except:
            print(" Invalid argument")
            
    def colors(self):
        print(""" 0 : White
 1 : Light Gray
 2 : Dark Gray
 3 : Black
 4 : Yellow
 5 : Dark Green
 6 : Light Green
 7 : Dark Red
 8 : Light Red
 9 : Brown
 10 : Dark Magenta
 11 : Light Magenta
 12 : Dark Cyan
 13 : Light Cyan
 14 : Dark Blue
 15 : Light Blue""")
        
    def speed(self, speedFunction):
        try:
            if int(speedFunction[1]) >= 0 and int(speedFunction[1]) <= 10: 
                speed(int(speedFunction[1]))
            else: 
                print(" Speed out of range (0-10)")
        except:
            print(" Invalid argument")
            
    def cmd(self):
        print(""" init : Initialize the board
 startDraw : Leaves a trace when the pointer moves
 endDraw : Stops leaving a trace when the pointer moves
 drawStatus : Returns the status of the pointer
 draw x y 0-15 : Moves the pointer via the relative position given and uses the color/brightness
 pos : Takes 1 or 2 arguments and returns the desired value (x or y)
 teleport x y : Teleports the pointer to the absolute position
 color 0-15 : Changes the color of the pen
 colors : (With colorType: color) Displays all colors
 speed 0-10 : Defines the speed at which the pointer moves""")
        
    def createFunction(self, functionName):
        continueParse = True
        createdFunctions[functionName] = []
        
        while continueParse:
            parseFunction = str(input(" "))
            if parseFunction == "end":
                continueParse = False
                break
            if checkValidFunction(parseFunction) == True:
                parseFunction.split()
                createdFunctions[functionName].append(parseFunction)
            else:
                print("  Invalid Function")
                
        json_object = json.dumps(createdFunctions, indent=4)
        with open("savedFunctions.json", "w") as outfile: outfile.write(json_object)
    
    def createdFunctionNames(self):
        if createdFunctions == {}:
            print()
        else:
            for keys, value in createdFunctions.items():
                print(" "+keys)
            
    def useCreatedFunctions(self, functionName):
        if functionName in createdFunctions:
            currentFunction = createdFunctions[functionName].copy()
            for i in range(len(currentFunction)):  
                currentParse = currentFunction[0]
                vectorDraw(currentParse)
                del currentFunction[0]
        else:
            print(" No Function Available")
            
    def editCreatedFunctions(self, functionName):
        if functionName in createdFunctions:
            currentFunction = createdFunctions[functionName].copy()
            continueEdit = True
            for i in range(len(currentFunction)):
                print(" "+ str(i) + ": " + str(currentFunction[i]))
            while continueEdit:
                editLine = str(input("  "))
                if editLine == "end":
                    continueEdit = False
                    break
                if continueEdit == False:
                    break
                else:
                    continueCode = False
                    try:
                        cache = int(editLine)   
                        continueCode = True                   
                    except:
                        print("   Invalid Line Value")
                        continueCode = False     
                    if continueCode == True:     
                        if int(editLine) >= 0 and int(editLine) <= (len(currentFunction)-1):
                            isEdittingFunc = True
                            while isEdittingFunc == True:
                                editFunction = str(input("   "))
                                if editFunction == "end":
                                    isEdittingFunc = False
                                    continueEdit = False
                                    break 
                                if checkValidFunction(editFunction) == False:
                                    print("    Invalid Function")
                                else:
                                    editFunction.split()
                                    currentFunction[int(editLine)] = editFunction
                                    createdFunctions[functionName] = currentFunction
                                    continueCode = False
                                    break
                        else:
                            print("   Line Index Out of Range")
                        
            for i in range(len(currentFunction)):
                print(" "+ str(i) + ": " + str(currentFunction[i]))
            
            json_object = json.dumps(createdFunctions, indent=4)
            with open("savedFunctions.json", "w") as outfile: outfile.write(json_object)
        else:
            print(" No Function Available")
    
    def readCreatedFunctions(self, functionName):
        if functionName in createdFunctions:
            for i in range(len(createdFunctions[functionName])):
                print(" "+ str(i) + ": " + str(createdFunctions[functionName][i]))
        else:
            print(" No Function Available")
    
    def deleteCreatedFuncions(self, functionName):
        if functionName in createdFunctions:
            createdFunctions.pop(functionName)
            
            json_object = json.dumps(createdFunctions, indent=4)
            with open("savedFunctions.json", "w") as outfile: outfile.write(json_object)
        else:
            print(" No Function Available")
    
    def movePointer(self, moveFunction):
        currentDrawStatus = isdown()
        penup()
        goto(xcor() + int(moveFunction[1]), ycor() + int(moveFunction[2]))
        if currentDrawStatus == True: pendown()
        else: penup()
    
    def reloadJsonFile(self):
        global createdFunctions
        with open('savedFunctions.json', 'r') as openfile: json_object = json.load(openfile)
        createdFunctions = json_object
    
    def drawText(self, letterName):
        if letterName == "undo":
            color(0,0,0)
            goto(xcor() - 15, ycor())
            begin_fill()
            goto(xcor() - 50, ycor())
            goto(xcor(), ycor() + 100)
            goto(xcor() + 50, ycor())
            goto(xcor(), ycor() - 100)
            goto(xcor() - 50, ycor())
            end_fill()
            color(255,255,255)
        elif letterName == "nextLine":
            color(0,0,0)
            goto(xcor() - 65, ycor() - 115)
            color(255,255,255)
        elif letterName == "prevLine":
            color(0,0,0)
            goto(xcor() - 65, ycor() + 115)
            color(255,255,255)
        elif letterName == "space":
            color(0,0,0)
            goto(xcor() + 25, ycor())
            color(255,255,255)
        
        else:
            if letterName in textFunctions:
                currentFunction = textFunctions[letterName].copy()
                for i in range(len(currentFunction)):  
                    currentParse = currentFunction[0]
                    vectorDraw(currentParse)
                    del currentFunction[0]
            elif letterName not in textFunctions:
                print(" No Letter Available")
    
    def drawWord(self, word):
        currentWord = list(word)
        for i in range(len(currentWord)):
            currentParse = currentWord[0]
            vectorDraw("text " + currentWord[0])
            del currentWord[0]


Pointer = pointer()

# Change user input into vector functions
def vectorDraw(userInput):

    userFunction = userInput.split()
    
    # Check functions
    if userFunction == []:
        print(" Invalid Function")
    
    elif userFunction[0] == "init" and len(userFunction) == 1:
        Pointer.init()

    elif userFunction[0] == "startDraw" and len(userFunction) == 1:
        Pointer.startDraw()

    elif userFunction[0] == "endDraw" and len(userFunction) == 1:
        Pointer.endDraw()

    elif userFunction[0] == "draw" and len(userFunction) == 4:
        Pointer.draw(userFunction)

    elif userFunction[0] == "drawStatus" and len(userFunction) == 1:
        Pointer.drawStatus()

    elif userFunction[0] == "pos" and (len(userFunction) >= 2 and len(userFunction) <= 3):
        Pointer.pos(userFunction)

    elif userFunction[0] == "teleport" and len(userFunction) == 3:
        Pointer.teleport(userFunction)

    elif userFunction[0] == "color" and len(userFunction) == 2:
        Pointer.color(userFunction)

    elif userFunction[0] == "colors" and colorType == "c":
        Pointer.colors()       

    elif userFunction[0] == "speed" and len(userFunction) == 2:
        Pointer.speed(userFunction)

    elif userFunction[0] == "cmd":
        Pointer.cmd()
    
    elif userFunction[0] == "newFunc" and len(userFunction) == 2:
        Pointer.createFunction(userFunction[1])
    
    elif userFunction[0] == "nameFunc" and len(userFunction) == 1:
        Pointer.createdFunctionNames()
    
    elif userFunction[0] == "call" and len(userFunction) == 2:
        Pointer.useCreatedFunctions(userFunction[1])
        
    elif userFunction[0] == "edit" and len(userFunction) == 2:
        Pointer.editCreatedFunctions(userFunction[1])
        
    elif userFunction[0] == "read" and len(userFunction) == 2:
        Pointer.readCreatedFunctions(userFunction[1])
    
    elif userFunction[0] == "del" and len(userFunction) == 2:
        Pointer.deleteCreatedFuncions(userFunction[1]) 
        
    elif userFunction[0] == "printJson" and len(userFunction) == 1:
        print(json.dumps(createdFunctions, indent=4))
        
    elif userFunction[0] == "move" and len(userFunction) == 3:
        Pointer.movePointer(userFunction)
    
    elif userFunction[0] == "reloadJson" and len(userFunction) == 1:
        Pointer.reloadJsonFile()
    
    elif userFunction[0] == "text" and len(userFunction) == 2:
        Pointer.drawText(userFunction[1])
    
    elif userFunction[0] == "word" and len(userFunction) == 2:
        Pointer.drawWord(userFunction[1])

    else:
        print(" Invalid function")

def checkValidFunction(userInput):
    userFunction = userInput.split()
    
    # Check functions
    if userFunction[0] == "init" and len(userFunction) == 1:
        return True

    elif userFunction[0] == "startDraw" and len(userFunction) == 1:
        return True

    elif userFunction[0] == "endDraw" and len(userFunction) == 1:
        return True

    elif userFunction[0] == "draw" and len(userFunction) == 4:
        return True

    elif userFunction[0] == "drawStatus" and len(userFunction) == 1:
        return True

    elif userFunction[0] == "pos" and (len(userFunction) >= 2 and len(userFunction) <= 3):
        return True

    elif userFunction[0] == "teleport" and len(userFunction) == 3:
        return True

    elif userFunction[0] == "color" and len(userFunction) == 2:
        return True

    elif userFunction[0] == "colors" and colorType == "c":
        return True       

    elif userFunction[0] == "speed" and len(userFunction) == 2:
        return True

    elif userFunction[0] == "cmd":
        return True

    elif userFunction[0] == "move" and len(userFunction) == 3:
        return True

    else:
        return False

# Loop it
while halt == False:

    # Get user input
    UserInputFunc = str(input(""))

    if UserInputFunc == "halt":
        halt = True
        break

    # Perform the functions
    vectorDraw(UserInputFunc)