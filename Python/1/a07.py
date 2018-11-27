## IMPORTS GO HERE
## END OF IMPORTS


### YOUR CODE FOR split_safe() FUNCTION GOES HERE ###
def split_safe(x):
    word=""
    c=0
    e=[]
    for letter in x:
        if letter!=",":
            word=word+letter
            c=c+1
        elif letter=="," or letter==x[-1]:
            
            word=word.strip()
            if word[0]=="'":
                if word[-1]!="'":
                        word=word+","
                elif word[-1]=="'":
                    word=word[1:-1]
                    e.append(word)
                    word=""
             
            else:
               
                e.append(word)
                word=''
                c=c+1
        #for the last lettter in input
    if c is 0:
       return e
    elif word[0] and word[-1] is "'":
        word=word[1:-1]
    word=word.strip()
    e.append(word)
    return e 

#### End OF MARKER



### YOUR CODE FOR read_data() FUNCTION GOES HERE ###
def read_data(x,y):
    import os
    h=os.path.join(x,y)
    e=[]
    with open(h,"r") as f:
        for line in f:
            s=split_safe(line)
            e.append(s)
        return e
    
#### End OF MARKER

if __name__ == '__main__':
    print(split_safe("Name,'Father Name',Address,Age"))
    print(split_safe("Ali,Tariq,'House 10, Street 20',30"))

    print(read_data('', 'file.csv'))
    pass
