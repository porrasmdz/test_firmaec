import os
import time

import pyautogui

from app.actions.base import BaseAction, ExecutionData
from app.constants import CERTS_PASSWORD, COMPONENTS, DEFAULT_SHORT_DELTATIME_SECS
from app.utils import click_element, is_element_present, is_macos, open_file_in_dialog


class GetCertificate(BaseAction):
    def __init__(self, cert_dir: str, cert_pass: str=CERTS_PASSWORD):
        super().__init__(name="Ingresar Certificado en la Opción de Firma", 
                         code_name="GET_CERT_SIGN", omit_screenshot=True)
        self.cert_dir = cert_dir
        self.cert_pass = cert_pass
        
    def execute(self, test_context) -> ExecutionData:
        file_btn = os.path.join(f"{test_context.config.profiles_dir}", COMPONENTS.FILE_BTN)
        cert_btn = os.path.join(f"{test_context.config.profiles_dir}", COMPONENTS.CERT_UP_BTN)
        cert_pass_input = os.path.join(f"{test_context.config.profiles_dir}", COMPONENTS.CERT_PASS_INPUT)
        filepath_input = os.path.join(f"{test_context.config.profiles_dir}", COMPONENTS.FILEPATH_INPUT)
        
        valid_cert_path = os.path.abspath(os.path.join(f"{test_context.config.certificates_dir}", self.cert_dir))
        
        if(not is_element_present(file_btn) or not is_element_present(cert_btn)):
            return ExecutionData(
                success=False,
                error_message="file btn or cert btn not found"
            )

        click_element(file_btn)
        click_element(cert_btn)
        if(not is_macos() and not is_element_present(filepath_input)):
            return ExecutionData(
                success=False,
                error_message="path input not found"
            )
        if not is_macos():
            click_element(filepath_input)
        open_file_in_dialog(valid_cert_path)
        time.sleep(DEFAULT_SHORT_DELTATIME_SECS)
        
        click_element(cert_pass_input)
        pyautogui.typewrite(self.cert_pass) 
        return ExecutionData(
                success=True,
            )
