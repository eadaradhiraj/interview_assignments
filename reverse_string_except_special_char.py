#!/usr/bin/python
# -*- coding: utf-8 -*-


def reverse_string(s: str) -> str:
    (resc, res, ss) = ([], [], '')
    if s[0].isalpha():
        resc.append('')
        ss += s[0]
    else:
        resc.append(s[0])
    for i in range(1, len(s)):
        if s[i].isalpha() and s[i - 1].isalpha():
            ss += s[i]
            continue
        else:
            if s[i].isalpha():
                ss += s[i]
                resc.append('')
            else:
                if ss:
                    res.append(ss[::-1])
                ss = ''
                if not s[i].isalpha() and not s[i - 1].isalpha():
                    resc[-1] += s[i]
                else:
                    resc.append(s[i])
    if ss:
        res.append(ss[::-1])
    cntr = len(res) - 1
    for i in range(len(resc)):
        if not resc[i]:
            resc[i] = res[cntr]
            cntr -= 1
    return ''.join(resc)
