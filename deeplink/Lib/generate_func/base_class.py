
INDENT = '    '


class FuncLine(object):
    __doc__ = """
    This file is aimed to provide basic function line as an object.
    Generate() is able to return a function line with indent choosen
    """

    def __init__(self, content='', next_indent_level_change=0, indent_level=-1):
        __doc__ = """
        next_indent_level_change is used to control next line's additional indent
        indent_level is used to control current line's indent with respect to function starting line

        indent level is currently not in use."""

        self.content = content
        self.next_indent_level_change = next_indent_level_change
        self.indent_level = indent_level


    def generate(self, current_level):
        if current_level<0: raise ValueError
        return INDENT*(current_level) + self.content + '\n'


class Func(object):
    __doc__ = """
    This class is the basics for function auto-creation
    It involves header() to create function line
    It involves body() to create function body
    It will generate function line with proper indent.
    """

    def __init__(self, func_def_indent_level=0):
        self.func_def_indent_level = func_def_indent_level
        self.func_lines = []

    def add(self, new_line):
        self.func_lines.append(new_line)

    def generate_function(self):
        content = ''
        start = self.func_def_indent_level
        for func_line in self.func_lines:
            if func_line.indent_level<0:
                content += func_line.generate(start)
                start += func_line.next_indent_level_change
            else:
                start = func_line.indent_level
                content += func_line.generate(start+self.func_def_indent_level)
        return content