# escape char

escapeChar = 'I\'m a prigrammer!'

print(escape)

# raw string

rawstring = r"I'm a rawstring"

# triple quotes """ """ multiline string

# strings could be used as lists string[2:3] or string[:-1]

# strings are immutable so you cant modify it after creation
# after creation if methods used on it it creates a new object

stringz = 'This is a stting'

print(stringz.upper())
print(strimgz.lower())

# islower isupper boolean

stringz.islower()

# string.isalpha() string.isalnum .isdecimal() .isspace()

# string.startswith() .endswith()

', '.join(['kenyer', 'krumpli', 'langos'])

# joins the lisy of strings with the given char 

'ezt.kell.splittelni'.split('.')

# splits on whitespace or given char

stringz.rjust(20, '×')
stringz.ljust(20, 'x')
stringz.center(20, 'x')

stringz.strip()

# string interpolation
# if several strings must be concatenated
# conversion specifiers

nev = 'Happy Day'
when = 'Monday'
where = 'in the forest'

text = 'On %s we had a walk with %s in the %s' % (nev, when, where)
