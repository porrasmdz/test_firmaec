
    
from dataclasses import dataclass
from enum import Enum
import os
TESTED_APP_VERSION="FirmaEC 5.0.0-BETA-6"
APP_NAME="FirmaEC 5.0.0-BETA-6"
DEFAULT_TARGET_BOX_PADDING=20
DEFAULT_FIRMA_APP_PATH = "C:\\Program Files\\FirmaEC\\firmador.exe"
DEFAULT_MAC_FIRMA_APP_PATH = "/Applications/FirmaEC.app"
LAUNCH_APP_TIMEOUT_SECS=10
DEFAULT_CONFIDENCE=0.8
DEFAULT_SHORT_DELTATIME_SECS=1
DEFAULT_BATCH_SIGN_TIMEOUT=120
DEFAULT_INSTANT_DELTATIME_SECS=0.05
CERTS_PASSWORD="Contrasenia123*"
DEFAULT_CERTS_PASSWORD="Contrasenia123*"
REVOKED_CERT_PASSWORD="5RpnEU4m"
EXPIRED_REVOKED_CERT_PASSWORD="66raYU7P"


class StampTypeLabels(str, Enum):
    qr = "qr"
    advanced = "avanzada"
    simple = "simple"

class OSTypes(str, Enum):
    WIN64 = "win64"
    WIN32 = "win32"
    MAC = "macos"

@dataclass
class PathsConfig:
    app_path: str
    profiles_dir: str
    pdf_dir: str
    results_dir: str
    screenshots_dir: str
    certificates_dir: str

class CERTIFICATES(str, Enum):
    EXPIRED_CERT = "expired.p12"
    REVOKED_CERT = "revoked.p12"
    EXPIRED_REVOKED_CERT = "expired_revoked.p12"
    TO_EXPIRE_CERT = "to_expire.p12"
    VALID_CERT = "valid.p12"
    AUTOGEN_CERT = "autogen.p12"
    EXTENSE_NAME_CERT = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.p12"
    DEEP_NESTED_CERT = os.path.join("nested",
                                    *[str(i) for i in range(1, 21)]
                                    ,"valid.p12")
class COMPONENTS(str, Enum):
    FILE_BTN = "archivo_btn.png"
    DOC_BTN = "doc_upload_btn.png"
    SIGN_BTN = "sign_btn.png"
    SIGN_STAMP_BTN = "sign_stamp_btn.png"
    SIGN_CONFIRM_BTN = "sign_accept_btn.png"
    SUCCESS_EXIT_BTN = "success_exit_btn.png"
    
    CERT_PASS_INPUT = "cert_pass_input.png"
    CERT_UP_BTN = "certificate_upload_btn.png"
    FILEPATH_INPUT = "file_path_input.png"
    SIGN_REASON_INPUT = "sign_reason_input.png"
    SIGN_LOCATION_INPUT = "sign_location_input.png"
    
    SIGN_SCROLLBAR = "scroll_bar.png"
    
    STAMP_BOX_UPP_HALF = "stamp_box_upp_half.png"
    STAMP_BOX_LOW_HALF = "stamp_box_lower_half.png"
    BLANK_STAMP_BOX = "blank_stamp_box.png"
    
    SIGN_MODULE = "sign_module.png"
    VERIFY_CRED_MODULE = "ver_cred_module.png"
    VERIFY_DOC_MODULE = "ver_doc_module.png"
    
    
    SIGN_MODULE_RESET_BUTTON = "sign_mod_reset_btn.png"
    SIGN_TARGET_BOX = "sign_target_box.png"
    RESIGN_TARGET_BOX = "resign_target_box.png"
    SIGN_MODULE_INVISIBLE_CHECKBOX = "sign_mod_invi_checkbox.png"
    
    VER_CRED_CRED_BTN = "ver_cred_cred_btn.png"
    VER_CRED_PASS_INPUT = "ver_cred_password_field.png"
    VER_CRED_VALIDATE_BTN = "ver_cred_validate_btn.png"
    VER_CRED_RESET_BTN = "ver_cred_reset_btn.png"
    VER_CRED_RESULT = "ver_cred_result_labels.png"
    VER_CRED_ERROR = "ver_cred_error_icon.png"
    
    VER_DOC_DOC_BTN = "ver_doc_doc_btn.png"
    VER_DOC_VERIFY_BTN = "ver_doc_verify_btn.png"
    VER_DOC_DETAIL_BTN = "ver_doc_detail_btn.png"
    VER_DOC_DETAILS_LABEL = "ver_doc_details_label.png"
    
    
    

class TEST_FILES(str, Enum):
    DIR_RESULTS = "desk_results"
 
    TEST = "test.pdf"
    VD_001 = os.path.join("ver_docs","V001_test-toexpire.pdf")
    VD_002 = os.path.join("ver_docs","V002_test_valid.pdf")
    VD_003 = os.path.join("ver_docs","V003_test_autogen.pdf")
    VD_004 = os.path.join("ver_docs","V004_test_extense.pdf")
    VD_005 = os.path.join("ver_docs","V005_test_nested.pdf")
    VD_006 = os.path.join("ver_docs","V006_test.pdf")
    
    VD_036 = "V036-test-qr.pdf"
    VD_037 = "V037-test-advanced.pdf"
    VD_038 = "V038-test-simple.pdf"
    VD_039 = "V039-test-fullqr.pdf"
    VD_040 = "V040-test-fulladvanced.pdf"
    VD_041 = "V041-test-fullsimple.pdf"
    VD_042 = "V042-test-fullresigned.pdf"
    VDIR_043 = ""
    VD_044 = "V044-test-date_changed.pdf"
    
    
    DOC_000 = "000-test.pdf"
    DOC_001 = "001-test-0kbs.pdf"
    DOC_002 = "002-test-20.pdf"
    DOC_003 = "003-test-40.pdf"
    DOC_004 = "004-test-60.pdf"
    DOC_005 = "005-test.pnf"
    DOC_006 = "006-corrupted.pdf"
    DOC_007 = "007-test.jpg"
    DOC_008 = "008-test.png"
    DOC_009 = "009-test.jpeg"
    DOC_010 = "010-test-jpg.pdf"
    DOC_011 = "011-test-png.pdf"
    DOC_012 = "012-test-jpeg.pdf"
    DOC_013 = "013-test-bmp.pdf"
    DOC_014 = "014-test-tif.pdf"
    DOC_015 = "015-aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.pdf"
    DOC_016 = "016-archivo_[prueba]\{validación\}(test)+=;,_-ñáéíóú@#$%^&!.pdf"
    DOC_017 = "017-test-ods.pdf"
    DOC_018 = "018-test-odt.pdf"
    DOC_01801 = "01801-test-scan.pdf"
    DOC_01802 = "01802-protected.pdf"
    DOC_019 = "019-test-wrd2013.pdf"
    DOC_020 = "020-test-officenew.pdf"
    DOC_021 = "021-test-horizontal.pdf"
    DOC_022 = "020-test-officenew.pdf" #VERTICAL
    DOC_023 = "023-test-horverpdf.pdf"
    DOC_024 = "024-test-a5.pdf"
    DOC_025 = "025-test-signededited.pdf"
    DOC_026 = "026-test-exe.pdf"
    DOC_027 = "027-test.PDF"
    DOC_028 = "028-test-signedextern.pdf"
    DOC_029 = "029-test-autogen.pdf"
    DOC_030 = "030-test-mac.pdf"
    DOC_031 = "031-test.xml"
    DOC_032 = "032-test-1gb.pdf"
    DOC_033 = "033-test-1_5gbs.pdf"
    
    DIR_034 = "034-batch"
    DIR_035 = "035-batch"
    
    DOC_042 = "042-test-fullresign.pdf"
    
