s1 = 'AATTGGAA'
s2 = 'TG'
s3 = ''

for s in s1:
    if s not in s2:
        s3 = s3 + s
    
print(s3)
