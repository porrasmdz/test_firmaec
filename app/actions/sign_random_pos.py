import os
import random
import time

import pyautogui

from app.actions.base import BaseAction, ExecutionData
from app.constants import COMPONENTS, DEFAULT_SHORT_DELTATIME_SECS, DEFAULT_CONFIDENCE
from app.utils import click_element, is_element_present


class SignDocumentRandomPosition(BaseAction):
    def __init__(self):
        super().__init__(name="Firmar Aleatoriamente en Espacio Blanco", 
                         code_name="SIGN_RANDOM",
                        )
        
        
    def get_test_blank_space(self, test_context ,right_offset=400, padding_x=30,padding_y=30):
        upperhalf_stamp_bx = os.path.join(f"{test_context.config.profiles_dir}", COMPONENTS.STAMP_BOX_UPP_HALF)
        lowerhalf_stamp_bx = os.path.join(f"{test_context.config.profiles_dir}", COMPONENTS.STAMP_BOX_LOW_HALF)
        if(not is_element_present(upperhalf_stamp_bx) or not is_element_present(lowerhalf_stamp_bx) ):
            return None
        
        top_loc = pyautogui.locateCenterOnScreen(upperhalf_stamp_bx, confidence=DEFAULT_CONFIDENCE)
        bot_loc = pyautogui.locateCenterOnScreen(lowerhalf_stamp_bx, confidence=DEFAULT_CONFIDENCE)
        
        center_x = top_loc.x
        top_y = top_loc.y
        bottom_y = bot_loc.y

        if bottom_y <= top_y:
            raise ValueError("El delimitador inferior está por encima del superior")

        left = center_x - padding_x
        right = center_x + right_offset - padding_x
        top = top_y + padding_y
        bottom = bottom_y - padding_y

        width = right - left
        height = bottom - top

        if width <= 0 or height <= 0:
            raise ValueError("La región calculada no es válida")

        return {
            "left": left,
            "top": top,
            "width": width,
            "height": height,
            "right": right,
            "bottom": bottom,
        }

    def sign_on_random_blank_space(self, test_context):
        stamp_box = self.get_test_blank_space(test_context=test_context)
        x = random.randint(stamp_box["left"], stamp_box["right"])
        y = random.randint(stamp_box["top"], stamp_box["bottom"])
        pyautogui.click(x, y)

    def execute(self, test_context) -> ExecutionData:
        try:
            reason_text = None
            location_text = None
            
            sign_btn = os.path.join(f"{test_context.config.profiles_dir}", COMPONENTS.SIGN_BTN)
            sign_stamp_btn = os.path.join(f"{test_context.config.profiles_dir}", COMPONENTS.SIGN_STAMP_BTN)
            sign_reason_input = os.path.join(f"{test_context.config.profiles_dir}", COMPONENTS.SIGN_REASON_INPUT)
            sign_location_input = os.path.join(f"{test_context.config.profiles_dir}", COMPONENTS.SIGN_LOCATION_INPUT)
            sign_scrollbar = os.path.join(f"{test_context.config.profiles_dir}", COMPONENTS.SIGN_SCROLLBAR)
            
            sign_confirm_btn = os.path.join(f"{test_context.config.profiles_dir}", COMPONENTS.SIGN_CONFIRM_BTN)
            success_btn = os.path.join(f"{test_context.config.profiles_dir}", COMPONENTS.SUCCESS_EXIT_BTN)
            
            if(not is_element_present(sign_btn)):
                return ExecutionData(
                    success=False,
                    error_message="Stamp button never got available"
                )
            click_element(sign_btn)
            
            if(not is_element_present(sign_reason_input) or not is_element_present(sign_location_input)):
                return ExecutionData(
                    success=False,
                    error_message="Stamp modal did not open"
                )
            if reason_text is not None:
                click_element(sign_reason_input)
                pyautogui.typewrite(sign_reason_input)
                pyautogui.hotkey("tab")
                
            if location_text is not None:
                click_element(sign_location_input)
                pyautogui.typewrite(sign_location_input)
                pyautogui.hotkey("tab")
            self.sign_on_random_blank_space(test_context)
            
            
            if(not is_element_present(sign_confirm_btn)):
                return ExecutionData(
                    success=False,
                    error_message="Confirmation button never got available"
                )
            click_element(sign_confirm_btn)
            time.sleep(DEFAULT_SHORT_DELTATIME_SECS)
            if(not is_element_present(sign_stamp_btn)):
                return ExecutionData(
                    success=False,
                    error_message="stamp btn never got available"
                )
            click_element(sign_stamp_btn)
            
            if(not is_element_present(success_btn)):
                return ExecutionData(
                    success=False,
                    error_message="Success modal didnt get available"
                )
            click_element(success_btn)
            
            return ExecutionData(
                    success=True,
                )
        except Exception as err:
            return ExecutionData(
                    success=False,
                    error_message=f"Error: {err}"
                )
