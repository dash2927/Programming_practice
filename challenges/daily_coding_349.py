# This is your coding interview problem for today.
#
# This problem was asked by Grammarly.
#
# Soundex is an algorithm used to categorize phonetically, such that two names
# that sound alike but are spelled differently have the same representation.
#
# Soundex maps every name to a string consisting of one letter and
# three numbers, like M460.
#
# One version of the algorithm is as follows:
#
# 1) Remove consecutive consonants with the same sound (for example,
# change ck -> c).
#
# 2) Keep the first letter. The remaining steps only apply to the rest of the
# string.
#
# 3) Remove all vowels, including y, w, and h.
#
# 4) Replace all consonants with the following digits:
#
#     b, f, p, v → 1
#     c, g, j, k, q, s, x, z → 2
#     d, t → 3
#     l → 4
#     m, n → 5
#     r → 6
#
# 5) If you don't have three numbers yet, append zeros until  you do. Keep
# the first three numbers.
#
# Using this scheme, Jackson and Jaxen both map to J250.
#
# Implement Soundex.

digits = {1: ['b', 'f', 'p', 'v'],
          2: ['c', 'g', 'j', 'k', 'q', 's', 'x', 'z'],
          3: ['d', 't'],
          4: ['l'],
          5: ['m', 'n'],
          6: ['r']}
vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'w', 'h']
same_sound = ['c', 'k']


def soundex(sound):
    mapping = sound[0]  # our 2nd rule
    sound_iter = iter(sound[1:])
    sound_iter2 = iter(sound[2:])
    for char in sound_iter:
        char2 = next(sound_iter2, None)
        # our first rule
        if (char in same_sound and char2 in same_sound):
            next(sound_iter, None)
            next(sound_iter, None)
            next(sound_iter2, None)
            next(sound_iter2, None)
        # our 3rd rule
        if char in vowels:
            continue
        # our 4th rule
        for key in digits.keys():
            if char in digits[key]:
                mapping += str(key)
    # our 5th rule
    while (len(mapping) != 4):
        mapping += '0'
    return mapping


if __name__ == '__main__':
    sound1 = "Jackson"
    map1 = soundex(sound1)
    sound2 = "Jaxen"
    map2 = soundex(sound2)
    print(f"{sound1} mapping : {map1}")
    print(f"{sound2} mapping : {map2}")
