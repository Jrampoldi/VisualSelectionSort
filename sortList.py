import pygame, sys, random  

WindowWidth, WindowHeight = (800, 400)
BLACK = (35, 35, 35)
WHITE = (235, 235, 235)
FPS = 60

#create list to hold random values with for loop to assign values
sortList = []
for i in range(0, WindowWidth):
    sortList.append([[i, WindowHeight], [i, random.randrange(WindowHeight)]])

#initialize values, create window, and create clock
pygame.init()
window = pygame.display.set_mode((WindowWidth, WindowHeight))
clock = pygame.time.Clock()

#initialize variable to control sorting algorithm index
k = 1

#create window loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #use selection sort to visually sort values
    key = sortList[k][1][1]
    j = k - 1
    while j > 0 and sortList[j][1][1] < key:
        sortList[j + 1][0][1] = sortList[j][0][1]
        sortList[j + 1][1][1] = sortList[j][1][1]
        j -= 1
    sortList[j + 1][1][1] = key

    #clear window
    window.fill(BLACK)
    
    #draw lines for each frame
    for i in range(len(sortList)):
        pygame.draw.line(window, WHITE, (sortList[i][0][0], sortList[i][0][1]), (sortList[i][1][0], sortList[i][1][1]))

    #update window
    pygame.display.update()

    #ensure index will not go out of bounds
    if k < (WindowWidth - 1):
        k += 1
    if k >= (WindowWidth - 1):
        k = 0

    #restrict frames per second
    clock.tick(FPS)