import os
import random
import time
from typing import Literal

import pyautogui

from app.actions.base import BaseAction, ExecutionData
from app.constants import COMPONENTS, DEFAULT_SHORT_DELTATIME_SECS, DEFAULT_CONFIDENCE, DEFAULT_TARGET_BOX_PADDING, LAUNCH_APP_TIMEOUT_SECS, StampTypeLabels
from app.utils import click_element, is_element_present

DEFAULT_RESIGN_MARGIN=40

    
class SignDocument(BaseAction):
    SIGN_REASON_TEXT = None
    LOCATION_TEXT = None
    INVISIBLE_SIGN = False
    STAMP_TYPE: Literal["qr", "advanced", "simple"] = "qr"
    SIGN_SUCCESS_TIMEOUT= LAUNCH_APP_TIMEOUT_SECS
    RESIGNING=False
    
    def __init__(self):
        super().__init__(name="Firmar Dentro de Recuadro rojo", 
                         code_name="SIGN_DOC",
        )
        
    
    def sign_on_blue_square(self, test_context)-> bool:
        PADDING = DEFAULT_TARGET_BOX_PADDING
        blue_box = os.path.join(f"{test_context.config.profiles_dir}", COMPONENTS.RESIGN_TARGET_BOX)
        sign_reason_input = os.path.join(f"{test_context.config.profiles_dir}", COMPONENTS.SIGN_REASON_INPUT)
            
        if(not is_element_present(blue_box)):
            if(not is_element_present(sign_reason_input)):
                return False
            else:
                click_element(sign_reason_input)
                pyautogui.hotkey("tab")
                pyautogui.hotkey("tab")
                pyautogui.hotkey("tab")
                
                pyautogui.hotkey("backspace")
                pyautogui.hotkey("backspace")
                pyautogui.hotkey("backspace")
                pyautogui.hotkey("delete")
                pyautogui.hotkey("delete")
                pyautogui.hotkey("delete")
                pyautogui.typewrite("1")
                
                pyautogui.hotkey("enter")
                if(not is_element_present(blue_box)):
                    return False
                else:
                    blue_box_location = pyautogui.locateOnScreen(blue_box, confidence=DEFAULT_CONFIDENCE)
                    x = blue_box_location.left - DEFAULT_RESIGN_MARGIN
                    y = blue_box_location.top + PADDING 
                    pyautogui.click(x, y)
                    return True

             
        else:
            blue_box_location = pyautogui.locateOnScreen(blue_box, confidence=DEFAULT_CONFIDENCE)
            x = blue_box_location.left- DEFAULT_RESIGN_MARGIN
            y = blue_box_location.top + PADDING 
            pyautogui.click(x, y)
            return True

                
        
    def sign_on_red_square(self, test_context)-> bool:
        PADDING = DEFAULT_TARGET_BOX_PADDING
        red_box = os.path.join(f"{test_context.config.profiles_dir}", COMPONENTS.SIGN_TARGET_BOX)
        sign_reason_input = os.path.join(f"{test_context.config.profiles_dir}", COMPONENTS.SIGN_REASON_INPUT)
            
        if(not is_element_present(red_box)):
            #attempt to change to first page
            if(not is_element_present(sign_reason_input)):
                return False
            else:
                click_element(sign_reason_input)
                pyautogui.hotkey("tab")
                pyautogui.hotkey("tab")
                pyautogui.hotkey("tab")
                
                pyautogui.hotkey("backspace")
                pyautogui.hotkey("backspace")
                pyautogui.hotkey("backspace")
                pyautogui.hotkey("delete")
                pyautogui.hotkey("delete")
                pyautogui.hotkey("delete")
                pyautogui.typewrite("1")
                
                pyautogui.hotkey("enter")
                if(not is_element_present(red_box)):
                    return False
                else:
                    red_box_location = pyautogui.locateOnScreen(red_box, confidence=DEFAULT_CONFIDENCE)
                    x = red_box_location.left + PADDING 
                    y = red_box_location.top + PADDING 
                    pyautogui.click(x, y)
                    return True

             
        else:
            red_box_location = pyautogui.locateOnScreen(red_box, confidence=DEFAULT_CONFIDENCE)
            x = red_box_location.left + PADDING
            y = red_box_location.top + PADDING 
            pyautogui.click(x, y)
            return True

            
    def execute(self, test_context) -> ExecutionData:
        try:
            reason_text = self.SIGN_REASON_TEXT
            location_text = self.LOCATION_TEXT
            is_invisible = self.INVISIBLE_SIGN
            stamp_type = self.STAMP_TYPE
            
            sign_btn = os.path.join(f"{test_context.config.profiles_dir}", COMPONENTS.SIGN_BTN)
            sign_stamp_btn = os.path.join(f"{test_context.config.profiles_dir}", COMPONENTS.SIGN_STAMP_BTN)
            sign_reason_input = os.path.join(f"{test_context.config.profiles_dir}", COMPONENTS.SIGN_REASON_INPUT)
            sign_location_input = os.path.join(f"{test_context.config.profiles_dir}", COMPONENTS.SIGN_LOCATION_INPUT)
            sign_scrollbar = os.path.join(f"{test_context.config.profiles_dir}", COMPONENTS.SIGN_SCROLLBAR)
            
            error = os.path.join(f"{test_context.config.profiles_dir}", COMPONENTS.VER_CRED_ERROR)
            sign_confirm_btn = os.path.join(f"{test_context.config.profiles_dir}", COMPONENTS.SIGN_CONFIRM_BTN)
            success_btn = os.path.join(f"{test_context.config.profiles_dir}", COMPONENTS.SUCCESS_EXIT_BTN)
            
            if(is_invisible):
                invisible_checkbox = os.path.join(f"{test_context.config.profiles_dir}", COMPONENTS.SIGN_MODULE_INVISIBLE_CHECKBOX)
                if(not is_element_present(invisible_checkbox)):
                    return ExecutionData(
                        success=False,
                        error_message="No se encontró el checkbox de Firma Invisible"
                    )
                click_element(invisible_checkbox)
                
            
            if(not is_element_present(sign_btn)):
                return ExecutionData(
                    success=False,
                    error_message="No aparece el botón 'Firmar'"
                )
            click_element(sign_btn)
            if not self.INVISIBLE_SIGN:    
                if(not is_element_present(sign_reason_input) and is_element_present(local_path=error, timeout=1)):
                    pyautogui.hotkey("enter")
                    return ExecutionData(
                        success=False,
                        error_message=f"El sistema produjo una excepción al hacer click en 'Firmar'."
                    )
                
                elif(not is_element_present(sign_reason_input)):
                    return ExecutionData(
                        success=False,
                        error_message="No se abrió el modal para firmar"
                    )
                    
                
                if stamp_type == 'advanced':
                    click_element(sign_reason_input)
                    pyautogui.hotkey("tab")
                    pyautogui.hotkey("tab")
                    pyautogui.typewrite(StampTypeLabels.advanced)
                    
                if stamp_type == 'simple':
                    click_element(sign_reason_input)
                    pyautogui.hotkey("tab")
                    pyautogui.hotkey("tab")
                    pyautogui.typewrite(StampTypeLabels.simple)
                    
                if reason_text is not None:
                    click_element(sign_reason_input)
                    pyautogui.typewrite(reason_text)
                    pyautogui.hotkey("tab")
                    
                if location_text is not None:
                    click_element(sign_location_input)
                    pyautogui.typewrite(location_text)
                    pyautogui.hotkey("tab")
                
                if not self.RESIGNING:                    
                    if not self.sign_on_red_square(test_context):
                        return ExecutionData(
                            success=False,
                            error_message="No se encontró la caja ROJA para firmar en el pdf",
                            metadata={
                                "hotkey": "esc"
                            }
                        )
                else:
                    if not self.sign_on_blue_square(test_context):
                        return ExecutionData(
                            success=False,
                            error_message="No se encontró la caja AZUL para firmar en el pdf",
                            metadata={
                                "hotkey": "esc"
                            }
                        )  
                if(not is_element_present(sign_confirm_btn)):
                    return ExecutionData(
                        success=False,
                        error_message="Confirmation button never got available",
                        metadata={
                            "hotkey": "esc"
                        }
                    )
                click_element(sign_confirm_btn)
                time.sleep(DEFAULT_SHORT_DELTATIME_SECS)
                if(not is_element_present(sign_stamp_btn)):
                    return ExecutionData(
                        success=False,
                        error_message="stamp btn never got available"
                    )
                click_element(sign_stamp_btn)
                
                if is_element_present(local_path=error, timeout=1):
                    
                    return ExecutionData(
                        success=False,
                        error_message=f"El sistema produjo una excepción al hacer click en 'Estampar'.",
                        metadata={
                            "hotkey": "esc",
                            "times": 5
                        }
                    )
            if(not is_element_present(success_btn, timeout=self.SIGN_SUCCESS_TIMEOUT)):
                return ExecutionData(
                    success=False,
                    error_message="Success modal didnt get available"
                )
            return ExecutionData(
                    success=True,
                    metadata={
                        "hotkey":"esc"
                    }
                )
        except Exception as err:
            return ExecutionData(
                    success=False,
                    error_message=f"Error: {err}",
                    metadata={
                        "hotkey":"esc"
                    }
                )

class ResignDocument(SignDocument):
    RESIGNING=True
