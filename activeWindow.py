import win32gui, win32process, psutil


# Code from https://stackoverflow.com/a/65363087
def active_window_process_name():
    try:
        pid = win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow())
        return (psutil.Process(pid[-1]).name())
    except:
        pass
