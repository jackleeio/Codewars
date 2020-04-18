"""
What is an anagram? Well, two words are anagrams（颠倒字母而成的字） of each other if they both contain the same letters.
For example:

'abba' & 'baab' == true

'abba' & 'bbaa' == true

'abba' & 'abbba' == false

'abba' & 'abca' == false
Write a function that will find all the anagrams of a word from a list.
You will be given two inputs a word and an array with words.
You should return an array of all the anagrams or an empty array if there are none. For example:

anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

anagrams('laser', ['lazing', 'lazy',  'lacer']) => []

author: Jack Lee
time: 2020/4/16 22:56

"""



def anagrams(word, words):
    result = []
    for i in range(0,len(words)):

        # word_list = word.split("") 这样子将字符串比如说abc 拆分会报错，""中必须填写拆分符号
        # 应该这样写
        word_list = list(word)  # 字符串abc会形成一个新的列表['a', 'b', 'c']

        #用于检查words中字符串的长度，长度大于word的长度时直接跳过该字符串
        initial_list_length = len(word_list)

        if len(words[i]) > initial_list_length:
            continue
        for j in range(0, len(words[i])):
            if j > len(words[i]):
                break;

            if words[i][j] in word_list:
                post = word_list.index(words[i][j])
                word_list.pop(post)
                # print(words[i][j], word_list, len(word_list))

            else:
                break
        if len(word_list) == 0:
            result.append(words[i])

    return result

if __name__ == '__main__':
    print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada', 'abbaa']))
    print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))