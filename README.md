# Phonetic Distance Metric

Simple library that will give you the phonetic distance between two phones, represented as IPA unicode.

You can find the full mapping of accepted symbols in data.py

```python
>>> from phonetic_distance import distance
>>> distance('m', 'n')
0.26086956521739135
>>> distance('b', 'p')
0.04347826086956522
>>> distance('e', 'i')
0.058823529411764705
>>> distance('a', 'e')
0.11764705882352941
>>> distance('f', 'v')
0.04347826086956522
>>> distance('p', 'k')
0.3478260869565218
```
