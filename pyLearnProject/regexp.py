import re

number = 'tralalalallala 411-123-4444'

regexp = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

mo = regexp.search(number)
mo2 = regexp.findall(number)

print(mo.group)

# groups

regexp = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo3 = regexp.search(number)

# the regexp groups separated with ()

mo.group(2)

# if we would look for literal ()

regexp = (r'\(\d\d\d\).....')

# pipes

batReg = re.compile(r'Batman|Batwoman')
batReg2 = re.compile(r'Bat(wo)?man')

# ? meaning matches zero or one time
# * meaning matches zero or more times
# r'Batwowowowoman will match
# + it has to appear at least one time
# r'Batman' won't match
# {x} the exact number of times

haha = 'HahaHaHaHa'

matchexactnumberoftimes = re.compile(r'(Ha){3}')

# this also could be a range {3,5}
# greedy matches the longest non-greedy matches the shortest occurrnce

regex.findall('text')
# this will return a list not an object of the matched occurrences. If groups involved in the pattern then those will be tuples in the list

# Character classes eg. \d \D \w \W or custom classes within [] like [a|b|c|1-5]
# ^ in the beginning of the char class and it makes it negative excludes it. It also means that the pattern has to match at the beginning of the string.
# $ at the end means that it should match at the end of the string.
# ^ $ together means that the exact string has to match.
# . is a wildcard matches anything except new line one char only at a time but using it with .* it matches anything and everything. 