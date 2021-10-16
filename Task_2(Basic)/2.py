if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    l = list(dict.fromkeys(arr)) 
    m = max(l)
    l.remove(max(l))
    print(max(l))