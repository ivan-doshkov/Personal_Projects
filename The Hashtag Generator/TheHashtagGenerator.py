def generate_hashtag(s):
    if s == "" or len(s) > 140:
        return False
    l1 = s.split()
    new_word = "#"
    for ch in l1:
        ch = ch.title()
        new_word += ch
    return new_word

print(generate_hashtag("   Hello   World"))