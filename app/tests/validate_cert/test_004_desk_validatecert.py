from typing import List

from app.actions.base import BaseAction
from app.actions.ver_cred.verify_cred_in_module import VerifyCredInModule
from app.constants import CERTIFICATES, OSTypes, PathsConfig
from app.tests.base import BaseTest


class DeskValidateCertToExpire(BaseTest):
    def __init__(self, os_type: OSTypes, config: PathsConfig):
       
        super().__init__(
            code_name="004-Escritorio-Validar Certificado",
            name="Validar certificado con Certificado a punto de expirar.",
            os_type=os_type,
            config=config
        )


    def build_actions(self) -> List[BaseAction]:
        actions: List[BaseAction] = []
        cert_path =  CERTIFICATES.TO_EXPIRE_CERT
       
        actions.append(VerifyCredInModule(cert_dir=cert_path))
        return actions