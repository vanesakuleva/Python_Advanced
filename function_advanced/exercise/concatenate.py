def concatenate(*args, **kwargs):
    whole_word = ''.join(args)
    for key, value in kwargs.items():
        whole_word = whole_word.replace(key, value)

    return whole_word


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))