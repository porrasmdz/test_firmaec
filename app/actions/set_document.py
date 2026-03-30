import os
import time

import pyautogui

from app.actions.base import BaseAction, ExecutionData
from app.constants import COMPONENTS, DEFAULT_SHORT_DELTATIME_SECS

from app.tests.base import TestContext
from app.utils import click_element, is_element_present, is_macos, open_file_in_dialog


class SetDocument(BaseAction):
    def __init__(self, src_file: str, tgt_file: str):
        super().__init__(name="Ingresar Documento en la Opción de Firma", 
                         code_name="SET_DOC_SIGN", omit_screenshot=True
                         )
        self.src_file = src_file
        self.tgt_file = tgt_file
    
    def execute(self, test_context: TestContext) -> ExecutionData:
        src_file = self.src_file 
        tgt_file = self.tgt_file 
        doc_btn = os.path.join(f"{test_context.config.profiles_dir}", COMPONENTS.DOC_BTN)
        filepath_input = os.path.join(f"{test_context.config.profiles_dir}", COMPONENTS.FILEPATH_INPUT)
        
        test_doc_path = os.path.abspath(os.path.join(f"{test_context.config.pdf_dir}", src_file))
        target_doc_path = os.path.abspath(os.path.join(f"{test_context.config.pdf_dir}", tgt_file))
        
        if(not is_element_present(doc_btn)):
            return ExecutionData(
                success=False,
                error_message="doc btn not found"
            )

        click_element(doc_btn)
        if(not is_macos() and not is_element_present(filepath_input)):
            return ExecutionData(
                success=False,
                error_message="path input not found"
            )
        if not is_macos():
            click_element(filepath_input)
        open_file_in_dialog(test_doc_path)
        time.sleep(DEFAULT_SHORT_DELTATIME_SECS)
        
        test_context.append_artifact(target_doc_path)
        return ExecutionData(
                success=True,
                metadata={
                    "src_file": test_doc_path,
                    "tgt_file": target_doc_path
                }
            )
