smax = 255

q_range = 65
q_level = 64

q = smax / q_level

for i in reversed(range(q_range)):
    ans = i * q
    print("\n|",i,"|","\n",ans)