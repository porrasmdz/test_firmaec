from typing import List

from app.actions.base import BaseAction
from app.actions.ver_cred.verify_cred_in_module import VerifyCredInModule
from app.constants import CERTIFICATES, REVOKED_CERT_PASSWORD, OSTypes, PathsConfig
from app.tests.base import BaseTest


class DeskValidateCertRevoked(BaseTest):
    def __init__(self, os_type: OSTypes, config: PathsConfig):
       
        super().__init__(
            code_name="002-Escritorio-Validar Certificado",
            name="Validar certificado con Certificado revocado",
            os_type=os_type,
            config=config
        )


    def build_actions(self) -> List[BaseAction]:
        actions: List[BaseAction] = []
        cert_path =  CERTIFICATES.REVOKED_CERT
        cert_pass = REVOKED_CERT_PASSWORD
        actions.append(VerifyCredInModule(cert_dir=cert_path, cert_password=cert_pass))
        return actions