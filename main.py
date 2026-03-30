import os
import sys

import pyautogui
from app.config import TestsConfig
from app.constants import TESTED_APP_VERSION
from app.logger import logger
import subprocess
from app.tests import sign_doc, validate_cert, validate_doc 
from app.utils import is_element_present, is_valid_os

# pyautogui.FAILSAFE = True
# pyautogui.PAUSE = 0.3
pyautogui.USE_IMAGE_NOT_FOUND_EXCEPTION = False

log = logger.getLogger("MAIN")

def main():
    log.info("init")
    if len(sys.argv) < 1:
        log.error(f"OS string not received")
        return
    os_sel = sys.argv[1]
    if(not is_valid_os(os_sel)):
        log.error(f"OS: {os_sel} is not valid")
        return
    log.info(f"Selected OS: {os_sel}")
    
    config = TestsConfig(os_sel).get_config_map()
    log.info(f"config data is: {config}")
    
    subprocess.Popen(config.app_path)
    
    if(not is_element_present(os.path.join(config.profiles_dir, "validator.png"))):
        log.error(f"Error launching app. Please retry in a few mins")
        return
    log.info(f"App is ready. Version {TESTED_APP_VERSION}")
    # log.info("################################VALIDACION DE CERTIFICADOS###############################")
    # validate_cert.Test001(os_sel, config).run()
    # validate_cert.Test002(os_sel, config).run()
    # validate_cert.Test003(os_sel, config).run()
    # validate_cert.Test004(os_sel, config).run()
    # validate_cert.Test005(os_sel, config).run()
    # validate_cert.Test006(os_sel, config).run()
    # validate_cert.Test007(os_sel, config).run()
    # validate_cert.Test008(os_sel, config).run()

    # log.info("################################VALIDACION DE DOCUMENTOS###############################")
    # validate_doc.Test001(os_sel, config).run()
    # validate_doc.Test002(os_sel, config).run()
    # validate_doc.Test003(os_sel, config).run()
    # validate_doc.Test004(os_sel, config).run()
    # validate_doc.Test005(os_sel, config).run()
    # validate_doc.Test006(os_sel, config).run()
    # validate_doc.Test007(os_sel, config).run()
    # validate_doc.Test008(os_sel, config).run()
    # validate_doc.Test009(os_sel, config).run()
    # validate_doc.Test010(os_sel, config).run()
    # validate_doc.Test011(os_sel, config).run()
    # validate_doc.Test012(os_sel, config).run()
    # validate_doc.Test013(os_sel, config).run()
    # validate_doc.Test014(os_sel, config).run()
    # validate_doc.Test015(os_sel, config).run()
    # validate_doc.Test016(os_sel, config).run()
    # validate_doc.Test017(os_sel, config).run()
    # validate_doc.Test018(os_sel, config).run()
    # validate_doc.Test019(os_sel, config).run()
    # validate_doc.Test020(os_sel, config).run()
    # validate_doc.Test021(os_sel, config).run()
    # validate_doc.Test022(os_sel, config).run()
    # validate_doc.Test023(os_sel, config).run()
    # validate_doc.Test024(os_sel, config).run()
    # validate_doc.Test025(os_sel, config).run()
    # validate_doc.Test026(os_sel, config).run()
    # validate_doc.Test027(os_sel, config).run()
    # # validate_doc.Test028(os_sel, config).run()
    # # validate_doc.Test029(os_sel, config).run()
    # validate_doc.Test030(os_sel, config).run()
    # validate_doc.Test031(os_sel, config).run()
    # validate_doc.Test032(os_sel, config).run()
    # validate_doc.Test033(os_sel, config).run()
    # validate_doc.Test034(os_sel, config).run()
    # validate_doc.Test035(os_sel, config).run()
    # validate_doc.Test036(os_sel, config).run()
    # # validate_doc.Test037(os_sel, config).run()
    # # validate_doc.Test038(os_sel, config).run()
    # # validate_doc.Test039(os_sel, config).run()
    # validate_doc.Test040(os_sel, config).run()
    # log.info("################################VALIDACION DE FIRMA###############################")
    # sign_doc.Test001(os_sel, config).run()
    # sign_doc.Test002(os_sel, config).run()
    # sign_doc.Test003(os_sel, config).run()
    # sign_doc.Test004(os_sel, config).run()
    # sign_doc.Test005(os_sel, config).run()
    # sign_doc.Test006(os_sel, config).run()
    # sign_doc.Test007(os_sel, config).run()
    # sign_doc.Test008(os_sel, config).run()
    # sign_doc.Test009(os_sel, config).run()
    # sign_doc.Test010(os_sel, config).run()
    # sign_doc.Test011(os_sel, config).run()
    # sign_doc.Test012(os_sel, config).run()
    # sign_doc.Test013(os_sel, config).run()
    # sign_doc.Test014(os_sel, config).run()
    # sign_doc.Test015(os_sel, config).run()
    # sign_doc.Test016(os_sel, config).run()
    # sign_doc.Test017(os_sel, config).run()
    # sign_doc.Test018(os_sel, config).run()
    # sign_doc.Test019(os_sel, config).run()
    # sign_doc.Test020(os_sel, config).run()
    # sign_doc.Test021(os_sel, config).run()
    # sign_doc.Test022(os_sel, config).run()
    # sign_doc.Test023(os_sel, config).run()
    # sign_doc.Test024(os_sel, config).run()
    # sign_doc.Test025(os_sel, config).run()
    # sign_doc.Test026(os_sel, config).run()
    # sign_doc.Test027(os_sel, config).run()
    # sign_doc.Test028(os_sel, config).run()
    # sign_doc.Test029(os_sel, config).run()
    # sign_doc.Test030(os_sel, config).run()
    # sign_doc.Test031(os_sel, config).run()
    # sign_doc.Test032(os_sel, config).run()
    # sign_doc.Test033(os_sel, config).run()
    # sign_doc.Test034(os_sel, config).run()
    # sign_doc.Test035(os_sel, config).run()
    # sign_doc.Test036(os_sel, config).run()
    # sign_doc.Test037(os_sel, config).run()
    # sign_doc.Test038(os_sel, config).run()
    # sign_doc.Test039(os_sel, config).run()
    # sign_doc.Test040(os_sel, config).run()
    
    # sign_doc.Test041(os_sel, config).run()
    # sign_doc.Test042(os_sel, config).run()
    # sign_doc.Test043(os_sel, config).run()
    # sign_doc.Test044(os_sel, config).run()
    # sign_doc.Test045(os_sel, config).run()
    # sign_doc.Test046(os_sel, config).run()
    # sign_doc.Test047(os_sel, config).run()
    # sign_doc.Test048(os_sel, config).run()
    # sign_doc.Test049(os_sel, config).run()
    # sign_doc.Test050(os_sel, config).run()
    # sign_doc.Test051(os_sel, config).run()
    # sign_doc.Test052(os_sel, config).run()
    # sign_doc.Test053(os_sel, config).run()
   
    # sign_doc.Test054(os_sel, config).run()
    
    # THIS TEST HAS TO BE MANUAL BECAUSE IT NEEDS TO BE CHANGED LOCAL TIME FIRST 
    # sign_doc.Test055(os_sel, config).run()
   
    
if __name__ == "__main__":
    main()