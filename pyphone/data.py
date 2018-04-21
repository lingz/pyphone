# flake8: noqa

# Indexes
# 0 - syllabic
# 1 - sonorant
# 2 - consonantal
# 3 - continuant
# 4 - delayed release
# 5 - lateral
# 6 - nasal
# 7 - strident
# 8 - voice
# 9 - spread glottis
# 10 - constricted glottis
# 11 - anterior
# 12 - coronal
# 13 - distributed
# 14 - labial
# 15 - high (vowel/consonant, not tone)
# 16 - low (vowel/consonant, not tone)
# 17 - back
# 18 - round
# 19 - tense
# 20 - long

NUM_FEATURES = 21

phone_features = {
    "c": [False, False, True, False, False, False, False, None, False, False, False, False, False, None, False, True, False, False, False, None, False],
    "ɡ": [False, False, True, False, False, False, False, None, True, False, False, False, False, None, False, True, False, True, False, None, False],
    "k": [False, False, True, False, False, False, False, None, False, False, False, False, False, None, False, True, False, True, False, None, False],
    "q": [False, False, True, False, False, False, False, None, False, False, False, False, False, None, False, False, False, True, False, None, False],
    "ɖ": [False, False, True, False, False, False, False, None, True, False, False, False, True, False, False, False, False, False, False, None, False],
    "ɟ": [False, False, True, False, False, False, False, None, True, False, False, False, False, None, False, True, False, False, False, None, False],
    "ɠ": [False, False, True, False, False, False, False, None, True, False, True, False, False, None, False, True, False, True, False, None, False],
    "ɢ": [False, False, True, False, False, False, False, None, True, False, False, False, False, None, False, False, False, True, False, None, False],
    "ʄ": [False, False, True, False, False, False, False, None, True, False, True, False, False, None, False, True, False, False, False, None, False],
    "ʈ": [False, False, True, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, None, False],
    "ʛ": [False, False, True, False, False, False, False, None, True, False, True, False, False, None, False, False, False, True, False, None, False],
    "b": [False, False, True, False, False, False, False, None, True, False, False, True, False, None, True, False, False, False, False, None, False],
    "d": [False, False, True, False, False, False, False, False, True, False, False, True, True, False, False, False, False, False, False, None, False],
    "p": [False, False, True, False, False, False, False, None, False, False, False, True, False, None, True, False, False, False, False, None, False],
    "t": [False, False, True, False, False, False, False, False, False, False, False, True, True, False, False, False, False, False, False, None, False],
    "ɓ": [False, False, True, False, False, False, False, None, True, False, True, True, False, None, True, False, False, False, False, None, False],
    "ɗ": [False, False, True, False, False, False, False, False, True, False, True, True, True, False, False, False, False, False, False, None, False],
    "x": [False, False, True, True, False, False, False, None, False, False, False, False, False, None, False, True, False, True, False, None, False],
    "ç": [False, False, True, True, False, False, False, None, False, False, False, False, False, None, False, True, False, False, False, None, False],
    "ħ": [False, False, True, True, False, False, False, None, False, False, False, False, False, None, False, False, True, True, False, None, False],
    "ɣ": [False, False, True, True, False, False, False, None, True, False, False, False, False, None, False, True, False, True, False, None, False],
    "ʁ": [False, False, True, True, False, False, False, None, True, False, False, False, False, None, False, False, False, True, False, None, False],
    "ʂ": [False, False, True, True, False, False, False, True, False, False, False, False, True, False, False, False, False, False, False, None, False],
    "ʃ": [False, False, True, True, False, False, False, True, False, False, False, False, True, True, False, False, False, False, False, None, False],
    "ʐ": [False, False, True, True, False, False, False, True, True, False, False, False, True, False, False, False, False, False, False, None, False],
    "ʒ": [False, False, True, True, False, False, False, True, True, False, False, False, True, True, False, False, False, False, False, None, False],
    "ʕ": [False, False, True, True, False, False, False, None, True, False, False, False, False, None, False, False, True, True, False, None, False],
    "ʝ": [False, False, True, True, False, False, False, None, True, False, False, False, False, None, False, True, False, False, False, None, False],
    "χ": [False, False, True, True, False, False, False, None, False, False, False, False, False, None, False, False, False, True, False, None, False],
    "f": [False, False, True, True, False, False, False, None, False, False, False, True, False, None, True, False, False, False, False, None, False],
    "s": [False, False, True, True, False, False, False, True, False, False, False, True, True, False, False, False, False, False, False, None, False],
    "v": [False, False, True, True, False, False, False, None, True, False, False, True, False, None, True, False, False, False, False, None, False],
    "z": [False, False, True, True, False, False, False, True, True, False, False, True, True, False, False, False, False, False, False, None, False],
    "ð": [False, False, True, True, False, False, False, False, True, False, False, True, True, True, False, False, False, False, False, None, False],
    "ɸ": [False, False, True, True, False, False, False, None, False, False, False, True, False, None, True, False, False, False, False, None, False],
    "β": [False, False, True, True, False, False, False, None, True, False, False, True, False, None, True, False, False, False, False, None, False],
    "θ": [False, False, True, True, False, False, False, False, False, False, False, True, True, True, False, False, False, False, False, None, False],
    "ɧ": [False, False, True, True, True, False, False, None, False, False, False, False, True, True, False, True, False, None, False, None, False],
    "ɕ": [False, False, True, True, True, False, False, True, False, False, False, True, True, True, False, True, False, False, False, None, False],
    "ɬ": [False, False, True, True, True, True, False, False, False, False, False, True, True, False, False, None, None, None, False, None, False],
    "ɮ": [False, False, True, True, True, True, False, False, True, False, False, True, True, False, False, None, None, None, False, None, False],
    "ʑ": [False, False, True, True, True, False, False, True, True, False, False, True, True, True, False, True, False, False, False, None, False],
    "ɱ": [False, True, True, False, None, False, True, None, True, False, False, True, False, None, True, None, None, None, False, None, False],
    "ʔ": [False, True, False, False, False, False, False, None, False, False, True, False, False, None, False, False, False, False, False, None, False],
    "ŋ": [False, True, True, False, False, False, True, None, True, False, False, False, False, None, False, True, False, True, False, None, False],
    "ɳ": [False, True, True, False, False, False, True, False, True, False, False, False, True, None, False, False, False, False, False, None, False],
    "ɴ": [False, True, True, False, False, False, True, None, True, False, False, False, False, None, False, False, False, True, False, None, False],
    "m": [False, True, True, False, False, False, True, None, True, False, False, True, False, None, True, False, False, False, False, None, False],
    "n": [False, True, True, False, False, False, True, False, True, False, False, True, True, False, False, False, False, False, False, None, False],
    "ɲ": [False, True, True, False, False, False, True, False, True, False, False, True, False, None, False, True, False, False, False, None, False],
    "ɥ": [False, True, False, True, None, False, False, None, True, False, False, None, False, None, True, True, False, False, True, True, False],
    "ɰ": [False, True, False, True, None, False, False, None, True, False, False, None, False, None, False, True, False, None, False, True, False],
    "ʋ": [False, True, False, True, None, False, False, None, True, False, False, True, False, None, True, None, None, None, False, None, False],
    "ʀ": [False, True, True, True, None, False, False, None, True, False, False, None, False, None, False, False, False, True, False, None, False],
    "ʙ": [False, True, True, True, None, False, False, None, True, False, False, True, False, None, True, None, None, None, False, None, False],
    "ʟ": [False, True, True, True, None, True, False, None, True, False, False, None, False, None, False, True, False, None, False, None, False],
    "ɭ": [False, True, True, True, None, True, False, False, True, False, False, False, True, False, False, None, None, None, False, None, False],
    "ɽ": [False, True, True, True, None, False, False, False, True, False, False, False, True, False, False, None, None, None, False, None, False],
    "ʎ": [False, True, True, True, None, True, False, None, True, False, False, False, True, True, False, True, False, False, False, None, False],
    "r": [False, True, True, True, None, False, False, False, True, False, False, True, True, False, False, None, None, None, False, None, False],
    "ɫ": [False, True, True, True, None, True, False, False, True, False, False, True, True, False, False, False, False, True, False, None, False],
    "ɺ": [False, True, True, True, None, True, False, False, True, False, False, True, True, False, False, None, None, None, False, None, False],
    "ɾ": [False, True, True, True, None, False, False, False, True, False, False, True, True, False, False, None, None, None, False, None, False],
    "ʍ": [False, True, False, True, False, False, False, None, False, False, False, False, False, None, True, True, False, True, True, None, False],
    "h": [False, True, True, True, False, False, False, False, False, False, False, False, False, None, False, False, False, False, False, None, False],
    "j": [False, True, False, True, False, False, False, None, True, False, False, False, False, None, False, True, False, False, False, None, False],
    "w": [False, True, False, True, False, False, False, None, True, False, False, False, False, None, True, True, False, True, True, None, False],
    "ɹ": [False, True, False, True, False, False, False, False, True, False, False, False, True, False, False, True, False, True, True, None, False],
    "ɻ": [False, True, False, True, False, False, False, False, True, False, False, False, True, False, False, False, False, False, False, None, False],
    "l": [False, True, True, True, False, True, False, False, True, False, False, True, True, False, False, False, False, False, False, None, False],
    "ɦ": [False, True, True, True, False, False, False, None, False, False, False, False, False, None, False, False, False, False, False, None, False],
    "ɑ": [True, True, False, True, None, False, False, None, True, False, False, False, False, False, False, False, True, True, False, True, False],
    "ɘ": [True, True, False, True, None, False, False, None, True, False, False, False, False, False, False, False, False, False, False, True, False],
    "ɞ": [True, True, False, True, None, False, False, None, True, False, False, False, False, False, True, False, False, False, True, False, False],
    "ɤ": [True, True, False, True, None, False, False, None, True, False, False, False, False, False, False, False, False, True, False, True, False],
    "ɵ": [True, True, False, True, None, False, False, None, True, False, False, False, False, False, True, False, False, False, True, True, False],
    "ʉ": [True, True, False, True, None, False, False, None, True, False, False, False, False, False, True, True, False, False, True, True, False],
    "a": [True, True, False, True, False, False, False, None, True, False, False, False, False, False, False, False, True, True, False, True, False],
    "e": [True, True, False, True, False, False, False, None, True, False, False, False, False, False, False, False, False, False, False, True, False],
    "i": [True, True, False, True, False, False, False, None, True, False, False, False, False, False, False, True, False, False, False, True, False],
    "o": [True, True, False, True, False, False, False, None, True, False, False, False, False, False, False, False, False, True, True, True, False],
    "u": [True, True, False, True, False, False, False, None, True, False, False, False, False, False, True, True, False, True, True, True, False],
    "y": [True, True, False, True, False, False, False, None, True, False, False, False, False, False, True, True, False, False, True, True, False],
    "æ": [True, True, False, True, False, False, False, None, True, False, False, False, False, False, False, False, True, False, False, True, False],
    "ø": [True, True, False, True, False, False, False, None, True, False, False, False, False, False, False, False, False, False, True, True, False],
    "œ": [True, True, False, True, False, False, False, None, True, False, False, False, False, False, False, False, False, False, True, False, False],
    "ɒ": [True, True, False, True, False, False, False, None, True, False, False, False, False, False, False, False, True, True, True, True, False],
    "ɔ": [True, True, False, True, False, False, False, None, True, False, False, False, False, False, False, False, False, True, True, False, False],
    "ə": [True, True, False, True, False, False, False, None, True, False, False, False, False, False, False, False, False, True, False, False, False],
    "ɘ": [True, True, False, True, False, False, False, None, True, False, False, False, False, False, False, False, False, True, False, False, False],
    "ɵ": [True, True, False, True, False, False, False, None, True, False, False, False, False, False, False, False, False, True, True, False, False],
    "ɞ": [True, True, False, True, False, False, False, None, True, False, False, False, False, False, False, False, False, True, True, True, False],
    "ɜ": [True, True, False, True, False, False, False, None, True, False, False, False, False, False, False, False, False, True, False, True, False],
    "ɛ": [True, True, False, True, False, False, False, None, True, False, False, False, False, False, False, False, False, False, False, False, False],
    "ɨ": [True, True, False, True, False, False, False, None, True, False, False, False, False, False, False, True, False, True, False, True, False],
    "ɪ": [True, True, False, True, False, False, False, None, True, False, False, False, False, False, False, True, False, False, False, False, False],
    "ɯ": [True, True, False, True, False, False, False, None, True, False, False, False, False, False, False, True, False, True, False, False, False],
    "ɶ": [True, True, False, True, False, False, False, None, True, False, False, False, False, False, False, False, True, False, True, True, False],
    "ʊ": [True, True, False, True, False, False, False, None, True, False, False, False, False, False, False, True, False, True, True, False, False],
    "ɐ": [True, True, False, True, False, False, False, None, True, False, False, False, False, False, False, False, False, True, False, True, False],
    "ʌ": [True, True, False, True, False, False, False, None, True, False, False, False, False, False, False, False, False, True, False, True, False],
    "ʏ": [True, True, False, True, False, False, False, None, True, False, False, False, False, False, False, True, False, False, True, False, False],
}

vowel_features = set([0, 1, 18, 3, 19, 17, 8, 15, 14, 16, 18, 20])
consonant_features = set([1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])


modifiers = {
    "ː": {
        20: True,
    },
    " ̻": {
        13: True,
    },
    "ˤ": {
        16: True,
        17: True
    },
    "˞": {
        11: False,
        15: True,
        18: True
    }
}

feature_weights = [0.14285714285714285, 0.14285714285714285, 0.14285714285714285, 0.07142857142857142, 0.03571428571428571, 0.03571428571428571, 0.03571428571428571, 0.017857142857142856, 0.017857142857142856, 0.017857142857142856, 0.017857142857142856, 0.03571428571428571, 0.03571428571428571, 0.017857142857142856, 0.03571428571428571, 0.03571428571428571, 0.03571428571428571, 0.03571428571428571, 0.03571428571428571, 0.03571428571428571, 0.017857142857142856]
total_vowel_weight = sum([feature_weights[vowel_feature] for vowel_feature in vowel_features])
total_consonant_weight = sum([feature_weights[consonant_feature] for consonant_feature in consonant_features])

# vowel_weights = [1 / (len(vowel_features) - 1) if i in vowel_features[1:] else 0 for i in range(21)]
# consonant_weights = [1 / len(consonant_features) if i in consonant_features else 0 for i in range(21)]
standard_weights = [1 / 21 for i in range(21)]
zero_weights = [0 for i in range(21)]
