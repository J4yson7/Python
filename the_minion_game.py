s = str(input().upper())

vow = 'AEIOU'

st = 0
kv = 0

for i in range(len(s)):
    if s[i] in vow:
        kv += (len(s)-i)
    else:
        st += (len(s)-i)

print(st, " " ,kv)
# 6+4 10+2 12
# 