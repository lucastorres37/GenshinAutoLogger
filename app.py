import pyautogui
import time
import dotenv
import os

dotenv.load_dotenv()
fbPass = os.getenv("FBPASSWORD")

def login(imageName):
    emailPosition = pyautogui.locateCenterOnScreen(imageName, confidence=.8)
    while(emailPosition == None):
        emailPosition = pyautogui.locateCenterOnScreen(imageName, confidence=.8)

    pyautogui.moveTo(emailPosition.x + 96, emailPosition.y)
    pyautogui.click()
    

buttonPosition = pyautogui.locateCenterOnScreen("genshin.png", confidence=.8)
print(buttonPosition)

if(buttonPosition == None):
    print('Not found')
    exit()
pyautogui.moveTo(buttonPosition.x, buttonPosition.y)
pyautogui.doubleClick()
  
  
  
time.sleep(2)



launchPosition = pyautogui.locateCenterOnScreen("Launch.png", confidence=.5)
print(launchPosition)

if(launchPosition == None):
    print('Not found')
    exit()
pyautogui.moveTo(launchPosition.x, launchPosition.y)
pyautogui.click()




fbPosition = pyautogui.locateCenterOnScreen("fb.png", confidence=.75)
while(fbPosition == None):
    fbPosition = pyautogui.locateCenterOnScreen("fb.png", confidence=.75)
    
pyautogui.moveTo(fbPosition.x, fbPosition.y)
pyautogui.click()

login("email.png")

pyautogui.write("lucastorresgomes@gmail.com")

login("senha.png") 

pyautogui.write(fbPass)
pyautogui.press('enter')




