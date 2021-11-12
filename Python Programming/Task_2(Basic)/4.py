if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    l = list(student_marks[query_name])
    sum1 = sum(l)
    print("%.2f"%(sum1/3))