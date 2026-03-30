import os
import platform
import subprocess
import time
from typing import Literal

import pyautogui

from app.actions.base import BaseAction, ExecutionData
from app.actions.ver_doc.ver_doc_check_details import VerDocCheckDetails
from app.actions.ver_doc.ver_doc_set_doc import VerDocSetDocument
from app.constants import CERTS_PASSWORD, COMPONENTS, DEFAULT_SHORT_DELTATIME_SECS
from app.tests.base import TestContext
from app.utils import click_element, is_element_present


class ValidateSignedDoc(BaseAction):
    VAL_MODE: Literal["firmaec", "chrome", "safari","firefox", "acrobat"] = "firmaec"
    
    def __init__(self):
        super().__init__(name="Validar Firma de un documento firmado en prueba", 
                         code_name="VAL_SIGN")
        
        
    def execute(self, test_context: TestContext) -> ExecutionData:
        pdf_files = [
            f for f in test_context.artifacts
            if f and f.lower().endswith(".pdf")
        ]
        if not pdf_files:
            return ExecutionData(
                success=False,
                error_message="No se encontró ningún PDF firmado en esta prueba"
            )
        sample_file = pdf_files.pop()
        pdf_dir = test_context.config.pdf_dir
        relative_path = os.path.relpath(sample_file, pdf_dir)
        if self.VAL_MODE == 'firmaec':
            result = VerDocSetDocument(doc_dir=relative_path).execute(test_context=test_context)
            if result.success:
                return VerDocCheckDetails().execute(test_context=test_context)
            else:
                return result
        else:
            return self.external_validate(test_context, sample_file)
        
    def external_validate(self, test_context: TestContext, absolute_path: str) -> ExecutionData:
        test_context.log_info(f"Derivando validación a {self.VAL_MODE}")
        try:
            command = self.get_open_command(absolute_path)

            if not command:
                return ExecutionData(
                    success=False,
                    error_message=f"No hay comando definido para modo {self.VAL_MODE}"
                )

            subprocess.Popen(command)

            test_context.log_info(
                f"Validación derivada a {self.VAL_MODE}: {absolute_path}"
            )
            time.sleep(3)
            return ExecutionData(
                success=True,
                metadata={
                    "validated_file": absolute_path,
                    "validation_mode": self.VAL_MODE
                }
            )

        except Exception as err:
            return ExecutionData(
                success=False,
                error_message=f"Error abriendo archivo con {self.VAL_MODE}: {err}"
            )

    def get_open_command(self, local_abs_path: str) -> list[str] | None:
        system = platform.system()
        absolute_path=os.path.abspath(local_abs_path)
        if system == "Windows":
            commands = {
                "chrome": ["chrome", absolute_path],
                "firefox": ["firefox", absolute_path],
                "acrobat": ["Acrobat", absolute_path],
                "safari": None,  
            }

        elif system == "Darwin":  
            commands = {
                "chrome": ["open", "-a", "Google Chrome", absolute_path],
                "firefox": ["open", "-a", "Firefox", absolute_path],
                "safari": ["open", "-a", "Safari", absolute_path],
                "acrobat": ["open", "-a", "Adobe Acrobat Reader", absolute_path],
            }

        else:  # Linux
            commands = {
                "chrome": ["google-chrome", absolute_path],
                "firefox": ["firefox", absolute_path],
                "acrobat": None, 
                "safari": None,
            }

        return commands.get(self.VAL_MODE)