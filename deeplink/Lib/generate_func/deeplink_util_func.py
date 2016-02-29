__author__ = 'yingbozhan'

from urlparse import urlparse, parse_qs

from base_class import Func
from consts import *
from base_class import FuncLine


class DeeplinkUtilFunc(Func):
    def __init__(self, depth, is_mobile, use_cache, use_class, url, options):
        super(DeeplinkUtilFunc, self).__init__(1 if use_class else 0)
        self.depth = depth
        self.is_mobile = is_mobile
        self.url = url
        self.options = options
        self.use_class = use_class
        self.use_cache = use_cache



    ######util functions
    ##################################

    def get_depth_name(self,level=0):
        return DEEPLINK_DEPTH[self.depth+level]['name']

    def get_depth_func_name(self, level=0):
        return DEEPLINK_DEPTH[self.depth+level]['func']

    def update_url(self, url):
        self.url = url




    #####func lines
    #####################################
    def func_def_line(self):
        content = "def {is_mobile}_{depth_name}({class_object}query):".format(
            is_mobile='mobile' if self.is_mobile else 'desktop',
            depth_name=self.get_depth_name(),
            class_object="self, " if self.use_class else ""
        )
        self.add(FuncLine(content,1))


    def func_body_lines(self):
        if not self.use_cache:
            func_lines, deeplink = self.func_request_body()
        else:
            func_lines, deeplink = self.func_cached_request_body()

        if self.depth!=HOMEPAGE and not self.use_class and deeplink:
            self.add(FuncLine("try:", 1))

        for func_line in func_lines:
            self.add(func_line)

        ###handlie for try/catch
        if self.depth!=HOMEPAGE and not self.use_class and deeplink:
            self.func_lines[-1].next_indent_level_change -= 1
            self.add(FuncLine("except c.NotInCache:", 1))
            self.add(FuncLine("return {is_mobile}_{depth_name}(query)".format(
                                                is_mobile='mobile' if self.is_mobile else 'desktop',
                                                depth_name=self.get_depth_name(-1),
                                            ), -1))

        ###return line
        if self.use_class:
            self.add(FuncLine("return req", -1))
        else:
            self.add(FuncLine("return c.Deeplink(req, c.{func_name})".format(
                func_name=self.get_depth_func_name()), -1))


    def func_request_body(self):
        url_object = URLParsers(self.url, self.options, self.get_depth_name())
        func_lines, deeplink = url_object.generate_request_lines()
        return func_lines, deeplink


    def func_cached_request_body(self):
        return [
            FuncLine("req = query.deeplink_cache.get_deeplink(query, c.{func}, False)".format(
                func=self.get_depth_func_name()
            ))
        ], True







class URLParsers(object):
    def __init__(self, url, options, depth_func):
        self.url = url
        self.options = options
        self.depth_func = depth_func

        p = urlparse(self.url)
        self.params = parse_qs(p.query)
        self.host_path = p.scheme+'://'+p.netloc+p.path if len(p.scheme)>0 else 'http://'+p.netloc+p.path


    def get_request_creation(self):
        if len(self.options) == 0:
            return [FuncLine('req = c.request("'+self.url+'")')]
        return [FuncLine('req = c.request("'+self.host_path+'")')]



    def generate_request_lines(self):
        request_func_lines = self.get_request_creation()

        if len(self.options) == 0:
            return request_func_lines, False

        arg_dict, confirmed, might_change, return_related, \
            deeplink_data_related = self.parse_params()

        request_func_lines.append(FuncLine("from_id, to_id = query.iata_ids(prefer_city=False)"))
        if len(deeplink_data_related)>0:
            request_func_lines.append(FuncLine(
                "deeplink_data = query.deeplink_cache.get_deeplink(query, {func}, False)".format(
                    func=self.depth_func)))
        request_func_lines.append(FuncLine("get_args = {", 1))
        for key in confirmed:
            request_func_lines.append(FuncLine("'{key}': {value}".format(key=key, value=arg_dict[key])))

        request_func_lines.append(FuncLine("########FOLLOWING MIGHT NEED CHANGE######"))
        for key in might_change+deeplink_data_related:
            request_func_lines.append(FuncLine("'{key}': {value}".format(key=key, value=arg_dict[key])))

        request_func_lines[-1].next_indent_level_change = -1
        request_func_lines.append(FuncLine("}"))

        if len(return_related)>0:
            request_func_lines.append(FuncLine("if not query.one_way:", 1))
            for key in return_related:
                values = arg_dict[key].split(',#')
                request_func_lines.append(FuncLine("""get_args.update({key}={value}){value2}""".format(
                        key=key,
                        value=values[0],
                        value2='#'+arg_dict[key].split(',#')[1] if len(values)>1 else '' )))

            request_func_lines[-1].next_indent_level_change = -1

        request_func_lines.append(FuncLine("req.update_get(get_args)"))


        return request_func_lines, len(deeplink_data_related)>0


    def parse_params(self):
        arg_dict, confirmed, might_change, return_related, deeplink_data_related = {}, [], [], [], []
        for key, option in self.options.iteritems():
            value = self.params[key][0]
            if option == DEPARTURE_AIRPORT_CODE:
                arg_dict[key] = "from_id,"
                confirmed.append(key)
            elif option == ARRIVAL_AIRPORT_CODE:
                arg_dict[key] = "to_id,"
                confirmed.append(key)
            elif option == DEPARTURE_DATE:
                arg_dict[key] = "query.date_out.strftime(""),#require date format: "+value
                might_change.append(key)
            elif option == ARRIVAL_DATE:
                return_related.append(key)
                arg_dict[key] = "query.date_back.strftime(""),#require date format: "+value
            elif option == NUMBER_OF_ADULTS:
                confirmed.append(key)
                arg_dict[key] = "query.passengers.adults,"
            elif option == NUMBER_OF_CHILDREN:
                confirmed.append(key)
                arg_dict[key] = "query.passengers.children,"
            elif option == NUMBER_OF_INFANTS:
                confirmed.append(key)
                arg_dict[key] = "query.passengers.infants,"
            elif option == CABIN:
                might_change.append(key)
                arg_dict[key] = "query.cabin_class, #might require changes: "+value
            elif option == DEEPLINK_RELATED:
                arg_dict[key] = "deeplink_data[''], #pls fill in deeplink_data key"
                deeplink_data_related.append(key)
            elif option == USEFUL_NEED_CHANGE:
                arg_dict[key] = "'{value}',".format(value=value)
                might_change.append(key)
            elif option == IGNORE_IT:
                pass
        return arg_dict, confirmed, might_change, return_related, deeplink_data_related