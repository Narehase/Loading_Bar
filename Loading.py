def Loading(max_, ins_):
    lo = "["
    pis = (max_-1) / 30.
    od = ins_/pis +1
    for i in range(30):    
        if round(od) > i:
            lo+= "="
        elif round(od) == i:
            lo+= ">"
        else:
            lo+= "."

    Al =  "{0} / {1}".format(max_-1, ins_) + "                      "
    if max_-1 == ins_:
        print(Al[:16]+lo+"]")
    else:
        print(Al[:16]+lo+"]", end="\r")
