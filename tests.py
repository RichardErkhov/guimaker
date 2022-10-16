import pygame
import tkinter as tk
import time
from helper import *
from main import gui
import unittest
def tests():
    pygame.init()
    screen = pygame.display.set_mode([500, 500])
    print(f"get_pygame_window_resolution:{get_pygame_window_resolution(screen)}")
    print(f"get_monitor_resolution:{get_monitor_resolution(0)}")
    pygame.quit()
    window_tkinter = gui(width=1280, height=720, window_type='tkinter', warnings=False, window_title="test_tkinter")
    #while True:
    window_tkinter.update()
    window_pygame = gui(width=1280, height=720, window_type='pygame', warnings=False, window_title="test_pygame")
    window_pygame.update()
    time.sleep(5)
    pygame.quit()

class Test(unittest.TestCase):

    def test_helper_get_tkinter_window_resolution(self):
        window = tk.Tk()
        window.configure(width=1280, height=720)
        window.update()
        self.assertEqual(get_tkinter_window_resolution(window), [1280, 720])
        window.destroy()
    
    def test_helper_get_pygame_window_resolution(self):
        pygame.init()
        window = pygame.display.set_mode([1280, 720])
        self.assertEqual(get_pygame_window_resolution(window), [1280, 720])
        pygame.display.quit()

    def test_helper_get_monitor_resolution(self):
        real_monitor_resolution = (1920, 1080)
        self.assertEqual(get_monitor_resolution(), real_monitor_resolution)

    #def test_tkinter_create_window(self):
    #    window_tkinter = gui(width=1280, height=720, window_type='tkinter', warnings=False, window_title="test_tkinter")



if __name__ == "__main__":
    unittest.main()
