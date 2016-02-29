
#!/usr/bin/env python
"""A simple Sawmill CLI tool
::
    $ python sawmill/cli.py
    $ python sawmill/cli.py tail searches
    $ python sawmill/cli.py tail searches --size 20
    $ python sawmill/cli.py tail searches --size 20 --market SG
    $ python sawmill/cli.py tail searches --size 20 --website-id vair
"""

import click
from Lib.util_diff import url_compare
from Lib.util_params import get_params
from Lib.generate_func.generate_func import generate_func



@click.group()
def deeplink():
    pass


@click.group()
def util():
    """deeplink util diff --url1 --url2 will provide url comparison result
       example:
       deeplink util diff --url1="www.google.com?x=2&y=1" --url2="wwww.x.com?x=3"
       Quotes could not be omitted!
    """
    pass

@click.command(name='diff')
@click.option('--url1', default="")
@click.option('--url2', default="")
def diff(url1, url2):
    """Compare URL1 and URL2"""

    if url1 == "" or url2 == "":
        print "URL could not be empty"
    else:
        print url_compare(url1, url2)




@click.command(name='params')
@click.option('--url', default="")
@click.option('--output', default="json")
def params(url, output):
    """Generate Params FOR URL"""
    print get_params(url, output)




@click.group()
def generate():
    """deeplink generate
       example:
       deeplink util diff --url1="www.google.com?x=2&y=1" --url2="wwww.x.com?x=3"
       Quotes could not be omitted!
    """
    pass


@click.command(name='fun')
@click.option('--depth', default='D', type=click.Choice(['H', 'D', 'B']))
@click.option('--mobile', default='F', type=click.Choice(['F', 'T']))
@click.option('--use_cache', default='F', type=click.Choice(['F', 'T']))
@click.option('--use_class', default='T', type=click.Choice(['F', 'T']))
@click.option('--url', default="")
@click.option('--options', default="{}")
def fun(depth, mobile, use_cache, use_class, url, options):
    print generate_func(depth, mobile, use_cache, use_class, url, options)





deeplink.add_command(util)
util.add_command(diff)
util.add_command(params)



deeplink.add_command(generate)
generate.add_command(fun)

if __name__ == "__main__":
    deeplink()