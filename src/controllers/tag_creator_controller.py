from typing import Dict
from src.drivers.barcode import Barcode

class TagCreatorController:
    def create_controller(self, product_code: str) -> Dict:
        path_tag = self.__create_tag(product_code)
        formatted_response = self.__format_response(path_tag)
        return formatted_response

    def __create_tag(self, product_code: str) -> str:
        barcode = Barcode()
        path_tag = barcode.create_barcode(product_code)
        return path_tag

    def __format_response(self, path_tag: str) -> Dict:
        return {
            "data": {
                "type": "Tag Image",
                "count": 1,
                "path": f'{path_tag}.png'
            }
       }
