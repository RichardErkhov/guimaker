from screeninfo import get_monitors
#for pygame window
def get_pygame_window_resolution(screen) -> [int, int]:
    return list(screen.get_size())

#for tkinter window
def get_tkinter_window_resolution(window) -> [int, int]:
    resolution = [window.winfo_width(),
                    window.winfo_height()]
    return resolution

#for monitor
def get_monitor_resolution(screen_number: int = 0) -> [int, int]:
    #https://stackoverflow.com/questions/3129322/how-do-i-get-monitor-resolution-in-python
    monitor_info = get_monitors()[screen_number]
    return monitor_info.width, monitor_info.height