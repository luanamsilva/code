from barcode import Code128
from barcode.writer import ImageWriter

class Barcode:
    def create_barcode(self, product_code: str) -> str:
        tag = Code128(product_code, writer=ImageWriter())
        path_tag = f'{tag}'
        tag.save(path_tag)

        return path_tag
