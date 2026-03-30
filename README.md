Python Version
    Python 3.10
    Java 17 sdk
    openjdk 17.0.17 2025-10-21
    
Tipos de certificado:
    - Certificado Expirado
    - Certificado Revocado
    - Certificado Caducado y Revocado
    - Certificado a punto de expirar
    - Certificado vigente
    - Certificado autogenerado
    - Certificado con nombre extenso
    - Certificado guardado en n carpetas anidadas

PREPARACION DE ENTORNO:
    - Instalar Python 3.10
    - Instalar Java
    - Instalar FirmaEC 
    - Actualizar FirmaEC a su version beta final 

    - Instalar ultima version de Chrome
    - Instalar ultima version de Firefox
    - Instalar ultima version de Adobe Acrobat Reader
    - Instalar ultima version de Safari
    - Agregar chrome, firefox, adobe acrobat reader, safari al path

SUPUESTOS:
    chrome, firefox, adobe acroba y sfari estan en el PATH del sistema MENOS MAC

    La firma debe entrar en un cuadro de 215x120 pixeles
    Por caducar es < 24 horas
    Nombre muy largo > 200 caracteres
    Version actual de word en 28/03/2026 -> https://learn.microsoft.com/en-us/officeupdates/update-history-microsoft365-apps-by-date
        Word Version 2603 - Build 19822.20114
    Generacion del certificado autogenerado:
        - Alternativamente se creo con OpenSSL la version autogen.p12 para pruebas
            $openssl genrsa -out key.pem 2048
            $openssl req -new -x509 -key key.pem -out cert.pem -days 365
            $openssl pkcs12 -export -out cert.p12 -inkey key.pem -in cert.pem
        
        - https://support.microsoft.com/es-es/office/obtener-un-certificado-digital-y-crear-una-firma-digital-e3d9d813-3305-4164-a820-2e063d86e512
        - Firmado con Adobe Acrobat Reader

PDF PARA FIRMAS:
    VD001 Pdf firmado (en Acrobat Reader) con Certificado a punto de expirar
    X VD002 Pdf firmado (en Acrobat Reader) con Certificado vigente
    X VD003 Pdf firmado (en Acrobat Reader) con Certificado autogenerado
    X VD004 Pdf firmado (en Acrobat Reader) con Certificado nombre extenso (irrelevante pq el certificado esta en el key manager del sistema signare pero bueno)
    X VD005 Pdf firmado (en Acrobat Reader) con Certificado anidado en n carpetas (20 carpetas) (irrelevante pq el certificado esta en el key manager con los datos del sistema signare pero bueno)
    X VD006 Pdf firmado (en Acrobat Reader) con Check en Firma Invisible (valid cert)

    .... EL RESTO DEBEN SER DEL RESULTADO DE ALGUN FLUJO DE EJECUCION DE FIRMAS
        (Y DE MOVIL TMB)
        LOS QUE SON DE 20, 40 y 60, 1gb y 1.5gb FIRMAS QUIZAS FALLEN POR TIMEOUT AUMENTARLO PUEDE SERVIR
        
    X VD036 pdf firmando con estampado QR - INCLUYE CAPTURA de ESCANEO DEL ESTAMPADO
    X VD037 pdf firmando con estampado avanzada - INCLUYE CAPTURA de ESCANEO DEL ESTAMPADO
    X VD038 pdf firmando con estampado simple - INCLUYE CAPTURA de ESCANEO DEL ESTAMPADO
    X VD039 pdf firmando con estampado QR llenando razon y localizacion
    X VD040 pdf firmando con estampado avanzada llenando razon y localizacion
    X VD041 pdf firmando con estampado simple llenando razon y localizacion
    X VD042 pdf firmado con razon y localizacion y firmar llenando razon y localizacion (refirmado)
    X VD043 Firmar resultado con lote de TODAS LAS EJECUCIONES ANTERIORES
    X VD044 Modificar fecha y hora de computador y realizar la firma



    X 001 Pdf de 0kbs
    X 002 Pdf de 20 firmas electrónicas
    X 003 Pdf de 40 firmas electrónicas
    X 004 Pdf de 60 firmas electrónicas

    X 005 Pdf con extension diferente a pdf (.pnf)
    X 006 Pdf corrupto
    X 007 Pdf con extension jpg
    X 008 Pdf con extension png
    X 009 Pdf con extension jpeg
    X 010 jpg con extension pdf
    X 011 png con extension pdf
    X 012 jpeg con extension pdf
    X 013 bmp con extension pdf
    X 014 tif con extension pdf

    X 015 pdf con nombre > 200 caracteres
    X 016 pdf con nombre caracteres especiales

    X 017 Documento ods y almacenado como PDF
    X 018 Documento odt y almacenado como PDF

    X 01801 Documento PDF escaneado
    X 01802 Documento PDF protegido por escritura 

    X 019 Word generado en Office 2013 y almacenado como pdf
        
    X 020 Word generado en Office (mas actual) y almacenado como pdf
    X 021 Word Office (v actual) con orientacion horizontal hecho pdf
    X 022 Word Office (v actual) con orientacion vertical hecho pdf -> 020
    X 023 Word Office (v actual) con 1 pag en orientacion vertical y 1 en horizontal hecho pdf. (Firmar en ambas hojas)

    X 024 Word Office (v actual) formato A5 hecho pdf. (Firmar en ambas hojas)

    X 025 PDF firmado y editado
    X 026 .exe almacenado como pdf 
    X 027 pdf con extension en mayuscula .PDF

    X 028 pdf en .pdf firmado por otras entidades certificadoras (mi firma en seccurity data)

    X 029 pdf firmado con certificado autogenerado
    X 030 pdf firmado en una MAC
    X 031 documento xml (si firma)
    X 032 pdf de 1GB - aprox. 995 MBs

    X 033 pdf de 1.5GB (mayor a 1Gb) - aprox. 1.45 Gbs

    X 034 Firmar un lote de documentos (20 pdfs)
    X 035 Firmar un lote de documentos (20 pdfs) 10 pdf y 10 xml e ingresar razon y localizacion

    - 036 pdf firmando con estampado QR - INCLUYE CAPTURA de ESCANEO DEL ESTAMPADO
    - 037 pdf firmando con estampado avanzada - INCLUYE CAPTURA de ESCANEO DEL ESTAMPADO
    - 038 pdf firmando con estampado simple - INCLUYE CAPTURA de ESCANEO DEL ESTAMPADO


    - 039 pdf firmando con estampado QR llenando razon y localizacion - INCLUYE CAPTURA de la firma en CHROME, Firefox, Safari, Adobe Acrobat
    - 040 pdf firmando con estampado avanzada llenando razon y localizacion - INCLUYE CAPTURA de la firma en CHROME, Firefox, Safari, Adobe Acrobat
    - 041 pdf firmando con estampado simple llenando razon y localizacion - INCLUYE CAPTURA de la firma en CHROME, Firefox, Safari, Adobe Acrobat

    X 042 pdf firmado con razon y localizacion y firmar llenando razon y localizacion (refirmado)

    - 043 Firmar resultado con lote de TODAS LAS EJECUCIONES ANTERIORES
    - 044 Modificar fecha y hora de computador y realizar la firma
    - 045 Firmar resultado con lote de TODAS LAS EJECUCIONES de FIRMA MOVIL EC
