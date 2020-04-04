#!/usr/bin/env python

# Greeting in English, Spanish, Chinese and Japanese
CODEC = 'UTF-8'
UNICODE_HELLO = u'''
Hello!
\u00A1Hola!
\u4F60\u597D!
\u3053\u3093\u306B\u3061\u306F!
'''

header = 'Content-Type: text/html; charset=%s\n\n' % (CODEC)

html = '''
<html>
<head>
    <title>Unicode CGI Demo</title>
</head>
<body>
    %s
</body>
</html>''' % (UNICODE_HELLO.encode(CODEC))

print header + html
