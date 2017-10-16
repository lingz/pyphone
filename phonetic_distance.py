import data
import math

phone_memory = {}
mems = {
    True: {},
    False: {}
}

def safe_log(num):
    if num <= 0:
        return float("-inf")
    else:
        # log 10 because that's what LM returns
        return math.log(num, 10)


def order_phones(a, b):
    if a < b:
        return a, b
    else:
        return b, a


def _get_vector(phones):
    global phone_memory
    if bad_phones.get(phones):
        phones = bad_phones.get(phones)
    try:
        if not phones:
            raise ValueError("No phone passed in")
        if len(phones) == 1:
            return data.phone_features[phones]
        else:
            if phone_memory.get(phones):
                return phone_memory[phones]
            vec = [None] * data.NUM_FEATURES
            # Combine the feature vectors
            mods = []
            for i in range(data.NUM_FEATURES):
                val = None
                for phone in phones:
                    if phone in data.modifiers:
                        mods.append(data.modifiers[phone])
                    else:
                        p_val = data.phone_features[phone][i]
                        if p_val is True:
                            val = True
                            break
                        elif p_val is False:
                            val = False
                vec[i] = val
            for mod in mods:
                for i, v in mod.items():
                    vec[i] = v
            phone_memory = {phones: vec}
            return vec
    except KeyError as e:
        raise ValueError("Unrecognized phone %s" % str(e))


bad_phones = {
    "ɝ": "ɜ˞",
}


def feature_diff(phoneA, phoneB):
    vecA = _get_vector(phoneA)
    vecB = _get_vector(phoneB)
    diff = [False for i in range(21)]
    for i in range(data.NUM_FEATURES):
        if (vecA[i] != vecB[i] and (vecA[i] is not None) and (vecB[i] is not
                                                              None)):
            diff[i] = True
    return diff


def is_vowel(phone):
    vec = _get_vector(phone)
    return vec[0]


def distance(phoneA, phoneB):
    weights = data.feature_weights
    # Handle spaces specially
    if phoneA == ' ' or phoneB == ' ':
        if phoneA == phoneB:
            # Certain
            return 0
        else:
            # Impossible to sub for something else
            return 1
    if is_vowel(phoneA) != is_vowel(phoneB):
        # If one is a vowel and the other is a consonant
        return 1

    vowel = is_vowel(phoneA)

    if vowel:
        total_weights = data.total_vowel_weight
        features = data.vowel_features
        factor = 1
    else:
        total_weights = data.total_consonant_weight
        features = data.consonant_features
        factor = 2

    vecA = _get_vector(phoneA)
    vecB = _get_vector(phoneB)

    different = 0
    for i in features:
        if vecA[i] != vecB[i]:
            different += weights[i]
    return (different / total_weights) * factor
