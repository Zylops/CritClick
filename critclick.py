import pyautogui as p
import time as t

print('\nWelcome to critclick, a 1.16 autoclicker made by Zylops.')
print('You are currently on v1.1.0\n')

axe = input('Press w for wooden axe, s for stone, g for gold, i for iron, d for diamond, and n for nethernite and press enter: ')

if axe == 'w':
    critseconds = 1.25
elif axe == 's':
    critseconds = 1.25
elif axe == 'g':
    critseconds = 1
elif axe == 'i':
    critseconds = 1.11
elif axe == 'd':
    critseconds = 1
elif axe == 'n':
    critseconds = 1
else:
    print('Invalid option. Please try again.')
    input('Press enter to quit.')

class Player:
    def jump(self):
        p.press('space')
    
    def hit(self):
        p.click()
    
    def crit(self):
        self.jump()
        self.hit()
    
    def shield(self, hold):
        if hold == True:
            p.mouseDown(button='right')
        elif hold == False:
            p.mouseUp(button='right')
    
    def waitforloadbar(self, critseconds):
        t.sleep(critseconds)

player = Player()

while True:
    try:
        player.shield(False)
        player.crit()
        player.shield(True)
        player.waitforloadbar(critseconds)
        print('Hit a crit! Press Ctrl+C in this window to exit')
    except KeyboardInterrupt:
        break
