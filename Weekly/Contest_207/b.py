def maxUniqueSplit(s: str) -> int:

    if len(s) == 1:
        return 1
    s = list(s)

    s1 = s[::-1]

    final_list = []
    take_away = 1

    while len(s) > take_away:

        first_part = s[: take_away]
        second_part = s[take_away:]

        if (first_part not in final_list) and (second_part not in final_list):
            if first_part == second_part:
                final_list.append(first_part + second_part)
                s = []
                continue
            final_list.append(first_part)
            s = second_part
            take_away = 1
        else:
            take_away += 1
    if len(s) == take_away:
        final_list.append(s)


    final_list2 = []
    take_away = 1
    while len(s1) > take_away:

        first_part = s1[: take_away]
        second_part = s1[take_away:]

        if (first_part not in final_list2) and (second_part not in final_list2):
            if first_part == second_part:
                final_list2.append(first_part + second_part)
                s1 = []
                continue
            final_list2.append(first_part)
            s1 = second_part
            take_away = 1
        else:
            take_away += 1
    if len(s1) == take_away:
        final_list2.append(s1)


    return max(len(final_list),len(final_list2))

c ="gpaccacseleac"
s = 'addbsd'
print(maxUniqueSplit(s))
