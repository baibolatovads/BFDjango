import string


def swap_case(s):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    arr = []
    for i in range(len(s)):
        if s[i] in lower:
            arr.append(s[i].upper())
        elif s[i] in upper:
            arr.append(s[i].lower())
        else:
            arr.append(s[i])
    return ''.join(arr)


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)