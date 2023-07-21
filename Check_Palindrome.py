string_ = str(input("Enter the string: "))
n=len(string_)-1
start=0
def check_pal(string_,start,end):
    if end<=1:
        return True
    if start>=end:
        return True
    elif string_[start]==string_[end]:
        return check_pal(string_,start+1,end-1)
    else:
        return False
if check_pal(string_,start,n):
    print("1")
else:
    print("0")