import os
import time

import pyautogui

from app.actions.base import BaseAction, ExecutionData
from app.constants import APP_NAME, CERTS_PASSWORD, COMPONENTS, DEFAULT_SHORT_DELTATIME_SECS
from app.utils import click_element, focus_app, is_element_present, press_escape


class ResetSignModule(BaseAction):
    def __init__(self):
        super().__init__(name="Restablecer el Módulo de Firmar al Estado Inicial", 
                         code_name="RESET_SIGN_MOD", omit_screenshot=True)
        
    def execute(self, test_context) -> ExecutionData:
        if focus_app(APP_NAME):
            test_context.log_info("Enfocando App")
        else:
            test_context.log_error("No se pudo enfocar la App FirmaEC")
            
        press_escape()
        sign_mod_btn = os.path.join(f"{test_context.config.profiles_dir}", COMPONENTS.SIGN_MODULE)
        restablish_btn = os.path.join(f"{test_context.config.profiles_dir}", COMPONENTS.SIGN_MODULE_RESET_BUTTON)
        
        if(not is_element_present(sign_mod_btn)):
            return ExecutionData(
                success=False,
                error_message="No se pudo abrir el módulo de Firmar Documento"
            )

        click_element(sign_mod_btn)
        
        if(not is_element_present(restablish_btn)):
            return ExecutionData(
                success=False,
                error_message="No se pudo encontrar el botón Restablecer"
            )

        click_element(restablish_btn)
        return ExecutionData(
            success=True,
        )
