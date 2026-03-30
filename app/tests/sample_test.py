import os
from typing import List

from app.actions.base import BaseAction
from app.actions.get_certificate import GetCertificate
from app.actions.set_document import SetDocument
from app.actions.sign_document import SignDocument
from app.constants import CERTIFICATES, TEST_FILES, OSTypes, PathsConfig
from app.tests.base import BaseTest


class ExampleTest(BaseTest):
    def __init__(self, os_type: OSTypes, config: PathsConfig):
       
        super().__init__(
            code_name="TEST_000-Example",
            name="Prueba de ejemplo",
            os_type=os_type,
            config=config
        )


    def build_actions(self) -> List[BaseAction]:
        actions: List[BaseAction] = []
        cert_path =  CERTIFICATES.VALID_CERT
        src_file= TEST_FILES.TEST
        tgt_file= f"{TEST_FILES.TEST.replace('.pdf','')}-signed.pdf"
        actions.append(GetCertificate(cert_dir=cert_path))
        actions.append(SetDocument(src_file=src_file,tgt_file=tgt_file))
        actions.append(SignDocument())
        return actions