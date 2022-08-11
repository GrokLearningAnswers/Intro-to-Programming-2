translator = [
    ('y', 'z'),
    ('z', 'y'),
    ('Y', 'Z'),
    ('Z', 'Y')
]


def fix_yz(s):
    s = s.replace('z', '💀')
    s = s.replace('y', 'z')
    s = s.replace('💀', 'y')
    s = s.replace('Z', '💀')
    s = s.replace('Y', 'Z')
    s = s.replace('💀', 'Y')
    return s
