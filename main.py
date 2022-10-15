from screeninfo import get_monitors
import pygame
import tkinter as tk

#for pygame window
def get_pygame_window_resolution(screen) -> [int, int]:
    return screen.get_size()

#for tkinter window
def get_tkinter_window_resolution(window) -> [int, int]:
    resolution = [window.winfo_screenwidth(),
                    window.winfo_screenheight()]
    return resolution

#for monitor
def get_monitor_resolution(screen_number: int = 0) -> [int, int]:
    #https://stackoverflow.com/questions/3129322/how-do-i-get-monitor-resolution-in-python
    monitor_info = get_monitors()[screen_number]
    return monitor_info.width, monitor_info.height

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
        self.window_type = str(window_type).lower()
        self.warnings = bool(warnings)
        self.window_title = str(window_title)
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
    
    def get_window_resolution(self) -> [int, int]:
        if self.window_type == "tkinter":
            return get_tkinter_window_resolution(self.window)
        
        elif self.window_type == "pygame":
            return get_pygame_window_resolution(self.window)

def tests():
    pygame.init()
    screen = pygame.display.set_mode([500, 500])
    print(f"get_pygame_window_resolution:{get_pygame_window_resolution(screen)}")
    print(f"get_monitor_resolution:{get_monitor_resolution(0)}")
    window_tkinter = gui(width=1280, height=720, window_type='tkinter', warnings=False, window_title="test_tkinter")
    pygame.quit()

if __name__ == "__main__":
    tests()
