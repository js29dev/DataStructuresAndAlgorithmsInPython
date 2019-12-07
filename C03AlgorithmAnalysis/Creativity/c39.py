"""
S = 1/2 + 2/4 + 3/8 + 4/16 + 5/32 ...

S1 = 1/2                    = 2 - 3/2
S2 = 1/2 + 2/4    = 4/4     = 2 - 4/4
S3 = 4/4 + 3/8    = 11/8    = 2 - 5/8
S4 = 11/8 + 4/16  = 26/16   = 2 - 6/32
S5 = 26/16 + 5/32 = 57/64   = 2 - 7/64

Sn = n/(2^n) + (n-1)/(2^(n-1)) + (n-2)/(2^(n-2)) ...
   = 1(n-0)/(2^n) + 2(n-1)/(2^n) + 4(n-2)/(2^n) ...
   = (1(n-0) + 2(n-1) + 4(n-2) + 8(n-3)...) / (2^n)
   = (2^(n+1)-1 - something) / 2^n
   <= 2^(n+1)/2^n
   <= 2

Not sure about what I have done.
"""

total = 0
for i in range(1, 21):
    total += i / 2 ** i
    print(i, total, 2 - total)
