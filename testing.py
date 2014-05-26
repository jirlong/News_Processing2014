#-*- coding: utf-8 -*-
import datetime
import re

def valid_date(datestring):
        try:
                mat=re.match('(.*)(\d{4})[-/](\d{2})[-/](\d{2})', datestring)
                if mat is not None:
                        print mat.groups()
                        return True
        except ValueError:
                pass
        return False
print valid_date("abc 2014-08-09")


matid = re.match('文章編號.*\[(\d{15})\]', '文章編號文章編號: [201302105303346]')
if matid is not None:
    print list(matid.groups())
else:
    print "ERROR"