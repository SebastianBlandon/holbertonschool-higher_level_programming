#!/usr/bin/python3
""" Module text identation prints a text with 2 new lines after each of
    these characters: ., ? and :
    Prototype: def text_identation(text):
    text must be a string, otherwise raise a TypeError exception
    with the message text must be a string
    There should be no space at the beginning or at the end of each
    printed line
"""


def text_indentation(text):
    """ Funcion text_identation
        Args:
            text (str): input string
        Return:
            Nothing
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    if not text.count(".") and not text.count("?") and not text.count(":"):
        print(text)
        return
    new_text = []
    index_cut = 0
    for i in range(len(text)):
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            if i == 0:
                new_text.append(text[i])
                index_cut += 1
            else:
                new_text.append(text[index_cut:i + 1])
                index_cut = i + 1
                while i + 1 < len(text) and text[index_cut] == " ":
                    index_cut += 1
    new_text.append(text[index_cut:i + 1])
    print("\n\n".join(new_text[:-1]))
    print()
    print(new_text[-1], end="")
