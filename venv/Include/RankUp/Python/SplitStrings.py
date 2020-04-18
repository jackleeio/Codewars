"""
Complete the solution so that it splits the string into pairs of two characters.
If the string contains an odd number of characters
then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']

author: Jack Lee
time: 2020/4/13 16:33

"""
def solution(s):

    result = []
    for i in range(0, len(s), 2):
        if i + 1 < len(s):
            temp_str = s[i] + s[i+1]
        else:
            temp_str = s[i] + '_'
        result.append(temp_str)
    return result



if __name__ == '__main__':
    print(solution('abc'))
    print(solution([]))
    print(solution('abcd'))

