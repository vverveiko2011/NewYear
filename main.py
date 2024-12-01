from pygame import *
font.init()

win = display.set_mode((1000, 700))
display.set_caption('New Year')
win.fill((255, 255, 255))

font1 = font.Font('Comfortaa.ttf', 35)
welcomeText = font1.render("Press number that is under the picture", True, (0, 0, 0))

num1 = transform.scale(image.load("shrack.png"), (220, 210))
num2 = transform.scale(image.load("frozen.png"), (220, 210))

numbers = [K_1, K_2]
characters = ["Shack", "Frozen"]

send = 0
message = 1

with open("hello.txt", "w", encoding = "utf-8") as file:
    file.write("")

Game = True
FPS = 60
clock = time.Clock()
while Game:

    win.blit(welcomeText, (130, 10))

    win.blit(num1, (25, 90))
    win.blit(num2, (275, 90))
    if send:
        with open("hello.txt", "a", encoding = "utf-8") as file:
            file.write("Hi! it's me "+characters[message]+" and I wish you a good new year!\n")
        send = 0

    for e in event.get():
        if e.type == QUIT:
            Game = False 
        if e.type == KEYDOWN:
            if e.key in numbers:
                for i in range(len(numbers)):
                    if e.key == numbers[i]:
                        message = i
                send = 1

    clock.tick(FPS)
    display.update()