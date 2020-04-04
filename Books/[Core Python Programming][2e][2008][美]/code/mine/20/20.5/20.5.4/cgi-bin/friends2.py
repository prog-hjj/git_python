#!/usr/bin/env python

import cgi

header = 'Content-Type: text/html\n\n'

formhtml = '''
<html>
<head>
    <title>Friends CGI Demo</title>
</head>
<body>
    <h3>Friends list for: <i>NEW USER</i></h3>
    <form action="/cgi-bin/friends2.py">
        <b>Enter your Name:</b>
        <input type="hidden" name="action" value="edit">
        <input type="text" name="person" value="NEW USER" size="15">
        <p>
        <b>How many friends do you have?</b>
        %s
        <p>
        <input type="submit">
    </form>
</body>
</html>'''

fradio = '<input type="radio" name="howmany" value="%s" %s> %s\n'

def showForm():
    friends = ''
    for i in [0, 10, 25, 50, 100]:
        checked = ''
        if i == 0:
            checked = 'checked'
        friends = friends + fradio % (str(i), checked, str(i))

    print header + formhtml % (friends)

reshtml = '''<html>
<head>
    <title>Friends CGI Demo</title>
</head>
<body>
    <h3>Friends list for: <i>%s</i></h3>
    Your name is: <b>%s</b><p>
    You have <b>%s</b> friends.
</body>
</html>'''

def doResults(who, howmany):
    print header + reshtml % (who, who, howmany)

def process():
    form = cgi.FieldStorage()
    if form.has_key('person'):
        who = form['person'].value
    else:
        who = 'NEW USER'

    if form.has_key('howmany'):
        howmany = form['howmany'].value
    else:
        howmany = 0

    if form.has_key('action'):
        doResults(who, howmany)
    else:
        showForm()

if __name__ == '__main__':
    process()
