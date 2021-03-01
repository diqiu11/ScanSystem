def check_ip(ipaddr):
    addr = ipaddr.strip().split('.')
    if len(addr) != 4:
        return False
    for i in range(4):
        try:
            addr[i] = int(addr[i])
        except:
            return False
        if addr[i]<=255 and addr[i]>=0:
            pass
        else:
            return False
    return True

def check_mask(mask):
    int_mask = int(mask)
    #print(int_mask)
    if int_mask<1 or int_mask>32:
        return False
    else:
        return True