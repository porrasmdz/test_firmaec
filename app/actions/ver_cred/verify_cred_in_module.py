import os
import time

import pyautogui

from app.actions.base import BaseAction, ExecutionData
from app.constants import COMPONENTS, DEFAULT_CERTS_PASSWORD, DEFAULT_SHORT_DELTATIME_SECS
from app.tests.base import TestContext
from app.utils import click_element, is_element_present, is_macos, open_file_in_dialog, press_enter


class VerifyCredInModule(BaseAction):
    def __init__(self, cert_dir: str, cert_password: str=DEFAULT_CERTS_PASSWORD):
        super().__init__(name="Verifica Credencial en Módulo Validar Credencial", 
                         code_name="VER_CRED_MOD")
        self.cert_dir = cert_dir
        self.cert_password= cert_password
        
    def execute(self, test_context: TestContext) -> ExecutionData:
        success = False
        ver_cred_mod = os.path.join(f"{test_context.config.profiles_dir}", COMPONENTS.VERIFY_CRED_MODULE)
        file_btn = os.path.join(f"{test_context.config.profiles_dir}", COMPONENTS.FILE_BTN)
        cert_btn = os.path.join(f"{test_context.config.profiles_dir}", COMPONENTS.VER_CRED_CRED_BTN)
        filepath_input = os.path.join(f"{test_context.config.profiles_dir}", COMPONENTS.FILEPATH_INPUT)
        cert_pass_input = os.path.join(f"{test_context.config.profiles_dir}", COMPONENTS.VER_CRED_PASS_INPUT)
        
        
        validate_btn = os.path.join(f"{test_context.config.profiles_dir}", COMPONENTS.VER_CRED_VALIDATE_BTN)
        reset_btn = os.path.join(f"{test_context.config.profiles_dir}", COMPONENTS.VER_CRED_RESET_BTN)
        
        if(not is_element_present(ver_cred_mod)):
            return ExecutionData(
                success=False,
                error_message="Couldnt find verify credential module"
            )

        click_element(ver_cred_mod)
        
        if(not is_element_present(reset_btn)):
            return ExecutionData(
                success=False,
                error_message="'Restablecer' btn not found"
            )
        click_element(reset_btn)
        
        path = os.path.join(f"{test_context.config.certificates_dir}", self.cert_dir)
        valid_cert_path = os.path.abspath(path)
        
        if(not os.path.exists(valid_cert_path)):
            return ExecutionData(
                success=False,
                error_message=f"Nonexistent Path provided: {valid_cert_path}"
            )
        
        
        if(not is_element_present(file_btn) or not is_element_present(cert_btn)):
            return ExecutionData(
                success=False,
                error_message="'Archivo' btn or 'Certificado' btn not found"
            )

        click_element(file_btn)
        click_element(cert_btn)
        if(not is_macos() and not is_element_present(filepath_input)):
            return ExecutionData(
                success=False,
                error_message="File chooser input not found"
            )
        if not is_macos():
            click_element(filepath_input)
        open_file_in_dialog(valid_cert_path)
        time.sleep(DEFAULT_SHORT_DELTATIME_SECS)
        
        if(not is_element_present(cert_pass_input)):
            return ExecutionData(
                success=False,
                error_message="Password field not found"
            )

        click_element(cert_pass_input)
        pyautogui.typewrite(self.cert_password) 
        
        if(not is_element_present(validate_btn)):
            return ExecutionData(
                success=False,
                error_message="'Validar' btn not found"
            )
        click_element(validate_btn)
 
        results = os.path.join(f"{test_context.config.profiles_dir}", COMPONENTS.VER_CRED_RESULT)
        error = os.path.join(f"{test_context.config.profiles_dir}", COMPONENTS.VER_CRED_ERROR)
        if(not is_element_present(results) and is_element_present(local_path=error, timeout=1)):
            
            press_enter()
            return ExecutionData(
                success=False,
                error_message=f"El sistema produjo una excepción al validar certificado."
            )
        elif(not is_element_present(results) and not is_element_present(error)):
            return ExecutionData(
                success=False,
                error_message="Resultados no aparecieron al validar certificado"
            )

        else:
            success = True
            
       
        if success:
            return ExecutionData(
                    success=True
            )

        else:
            return ExecutionData(
                    success=False,
                    error_message="Execution Timeout"
            )
