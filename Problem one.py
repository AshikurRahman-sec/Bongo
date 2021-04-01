a = {"key1": 1,"key2": {"key3": 1,"key4": {"key5": 4}}}

def display_dic(b,n=1):
    for i in b:
        if not isinstance(b[i],dict):
            print(i,n)
        else:
            print(i,n)
            display_dic(b[i],n=n+1)

display_dic(a)
