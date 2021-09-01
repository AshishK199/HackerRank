def check(s):
c=0
for i in range(0,len(s)):
for j in range(i+1,len(s)+1):
k=s[i:j]
if((len(k)>=4) and ((‘/’ in k) and (‘\\’ in k)) and (k[0].isalpha()) and (k.index(‘/’)<k.index('\\')) and (k[k.index('\\')+1:].isalpha())):
c=c+1
# print(k)
return c
print(check(r'w:/a\bc::/12\xyz'))