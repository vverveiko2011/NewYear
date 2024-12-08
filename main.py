from pygame import *
font.init()
import random as rnd

win = display.set_mode((900, 500))
display.set_caption('New Year')
win.fill((255, 255, 255))

font1 = font.Font('Comfortaa.ttf', 35)
welcomeText = font1.render("Нажми на клавиатуре цифру на картинке", True, (0, 0, 0))

back = transform.scale(image.load("main.png"), (850, 400))

numbers = [K_1, K_2, K_3, K_4, K_5]
characters = ["Эрен Йегер", "Тоторо", "Тихиро Огино", "Поньо", "Кики"]
hihello = ["Привет", "Здравствуйте", "Доброго времени суток", "Ку", "Hi"]
text = [" желаю тебе встретить Новый год так, чтобы потом весь следующий год вспоминать эти моменты с улыбкой!",
" в Новом году пусть все твои желания исполняются быстрее, чем ты успеваешь загадать новые!",
" пусть твой календарь на следующий год будет полон приключений, смеха и счастья!",
" пусть каждый день следующего года будет таким же ярким и волшебным, как новогодняя ночь!",
" зажигай в Новом году так, чтобы даже звезды завидовали твоему блеску!"]

send = 0
message = 1

with open("hello.txt", "w", encoding = "utf-8") as file:
    file.write("")

Game = True
FPS = 60
clock = time.Clock()
while Game:

    win.blit(welcomeText, (25, 10))

    win.blit(back, (25, 55))
    if send:
        with open("hello.txt", "a", encoding = "utf-8") as file:
            file.write(hihello[rnd.randint(0,4)]+", это "+characters[message]+text[rnd.randint(0,4)]+"\n")
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