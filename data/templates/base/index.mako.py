# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1371447877.376817
_enable_loop = True
_template_filename = u'/home/ec2-user/practice/practice/templates/base/index.mako'
_template_uri = u'/base/index.mako'
_source_encoding = 'utf-8'
from markupsafe import escape
_exports = ['header', 'css', 'footer']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        next = context.get('next', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<html>\n<head>\n    <title>')
        # SOURCE LINE 3
        __M_writer(escape(next.title()))
        __M_writer(u'</title>\n    ')
        # SOURCE LINE 4
        __M_writer(escape(self.css()))
        __M_writer(u'\n</head>\n<body>\n    ')
        # SOURCE LINE 7
        __M_writer(escape(self.header()))
        __M_writer(u'\n    ')
        # SOURCE LINE 8
        __M_writer(escape(next.heading()))
        __M_writer(u'\n    ')
        # SOURCE LINE 9
        __M_writer(escape(next.body()))
        __M_writer(u'\n    ')
        # SOURCE LINE 10
        __M_writer(escape(self.footer()))
        __M_writer(u'\n</body>\n</html>\n\n')
        # SOURCE LINE 16
        __M_writer(u'\n\n')
        # SOURCE LINE 24
        __M_writer(u'\n\n')
        # SOURCE LINE 33
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 18
        __M_writer(u'\n    <p><a href="/">Chestnut</a></p>\n    <p><a href="/aliases/create_alias_form">Create an alias</a></p>\n    <p><a href="/aliases/displayAll">See all aliases</a></p>\n<!--    <p><a href="/about.html">About Chestnut</a></p> -->\n    <hr />\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_css(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 14
        __M_writer(u'\n    <link rel="stylesheet" type="text/css" href="/css/main.css">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 26
        __M_writer(u"\n    <br /><br />\n    <hr />\n    <div id='footer'>\n    Designed by an engineer. Built by a CMU CS major. <br />\n    Want to contact us? Email Chestnut at aguo@andrew.cmu.edu\n    </div>\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


