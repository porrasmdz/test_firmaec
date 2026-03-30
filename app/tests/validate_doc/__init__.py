from app.constants import TEST_FILES

from .test_XYZ_desk_valdoc import DeskValidateDoc

class Test001(DeskValidateDoc):
    def __init__(self, os_type, config):
        super().__init__(
            "004", 
            "Verificar documento con Certificado a punto de expirar.",
            TEST_FILES.VD_001, 
            os_type, config)
        
class Test002(DeskValidateDoc):
    def __init__(self, os_type, config):
        super().__init__(
            "005",
            "Verificar documento con Certificado vigente.",
            TEST_FILES.VD_002, 
            os_type, config)


class Test003(DeskValidateDoc):
    def __init__(self, os_type, config):
        super().__init__(
            "006",
            "Verificar documento con Certificado autogenerado.",
            TEST_FILES.VD_003, 
            os_type, config)
        
        
class Test004(DeskValidateDoc):
    def __init__(self, os_type, config):
        super().__init__(
            "007",
            "Verificar documento con Certificado con nombre extenso.",
            TEST_FILES.VD_004, 
            os_type, config)
        
class Test005(DeskValidateDoc):
    def __init__(self, os_type, config):
        super().__init__(
            "008",
            "Verificar documento con Certificado guardado en n carpetas anidadas (n=20).",
            TEST_FILES.VD_005, 
            os_type, config)

class Test006(DeskValidateDoc):
    def __init__(self, os_type, config):
        super().__init__(
            "009",
            "Verificar documento con Firmar con check en 'Firma Invisible'(Aplica a FirmaEC - Escritorio)",
            TEST_FILES.VD_006, 
            os_type, config)
        

class Test007(DeskValidateDoc):
    def __init__(self, os_type, config):
        super().__init__(
            "011",
            "Verificar documento con Documento que tengan 20 firmas digitales ( en diferentes fechas de firma).",
            TEST_FILES.DOC_002, 
            os_type, config)

class Test008(DeskValidateDoc):
    def __init__(self, os_type, config):
        super().__init__(
            "012",
            "Verificar documento con Documento que tengan 40 firmas digitales ( en diferentes fechas de firma).",
            TEST_FILES.DOC_003, 
            os_type, config)
        
class Test009(DeskValidateDoc):
    def __init__(self, os_type, config):
        super().__init__(
            "013",
            "Verificar documento con Documento que tengan 60 firmas digitales ( en diferentes fechas de firma).",
            TEST_FILES.DOC_004, 
            os_type, config)

        
class Test010(DeskValidateDoc):
    def __init__(self, os_type, config):
        super().__init__(
            "024",
            "Verificar documento con Documento en formato PDF con el nombre mayor a 200 caracteres.",
            TEST_FILES.DOC_015, 
            os_type, config)
class Test011(DeskValidateDoc):
    def __init__(self, os_type, config):
        super().__init__(
            "025",
            "Verificar documento con Documento en  formato PDF  con el nombre que contenga caracteres especiales.",
            TEST_FILES.DOC_016, 
            os_type, config)
class Test012(DeskValidateDoc):
    def __init__(self, os_type, config):
        super().__init__(
            "026",
            "Verificar documento con Documento con formato ods  y almacenados en formato PDF.",
            TEST_FILES.DOC_017, 
            os_type, config)
        
class Test013(DeskValidateDoc):
    def __init__(self, os_type, config):
        super().__init__(
            "027",
            "Verificar documento con Documento con formato odt  y almacenados en formato PDF.",
            TEST_FILES.DOC_018, 
            os_type, config)

class Test014(DeskValidateDoc):
    def __init__(self, os_type, config):
        super().__init__(
            "028",
            "Verificar documento con Documento con formato pdf y escaneado.",
            TEST_FILES.DOC_01801, 
            os_type, config)
        

class Test015(DeskValidateDoc):
    def __init__(self, os_type, config):
        super().__init__(
            "030",
            "Verificar documento con Archivos generados en Microsoft Office 2013 y almacenados en formato PDF.",
            TEST_FILES.DOC_019, 
            os_type, config)
class Test016(DeskValidateDoc):
    def __init__(self, os_type, config):
        super().__init__(
            "031",
            "Verificar documento con Archivos generados en Microsoft Office ( con la versión más actual disponible ) y almacenados en formato PDF.",
            TEST_FILES.DOC_020, 
            os_type, config)
class Test017(DeskValidateDoc):
    def __init__(self, os_type, config):
        super().__init__(
            "032",
            "Verificar documento con Documento elaborado en Word con orientación horizontal  y almacenado en formato PDF.",
            TEST_FILES.DOC_021, 
            os_type, config)
class Test018(DeskValidateDoc):
    def __init__(self, os_type, config):
        super().__init__(
            "033",
            "Verificar documento con Documento elaborado en Word con orientación vertical  y almacenado en formato PDF.",
            TEST_FILES.DOC_022, 
            os_type, config)
class Test019(DeskValidateDoc):
    def __init__(self, os_type, config):
        super().__init__(
            "034",
            "Verificar documento con Documento elaborado en Word con orientación vertical  y horizontal almacenado en formato PDF.",
            TEST_FILES.DOC_023, 
            os_type, config)
class Test020(DeskValidateDoc):
    def __init__(self, os_type, config):
        super().__init__(
            "035",
            "Verificar documento con Documento elaborado en Word con formato A5 y almacenado en formato PDF.",
            TEST_FILES.DOC_024, 
            os_type, config)
class Test021(DeskValidateDoc):
    def __init__(self, os_type, config):
        super().__init__(
            "036",
            "Verificar documento con Documento firmado electronicamente y modificado.",
            TEST_FILES.DOC_025, 
            os_type, config)

class Test022(DeskValidateDoc):
    def __init__(self, os_type, config):
        super().__init__(
            "038",
            "Verificar documento con Documento con formato pdf y con la extensión (pdf ) en mayúscula . Ejm: mama.PDF.",
            TEST_FILES.DOC_027, 
            os_type, config)
        
class Test023(DeskValidateDoc):
    def __init__(self, os_type, config):
        super().__init__(
            "039",
            "Verificar documento con Documento con formato pdf y firmado con otras entidades certificadoras válidas.",
            TEST_FILES.DOC_028, 
            os_type, config)
        
class Test024(DeskValidateDoc):
    def __init__(self, os_type, config):
        super().__init__(
            "040",
            "Verificar documento con Documento con formato pdf y firmado con certificado autogenerado",
            TEST_FILES.DOC_029, 
            os_type, config)
class Test025(DeskValidateDoc):
    def __init__(self, os_type, config):
        super().__init__(
            "041",
            "Verificar documento con Documento con formato pdf y  firmado en MAC.",
            TEST_FILES.DOC_030, 
            os_type, config)
class Test026(DeskValidateDoc):
    def __init__(self, os_type, config):
        super().__init__(
            "042",
            "Verificar documento con Documento con formato xml.(Solo aplica a FirmaEC - Escritorio)",
            TEST_FILES.DOC_031, 
            os_type, config)
class Test027(DeskValidateDoc):
    def __init__(self, os_type, config):
        super().__init__(
            "045",
            "Verificar documento con Documento PDF con peso de 1GB. (Aplica a FirmaEC - escritorio).Nota: Depende de las características del equipo de pruebas.",
            TEST_FILES.DOC_032, 
            os_type, config)
    
#TODO: BATCH VALIDATE TESTS
# class Test028(DeskValidateDocBatch):
#     def __init__(self, os_type, config):
#         super().__init__(
#             "047",
#             "Verificar documento con Firmar un lote de documentos (mínimo 20 )(Aplica a FirmaEC - Escritorio)",
#             TEST_FILES.DIR_034, 
#             os_type, config)
        
# class Test029(DeskValidateDocBatch):
#     def __init__(self, os_type, config):
#         super().__init__(
#             "048",
#             "Verificar documento con Firmar un lote de documentos pdf y xml , e ingresar información en campos razón y localización.(Aplica a FirmaEC - escritorio).",
#             TEST_FILES.DIR_035, 
#             os_type, config)

class Test030(DeskValidateDoc):
    def __init__(self, os_type, config):
        super().__init__(
            "049",
            "Verificar documento con Documento con formato pdf  y con estampado  QR.",
            TEST_FILES.VD_036, 
            os_type, config)

class Test031(DeskValidateDoc):
    def __init__(self, os_type, config):
        super().__init__(
            "050",
            "Verificar documento con Documento con formato pdf  y con estampado Avanzada.(Aplica a FirmaEC - escritorio).",
            TEST_FILES.VD_037,  
            os_type, config)
        
class Test032(DeskValidateDoc):
    def __init__(self, os_type, config):
        super().__init__(
            "051",
            "Verificar documento con Documento con formato pdf  y con estampado Simple.(Aplica a FirmaEC - escritorio).",
            TEST_FILES.VD_038,  
            os_type, config)
class Test033(DeskValidateDoc):
    def __init__(self, os_type, config):
        super().__init__(
            "052",
            "Verificar documento con Documento con formato pdf , estampado QR  e ingresando información en campos  Razón de firma y Localización.(Aplica a FirmaEC - escritorio).",
            TEST_FILES.VD_039,  
            os_type, config)
class Test034(DeskValidateDoc):
    def __init__(self, os_type, config):
        super().__init__(
            "053",
            "Verificar documento con Documento con formato pdf  , con estampado Avanzada  e ingresando información en campos  Razón de firma y Localización.(Aplica a FirmaEC - escritorio).",
            TEST_FILES.VD_040,  
            os_type, config)
class Test035(DeskValidateDoc):
    def __init__(self, os_type, config):
        super().__init__(
            "054",
            "Verificar documento con Documento con formato pdf  , con estampado Simple  e ingresando información en campos  Razón de firma y Localización.(Aplica a FirmaEC - escritorio).",
            TEST_FILES.VD_041,  
            os_type, config)
class Test036(DeskValidateDoc):
    def __init__(self, os_type, config):
        super().__init__(
            "055",
            "Verificar documento con -Disponer un documento que se encuentre firmado digitalmente y tenga información en los campos Razón de firma y Localización. -Firmar el documento e ingresar información en los campos Razón de firma y Localización.(Aplica a FirmaEC - Escritorio)",
            TEST_FILES.VD_042,  
            os_type, config)
        
        
# class Test037(DeskValidateDocBatchResult): #TODO
#     def __init__(self, os_type, config):
#         super().__init__( #ESTE ES UN LOTE DE TODOS LOS RESULTADOS DE LAS FIRMAS REFIRMARLOS Y VALIDARLOS
#             "056",
#             "Verificar documento con Firmar todo el lote de documentos que fueron firmados en los escenarios anteriores.(Aplica a FirmaEC - Escritorio)",
#             TEST_FILES.DIR_043, #TODO: resigned or smth 
#             os_type, config)
# class Test038(DeskValidateDocBatchResult): #TODO
#     def __init__(self, os_type, config):
#         super().__init__( #ESTE ES UN LOTE DE TODOS LOS RESULTADOS DE LAS FIRMAS SOLO VALIDARLOS
#             "057", 
#             "Verificar documento con Verificar todo el lote de documentos que fueron firmados en los escenarios anteriores.(Aplica a FirmaEC - Escritorio)",
#             TEST_FILES.DIR_044,  
#             os_type, config)

# class Test039(DeskValidateDocBatchResult): #TODO
#     def __init__(self, os_type, config):
#         super().__init__( #ESTE ES UN LOTE DE TODOS LOS RESULTADOS DE LAS FIRMAS EN MOVIL
#             "058", 
#             "Verificar documento con Verificar  en firmaEC - escritorio, todo el lote de documentos que fueron firmados en firmaEC movil",
#             TEST_FILES.DIR_044, #TODO: mobile resigned or smth 
#             os_type, config)
        
class Test040(DeskValidateDoc): 
    def __init__(self, os_type, config):
        super().__init__( 
            "059", 
            "Verificar documento con Modificar la fecha y hora del computador, y posteriormente realizar la firma.",
            TEST_FILES.VD_044, 
            os_type, config)
        