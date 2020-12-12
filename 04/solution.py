import sys

req = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
def main(args):
    passport = ''
    matches = 0
    last = 0
    for line in sys.stdin:
        if line.strip():
            passport += line + ' '
            last = 1
            continue
        matches += isvalid(passport)
        passport = ''
        last = 0
    if last:
        matches += isvalid(passport)
    print(matches)

def isvalid(p):
    sections = [a.split(':') for a in p.split()]
    parts = [s[0] for s in sections]
    if not all(r in parts for r in req):
        return False
    try:
        for (p, v) in sections:
            p, v = p.strip(), v.strip()
            if p == 'byr':
                if int(v) not in range(1920, 2003):
                    return False
            elif p == 'iyr':
                if int(v) not in range(2010, 2021):
                    return False
            elif p == 'eyr':
                if int(v) not in range(2020, 2031):
                    return False
            elif p == 'hgt':
                if (v[-2:] == 'cm'):
                    if int(v[:-2]) not in range(150, 194):
                        return False
                elif (v[-2:] == 'in'):
                    if int(v[:-2]) not in range(59, 77):
                        return False
                else:
                    return False
            elif p == 'hcl':
                if not (v[0] == '#' and len(v) == 7 and all(c in '1234567890abcdef' for c in v[1:])):
                    return False
            elif p == 'ecl':
                if v not in ('amb', 'blu', 'brn', 'gry', 'hzl', 'grn', 'oth'):
                    return False
            elif p == 'pid':
                if not (len(v) == 9 and all (c in '0123456789' for c in v)):
                    return False
    except:
        return False
    return True

if __name__ == '__main__':
    print main(sys.argv)
