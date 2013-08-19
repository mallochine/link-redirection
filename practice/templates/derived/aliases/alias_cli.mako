<%inherit file="/base/index.mako"/>

<%def name="title()">Chestnut</%def>

<%def name="heading()">
    <h1>Chestnut</h1>
</%def>

<form method="get" action="/aliases/from_web_form">
    Type where you want to go: <input type='text' name='query' />
    <input type='submit' value='Go' />
</form>

Example: typing in 'chestnut' will go to http://54.214.49.23/
