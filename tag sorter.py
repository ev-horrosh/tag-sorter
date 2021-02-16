import os
from tkinter import Tk
from tkinter import filedialog


root = Tk().withdraw()


def open_tags():
    filepath = filedialog.askopenfilename(title="Select txt")
    path = os.path.dirname(filepath)
    filename = os.path.basename(filepath)
    name = os.path.splitext(filename)[0]+'_sorted.txt'
    print(path+name)

    with open(filepath, 'r', encoding="utf-8") as list_of_tags:
        with open(path + '\\' + name, 'w', encoding="utf-8") as list_of_sorted_tags:
            tags = list_of_tags.readlines()
            words_no = []

            for words in tags:
                for w in words.split(" "):
                    words_no.append(w)

            words_no = sorted(words_no)

            new_list = []

            for s in words_no:
                if s not in new_list:
                    new_list.append(s.strip('\n'))

            new_tags = []
            for i in new_list:
                if len(i) >= 3:
                    new_hashtag = i + '\n'
                    new_tags.append(new_hashtag)

            for t in new_tags:
                list_of_sorted_tags.write(t)


open_tags()
