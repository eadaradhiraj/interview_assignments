#!/usr/bin/python
# -*- coding: utf-8 -*-


def reverse_string(s):
    (res, ss) = ([], '')
    for c in s:
        if c.isalpha():
            ss += c
        else:
            res.append(ss[::-1])
            ss = ''
            res.append(c)
    res.append(ss[::-1])
    return ''.join(res)
