<html>
<head>
    <title>${next.title()}</title>
    ${self.css()}
</head>
<body>
    ${self.header()}
    ${next.heading()}
    ${next.body()}
    ${self.footer()}
</body>
</html>

<%def name="css()">
    <link rel="stylesheet" type="text/css" href="/css/main.css">
</%def>

<%def name="header()">
    <p><a href="/">Chestnut</a></p>
    <p><a href="/aliases/create_alias_form">Create an alias</a></p>
    <p><a href="/aliases/displayAll">See all aliases</a></p>
<!--    <p><a href="/about.html">About Chestnut</a></p> -->
    <hr />
</%def>

<%def name="footer()">
    <br /><br />
    <hr />
    <div id='footer'>
    Designed by an engineer. Built by a CMU CS major. <br />
    Want to contact us? Email Chestnut at aguo@andrew.cmu.edu
    </div>
</%def>
