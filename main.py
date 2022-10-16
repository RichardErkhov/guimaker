import pygame
import tkinter as tk
import time
from helper import *

class gui:
    def __init__(self, 
        width:int = 500, 
        height:int = 500, 
        window_type:str = "pygame", 
        warnings:bool = True, 
        window_title:str = "GUI"):
        #height of the window
        self.height = int(height)
        #width of the window
        self.width = int(width)
        #type of the window:
        # -> tkinter (supported)
        # -> pygame  (supported)
        # -> pyqt    (planning)
        # -> cv2     (planning)
        self.window_type = str(window_type).lower()
        self.warnings = bool(warnings)
        self.window_title = str(window_title)
        self.gui_coordinates = []
        #for rectangle: [x1, y1, x2, y2]:[int, int, int, int]
        #for text: [x, y]:[int, int]
        self.gui_types = []
        #gui types: rectangle, text
        self.gui_additionals = []
        #gui additionals for rectangle:
        '''
        [0] Visible: bool 
        [1] Color: str #usually hex format

        '''
        #gui additionals for text:
        '''
        [0] visible: bool
        [1] text_color: str #usually hex format
        [2] text_size: int
        [3] text_font: str 
        
        '''
        self.create_window()
    
    def create_window(self, warnings = False):
        if warnings:
            monitor_x, monitor_y = get_monitor_resolution()
            if monitor_x < self.width or monitor_y < self.height:
                print(f"WARNING| Window resolution ({self.width}x{self.height}) is bigger than the 0th display size ({monitor_x}x{monitor_y})")

        if self.window_type == "pygame":
            pygame.init()
            self.window = pygame.display.set_mode([self.width, self.height])
            pygame.display.set_caption(self.window_title)

        elif self.window_type == "tkinter":
            self.window = tk.Tk()
            self.window.configure(width=self.width, height=self.height)
            self.window.title(self.window_title)

    def change_window_title(self, title:str = "GUI"):
        self.window_title = title

        if self.window_type == "tkinter":
            self.window.title(self.window_title)

        if self.window_type == "pygame":
            pygame.display.set_caption(self.window_title)
        
    def change_window_resolution(self, resolution:list = [500, 500]):
        self.width = int(resolution[0])
        self.height = int(resolution[1])
        
        if self.window_type == "tkinter":
            self.window.configure(width = self.width, height = self.height)

        elif self.window_type == "pygame":
            pygame.transform.scale(self.window, (self.width, self.height))
    
    def get_window_resolution(self):
        if self.window_type == "tkinter":
            return get_tkinter_window_resolution(self.window)
        
        elif self.window_type == "pygame":
            return get_pygame_window_resolution(self.window)
        
    def update(self):
        if self.window_type == "tkinter":
            self.window.update()
        if self.window_type == "pygame":
            pass
    
    def add_button(self, command, x1=0, y1=0, x2=0, y2=0, borders_x1 = 0, borders_y1 = 0, borders_x2 = 0, borders_y2 = 0,
    color_inside = "#000000", color_outside = "#000000", text_color="#FFFFFF", text_size=10, text_position='center', text_font = "Arial",
    text = "test"
    ):
        if self.window_type == "tkinter":
            #what the hell I suppose to write here? How do I implement coords, color?
            pass
        if self.window_type == "pygame":
            self.create_shape(shape_type = "rectangle", visible = True, x1 = x1, y1 = y1, x2 = x2, y2 = y2, color = color_outside)
            self.create_shape(shape_type = "rectangle", visible = True, x1 = x1+borders_x1, y1 = y1 + borders_y1, x2 = x2 - borders_x2, y2 = y2-borders_y2,
            color = color_outside)
            xx,yy = self.get_coords(x1, y1, x2, y2, text_position, text, text_size, text_font)
            self.create_text(visible = True, x = xx, y = yy) #TODO finish the text function
    def get_coords(self, x1, y1, x2, y2, text_position, text, text_size, text_font):
        pass
    def create_shape(self, shape_type = "rectangle", visible = True, x1=0, y1=0, x2=0,y2=0, color = '#000000'):
        if self.window_type == 'tkinter':
            pass
        elif self.window_type == 'pygame':
            self.gui_coordinates.append([x1, y1, x2, y2])
            self.gui_types.append(shape_type)
            self.gui_additionals.append([visible, color])

    def create_text(self, visible = True, x = 0, y = 0, text_color = "#000000", text_size=10, text_font='Arial'):
        if self.window_type == "tkinter":
            pass
        elif self.window_type == "pygame":
            self.gui_coordinates.append([x, y])
            self.gui_types.append('text')
            self.gui_additionals.append([visible, text_color, text_size, text_font])

    def close(self):
        if self.window_type == 'tkinter':
            self.window.destroy()
        elif self.window_type == 'pygame':
            pygame.display.quit()

if __name__ == "__main__":
    from tests import tests
    tests()
