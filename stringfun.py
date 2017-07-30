def string_test(s):
    if len(s)>2 and s[0] == s[-1]:
        return(True)
    else:
        return(False)


def add_x(s):
    #s = input('give me a string: ')
    a=  'x'+ s +'x'
    return(a)
        
    
#for i in range(1000):
#    answer = add_x('hi')
#    print(answer)

def add_strings(s,a,d):
    c = s+a+d
    return c
