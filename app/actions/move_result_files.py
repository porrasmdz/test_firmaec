import os
import time

import pyautogui

from app.actions.base import BaseAction, ExecutionData
from app.constants import CERTS_PASSWORD, COMPONENTS, DEFAULT_SHORT_DELTATIME_SECS
from app.tests.base import TestContext
from app.utils import click_element, is_element_present, sanitize_filename


class MoveResultFiles(BaseAction):
    def __init__(self):
        super().__init__(name="Mover los archivos firmados a carpeta de resultados", 
                         code_name="MOV_RES_FILES", omit_screenshot=True)
        
        
    def execute(self, test_context: TestContext) -> ExecutionData:
        result_files = test_context.artifacts or []
        results_dir = test_context.config.results_dir

        IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".gif", ".webp", ".tiff"}

        os.makedirs(results_dir, exist_ok=True)

        for file_path in result_files[:]:
            try:

                if not file_path:
                    continue
                file_name = os.path.basename(file_path)
                _, ext = os.path.splitext(file_name)

                if ext.lower() in IMAGE_EXTENSIONS:
                    continue
                
                if not os.path.exists(file_path):
                    continue

                file_name = os.path.basename(file_path)
                new_filename= f"TEST-{test_context.code_name}-{test_context.test_name}-{file_name}"
                
                target_path = os.path.join(results_dir, new_filename)
                os.replace(file_path, target_path)
                test_context.artifacts.remove(file_path)
                test_context.artifacts.append(target_path)
                test_context.log_info(f"Archivo movido: {file_path} -> {target_path}")

            except Exception as e:
                test_context.log_error(f"Error moviendo archivo {file_path}: {e}")
                continue

        return ExecutionData(success=True) 
