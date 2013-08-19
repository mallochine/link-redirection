<%inherit file="/base/index.mako"/>

<%def name="title()">Create an Alias</%def>

<%def name="heading()">
    <h1>Create an Alias</h1>
</%def>

Note: it is important to specify http:// or https:// at the beginning
of the URL! <br><br>

Example: 'chestnut' with 'http://54.214.49.23/'<br /><br />

<form method="post" action="/aliases/create">
    Alias: <input type='text' name='name' size='20' /> <br />
    URL: <input type='text' name='url' /> <br />
    <input type='submit' />
</form>
