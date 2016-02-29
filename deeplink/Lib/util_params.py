from urlparse import urlparse, parse_qs
import json
from generate_func.consts import CHOICE_NAME
def get_params(url, output):
    p = urlparse(url)
    params = parse_qs(p.query)
    result = {'params': list(set(params.keys())), 'select_options':CHOICE_NAME}
    if output=='json': return json.dumps(result)
    return list(set.params.keys())

