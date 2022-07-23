from common.logging import InfoLogger, ErrorLogger, InfoLogger

import bson
from bson.objectid import ObjectId

class Post:
    def __init__(self):
        self.content = ''
        self.publish_count = 0
        self.product_id = ObjectId()

    def set_content(self, val):
        if type(val) is type(self.content):
            self.content = val
            return None

        e = Exception('post_model.set_content.unsupported_datatype')
        ErrorLogger.error(f'post_model.set_content.unsupported_datatype. Details: {str({"content_type": type(self.content), "value_type": type(val)})}')
        return e

    def set_product_id(self, val):
        if type(val) is type(self.product_id):
            self.product_id = val
            return None

        e = Exception('post_model.set_product_id.unsupported_datatype')
        ErrorLogger.error(f'post_model.set_product_id.unsupported_datatype. Details: {str({"product_id_type": type(self.product_id), "value_type": type(val)})}')
        return e

    def set_publish_count(self, val):
        if type(val) is type(self.publish_count):
            self.publish_count = val
            return None

        e = Exception('post_model.set_publish_count.unsupported_datatype')
        ErrorLogger.error(f'post_model.set_publish_count.unsupported_datatype. Details: {str({"publish_count_type": type(self.publish_count), "value_type": type(val)})}')
        return e
