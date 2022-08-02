def arithmetic_arranger(problems):
    ans = []
    for el in problems:
        for i in el.split(','):
            if i.split()[1] == '+':
                ans.append(int(i.split()[0]) + int(i.split()[-1]))
            if i.split()[1] == '-':
                ans.append(int(i.split()[0]) - int(i.split()[-1]))
    return ans
