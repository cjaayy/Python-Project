import turtle
import pygame

def draw_tulip():
    turtle.fillcolor("red")
    turtle.begin_fill()

    turtle.circle(50, 180)
    turtle.circle(120, 180)
    turtle.left(90)
    turtle.forward(200)

    turtle.left(90)
    turtle.circle(-120, 180)
    turtle.circle(-50, 180)

    turtle.end_fill()

def play_sound(sound_file):
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()
    pygame.time.wait(3000)  # Wait for the sound to finish (adjust time if needed)
    pygame.mixer.music.stop()

def main():
    turtle.speed(2)
    turtle.bgcolor("lightgreen")
    turtle.penup()
    turtle.goto(0, -200)
    turtle.pendown()

    draw_tulip()

    # Replace 'your_sound_file.mp3' with the path to your sound file
    sound_file = 'your_sound_file.mp3'
    play_sound(sound_file)

    turtle.done()

if __name__ == "__main__":
    main()