<%inherit file="/base/index.mako"/>

<%def name="title()">All Aliases</%def>

<%def name="heading()">
    <h1>All Aliases</h1>
</%def>

<table>
    <tr>
        <th>Name</th>
        <th>URL</th>
    </tr>

    % for alias in c.aliases:
        ${makerow(alias)}
    % endfor
</table>

<%def name="makerow(alias)">
    <tr>
        <td>${alias.name}</td>
        <td>${alias.url}</td>
    </tr>
</%def>
