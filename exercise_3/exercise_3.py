import pickle
import re
import string


def TakeSecond(elem):
    return elem[1]


def TakeFirst(elem):
    return elem[0]


def sort_function(input_sent):
    x_f = []
    x = input_sent
    new_x = []
    new_x_a = []
    if x != "previous":
        x = x.split()
        for words in x:
            if words[-1] == "." or words[-1] == "?" or words[-1] == "!":
                words = words.replace(words[-1], "")
                new_x.append(words)
            else:
                new_x.append(words)
        for num in range(0, len(new_x)):
            if len(new_x[num]) < 2:
                x_f.append(new_x[num])
            else:
                new_x_a.append(new_x[num])
        new_x_a.sort(key=TakeSecond)
        x_f.sort(key=TakeFirst)
        new_x_a += x_f
        # print(new_x_a)
        pickle.dump(new_x_a, open("save_1", "wb"))
        pickle.dump(input_sent, open("save_2", "wb"))
        return new_x_a
    else:
        try:
            if x == "previous":
                sorted_one = pickle.load(open("save_1", "rb"))
                input_one = pickle.load(open("save_2", "rb"))
                # print("previous sorted list is:", sorted_one)
                # print("previous input is: ", input_one)
                return input_one
        except:
            x = x.split()
            x.sort(key=TakeSecond)
            # print(x)
            pickle.dump(x, open("save_1", "wb"))
            pickle.dump(input_sent, open("save_2", "wb"))
            return x


def get_words_sentences(input_sent):
    new_words = []
    words = input_sent
    sentences = input_sent
    sentences = sentences.strip(string.punctuation)
    words = words.split(" ")
    for w in words:
        if w[-1] == "." or w[-1] == "?" or w[-1] == "!":
            w = w.replace(w[-1], "")
            new_words.append(w)
        else:
            new_words.append(w)
    sentences = re.split("(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s", sentences)
    # print(new_words)
    # print(sentences)
    print("The number of words is:", len(words))
    print("The number of sentences is:", len(sentences))


def get_less_than5(input_sent):
    less_than5 = []
    new_list = []
    spx = input_sent
    spx = spx.split(" ")
    for words in spx:
        if words[-1] == "." or words[-1] == "?" or words[-1] == "!":
            words = words.replace(words[-1], "")
            new_list.append(words)
        else:
            new_list.append(words)
    for words in new_list:
        if len(words) < 5:
            less_than5.append(words)
    print(less_than5)


def get_less_than5_ex_vo(input_sent):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    less_than5_ex = []
    new_list_ex = []
    spx = input_sent
    spx = spx.split(" ")
    for words in spx:
        if words[-1] == "." or words[-1] == "?" or words[-1] == "!":
            words = words.replace(words[-1], "")
            new_list_ex.append(words)
        else:
            new_list_ex.append(words)
    for words in new_list_ex:
        lens_num = len(words)
        for n in words:
            if n in vowels:
                lens_num -= 1
        if lens_num < 5:
            less_than5_ex.append(words)
    print(less_than5_ex)


def exercise_3(inputs): # DO NOT CHANGE THIS LINE
    """
    This functions receives the input in the parameter 'inputs'. 
    Change the code, so that the output is sqaure of the given input.

    Output should be the name of the class.
    """
    output = inputs

    return output       # DO NOT CHANGE THIS LINE
