def fraction_value(fraction):
    value = fraction[0] / fraction[1]
    return value


def swapy(list, index1, index2):
  list[index1],list[index2] = list[index2], list[index1]


def sort_fractions(fractions):
    for i in range(0, int(len(fractions))):
        for j in range(0, int(len(fractions))):
            if (fraction_value(fractions[i]) < fraction_value(fractions[j])):
                swapy(fractions, i, j)
    return fractions


print (sort_fractions([(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]))