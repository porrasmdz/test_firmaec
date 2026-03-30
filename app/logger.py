from datetime import datetime
import logging as logger
import os

fecha = datetime.now().strftime("%d%m%Y_%H%M%S")
log_filename = os.path.join("logs", f"{fecha}_execution.log")

logger.basicConfig(
    level=logger.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logger.StreamHandler(),                 
        logger.FileHandler(log_filename, encoding="utf-8")
    ]
)

