#!/usr/bin/python
# -*- coding:utf-8 -*-
class Different:
    def checkDifferent(self, iniString):
        n = len(iniString)
        c = []
        state = False
        if (n > 3000):
            return state
        for s in iniString:
            if(ord(s)>255 ):
                return state
            else:
                c.append(ord(s))
                d = set(c)
        if (len(d)< n):
            return state
        else:
            state = True
            return state