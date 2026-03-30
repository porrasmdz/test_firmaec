import os
from typing import List

from app.actions.base import BaseAction
from app.actions.get_certificate import GetCertificate
from app.actions.move_result_files import MoveResultFiles
from app.actions.reset_sign_mod import ResetSignModule
from app.actions.set_document import SetDocument
from app.actions.sign_document import ResignDocument, SignDocument
from app.actions.validate_signed_doc import ValidateSignedDoc
from app.constants import DEFAULT_BATCH_SIGN_TIMEOUT, DEFAULT_CERTS_PASSWORD, OSTypes, PathsConfig
from app.tests.base import BaseTest

class InvisibleSign(SignDocument):
    INVISIBLE_SIGN= True
class AdvancedSignDoc(SignDocument):
    STAMP_TYPE="advanced"
class SimpleSignDoc(SignDocument):
    STAMP_TYPE="simple"
class QRSignDoc(SignDocument):
    STAMP_TYPE="qr"

class FullAdvancedSignDoc(SignDocument):
    SIGN_REASON_TEXT="TEST REASON"
    LOCATION_TEXT="TEST LOCATION"
    STAMP_TYPE="advanced"
class FullSimpleSignDoc(SignDocument):
    SIGN_REASON_TEXT="TEST REASON"
    LOCATION_TEXT="TEST LOCATION"
    STAMP_TYPE="simple"
class FullQRSignDoc(SignDocument):
    SIGN_REASON_TEXT="TEST REASON"
    LOCATION_TEXT="TEST LOCATION"
    STAMP_TYPE="qr"


class BatchReSignDocument(ResignDocument):
    SIGN_SUCCESS_TIMEOUT=DEFAULT_BATCH_SIGN_TIMEOUT
class BatchSignDocument(SignDocument):
    SIGN_SUCCESS_TIMEOUT=DEFAULT_BATCH_SIGN_TIMEOUT
class FullSignDocument(SignDocument):
    SIGN_REASON_TEXT="TEST REASON"
    LOCATION_TEXT="TEST LOCATION"
    STAMP_TYPE="simple"
    SIGN_SUCCESS_TIMEOUT=DEFAULT_BATCH_SIGN_TIMEOUT
    
class ChromeValidateSignedDoc(ValidateSignedDoc):
    VAL_MODE="chrome"
    
class SafariValidateSignedDoc(ValidateSignedDoc):
    VAL_MODE="safari"
class FirefoxValidateSignedDoc(ValidateSignedDoc):
    VAL_MODE="firefox"
class AcrobatValidateSignedDoc(ValidateSignedDoc):
    VAL_MODE="acrobat"

class DeskSignDoc(BaseTest):
    def __init__(self, code_name: str, name:str, 
                 cert_path: str, 
                 doc_path: str, os_type: OSTypes, 
                 config: PathsConfig,
                 cert_password: str=DEFAULT_CERTS_PASSWORD,):
       
        super().__init__(
            code_name=code_name,
            name=name,
            os_type=os_type,
            config=config
        )
        self.cert_path = cert_path
        self.cert_password = cert_password
        self.doc_path = doc_path


    def build_actions(self) -> List[BaseAction]:
        actions: List[BaseAction] = []
        doc_path = self.doc_path
        base, ext = os.path.splitext(doc_path)
        target_doc_path = f"{base}-signed{ext}"
        
        cert_path = self.cert_path
        cert_password = self.cert_password
        
        actions.append(ResetSignModule())
        actions.append(GetCertificate(cert_path, cert_password))
        actions.append(SetDocument(doc_path, target_doc_path))
        actions.append(SignDocument())
        actions.append(MoveResultFiles())
        
        return actions
    
class DeskInvisibleSignDoc(DeskSignDoc):
    def build_actions(self) -> List[BaseAction]:
        actions: List[BaseAction] = []
        doc_path = self.doc_path
        base, ext = os.path.splitext(doc_path)
        target_doc_path = f"{base}-signed{ext}"
        
        cert_path = self.cert_path
        cert_password = self.cert_password
        
        actions.append(ResetSignModule())
        actions.append(GetCertificate(cert_path, cert_password))
        actions.append(SetDocument(doc_path, target_doc_path))
        
        actions.append(InvisibleSign())
        actions.append(MoveResultFiles())
        
        return actions

class DeskReSignDocBatch(DeskSignDoc):
    def build_actions(self) -> List[BaseAction]:
        actions: List[BaseAction] = []
        doc_dir = os.path.abspath(os.path.join(self.context.config.pdf_dir, self.doc_path))
        files = os.listdir(doc_dir)
        cert_path = self.cert_path
        cert_password = self.cert_password
        actions.append(ResetSignModule())
        actions.append(GetCertificate(cert_path, cert_password))

        for file_name in files:
            file_path = os.path.join(doc_dir, file_name)
            if not os.path.isfile(file_path):
                continue 
            base, ext = os.path.splitext(file_path)
            target_doc_path = f"{base}-signed{ext}"
            actions.append(SetDocument(file_path, target_doc_path))
            
        actions.append(BatchReSignDocument())
        actions.append(MoveResultFiles())
        
        return actions


class DeskSignDocBatch(DeskSignDoc):
    def build_actions(self) -> List[BaseAction]:
        actions: List[BaseAction] = []
        doc_dir = os.path.abspath(os.path.join(self.context.config.pdf_dir, self.doc_path))
        files = os.listdir(doc_dir)
        cert_path = self.cert_path
        cert_password = self.cert_password
        actions.append(ResetSignModule())
        actions.append(GetCertificate(cert_path, cert_password))

        for file_name in files:
            file_path = os.path.join(doc_dir, file_name)
            if not os.path.isfile(file_path):
                continue 
            base, ext = os.path.splitext(file_path)
            target_doc_path = f"{base}-signed{ext}"
            actions.append(SetDocument(file_path, target_doc_path))
            
        actions.append(BatchSignDocument())
        actions.append(MoveResultFiles())
        
        return actions

class DeskFullSignDocBatch(DeskSignDoc):
    def build_actions(self) -> List[BaseAction]:
        actions: List[BaseAction] = []
        doc_dir = os.path.abspath(os.path.join(self.context.config.pdf_dir, self.doc_path))
        files = os.listdir(doc_dir)
        cert_path = self.cert_path
        cert_password = self.cert_password
        actions.append(ResetSignModule())
        actions.append(GetCertificate(cert_path, cert_password))

        for file_name in files:
            file_path = os.path.join(doc_dir, file_name)
            if not os.path.isfile(file_path):
                continue 
            base, ext = os.path.splitext(file_path)
            target_doc_path = f"{base}-signed{ext}"
            actions.append(SetDocument(file_path, target_doc_path))
            
        actions.append(FullSignDocument())
        actions.append(MoveResultFiles())
        
        return actions

class FullQRDeskSignDoc(DeskSignDoc):
    def build_actions(self) -> List[BaseAction]:
        actions: List[BaseAction] = []
        doc_path = self.doc_path
        base, ext = os.path.splitext(doc_path)
        target_doc_path = f"{base}-signed{ext}"
        
        cert_path = self.cert_path
        cert_password = self.cert_password
        
        actions.append(ResetSignModule())
        actions.append(GetCertificate(cert_path, cert_password))
        actions.append(SetDocument(doc_path, target_doc_path))
        
        actions.append(FullQRSignDoc())
        actions.append(MoveResultFiles())
        return actions


class ValidatedQRDeskSignDoc(DeskSignDoc):
    def build_actions(self):
        base_actions= super().build_actions()
        actions = [*base_actions]
        actions.append(ValidateSignedDoc())
        return actions

class ValidatedDeskAdvancedSignDoc(DeskSignDoc):
    def build_actions(self) -> List[BaseAction]:
        actions: List[BaseAction] = []
        doc_path = self.doc_path
        base, ext = os.path.splitext(doc_path)
        target_doc_path = f"{base}-signed{ext}"
        
        cert_path = self.cert_path
        cert_password = self.cert_password
        
        actions.append(ResetSignModule())
        actions.append(GetCertificate(cert_path, cert_password))
        actions.append(SetDocument(doc_path, target_doc_path))
        
        actions.append(AdvancedSignDoc())
        actions.append(MoveResultFiles())
        actions.append(ValidateSignedDoc())
        return actions
class ValidatedDeskSimpleSignDoc(DeskSignDoc):
    def build_actions(self) -> List[BaseAction]:
        actions: List[BaseAction] = []
        doc_path = self.doc_path
        base, ext = os.path.splitext(doc_path)
        target_doc_path = f"{base}-signed{ext}"
        
        cert_path = self.cert_path
        cert_password = self.cert_password
        
        actions.append(ResetSignModule())
        actions.append(GetCertificate(cert_path, cert_password))
        actions.append(SetDocument(doc_path, target_doc_path))
        
        actions.append(SimpleSignDoc())
        actions.append(MoveResultFiles())
        actions.append(ValidateSignedDoc())
        return actions

class ValidatedFullQRDeskSignDoc(DeskSignDoc):
    def build_actions(self) -> List[BaseAction]:
        actions: List[BaseAction] = []
        doc_path = self.doc_path
        base, ext = os.path.splitext(doc_path)
        target_doc_path = f"{base}-signed{ext}"
        
        cert_path = self.cert_path
        cert_password = self.cert_password
        
        actions.append(ResetSignModule())
        actions.append(GetCertificate(cert_path, cert_password))
        actions.append(SetDocument(doc_path, target_doc_path))
        
        actions.append(FullQRSignDoc())
        actions.append(MoveResultFiles())
        actions.append(ChromeValidateSignedDoc())
        actions.append(FirefoxValidateSignedDoc())
        
        actions.append(AcrobatValidateSignedDoc())
        actions.append(SafariValidateSignedDoc())
        return actions

class ValidatedDeskFullAdvancedSignDoc(DeskSignDoc):
    def build_actions(self) -> List[BaseAction]:
        actions: List[BaseAction] = []
        doc_path = self.doc_path
        base, ext = os.path.splitext(doc_path)
        target_doc_path = f"{base}-signed{ext}"
        
        cert_path = self.cert_path
        cert_password = self.cert_password
        
        actions.append(ResetSignModule())
        actions.append(GetCertificate(cert_path, cert_password))
        actions.append(SetDocument(doc_path, target_doc_path))
        
        actions.append(FullAdvancedSignDoc())
        actions.append(MoveResultFiles())       
        actions.append(ChromeValidateSignedDoc())
        actions.append(FirefoxValidateSignedDoc())
        actions.append(AcrobatValidateSignedDoc())
        actions.append(SafariValidateSignedDoc())

        return actions
    
class ValidatedDeskFullSimpleSignDoc(DeskSignDoc):
    def build_actions(self) -> List[BaseAction]:
        actions: List[BaseAction] = []
        doc_path = self.doc_path
        base, ext = os.path.splitext(doc_path)
        target_doc_path = f"{base}-signed{ext}"
        
        cert_path = self.cert_path
        cert_password = self.cert_password
        
        actions.append(ResetSignModule())
        actions.append(GetCertificate(cert_path, cert_password))
        actions.append(SetDocument(doc_path, target_doc_path))
        
        actions.append(FullSimpleSignDoc())
        actions.append(MoveResultFiles())
        actions.append(ChromeValidateSignedDoc())
        actions.append(FirefoxValidateSignedDoc())
        actions.append(AcrobatValidateSignedDoc())
        actions.append(SafariValidateSignedDoc())
        return actions


