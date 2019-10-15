def longest_substring(string):
    l = len(string)
    xy = 0
    max = 0
    initial = 0
    position = {}
    position[string[0]] = 0
    for i in range(1, l):
        if string[i] not in position:
            position[string[i]] = i
        else:
            if position[string[i]] >= xy:

                current_length = i - xy
                if max < current_length:
                    max = current_length
                    initial = xy
                xy = position[string[i]] + 1
            position[string[i]] = i
    if max < i - xy:
        max = i - xy
        initial = xy
    return string[initial: initial + max]
if __name__ == "__main__":
    string = input("enter a string")
    print(longest_substring(string))
