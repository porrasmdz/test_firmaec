import os
import time

import pyautogui

from app.actions.base import BaseAction, ExecutionData
from app.constants import COMPONENTS, DEFAULT_SHORT_DELTATIME_SECS, LAUNCH_APP_TIMEOUT_SECS
from app.tests.base import TestContext
from app.utils import click_element, is_element_present


class VerDocCheckDetails(BaseAction):
    def __init__(self):
        super().__init__(name="Verifica los detalles de los documentos validados", 
                         code_name="VER_DOC_DETAILS")
        
    def execute(self, test_context: TestContext) -> ExecutionData:
        success = False
        
        result_detail_btn = os.path.join(f"{test_context.config.profiles_dir}", COMPONENTS.VER_DOC_DETAIL_BTN)
        results_box = os.path.join(f"{test_context.config.profiles_dir}", COMPONENTS.VER_DOC_DETAILS_LABEL)

        error = os.path.join(f"{test_context.config.profiles_dir}", COMPONENTS.VER_CRED_ERROR)


        if(is_element_present(local_path=error, timeout=1)):
            # pyautogui.hotkey("enter")
            return ExecutionData(
                success=False,
                error_message=f"El sistema produjo una excepción al verificar documento.",
                metadata={
                    "hotkey": "enter"
                }
            )
        
        
        if(not is_element_present(result_detail_btn)):
            return ExecutionData(
                success=False,
                error_message="'Detalles' btn not found"
            )
        click_element(result_detail_btn)
            
        error = os.path.join(f"{test_context.config.profiles_dir}", COMPONENTS.VER_CRED_ERROR)
        if(not is_element_present(results_box) and is_element_present(local_path=error)):
            # pyautogui.hotkey("enter")
            return ExecutionData(
                success=False,
                error_message=f"El sistema produjo una excepción al abrir los detalles del documento.",
                metadata={
                    "hotkey": "enter"
                }
            )
            
        elif(not is_element_present(results_box) and not is_element_present(error)):
            return ExecutionData(
                success=False,
                error_message=f"Resultados no aparecieron al hacer click en 'Detalles' despues de {LAUNCH_APP_TIMEOUT_SECS} segundos"
            )

        else:
            success = True
            
       
        if success:
            return ExecutionData(
                    success=True,
                    metadata={
                        "hotkey": "enter"
                    }
            )

        else:
            return ExecutionData(
                    success=False,
                    error_message="Execution Timeout",
                    metadata={
                        "hotkey": "enter"
                    }
            )
