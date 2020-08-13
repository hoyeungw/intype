from intype.literal import is_literal

candidates = [
    '123',
    'cyberpunk',
    '...',
    'a-b'
]

for word in candidates:
    print(word, ':', is_literal(word))
