from typing import List

from app.actions.base import BaseAction
from app.actions.ver_doc.ver_doc_check_details import VerDocCheckDetails
from app.actions.ver_doc.ver_doc_set_doc import VerDocSetDocument
from app.constants import TEST_FILES, OSTypes, PathsConfig
from app.tests.base import BaseTest


class DeskValidateDoc(BaseTest):
    def __init__(self, code_name: str, name:str, doc_path: str ,os_type: OSTypes, config: PathsConfig):
       
        super().__init__(
            code_name=code_name,
            name=name,
            os_type=os_type,
            config=config
        )
        self.doc_path = doc_path


    def build_actions(self) -> List[BaseAction]:
        actions: List[BaseAction] = []
        doc_path = self.doc_path
        
        actions.append(VerDocSetDocument(doc_dir=doc_path))
        actions.append(VerDocCheckDetails())
        return actions