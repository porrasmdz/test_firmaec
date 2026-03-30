


from app.constants import CERTIFICATES, DEFAULT_CERTS_PASSWORD, EXPIRED_REVOKED_CERT_PASSWORD, REVOKED_CERT_PASSWORD, TEST_FILES, OSTypes
from app.tests.sign_doc.test_AAA_desk_sign import DeskFullSignDocBatch, DeskInvisibleSignDoc, DeskReSignDocBatch, DeskSignDoc, DeskSignDocBatch, FullQRDeskSignDoc, ValidatedDeskAdvancedSignDoc, ValidatedDeskFullAdvancedSignDoc, ValidatedDeskFullSimpleSignDoc, ValidatedDeskSimpleSignDoc, ValidatedFullQRDeskSignDoc, ValidatedQRDeskSignDoc


class Test001(DeskSignDoc): 
    def __init__(self, os_type: OSTypes, config):
        super().__init__(
            code_name="001", 
            name="Firmar con Certificado expirado", 
            cert_path=CERTIFICATES.EXPIRED_CERT,
            cert_password=DEFAULT_CERTS_PASSWORD, 
            doc_path=TEST_FILES.DOC_000, 
            os_type=os_type, config=config)
        
class Test002(DeskSignDoc): 
    def __init__(self, os_type: OSTypes, config):
        super().__init__(
            code_name="002", 
            name="Firmar con Certificado revocado.", 
            cert_path=CERTIFICATES.REVOKED_CERT,
            cert_password=REVOKED_CERT_PASSWORD, 
            doc_path=TEST_FILES.DOC_000, 
            os_type=os_type, config=config)

class Test003(DeskSignDoc): 
    def __init__(self, os_type: OSTypes, config):
        super().__init__(
            code_name="003", 
            name="Firmar con Certificado caducado y revocado", 
            cert_path=CERTIFICATES.EXPIRED_REVOKED_CERT,
            cert_password=EXPIRED_REVOKED_CERT_PASSWORD, 
            doc_path=TEST_FILES.DOC_000, 
            os_type=os_type, config=config)
class Test004(DeskSignDoc): 
    def __init__(self, os_type: OSTypes, config):
        super().__init__(
            code_name="004", 
            name="Firmar con Certificado a punto de expirar.", 
            cert_path=CERTIFICATES.TO_EXPIRE_CERT,
            cert_password=DEFAULT_CERTS_PASSWORD, 
            doc_path=TEST_FILES.DOC_000, 
            os_type=os_type, config=config)
class Test005(DeskSignDoc): 
    def __init__(self, os_type: OSTypes, config):
        super().__init__(
            code_name="005", 
            name="Firmar con Certificado vigente..", 
            cert_path=CERTIFICATES.VALID_CERT,
            cert_password=DEFAULT_CERTS_PASSWORD, 
            doc_path=TEST_FILES.DOC_000, 
            os_type=os_type, config=config)
        
class Test006(DeskSignDoc): 
    def __init__(self, os_type: OSTypes, config):
        super().__init__(
            code_name="006", 
            name="Firmar con Certificado autogenerado.", 
            cert_path=CERTIFICATES.AUTOGEN_CERT,
            cert_password=DEFAULT_CERTS_PASSWORD, 
            doc_path=TEST_FILES.DOC_000, 
            os_type=os_type, config=config)
class Test007(DeskSignDoc): 
    def __init__(self, os_type: OSTypes, config):
        super().__init__(
            code_name="007", 
            name="Firmar con Certificado con nombre extenso.", 
            cert_path=CERTIFICATES.EXTENSE_NAME_CERT,
            cert_password=DEFAULT_CERTS_PASSWORD, 
            doc_path=TEST_FILES.DOC_000, 
            os_type=os_type, config=config)
class Test008(DeskSignDoc): 
    def __init__(self, os_type: OSTypes, config):
        super().__init__(
            code_name="008", 
            name="Firmar con Certificado guardado en n carpetas anidadas.", 
            cert_path=CERTIFICATES.DEEP_NESTED_CERT,
            cert_password=DEFAULT_CERTS_PASSWORD, 
            doc_path=TEST_FILES.DOC_000, 
            os_type=os_type, config=config)

class Test009(DeskInvisibleSignDoc): 
    def __init__(self, os_type: OSTypes, config):
        super().__init__(
            code_name="009", 
            name="Firmar con check en Firma Invisible (Aplica a FirmaEC - Escritorio)", 
            cert_path=CERTIFICATES.VALID_CERT,
            cert_password=DEFAULT_CERTS_PASSWORD, 
            doc_path=TEST_FILES.DOC_000, 
            os_type=os_type, config=config)
        
class Test010(DeskSignDoc): 
    def __init__(self, os_type: OSTypes, config):
        super().__init__(
            code_name="010", 
            name="Firmar Archivos PDF de 0 kb.", 
            cert_path=CERTIFICATES.VALID_CERT,
            cert_password=DEFAULT_CERTS_PASSWORD, 
            doc_path=TEST_FILES.DOC_001, 
            os_type=os_type, config=config)
class Test011(DeskSignDoc): 
    def __init__(self, os_type: OSTypes, config):
        super().__init__(
            code_name="011", 
            name="Firmar Documento que tengan 20 firmas digitales ( en diferentes fechas de firma).", 
            cert_path=CERTIFICATES.VALID_CERT,
            cert_password=DEFAULT_CERTS_PASSWORD, 
            doc_path=TEST_FILES.DOC_002, 
            os_type=os_type, config=config)
class Test012(DeskSignDoc): 
    def __init__(self, os_type: OSTypes, config):
        super().__init__(
            code_name="012", 
            name="Firmar Documento que tengan 40 firmas digitales ( en diferentes fechas de firma).", 
            cert_path=CERTIFICATES.VALID_CERT,
            cert_password=DEFAULT_CERTS_PASSWORD, 
            doc_path=TEST_FILES.DOC_003, 
            os_type=os_type, config=config)
class Test013(DeskSignDoc): 
    def __init__(self, os_type: OSTypes, config):
        super().__init__(
            code_name="013", 
            name="Firmar Documento que tengan 60 firmas digitales ( en diferentes fechas de firma).", 
            cert_path=CERTIFICATES.VALID_CERT,
            cert_password=DEFAULT_CERTS_PASSWORD, 
            doc_path=TEST_FILES.DOC_004, 
            os_type=os_type, config=config)
class Test014(DeskSignDoc): 
    def __init__(self, os_type: OSTypes, config):
        super().__init__(
            code_name="014", 
            name="Firmar Documento en  formato PDF  Aalmacenado con extensión diferente a pdf.", 
            cert_path=CERTIFICATES.VALID_CERT,
            cert_password=DEFAULT_CERTS_PASSWORD, 
            doc_path=TEST_FILES.DOC_005, 
            os_type=os_type, config=config)

class Test015(DeskSignDoc): 
    def __init__(self, os_type: OSTypes, config):
        super().__init__(
            code_name="015", 
            name="Firmar Documento en formato PDF corrupto o dañado.", 
            cert_path=CERTIFICATES.VALID_CERT,
            cert_password=DEFAULT_CERTS_PASSWORD, 
            doc_path=TEST_FILES.DOC_006, 
            os_type=os_type, config=config)
        

class Test016(DeskSignDoc): 
    def __init__(self, os_type: OSTypes, config):
        super().__init__(
            code_name="016", 
            name="Firmar Documento en  formato PDF  con extensión jpg.", 
            cert_path=CERTIFICATES.VALID_CERT,
            cert_password=DEFAULT_CERTS_PASSWORD, 
            doc_path=TEST_FILES.DOC_007, 
            os_type=os_type, config=config)

class Test017(DeskSignDoc):
    def __init__(self, os_type: OSTypes, config):
        super().__init__(
            code_name="017",
            name="Firmar Documento en  formato PDF  con extensión png.",
            cert_path=CERTIFICATES.VALID_CERT,
            cert_password=DEFAULT_CERTS_PASSWORD,
            doc_path=TEST_FILES.DOC_008,
            os_type=os_type, config=config)
class Test018(DeskSignDoc):
    def __init__(self, os_type: OSTypes, config):
        super().__init__(
            code_name="018",
            name="Firmar Documento en  formato PDF  con extensión jpeg.",
            cert_path=CERTIFICATES.VALID_CERT,
            cert_password=DEFAULT_CERTS_PASSWORD,
            doc_path=TEST_FILES.DOC_009,
            os_type=os_type, config=config)
class Test019(DeskSignDoc):
    def __init__(self, os_type: OSTypes, config):
        super().__init__(
            code_name="019",
            name="Firmar Documento  en formato jpg y guardado con extensión PDF.",
            cert_path=CERTIFICATES.VALID_CERT,
            cert_password=DEFAULT_CERTS_PASSWORD,
            doc_path=TEST_FILES.DOC_010,
            os_type=os_type, config=config)

class Test020(DeskSignDoc):
    def __init__(self, os_type: OSTypes, config):
        super().__init__(
            code_name="020",
            name="Firmar Documento en formato  png y guardado con extensión PDF.",
            cert_path=CERTIFICATES.VALID_CERT,
            cert_password=DEFAULT_CERTS_PASSWORD,
            doc_path=TEST_FILES.DOC_011,
            os_type=os_type, config=config)
class Test021(DeskSignDoc):
    def __init__(self, os_type: OSTypes, config):
        super().__init__(
            code_name="021",
            name="Firmar Documento en formato jpeg y guardado con extensión PDF.",
            cert_path=CERTIFICATES.VALID_CERT,
            cert_password=DEFAULT_CERTS_PASSWORD,
            doc_path=TEST_FILES.DOC_012,
            os_type=os_type, config=config)
class Test022(DeskSignDoc):
    def __init__(self, os_type: OSTypes, config):
        super().__init__(
            code_name="022",
            name="Firmar Documento en formato  bmp  y guardado con extensión PDF.",
            cert_path=CERTIFICATES.VALID_CERT,
            cert_password=DEFAULT_CERTS_PASSWORD,
            doc_path=TEST_FILES.DOC_013,
            os_type=os_type, config=config)
class Test023(DeskSignDoc):
    def __init__(self, os_type: OSTypes, config):
        super().__init__(
            code_name="023",
            name="Firmar Documento en formato  tif  y guardado con extensión PDF.",
            cert_path=CERTIFICATES.VALID_CERT,
            cert_password=DEFAULT_CERTS_PASSWORD,
            doc_path=TEST_FILES.DOC_014,
            os_type=os_type, config=config)
class Test024(DeskSignDoc):
    def __init__(self, os_type: OSTypes, config):
        super().__init__(
            code_name="024",
            name="Firmar Documento en  formato PDF  con el nombre mayor a 200 caracteres.",
            cert_path=CERTIFICATES.VALID_CERT,
            cert_password=DEFAULT_CERTS_PASSWORD,
            doc_path=TEST_FILES.DOC_015,
            os_type=os_type, config=config)
        
class Test025(DeskSignDoc):
    def __init__(self, os_type: OSTypes, config):
        super().__init__(
            code_name="025",
            name="Firmar Documento en  formato PDF  con el nombre que contenga caracteres especiales.",
            cert_path=CERTIFICATES.VALID_CERT,
            cert_password=DEFAULT_CERTS_PASSWORD,
            doc_path=TEST_FILES.DOC_016,
            os_type=os_type, config=config)
class Test026(DeskSignDoc):
    def __init__(self, os_type: OSTypes, config):
        super().__init__(
            code_name="026",
            name="Firmar Documento con formato ods  y almacenados en formato PDF..",
            cert_path=CERTIFICATES.VALID_CERT,
            cert_password=DEFAULT_CERTS_PASSWORD,
            doc_path=TEST_FILES.DOC_017,
            os_type=os_type, config=config)
class Test027(DeskSignDoc):
    def __init__(self, os_type: OSTypes, config):
        super().__init__(
            code_name="027",
            name="Firmar Documento con formato odt y almacenados en formato PDF..",
            cert_path=CERTIFICATES.VALID_CERT,
            cert_password=DEFAULT_CERTS_PASSWORD,
            doc_path=TEST_FILES.DOC_018,
            os_type=os_type, config=config)
class Test028(DeskSignDoc):
    def __init__(self, os_type: OSTypes, config):
        super().__init__(
            code_name="028",
            name="Firmar Documento con formato pdf y escaneado.",
            cert_path=CERTIFICATES.VALID_CERT,
            cert_password=DEFAULT_CERTS_PASSWORD,
            doc_path=TEST_FILES.DOC_01801,
            os_type=os_type, config=config)
class Test029(DeskSignDoc):
    def __init__(self, os_type: OSTypes, config):
        super().__init__(
            code_name="029",
            name="Firmar Documento con formato pdf y  protegido por escritura.",
            cert_path=CERTIFICATES.VALID_CERT,
            cert_password=DEFAULT_CERTS_PASSWORD,
            doc_path=TEST_FILES.DOC_01802,
            os_type=os_type, config=config)
class Test030(DeskSignDoc):
    def __init__(self, os_type: OSTypes, config):
        super().__init__(
            code_name="030",
            name="Firmar Archivos generados en Microsoft Office 2013 y almacenados en formato PDF.",
            cert_path=CERTIFICATES.VALID_CERT,
            cert_password=DEFAULT_CERTS_PASSWORD,
            doc_path=TEST_FILES.DOC_019,
            os_type=os_type, config=config)
class Test031(DeskSignDoc):
    def __init__(self, os_type: OSTypes, config):
        super().__init__(
            code_name="031",
            name="Firmar Archivos generados en Microsoft Office ( con la versión más actual disponible ) y almacenados en formato PDF.",
            cert_path=CERTIFICATES.VALID_CERT,
            cert_password=DEFAULT_CERTS_PASSWORD,
            doc_path=TEST_FILES.DOC_020,
            os_type=os_type, config=config)
class Test032(DeskSignDoc):
    def __init__(self, os_type: OSTypes, config):
        super().__init__(
            code_name="032",
            name="Firmar Documento elaborado en Word con orientación horizontal  y almacenado en formato PDF.",
            cert_path=CERTIFICATES.VALID_CERT,
            cert_password=DEFAULT_CERTS_PASSWORD,
            doc_path=TEST_FILES.DOC_021,
            os_type=os_type, config=config)
class Test033(DeskSignDoc):
    def __init__(self, os_type: OSTypes, config):
        super().__init__(
            code_name="033",
            name="Firmar Documento elaborado en Word con orientación vertical  y almacenado en formato PDF.",
            cert_path=CERTIFICATES.VALID_CERT,
            cert_password=DEFAULT_CERTS_PASSWORD,
            doc_path=TEST_FILES.DOC_022,
            os_type=os_type, config=config)
class Test034(DeskSignDoc):
    def __init__(self, os_type: OSTypes, config):
        super().__init__(
            code_name="034",
            name="Firmar Documento elaborado en Word con orientación Vertical y Horizontal  y almacenado en formato PDF. Firmar en la hoja horizontal  y Firmar en la hoja Vertical",
            cert_path=CERTIFICATES.VALID_CERT,
            cert_password=DEFAULT_CERTS_PASSWORD,
            doc_path=TEST_FILES.DOC_023,
            os_type=os_type, config=config)
class Test035(DeskSignDoc):
    def __init__(self, os_type: OSTypes, config):
        super().__init__(
            code_name="035",
            name="Firmar Documento elaborado en Word con formato A5 y almacenado en formato PDF.",
            cert_path=CERTIFICATES.VALID_CERT,
            cert_password=DEFAULT_CERTS_PASSWORD,
            doc_path=TEST_FILES.DOC_024,
            os_type=os_type, config=config)
class Test036(DeskSignDoc):
    def __init__(self, os_type: OSTypes, config):
        super().__init__(
            code_name="036",
            name="Firmar Documento firmado electronicamente y modificado.",
            cert_path=CERTIFICATES.VALID_CERT,
            cert_password=DEFAULT_CERTS_PASSWORD,
            doc_path=TEST_FILES.DOC_025,
            os_type=os_type, config=config)
class Test037(DeskSignDoc):
    def __init__(self, os_type: OSTypes, config):
        super().__init__(
            code_name="037",
            name="Firmar Documento con formato exe y almacenado en formato PDF.",
            cert_path=CERTIFICATES.VALID_CERT,
            cert_password=DEFAULT_CERTS_PASSWORD,
            doc_path=TEST_FILES.DOC_026,
            os_type=os_type, config=config)
class Test038(DeskSignDoc):
    def __init__(self, os_type: OSTypes, config):
        super().__init__(
            code_name="038",
            name="Firmar Documento con formato PDF mayus",
            cert_path=CERTIFICATES.VALID_CERT,
            cert_password=DEFAULT_CERTS_PASSWORD,
            doc_path=TEST_FILES.DOC_027,
            os_type=os_type, config=config)
class Test039(DeskSignDoc):
    def __init__(self, os_type: OSTypes, config):
        super().__init__(
            code_name="039",
            name="Firmar Documento con formato pdf y firmado con otras entidades certificadoras válidas.",
            cert_path=CERTIFICATES.VALID_CERT,
            cert_password=DEFAULT_CERTS_PASSWORD,
            doc_path=TEST_FILES.DOC_028,
            os_type=os_type, config=config)
class Test040(DeskSignDoc):
    def __init__(self, os_type: OSTypes, config):
        super().__init__(
            code_name="040",
            name="Firmar Documento con formato pdf y firmado con certificado autogenerado",
            cert_path=CERTIFICATES.VALID_CERT,
            cert_password=DEFAULT_CERTS_PASSWORD,
            doc_path=TEST_FILES.DOC_029,
            os_type=os_type, config=config)
class Test041(DeskSignDoc):
    def __init__(self, os_type: OSTypes, config):
        super().__init__(
            code_name="041",
            name="Firmar Documento con formato pdf y  firmado en MAC.",
            cert_path=CERTIFICATES.VALID_CERT,
            cert_password=DEFAULT_CERTS_PASSWORD,
            doc_path=TEST_FILES.DOC_030,       
            os_type=os_type, config=config)
class Test042(DeskSignDoc):
    def __init__(self, os_type: OSTypes, config):
        super().__init__(
            code_name="042",
            name="Firmar Documento con formato xml. (Solo aplica a FirmaEC - Escritorio)",
            cert_path=CERTIFICATES.VALID_CERT,
            cert_password=DEFAULT_CERTS_PASSWORD,
            doc_path=TEST_FILES.DOC_031,
            os_type=os_type, config=config)
class Test043(DeskSignDoc):
    def __init__(self, os_type: OSTypes, config):
        super().__init__(
            code_name="045",
            name="Firmar Documento PDF con peso de 1GB.(Aplica a FirmaEC - escritorio).Nota: Depende de las características del equipo de pruebas.",
            cert_path=CERTIFICATES.VALID_CERT,
            cert_password=DEFAULT_CERTS_PASSWORD,
            doc_path=TEST_FILES.DOC_032,
            os_type=os_type, config=config)
class Test044(DeskSignDoc):
    def __init__(self, os_type: OSTypes, config):
        super().__init__(
            code_name="046",
            name="Firmar Documento PDF con peso  mayor  1GB.(Aplica a FirmaEC - escritorio).Nota: Depende de las características del equipo de pruebas.",
            cert_path=CERTIFICATES.VALID_CERT,
            cert_password=DEFAULT_CERTS_PASSWORD,
            doc_path=TEST_FILES.DOC_033,
            os_type=os_type, config=config)
       
class Test045(DeskSignDocBatch):
    def __init__(self, os_type: OSTypes, config):
        super().__init__(
            code_name="047",
            name="Firmar un lote de documentos (mínimo 20 )(Aplica a FirmaEC - Escritorio)",
            cert_path=CERTIFICATES.VALID_CERT,
            cert_password=DEFAULT_CERTS_PASSWORD,
            doc_path=TEST_FILES.DIR_034,
            os_type=os_type, config=config)


class Test046(DeskFullSignDocBatch):
    def __init__(self, os_type: OSTypes, config):
        super().__init__(
            code_name="048",
            name="Firmar un lote de documentos pdf y xml , e ingresar información en campos razón y localización.(Aplica a FirmaEC - escritorio).",
            cert_path=CERTIFICATES.VALID_CERT,
            cert_password=DEFAULT_CERTS_PASSWORD,
            doc_path=TEST_FILES.DIR_035,
            os_type=os_type, config=config)

class Test047(ValidatedQRDeskSignDoc):
    def __init__(self, os_type: OSTypes, config):
        super().__init__(
            code_name="049",
            name="Firmar Documento con formato pdf  y con estampado  QR.",
            cert_path=CERTIFICATES.VALID_CERT,
            cert_password=DEFAULT_CERTS_PASSWORD,
            doc_path=TEST_FILES.DOC_000,
            os_type=os_type, config=config)
    
class Test048(ValidatedDeskAdvancedSignDoc):
    def __init__(self, os_type: OSTypes, config):
        super().__init__(
            code_name="050",
            name="Firmar Documento con formato pdf  y con estampado Avanzada.(Aplica a FirmaEC - escritorio).",
            cert_path=CERTIFICATES.VALID_CERT,
            cert_password=DEFAULT_CERTS_PASSWORD,
            doc_path=TEST_FILES.DOC_000,
            os_type=os_type, config=config)
        
class Test049(ValidatedDeskSimpleSignDoc):
    def __init__(self, os_type: OSTypes, config):
        super().__init__(
            code_name="051",
            name="Firmar Documento con formato pdf  y con estampado Simple.(Aplica a FirmaEC - escritorio).",
            cert_path=CERTIFICATES.VALID_CERT,
            cert_password=DEFAULT_CERTS_PASSWORD,
            doc_path=TEST_FILES.DOC_000,
            os_type=os_type, config=config)
        
class Test050(ValidatedFullQRDeskSignDoc):
    def __init__(self, os_type: OSTypes, config):
        super().__init__(
            code_name="052",
            name="Firmar Documento con formato pdf , estampado QR  e ingresando información en campos  Razón de firma y Localización.(Aplica a FirmaEC - escritorio).",
            cert_path=CERTIFICATES.VALID_CERT,
            cert_password=DEFAULT_CERTS_PASSWORD,
            doc_path=TEST_FILES.DOC_000,
            os_type=os_type, config=config)

class Test051(ValidatedDeskFullAdvancedSignDoc):
    def __init__(self, os_type: OSTypes, config):
        super().__init__(
            code_name="053",
            name="Firmar Documento con formato pdf  , con estampado Avanzada  e ingresando información en campos  Razón de firma y Localización.(Aplica a FirmaEC - escritorio).",
            cert_path=CERTIFICATES.VALID_CERT,
            cert_password=DEFAULT_CERTS_PASSWORD,
            doc_path=TEST_FILES.DOC_000,
            os_type=os_type, config=config)

class Test052(ValidatedDeskFullSimpleSignDoc):
    def __init__(self, os_type: OSTypes, config):
        super().__init__(
            code_name="054",
            name="Firmar Documento con formato pdf  , con estampado Simple  e ingresando información en campos  Razón de firma y Localización.(Aplica a FirmaEC - escritorio).",
            cert_path=CERTIFICATES.VALID_CERT,
            cert_password=DEFAULT_CERTS_PASSWORD,
            doc_path=TEST_FILES.DOC_000,
            os_type=os_type, config=config)
        
class Test053(FullQRDeskSignDoc):
    def __init__(self, os_type: OSTypes, config):
        super().__init__(
            code_name="055",
            name="-Disponer un documento que se encuentre firmado digitalmente y tenga información en los campos Razón de firma y Localización.-Firmar",
            cert_path=CERTIFICATES.VALID_CERT,
            cert_password=DEFAULT_CERTS_PASSWORD,
            doc_path=TEST_FILES.DOC_042,
            os_type=os_type, config=config)

class Test054(DeskReSignDocBatch):
    def __init__(self, os_type: OSTypes, config):
        super().__init__(
            code_name="056",
            name="Firmar todo el lote de documentos que fueron firmados en los escenarios anteriores",
            cert_path=CERTIFICATES.VALID_CERT,
            cert_password=DEFAULT_CERTS_PASSWORD,
            doc_path=TEST_FILES.DIR_RESULTS,
            os_type=os_type, config=config)
  
class Test055(ValidatedQRDeskSignDoc):
    def __init__(self, os_type: OSTypes, config):
        super().__init__(
            code_name="059",
            name="Firmar Modificar la fecha y hora del computador, y posteriormente realizar la firma.",
            cert_path=CERTIFICATES.VALID_CERT,
            cert_password=DEFAULT_CERTS_PASSWORD,
            doc_path=TEST_FILES.DOC_000,
            os_type=os_type, config=config)

