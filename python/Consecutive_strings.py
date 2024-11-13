def longest_consec(strarr, k):
    if k <= 0 or k > len(strarr):
        return ""

    longest = ""
    for i in range(len(strarr) - k + 1):
        concatenated = ''.join(strarr[i:i + k])
        if len(concatenated) > len(longest):
            longest = concatenated

    return longest
