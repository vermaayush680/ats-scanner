import pandas as pd
def counter(clean_jd):
    d={}
    for i,val in enumerate(clean_jd):
        d[val] = d.get(val,0)+1

    d1 = dict(sorted(d.items(), key=lambda item: item[1],reverse=True))

    col1 = d1.keys()
    col2 = d1.values()

    
    data = pd.DataFrame({'KeyWords':col1,'Count In Job Description':col2})
    return(data)