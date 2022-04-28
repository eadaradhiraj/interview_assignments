#Return path where value is equal to t

def fnd(d,t,s=[]):
    for i in d:
        if type(d[i]) == dict:
            cres = fnd(d[i],t,s+[i])
            if not cres:
                continue
            return cres
        else:
            if d[i] == t:
                return s+[i]
    return ""

print(fnd(d={"a":{"f":1,"b":{"c":{"d":2}}},"d":{"e":3},"g":4},t=2))
