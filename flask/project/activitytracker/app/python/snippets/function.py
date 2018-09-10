def printing(a,b,c):
   print a,b,c

def addition(*values):
    sum=0
    for val in values:
        sum+=val
    return sum

def var_key(**vargs):
    for key in vargs:
        print key, vargs[key]
         
if __name__ == "__main__":
    val = [1,2,3]
    printing(*val)
    printing(3,4,5)
    printing(a=20, b=12,c=13)
    print addition(1,2,3)
    print addition(1,2,3,5)
    var_key(name="tanigai", marks=23)
   
