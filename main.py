import os
import pygame
from pygame import mixer

def play_music(file_path):
    mixer.init()
    mixer.music.load(file_path)
    mixer.music.play()

def stop_music():
    mixer.music.stop()

def pause_music():
    mixer.music.pause()

def unpause_music():
    mixer.music.unpause()

if __name__ == "__main__":
    while True:
        print("Commands: play / stop / pause / unpause / quit")
        cmd = input("->")

        if cmd == "play":
            file_path = input("Enter the path of the music file: ")
            play_music(file_path)
        elif cmd == "stop":
            stop_music()
        elif cmd == "pause":
            pause_music()
        elif cmd == "unpause":
            unpause_music()
        elif cmd == "quit":
            break
        else:
            print("Invalid command!")
