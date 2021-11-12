# Enter your code here. Read input from STDIN. Print output to STDOUT
a = input()
ax = set(input().split())
#print(ax)
b = input()
bx = set(input().split())
#print(ax)

print(len(ax.intersection(set(bx))))