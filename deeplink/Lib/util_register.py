def get_register(use_class):
    if use_class:
        return """
register = c.register_transport_deeplink(
    XXXXDeeplink().deeplink,
    support=c.DeeplinkSupport(
            reviewed_date=c.DateTime('%s'),
            possible='UHDB',
            implemented='UHDB',
            notes='',
            passenger_limits=''
    ),
    transport_register=trans_register
)"""
    else:
        return """
register = c.register_transport_deeplink(
    deeplink,
    support=c.DeeplinkSupport(
            reviewed_date=c.DateTime('%s'),
            possible='UHDB',
            implemented='UHDB',
            notes='',
            passenger_limits=''
    ),
    transport_register=trans_register
)"""

