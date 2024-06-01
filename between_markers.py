def between_markers(sentence, im, fm):
    i = 0
    while i < len(sentence):
        if sentence[i] == im:
            im_pos = i
        if sentence[i] == fm:
            fm_pos = i
            break
        i = i + 1

    # print(sentence[im_pos + 1])
    # print(sentence[im_pos + 2])
    # print(sentence[im_pos + 3])

    z = 1
    result = ""
    while z < fm_pos - im_pos:
        result = result + sentence[im_pos + z]
        z = z + 1

    print(result)
    return result


assert between_markers("What is >apple<", ">", "<") == "apple"
