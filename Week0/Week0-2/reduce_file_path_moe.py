def reduce_file_path(path):
    path = path.split('/')
    result = []
    for i, item in enumerate(path):
        if item == '..':
            if result:
                del result[-1]
        elif item != '' and item != '.':
            result.append(item)
    return "/".join(result)

print(reduce_file_path(
    "/home//////////////radorado/code/./hackbulgaria/week0/../../../."))
