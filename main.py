import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from genel_islemler import GenelIslemler

if __name__ == "__main__":
    menu = GenelIslemler()
    menu.menu_goster()
    


    