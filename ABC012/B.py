n = int(input())
hour = n//3600
n -= 3600*hour
minute = n//60
n -= 60*minute
second = n

print("%02d:%02d:%02d" %(hour, minute, second))