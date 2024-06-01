def largest(sentence):
    words = sentence.split(" ")

    largest = words[0]

    for word in words:
        if len(word) > len(largest):
            largest = word

    return largest


assert largest("the quick brown fox") == "quick"
assert largest("openai gpt") == "openai"
assert largest("this is a sentence") == "sentence"
