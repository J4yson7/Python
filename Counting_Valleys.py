if __name__ == '__main__':
    n = int(input())
    s = input()
    d,val = 0,0
    for i in s:
        if i == "U": d += 1
        else: d -= 1

        if d == -1 and i == 'D': val += 1 

    print(val)