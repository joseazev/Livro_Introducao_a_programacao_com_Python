s1 = 'CTA'
s2 = 'ABC'
s3 = ''
for sa in s2:
    if sa not in s1:
       s3 = s3 + sa

for sa in s1:
    if sa not in s2:
        s3 = s3 + sa

print(s3)
