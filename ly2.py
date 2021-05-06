ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def base62_encode(num,alphabet=ALPHABET):
    """
    10进制转62进制
    :param num:
    :param alphabet:
    :return:
    """
    if num ==0:
        return alphabet[0]
    arr=[]
    base=len(alphabet)
    while num:
        rem=num%base
        num=num//base
        arr.append(alphabet[rem])
    arr.reverse()
    return ''.join(arr)
def base62_decode(string,alphbet=ALPHABET):
    """
    62进制转10进制
    :param string:
    :param alphabet:
    :return:
    """
    base=len(alphbet)
    strlen=len(string)
    num=0
    idx=0
    for cher in string:
        power=strlen-(idx+1)
        num=alphbet.index(cher)*(base**power)
        idx+=1
    return num
if __name__=='__main__':
    print(base62_encode(4302842))
    print(base62_decode('i3mG'))













