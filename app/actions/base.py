
from abc import ABC, abstractmethod
from dataclasses import asdict, dataclass, field
import time
from typing import Any, Dict, Optional

import pyautogui

from app.constants import DEFAULT_SHORT_DELTATIME_SECS, OSTypes
from app.utils import press_enter, press_escape

@dataclass
class ActionResult:
    name: str
    os: OSTypes
    success: bool = False
    error_message: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
@dataclass
class ExecutionData:
    success: bool
    error_message: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = field(default_factory=dict)
    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)



class BaseAction(ABC):
    def __init__(
        self,
        code_name: str,
        name: str,
        omit_screenshot=False
    ) -> None:
        self.name = name
        self.code_name = code_name
        self.success = False
        self.omit_screenshot = omit_screenshot
        
    @abstractmethod
    def execute(self, test_context) -> ExecutionData:
        """
        Lógica de cada acción.
        Puede devolver info adicional como screenshot y si resolvio con exito o no.
        Ejemplo:
        {
            "success": True,
        }
        """
        raise NotImplementedError

    def before_execute(self) -> None:
        """Hook opcional antes de correr la prueba."""
        pass
    def after_execute(self, result: ActionResult) -> None:
        """Hook opcional después de correr la prueba."""
        pass

    def run(self, test_context) -> ActionResult:
        result = ActionResult(
            name=self.name,
            os=test_context.os_type,
            success=self.success,
        )
        try:
            self.before_execute()

            execution_data = self.execute(test_context) or {}

            result.success = execution_data.success
            result.error_message = execution_data.error_message
            result.metadata = execution_data.metadata
            
        except Exception as e:
            result.success = False
            result.error_message = str(e)
            result.metadata = execution_data.metadata

        finally:
            self.after_execute(result)
            if not self.omit_screenshot or (self.omit_screenshot and result.success == False):
                test_context.take_screenshot(self.code_name)
            repetitions = 1
            if result.metadata.get("hotkey", "") != "" and result.metadata.get("times",0) != 0:
                repetitions = result.metadata.get("times")
            
            if result.metadata.get("hotkey", "") == "esc":
                for i in range(repetitions):
                    press_escape()
            
            if result.metadata.get("hotkey", "") == "enter":
                for i in range(repetitions):
                    press_enter()
            test_context.metadata = {
                **(test_context.metadata or {}),
                **(result.metadata or {})
            }    
        return result
