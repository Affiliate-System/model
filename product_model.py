from common.logging import InfoLogger, ErrorLogger, InfoLogger

import bson

class Product:
    def __init__(self):
        self.title = ''
        self.description = ''
        self.price_original = bson.Int64(0)
        self.price_discount = bson.Int64(0)
        self.url_original = ''
        self.url_affiliate = ''
        self.photos = []
        self.videos = []
        self.comments = []
        self.ratings = {
            '1': 0,
            '2': 0,
            '3': 0,
            '4': 0,
            '5': 0}
        self.product_id_ext = ''
        self.shop_id_ext = ''

    def set_title(self, val):
        if type(val) is type(self.title):
            self.title = val
            return None

        e = Exception('product_model.set_title.unsupported_datatype')
        ErrorLogger.error(f'product_model.set_title.unsupported_datatype. Details: {str({"title_type": type(self.title), "value_type": type(val)})}')
        return e

    def set_description(self, val):
        if type(val) is type(self.description):
            self.description = val
            return None

        e = Exception('product_model.set_description.unsupported_datatype')
        ErrorLogger.error(f'product_model.set_description.unsupported_datatype. Details: {str({"description_type": type(self.description), "value_type": type(val)})}')
        return e

    def set_url_original(self, val):
        if type(val) is type(self.url_original):
            self.url_original = val
            return None

        e = Exception('product_model.set_url_original.unsupported_datatype')
        ErrorLogger.error(f'product_model.set_url_original.unsupported_datatype. Details: {str({"url_original_type": type(self.url_original), "value_type": type(val)})}')
        return e

    def set_photos(self, val):
        if type(val) is type(self.photos):
            self.photos = val
            return None

        e = Exception('product_model.set_photos.unsupported_datatype')
        ErrorLogger.error(f'product_model.set_photos.unsupported_datatype. Details: {str({"photos_type": type(self.photos), "value_type": type(val)})}')
        return e

    def set_price_original(self, val):
        if type(val) is type(self.price_original):
            self.price_original = val
            return None

        if type(val) is int:
            self.price_original = bson.Int64(val)
            return None

        e = Exception('product_model.set_price_original.unsupported_datatype')
        ErrorLogger.error(f'product_model.set_price_original.unsupported_datatype. Details: {str({"price_original_type": type(self.price_original), "value_type": type(val)})}')
        return e

    def set_price_discount(self, val):
        if type(val) is type(self.price_discount):
            self.price_discount = val
            return None

        if type(val) is int:
            self.price_discount = bson.Int64(val)
            return None

        e = Exception('product_model.set_price_discount.unsupported_datatype')
        ErrorLogger.error(
            f'product_model.set_price_discount.unsupported_datatype. Details: {str({"price_discount_type": type(self.price_discount), "value_type": type(val)})}')
        return e
