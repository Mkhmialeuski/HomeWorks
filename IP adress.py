def ip(s):
    for i in s:
        try:
            int(i)
            if 0 <= int(i) <= 255:
                continue
            else:
                return False
        except TypeError:
            return False
        except ValueError:
            return False
    return True
stri = input()
n =stri.count('.')
a = False
if n == 3:
    s = stri.split('.')

    for i in range(len(s)):
        if 1<len(s[i])<=3 and s[i]== 0:
            a = True
            break

    if a == False and ip(s):
           print('.'.join(s))
           print('yes')
    else:
        print('no')
else:
    print('no')