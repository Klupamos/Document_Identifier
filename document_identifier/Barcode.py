import re
from . import DocumentBase

__all__ = ["UPC_A"]

class Barcode(DocumentBase):
    pass


class UPC(Barcode):
    pass

    
class UPC_A(UPC):
    Format = {
        'raw_input': re.compile(r'^(?P<number>\d{12})$'),
    }
    
    def __init__(self, **kwargs):
        super(UPC_A, self).__init__(**kwargs)
        
        product = 0
        for num, mul in zip(map(int, self.number[:-1]), [3,1]*6):
            product += num * mul
        product = 10 - (product % 10)
        
        if product != int(self.number[-1]):
            raise ValueError("Invalid check digit")
            
        if self.number[0] in "01678":
            self.system = "product"
            self.manufacture_code = self.number[1:5]
            self.product_code = self.number[5:10]
        elif self.number[0] == "3":
            self.system = "pharmaceutical"
            
            pass
        elif self.number[0] == "4":
            pass
        elif self.number[0] in "59":
            self.system = "coupon"
            self.manufacture_code = self.number[1:5]
            self.family_code = self.number[5:8]
            self.coupon_code = self.number[8:10]