import data
import math
import os
import json
import re
import scipy.cluster.hierarchy as hierarchy

phone_memory = {}

def _get_vector(phones):
    global phone_memory
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
        if letter != last_letter:
            stripped.append(letter)
        last_letter = letter
    return tuple(stripped)


def phoneticize(word, language="english"):
    tokenized = tokenize(word)
    next_words = set([tokenized])
    results = set()
    mappings = get_mapping(language)
    tokenized_mappings = {
        tokenize(key): list(map(lambda x: "$"+ x, mapping))
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

cached_mappings = {}
def get_mapping(language):
    cached = cached_mappings.get(language)
    if cached:
        return cached
    
    with open(os.path.join(os.path.dirname(__file__),
                           "mappings",
                           language + ".json")) as f:
        mappings = json.load(f)
        cached_mappings[language]= mappings
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

cached_cluster_maps = {}

CLUSTER_SENSITIVITY = 0.5
def cluster_phones(language):
    cached = cached_cluster_maps.get(language)
    if cached:
        return cached
    phones = list(phone_set(language))
    cluster_map = cluster_phone_set(phones)
    cached_cluster_maps[language] = cluster_map
    return cluster_map

def cluster_phone_set(phones):
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
    
    return cluster_map

# Short for phone index, maps a word onto its phone clusters
def phonex(word, language="english"):
    phone_variants = phoneticize(word)
    mappings = cluster_phones(language)
    results = []
    for phone_variant in phone_variants:
        try:
            phonex_variant = tuple([mappings[phone] for phone in phone_variant])
        except:
            print(word, phone_variant)
            exit(1)
        results.append(phonex_variant)
    return results

# import pprint
# pp = pprint.PrettyPrinter(indent=4)
    # for index in range(len(clusters)):
    #     set_phones = forward_map.get(clusters[index])
    #     if not set_phones:
    #         set_phones = []
    #         forward_map[clusters[index]] = set_phones
    #     set_phones.append(phones[index])
