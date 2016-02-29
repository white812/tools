__author__ = 'yingbozhan'


DEEPLINK_DEPTH = {
    1: dict(name='home_page',
            func='HomePage()',
            short='H'),
    2: dict(name='day_view',
            func='DayView()',
            short='D'),
    3: dict(name='booking_page',
            func='BookingPage()',
            short='B')
}

MOBILE = 'mobile'
DESKTOP = 'desktop'

HOMEPAGE = 1
DAYVIEW = 2
BOOKINGPAGE = 3



DEPARTURE_AIRPORT_CODE = 1
ARRIVAL_AIRPORT_CODE = 2
DEPARTURE_DATE = 3
ARRIVAL_DATE = 4
NUMBER_OF_ADULTS = 5
NUMBER_OF_CHILDREN = 6
NUMBER_OF_INFANTS = 7
CABIN = 8
DEEPLINK_RELATED = 9
USEFUL_NEED_CHANGE = 10
IGNORE_IT = 0

CHOICE_NAME = (
    'IGNORE_IT',
    'DEPARTURE_AIRPORT_CODE',
    'ARRIVAL_AIRPORT_CODE',
    'DEPARTURE_DATE',
    'ARRIVAL_DATE',
    'NUMBER_OF_ADULTS',
    'NUMBER_OF_CHILDREN',
    'NUMBER_OF_INFANTS',
    'CABIN',
    'DEEPLINK_RELATED',
    'USEFUL_NEED_CHANGE',
)

CHOICES = {ARRIVAL_DATE: 'Arrival_Date',
           NUMBER_OF_ADULTS: 'Number_of_Adults',
           DEPARTURE_DATE: 'Departure_Date',
           ARRIVAL_AIRPORT_CODE: 'Arrival_Airport_Code',
           DEPARTURE_AIRPORT_CODE: 'Departure_Airport_Code',
           NUMBER_OF_INFANTS: 'Number_of_Infants',
           NUMBER_OF_CHILDREN: 'Number_of_Children',
           CABIN: 'Cabin',
           DEEPLINK_RELATED: 'Deeplink_Related',
           USEFUL_NEED_CHANGE: 'Useful_Need_Change',
           IGNORE_IT: 'Ignore it, no use!'}