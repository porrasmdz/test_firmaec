import os
import time

import pyautogui

from app.actions.base import BaseAction, ExecutionData
from app.constants import COMPONENTS, DEFAULT_CERTS_PASSWORD, DEFAULT_SHORT_DELTATIME_SECS
from app.tests.base import TestContext
from app.utils import click_element, is_element_present, is_macos, open_file_in_dialog


class VerDocSetDocument(BaseAction):
    def __init__(self, doc_dir: str):
        super().__init__(name="Verifica documento en Módulo Validar Documento", 
                         code_name="VER_DOC_MOD")
        self.doc_dir = doc_dir
        
    def execute(self, test_context: TestContext) -> ExecutionData:
        success = False
        # pyautogui.hotkey("enter")
        ver_doc_mod = os.path.join(f"{test_context.config.profiles_dir}", COMPONENTS.VERIFY_DOC_MODULE)
        
        doc_btn = os.path.join(f"{test_context.config.profiles_dir}", COMPONENTS.VER_DOC_DOC_BTN)
        filepath_input = os.path.join(f"{test_context.config.profiles_dir}", COMPONENTS.FILEPATH_INPUT)
        
        
        verify_btn = os.path.join(f"{test_context.config.profiles_dir}", COMPONENTS.VER_DOC_VERIFY_BTN)
        reset_btn = os.path.join(f"{test_context.config.profiles_dir}", COMPONENTS.VER_CRED_RESET_BTN)
        
        if(not is_element_present(ver_doc_mod)):
            return ExecutionData(
                success=False,
                error_message="Couldnt find verify document module"
            )
        click_element(ver_doc_mod)
        
        if(not is_element_present(reset_btn)):
            return ExecutionData(
                success=False,
                error_message="'Restablecer' btn not found"
            )
        click_element(reset_btn)
        
        path = os.path.join(f"{test_context.config.pdf_dir}", self.doc_dir)
        valid_doc_path = os.path.abspath(path)
        
        if(not os.path.exists(valid_doc_path)):
            return ExecutionData(
                success=False,
                error_message=f"Nonexistent Path provided: {valid_doc_path}"
            )
        
        
        if(not is_element_present(doc_btn)):
            return ExecutionData(
                success=False,
                error_message="'Buscar Documento' btn not found"
            )
        click_element(doc_btn)
        
        if(not is_macos() and not is_element_present(filepath_input)):
            return ExecutionData(
                success=False,
                error_message="File chooser input not found"
            )
        if not is_macos():
            click_element(filepath_input)

        open_file_in_dialog(valid_doc_path)
        time.sleep(DEFAULT_SHORT_DELTATIME_SECS)
                
        if(not is_element_present(verify_btn)):
            return ExecutionData(
                success=False,
                error_message="'Verificar' btn not found"
            )
        click_element(verify_btn)
 
        result_detail_btn = os.path.join(f"{test_context.config.profiles_dir}", COMPONENTS.VER_DOC_DETAIL_BTN)
        error = os.path.join(f"{test_context.config.profiles_dir}", COMPONENTS.VER_CRED_ERROR)
        if(not is_element_present(result_detail_btn) and is_element_present(local_path=error, timeout=1)):
            return ExecutionData(
                success=False,
                error_message=f"El sistema produjo una excepción al verificar documento.",
                metadata={
                    "hotkey": "enter"
                }
            )
        elif(not is_element_present(result_detail_btn) and not is_element_present(error)):
            return ExecutionData(
                success=False,
                error_message="Resultados no aparecieron al hacer click en verificar",
            )

        else:
            success = True
            
       
        if success:
            return ExecutionData(
                    success=True,
                    
            )

        else:
            return ExecutionData(
                    success=False,
                    error_message="Execution Timeout",
            )
