#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6
# T(f) = T(c) (9/5) + 32
d={'BLR':28,'CHN':34,'HYD':32}
# for k,v in d.items():
    # v = (v * (9 / 5) + 32)
    # print("Temperature of '{}' is {} farenheits".format(k, v))
    # d[k] = v * 9/5 + 32
    # print("Temperature of '{}' is {} farenheits".format(k,d[k]))

# for sorting based on values
for k,v in d.items():
    for v1 in d.values():
        if v < v1:
            print("Temperature of '{}' is {} farenheits".format(k, v))
            continue


