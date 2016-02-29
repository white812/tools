import json
from consts import *
from deeplink_func import DeeplinkFunc


def generate_func(depth, mobile, use_cache, class_structure, url, options):
    depth_mapping = {'H': HOMEPAGE, 'D': DAYVIEW, 'B': BOOKINGPAGE}
    true_false_mapping = {'T': True, 'F': False}
    depth = depth_mapping[depth]
    mobile = true_false_mapping[mobile]
    use_cache = true_false_mapping[use_cache]
    class_structure = true_false_mapping[class_structure]

    try:
        url = url.decode("hex")
        options = json.loads(options.decode("hex"))
        #print options
    except:
        url = url
        options = json.loads(options)


    #verifications options matched url

    #create objects
    df = DeeplinkFunc(depth, mobile, use_cache, class_structure, url, options)
    return df.generate_function()




