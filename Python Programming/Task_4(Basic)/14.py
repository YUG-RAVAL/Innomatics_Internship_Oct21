def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        uniq = ''
        for c in string[i : i+k]:
            if (c not in uniq):
                uniq+=c
        print(uniq)