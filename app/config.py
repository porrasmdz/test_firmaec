
import os

from app.constants import DEFAULT_FIRMA_APP_PATH, DEFAULT_MAC_FIRMA_APP_PATH, OSTypes, PathsConfig


class TestsConfig:
    def __init__(self, os_type: OSTypes):
        self.os_type = os_type
        
    def get_config_map(self) -> PathsConfig:
        pdf_dir=os.path.join("pdf_files","original")
        if self.os_type == "win64":
            certificates_path = "certificates"
            return PathsConfig(
                app_path=DEFAULT_FIRMA_APP_PATH,
                profiles_dir="profiles/win64",
                screenshots_dir="screenshots/win64",
                pdf_dir=pdf_dir,
                results_dir="results/win64",
                certificates_dir=certificates_path
            )
        if self.os_type == "win32":    
            certificates_path = "certificates"
            return PathsConfig(
                app_path=DEFAULT_FIRMA_APP_PATH,
                profiles_dir="profiles/win32",
                screenshots_dir="screenshots/win32",
                pdf_dir=pdf_dir,
                results_dir="results/win32",
                certificates_dir=certificates_path
            )
        if self.os_type == OSTypes.MAC:
            profiles_dir = "profiles/macos" if os.path.isdir("profiles/macos") else "profiles/win64"
            return PathsConfig(
                app_path=os.environ.get("FIRMAEC_APP_PATH", DEFAULT_MAC_FIRMA_APP_PATH),
                profiles_dir=profiles_dir,
                screenshots_dir="screenshots/macos",
                pdf_dir=pdf_dir,
                results_dir="results/macos",
                certificates_dir="certificates"
            )
        raise ValueError(f"Unsupported os_type: {self.os_type}")
