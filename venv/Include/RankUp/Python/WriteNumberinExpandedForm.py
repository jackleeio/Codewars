"""
You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
NOTE: All numbers will be whole numbers greater than 0.

author: Jack Lee
time: 2020/4/14 20:25

"""

def expanded_form(num):
    # 将数字拆分到列表中
    i = 0
    temp = []
    while num != 0:
        temp.append(num % (10 ** (i+1)))
        num = num - temp[i]
        i += 1
    temp.reverse()

    string = str(temp[0])
    # 列表转换为字符串
    for i in range(1, len(temp)):
        if temp[i] != 0:
            string += ' + ' + str(temp[i])

    return string

if __name__ == '__main__':
    print(expanded_form(1231))
    print(expanded_form(70304))