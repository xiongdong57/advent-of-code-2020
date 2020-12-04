import re

from utils import read_input


def parse_check(info, check_info):
    info_map = {}
    for key, value in re.findall(r'(\w+):(#\w+|\w+)', info):
        info_map[key] = value
    return check_info(info_map)


def check_info_p1(info_map):
    keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    return all(key in info_map for key in keys)


def check_info_p2(info_map):
    keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    if all(key in info_map for key in keys):
        return (('1920' <= info_map['byr'] <= '2002') &
                ('2010' <= info_map['iyr'] <= '2020') &
                ('2020' <= info_map['eyr'] <= '2030') &
                valid_hgt(info_map['hgt']) &
                valid_hcl(info_map['hcl']) &
                valid_ecl(info_map['ecl']) &
                valid_pid(info_map['pid'])
                )
    return False


def valid_hgt(x):
    return ('150cm' <= x <= '193cm') if 'cm' in x else ('59in' <= x <= '76in')


def valid_hcl(x):
    return (x[0] == '#') & (len(re.findall('[0-9a-f]', x)) == 6)


def valid_ecl(x):
    return x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def valid_pid(x):
    return (len(x) == 9) & (len(re.findall('[0-9]', x)) == 9)


def solve_part_one(seq):
    infos = ''.join(seq).split('\n\n')
    return sum(parse_check(info, check_info_p1) for info in infos)


def solve_part_two(seq):
    infos = ''.join(seq).split('\n\n')
    return sum(parse_check(info, check_info_p2) for info in infos)


def main():
    input_seq = read_input('day4', 'input.txt')
    test_seq = read_input('day4', 'test.txt')

    assert solve_part_one(test_seq) == 2
    print('part one result: ', solve_part_one(input_seq))

    assert solve_part_two(read_input('day4', 'test_p2.txt')) == 4
    print('part two result: ', solve_part_two(input_seq))


if __name__ == "__main__":
    main()
