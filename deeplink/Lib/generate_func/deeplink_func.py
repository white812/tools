
from consts import HOMEPAGE, DAYVIEW, BOOKINGPAGE
from consts import CHOICES
from deeplink_util_func import DeeplinkUtilFunc
import json
from datetime import date





class DeeplinkFunc(DeeplinkUtilFunc):
    def __init__(self, depth, is_mobile, use_cache, use_class, url, options):
        super(DeeplinkFunc, self).__init__(depth, is_mobile, use_cache, use_class, url, options)

    # correspond to frontend request /api/processOptions
    def get_code(self):
        response = {'is_code': True,
                    'code_text': self.func.generate_function()}
        return json.dumps(response)

    def generate_function(self):
        self.func_def_line()
        self.func_body_lines()
        function_string =  super(DeeplinkFunc, self).generate_function()
        function_string = self.get_header() + function_string
        function_string += self.get_register()
        return function_string


    # const headers/registers
    def get_header(self):
        if self.use_class:
            return """from sw4 import cordyceps as c
from sw4.cordyceps.skyscanner.deeplink_base import BaseDeeplink
from transport import register as trans_register

class XXXXDeeplink(BaseDeeplink):
"""
        else:
            return """from sw4 import cordyceps as c
from transport import register as trans_register

"""

    def get_register(self):
        if self.use_class:
            return """
register = c.register_transport_deeplink(
    XXXXDeeplink().deeplink,
    support=c.DeeplinkSupport(
            reviewed_date=c.DateTime('{today}'),
            possible='UHDB',
            implemented='UHDB',
            notes='',
            passenger_limits=''
    ),
    transport_register=trans_register
)""".format(today=date.today().strftime("%Y-%m-%d"))
        else:
            return """
register = c.register_transport_deeplink(
    deeplink,
    support=c.DeeplinkSupport(
            reviewed_date=c.DateTime('{today}'),
            possible='UHDB',
            implemented='UHDB',
            notes='',
            passenger_limits=''
    ),
    transport_register=trans_register
)""".format(today=date.today().strftime("%Y-%m-%d"))
