def convert_seconds(a):
    hr = a/3600
    a = a%3600
    mn = a/60
    a = a%60
    return str(int(hr)) +" hour, "+str(int(mn))+" minute, "+ str(int(a)) +" second"
