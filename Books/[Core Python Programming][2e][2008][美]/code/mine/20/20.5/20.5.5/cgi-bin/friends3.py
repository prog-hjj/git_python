#!/usr/bin/env python

import cgi
from urllib import quote_plus
from string import capwords

header = 'Content-Type: text/html\n\n'
url = '/cgi-bin/friends3.py'

errhtml = '''
<html>
<head>
    <title>Friends CGI Demo</title>
</head>
<body>
    <h3>ERROR</h3>
    <b>%s</b>
    <p>
    <form>
        <input type="button" value="Back" onclick="window.history.back()">
    </form>
</body>
</html>'''

def showError(error_str):
    print header + errhtml % (error_str)

formhtml = '''
<html>
<head>
    <title>Friends CGI Demo</title>
</head>
<body>
    <h3>Friends list for: <i>%s</i></h3>
    <form action="%s">
        <b>Enter your Name:</b>
        <input type="hidden" name="action" value="edit">
        <input type="text" name="person" value="%s" size="15">
        <p>
        <b>How many friends do you have?</b>
        %s
        <p>
        <input type="submit">
    </form>
</body>
</html>'''

fradio = '<input type="radio" name="howmany" value="%s" %s> %s\n'

def showForm(who, howmany):
    friends = ''
    for i in [0, 10, 25, 50, 100]:
        checked = ''
        if str(i) == howmany:
            checked = 'checked'
        friends = friends + fradio % (str(i), checked, str(i))

    print header + formhtml % (who, url, who, friends)

reshtml = '''<html>
<head>
    <title>Friends CGI Demo</title>
</head>
<body>
    <h3>Friends list for: <i>%s</i></h3>
    Your name is: <b>%s</b><p>
    You have <b>%s</b> friends.
    <p>
    Click <a href="%s">here</a> to edit your data again.
</body>
</html>'''

def doResults(who, howmany):
    newurl = url + '?action=reedit&person=%s&howmany=%s' % \
        (quote_plus(who), howmany)
    print header + reshtml % (who, who, howmany, newurl)

def process():
    error = ''
    form = cgi.FieldStorage()

    if form.has_key('person'):
        who = capwords(form['person'].value)
    else:
        who = 'NEW USER'

    if form.has_key('howmany'):
        howmany = form['howmany'].value
    else:
        if form.has_key('action') and \
                form['action'].value == 'edit':
            error = 'Please select number of friends.'
        else:
            howmany = 0

    if not error:
        if form.has_key('action') and \
                form['action'].value != 'reedit':
            doResults(who, howmany)
        else:
            showForm(who, howmany)
    else:
        showError(error)

if __name__ == '__main__':
    process()
