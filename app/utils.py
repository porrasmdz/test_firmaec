
import os
import time
import platform
    
import re
import unicodedata


import subprocess
import pyautogui
import pyperclip
from app.constants import DEFAULT_CONFIDENCE, DEFAULT_SHORT_DELTATIME_SECS, LAUNCH_APP_TIMEOUT_SECS, OSTypes
from app.logger import logger

log = logger.getLogger("")

def click_element(local_path, confidence=DEFAULT_CONFIDENCE, timeout=LAUNCH_APP_TIMEOUT_SECS):
    inicio = time.time()
    
    if(not os.path.exists(local_path)):
        log.error(f"click_element - El archivo {local_path} no existe")
        return False
    
    path_imagen= os.path.abspath(local_path)
    while time.time() - inicio < timeout:
        try:
            ubicacion = pyautogui.locateCenterOnScreen(path_imagen, confidence=confidence)
            if ubicacion:
                pyautogui.click(ubicacion.x, ubicacion.y)
                return True
            time.sleep(DEFAULT_SHORT_DELTATIME_SECS)
        except pyautogui.ImageNotFoundException:
            pass
        except Exception as err:
            log.error(f"click_element - ERROR: f{err}")
    return False


def is_element_present(local_path, confidence=DEFAULT_CONFIDENCE, timeout=LAUNCH_APP_TIMEOUT_SECS):
    inicio = time.time()
    
    if(not os.path.exists(local_path)):
        log.error(f"is_element_present - El archivo {local_path} no existe")
        return False
    
    path_imagen= os.path.abspath(local_path)
    while time.time() - inicio < timeout:
        try:
            ubicacion = pyautogui.locateCenterOnScreen(path_imagen, confidence=confidence)
            if ubicacion:
                return True
            time.sleep(DEFAULT_SHORT_DELTATIME_SECS)
        except pyautogui.ImageNotFoundException:
            pass
        except Exception as err:
            log.error(f"is_element_present - ERROR: f{err}")
    return False
    
def is_valid_os(os_test: str):
    return os_test in [os.value for os in OSTypes]


def is_macos() -> bool:
    return platform.system() == "Darwin"


def press_enter() -> None:
    pyautogui.press("enter")


def press_escape() -> None:
    pyautogui.press("esc")


def paste_text(value: str) -> None:
    if is_macos():
        pyperclip.copy(value)
        pyautogui.hotkey("command", "v")
    else:
        pyautogui.write(value)


def open_file_in_dialog(absolute_path: str) -> None:
    if is_macos():
        pyautogui.hotkey("command", "shift", "g")
        time.sleep(DEFAULT_SHORT_DELTATIME_SECS)
        paste_text(absolute_path)
        press_enter()
        time.sleep(DEFAULT_SHORT_DELTATIME_SECS)
        press_enter()
        return

    paste_text(absolute_path)
    press_enter()
        
        

def focus_app(app_name: str) -> bool:
    system = platform.system()

    try:
        if system == "Windows":
            return _focus_app_windows(app_name)
        elif system == "Darwin":
            return _focus_app_mac(app_name)
        elif system == "Linux":
            return _focus_app_linux(app_name)
        return False
    except Exception:
        return False


def _focus_app_windows(app_name: str) -> bool:
    try:
        import pygetwindow as gw

        windows = gw.getWindowsWithTitle(app_name)
        if not windows:
            return False

        win = windows[0]

        if win.isMinimized:
            win.restore()

        win.activate()
        return True
    except Exception:
        return False


def _focus_app_mac(app_name: str) -> bool:
    try:
        subprocess.run(
            ["osascript", "-e", f'tell application "{app_name}" to activate'],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        return True
    except Exception:
        return False


def _focus_app_linux(app_name: str) -> bool:
    try:
        subprocess.run(
            ["wmctrl", "-a", app_name],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        return True
    except Exception:
        return False
    
    

def sanitize_filename(value: str, max_length: int = 120) -> str:
    if not value:
        return "unnamed"

    value = unicodedata.normalize("NFKD", value)
    value = value.encode("ascii", "ignore").decode("ascii")

    value = re.sub(r'[<>:"/\\|?*]', "-", value)

    value = re.sub(r"\s+", " ", value).strip()

    value = value.replace(" ", "_")

    value = value.strip(" .-_")

    if not value:
        value = "unnamed"

    value = value[:max_length].rstrip(" .-_")

    reserved = {
        "CON", "PRN", "AUX", "NUL",
        "COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9",
        "LPT1", "LPT2", "LPT3", "LPT4", "LPT5", "LPT6", "LPT7", "LPT8", "LPT9"
    }
    if value.upper() in reserved:
        value = f"_{value}"

    return value
