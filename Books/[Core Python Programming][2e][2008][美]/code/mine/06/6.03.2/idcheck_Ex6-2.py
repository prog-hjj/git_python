#!usr/bin/env python

import string

alphas = string.letters + '_'
alnums = alphas + string.digits

iden = raw_input('Identifier to check? ')

if len(iden) > 0:
    if iden[0] not in alphas:
        print "Error: first char must be alphabetic"
    else:
        if len(iden) > 1:
            for eachChar in iden[1:]:
                if eachChar not in alnums:
                    print "Error: others must be alnum"
                    break
            else:
                import keyword
                if iden not in keyword.kwlist:
                    print 'ok'
                else:
                    print 'Error: keyword name'
else:
    print 'Error: no identifier entered'
