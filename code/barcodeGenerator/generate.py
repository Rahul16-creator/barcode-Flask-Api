import barcode
hr=barcode.get_barcode_class('ean13')
Hr=hr('9464474730951')
Hr.save('bcde1')