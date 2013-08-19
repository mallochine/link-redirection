# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1371522334.7445669
_enable_loop = True
_template_filename = '/home/ec2-user/practice/practice/templates/derived/aliases/alias_cli.mako'
_template_uri = '/derived/aliases/alias_cli.mako'
_source_encoding = 'utf-8'
from markupsafe import escape
_exports = ['heading', 'title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base/index.mako', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 3
        __M_writer(u'\n\n')
        # SOURCE LINE 7
        __M_writer(u'\n\n<form method="get" action="/aliases/from_web_form">\n    Type where you want to go: <input type=\'text\' name=\'query\' />\n    <input type=\'submit\' value=\'Go\' />\n</form>\n\nExample: typing in \'chestnut\' will go to http://54.214.49.23/\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer(u'\n    <h1>Chestnut</h1>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'Chestnut')
        return ''
    finally:
        context.caller_stack._pop_frame()


