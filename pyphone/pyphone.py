from pyphone import data
import os
import json
import re
import scipy.cluster.hierarchy as hierarchy

phone_memory = {}

bad_phones = {
    "ɝ": "ɜ˞",
}


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
    return different / total_weights * factor


# Change this filter to expand to other languages
alpha_only = re.compile('[^a-zA-Z]')


def tokenize(word):
    word = alpha_only.sub('', word)
    return "".join(["_" + letter for letter in word])


def strip_repeats(word):
    stripped = []
    last_letter = None
    word = filter(None, word.split("$"))
    for letter in word:
        if letter != last_letter and not letter.startswith('_'):
            stripped.append(letter)
        last_letter = letter
    return tuple(stripped)


def phoneticize(word, language="english"):
    tokenized = tokenize(word.lower())
    next_words = set([tokenized])
    results = set()
    mappings = get_mapping(language)
    tokenized_mappings = {
        tokenize(key): list(map(lambda x: "$" + x, mapping))
        for (key, mapping) in mappings.items()
    }
    while len(next_words) > 0:
        next_word = next_words.pop()

        has_replacements = False
        for key, replacements in tokenized_mappings.items():
            if key in next_word:
                has_replacements = True
                for replacement in replacements:
                    next_words.add(next_word.replace(key, replacement, 1))
        if not has_replacements:
            results.add(strip_repeats(next_word))
    return results


cached_json = {}


def get_mapping(language):
    cached = cached_json.get(language)
    if cached:
        return cached
    with open(os.path.join(os.path.dirname(__file__),
                           "data",
                           "mappings",
                           language + ".json")) as f:
        mappings = json.load(f)
        cached_json[language] = mappings
        return mappings


cached_phone_sets = {}


def phone_set(language="english"):
    cached = cached_phone_sets.get(language)
    if cached:
        return cached

    phone_set = set()
    mapping = get_mapping(language)
    for key, phones in mapping.items():
        for phone in phones:
            phone_set.add(phone)
    cached_phone_sets[language] = phone_set
    return phone_set


def phonex(word, language="english"):
    """
    Short for phone index, maps a word onto a sequence of phone clusters
    Strips non supported characters (for english, non alpha characters)
    """
    phone_variants = phoneticize(word)
    mappings = cluster_phones(language)
    results = []
    for phone_variant in phone_variants:
        try:
            phonex_variant = tuple([mappings[phone] for phone in
                                    phone_variant])
            results.append(phonex_variant)
        except:
            print('Error:', word, phone_variant)
            exit(1)
    return results


CLUSTER_SENSITIVITY = 0.5
cluster_cache = {}


def cluster_phones(language):
    if cluster_cache.get(language):
        return cluster_cache[language]
    phones = sorted(list(phone_set(language)))
    phones = sorted(phones)
    triangle_distance = []

    for a in range(len(phones)):
        for b in range(a + 1, len(phones)):
            triangle_distance.append(distance(phones[a], phones[b]))

    linkages = hierarchy.linkage(triangle_distance)
    clusters = hierarchy.fcluster(linkages, CLUSTER_SENSITIVITY)
    cluster_map = {}

    for index in range(len(clusters)):
        cluster_map[phones[index]] = clusters[index]

    cluster_cache[language] = cluster_map
    return cluster_map

# import pprint
# pp = pprint.PrettyPrinter(indent=4)
    # for index in range(len(clusters)):
    #     set_phones = forward_map.get(clusters[index])
    #     if not set_phones:
    #         set_phones = []
    #         forward_map[clusters[index]] = set_phones
    #     set_phones.append(phones[index])
