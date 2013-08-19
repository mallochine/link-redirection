# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1371445732.2221169
_enable_loop = True
_template_filename = '/home/ec2-user/practice/practice/templates/derived/all_aliases.mako'
_template_uri = '/derived/all_aliases.mako'
_source_encoding = 'utf-8'
from markupsafe import escape
_exports = ['makerow', 'heading', 'title']


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
        c = context.get('c', UNDEFINED)
        def makerow(alias):
            return render_makerow(context.locals_(__M_locals),alias)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 3
        __M_writer(u'\n\n')
        # SOURCE LINE 7
        __M_writer(u'\n\n<table>\n    <tr>\n        <th>Name</th>\n        <th>URL</th>\n    </tr>\n\n')
        # SOURCE LINE 15
        for alias in c.aliases:
            # SOURCE LINE 16
            __M_writer(u'        ')
            __M_writer(escape(makerow(alias)))
            __M_writer(u'\n')
        # SOURCE LINE 18
        __M_writer(u'</table>\n\n')
        # SOURCE LINE 25
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_makerow(context,alias):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 20
        __M_writer(u'\n    <tr>\n        <td>')
        # SOURCE LINE 22
        __M_writer(escape(alias.name))
        __M_writer(u'</td>\n        <td>')
        # SOURCE LINE 23
        __M_writer(escape(alias.url))
        __M_writer(u'</td>\n    </tr>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer(u'\n    <h1>All Aliases</h1>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'All Aliases')
        return ''
    finally:
        context.caller_stack._pop_frame()


