n = int(input())
if n % 2 == 1:
    print("Weird")
elif n % 2 == 0 & 2 <= n <=5:
    print("Not Weird")
elif n % 2 == 0 & 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")