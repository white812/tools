__author__ = 'yingbozhan'

import sys
from urlparse import urlparse, parse_qs



def url_compare(url1, url2):
    diff = compare_path(url1, url2) + '\n'
    diff += compare_params(url1, url2)
    return diff

def compare_path(url1, url2):
    try:
        p1 = urlparse(url1)
        p2 = urlparse(url2)
    except:
        return "URL is not in the right format!"
    if p1.scheme == p2.scheme and p1.netloc==p2.netloc and p1.path==p2.path:
        return "HOST PATH ARE THE SAME\n"
    else:
        diff = ''
        diff += "HOST PATH ARE DIFFERENT\n"
        diff += "1st URL: " + p1.scheme+'://'+p1.netloc+p1.path+'\n'
        diff += "2nd URL: " + p2.scheme+'://'+p2.netloc+p2.path+'\n'
        return diff


def compare_params(url1, url2):
    p1 = urlparse(url1)
    params1 = parse_qs(p1.query)
    p2 = urlparse(url2)
    params2 = parse_qs(p2.query)

    p1_key = set(params1.keys())
    p2_key = set(params2.keys())

    diff_p1_p2 = p1_key - p2_key
    diff_p2_p1 = p2_key - p1_key

    # print diff_p1_p2
    # print diff_p2_p1

    diff = ''

    if len(diff_p1_p2) > 0:
        diff += "1st URL contains more Keys: " + ','.join(diff_p1_p2) +'\n'
    if len(diff_p2_p1) > 0 :
        diff +=  "2nd URL contains more Keys: " + ','.join(diff_p2_p1) +'\n'
    if len(diff_p1_p2)==0 and len(diff_p2_p1)==0:
        diff += "Both URL contains same set of keys\n"

    diff += '\n'

    inter_sect = p1_key.intersection(p2_key)
    for key in inter_sect:
        if params1[key] != params2[key]:
            diff +=  "Key {key}\n- 1st URL : {value1}\n- 2nd URL : {value2}\n\n".format(
                key=key,
                value1=params1[key],
                value2=params2[key],
            )
    return diff



def main():
    option = raw_input("""
1. URL Comparison
0. Exit
    """)

    try:
        option = int(option)
    except:
        main()

    if option == 0:
        sys.exit(0)
    elif option == 1:
        try:
            print url_compare(raw_input("URL1:\n"), raw_input("URL2:\n"))
        except:
            main()


#main()
