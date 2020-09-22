def reorderSpaces(text: str) -> str:
    if ' ' not in text:
        return text

    word_list = list(filter(None, text.split(' ')))
    word_count = len(word_list)

    space_count = 0
    for i in text:
        if i == ' ':
            space_count += 1

    if word_count == 1:
        return word_list[0] + ' ' * space_count

    extra_space = space_count % (word_count - 1)

    insert_space_len = int(space_count / (word_count - 1))

    insert_space = ' ' * insert_space_len
    result = insert_space.join(word_list)

    if extra_space != 0:
        result += extra_space * ' '
    return result


a = ' practicemakes  '
# word_list = list(filter(None, a.split(' ')))
# b = ' '*2
# print(word_list)
#
# print(b.join(word_list))
print(reorderSpaces(a))
