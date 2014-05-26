#-*- coding: utf-8 -*-
import re


class MyNews:
    def __init__(self, n, a, d):
        self.no = n
        self.agency = a
        self.date = d ## convert to datatime next time
        self.title = ""
        self.content = ""
        self.id = ""
        self.tags = [] # detected by re
        self.board = "" # detected by re
        self.category = "" # detected by re
        self.contries = [] # detected by re

def preprocessing():
    linedata = []
    fin = open("newstext.txt", "r")
    t_ctr = 0
    fout = file('newdata.txt', "w")
    for line in fin:
        line = line.strip()
        if len(line)>1 and "慧科" not in line:
            if "文章編號" in line:
                t_ctr += 1
            fout.write("%s\n"%(line))
            linedata.append(line)
    return linedata, t_ctr

def createDB(indata):
    news_ctr = 0
    linedb = []
    level = 0
    temp = []
    i = 0
    while i < len(indata):
        mat = re.match('(.*)[.]\s*(.*)\s*[|].*(\d{4}[-/]\d{2}[-/]\d{2})', indata[i])
        if mat is not None:
            level = 1
            temp = list(mat.groups())
            ns = MyNews(temp[0], temp[1], temp[2])
            news_ctr += 1
#             tagtemp = indata[i+1].strip().split('|')
#             for tag in tagtemp:
#                 tag = tag.strip()
            i+=2
        elif level == 1: #match title
            ns.title = indata[i].strip() #title
            i+=2
            level = 2
        elif level == 2:
            matid = re.match('文章編號.*\[(\d{15})\]', indata[i])
            if matid is not None:
                ns.id = list(matid.groups())[0]
                linedb.append(ns)
                level = 0
            else:
                ns.content+=indata[i]
            i+=1
        else:
            i+=1
    print news_ctr
    return linedb

def print2Dlist(inlist):
    for ns in linedb:
        print "="*20
        print ns.no, ns.id, ns.title
        print ns.content
if __name__=="__main__":
    linedata, news_ctr = preprocessing()
    linedb = createDB(linedata)
    print2Dlist(linedb)
    print "LENGTH OF DATABASE IS %d"%(len(linedb))
