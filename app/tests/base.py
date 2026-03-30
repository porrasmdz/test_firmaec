from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from logging import Logger
import os
import time
from typing import Any, Dict, List, Optional

import pyautogui

from app.logger import logger
from app.actions.base import ActionResult, BaseAction
from app.constants import OSTypes, PathsConfig

@dataclass
class TestResult:
    success: bool
    test_name: str
    total_steps: int
    executed_steps: int
    failed_step: Optional[str] = None
    started_at: float = 0.0
    ended_at: float = 0.0
    duration_seconds: float = 0.0
    step_results: List[ActionResult] = field(default_factory=list)
    

class BaseTest(ABC):
    def __init__(self, code_name:str, name: str, os_type: OSTypes, config: PathsConfig):
        self.code_name = code_name
        self.name = name
        self.os_type = os_type
        self.config = config
        test_logger = logger.getLogger(code_name)
        self.logger = test_logger
        self.context = TestContext(
            code_name=code_name,
            test_name=name,
            os_type=os_type,
            config=config,
            logger=test_logger,
        )

    @abstractmethod
    def build_actions(self) -> List[BaseAction]:
        pass

    def before_test(self) -> None:
        self.context.logger.info(f"######################################################################################")
        self.context.log_info(f"Inicializando prueba: {self.name}")

    def after_test(self, result: TestResult) -> None:
        self.context.log_info(
            f"Prueba Finalizada. success={result.success}, "
            f"steps={result.executed_steps}/{result.total_steps}, "
            f"duration={result.duration_seconds:.2f}s"
        )

    def on_test_failure(self, failed_action: BaseAction, action_result: ActionResult) -> None:
        self.context.log_error(
            f"Test detenido por fallo en paso: {failed_action.name}, "
            f"Error: {action_result.error_message}, "
        )

    def run(self) -> TestResult:
        actions = self.build_actions()
        started_at = time.time()

        self.before_test()

        result = TestResult(
            success=True,
            test_name=self.name,
            total_steps=len(actions),
            executed_steps=0,
            started_at=started_at,
        )

        for action in actions:
            action_result = action.run(self.context)
            result.executed_steps += 1
            result.step_results.append(action_result)
            if not action_result.success:
                result.success = False
                result.failed_step = action.code_name
                self.on_test_failure(action, action_result)
                break

        result.ended_at = time.time()
        result.duration_seconds = result.ended_at - result.started_at

        self.after_test(result)
        return result
    

class TestContext:
    def __init__(self, code_name: str, test_name: str, os_type: OSTypes, config: PathsConfig, logger: Logger):
        self.code_name = code_name
        self.test_name = test_name
        self.os_type = os_type
        self.config = config
        self.logger = logger
        self.metadata: Dict[str, Any] = {}
        self.artifacts: List[str] = []
        self.started_at = time.time()
        self.finished_at = None

    def setMetaField(self, key: str, value: Any) -> None:
        self.metadata[key] = value

    def getMetaField(self, key: str, default: Any = None) -> Any:
        return self.metadata.get(key, default)

    def append_artifact(self, path: str) -> None:
        self.artifacts.append(path)

    def log_info(self, message: str) -> None:
        self.logger.info(f"[{self.code_name}] {message}")

    def log_error(self, message: str) -> None:
        self.logger.error(f"[{self.code_name}] {message}")

    def log_warning(self, message: str) -> None:
        self.logger.warning(f"[{self.code_name}] {message}")

    def take_screenshot(self, step_name: str) -> Optional[str]:
        try:
            screenshots_dir = self.config.screenshots_dir
            os.makedirs(screenshots_dir, exist_ok=True)

            filename = f"{self.code_name}_{self.test_name}_{step_name}_{int(time.time())}.png"
            full_path = os.path.join(screenshots_dir, filename)

            pyautogui.screenshot(full_path)
            
            self.append_artifact(full_path)
            self.log_info(f"Screenshot guardado en: {full_path}")
            return full_path
        except Exception as ex:
            self.log_error(f"No se pudo guardar screenshot: {ex}")
            return None