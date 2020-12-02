from typing import List
from collections import namedtuple


Rule = namedtuple("Rule", ["char", "min", "max"])

RULES = [Rule("a", 1, 3), Rule("b", 1, 3), Rule("c", 2, 9)]
PASSWORDS = ["abcde", "cdefg", "ccccccccc"]


def is_password_correct(password: str, rule: Rule) -> bool:

    num_times = sum([char == rule.char for char in password])
    if rule.min <= num_times <= rule.max:
        return True
    else:
        return False


def how_many_passwords_are_correct(passwords: List[str], rules: List[Rule]) -> int:
    return sum([is_password_correct(password, rule) for password, rule in zip(passwords, rules)])


assert how_many_passwords_are_correct(PASSWORDS, RULES) == 2


NewRule = namedtuple("Rule", ["char", "first_position", "second_position"])
NEW_RULES = [NewRule("a", 1, 3), NewRule("b", 1, 3), NewRule("c", 2, 9)]


def is_password_correct_new_rule(password: str, rule: NewRule) -> bool:
    first_char = password[rule.first_position - 1]
    second_char = password[rule.second_position - 1]

    num_times = sum([first_char == rule.char, second_char == rule.char])

    if num_times == 1:
        return True
    else:
        return False


def how_many_passwords_are_correct_new_rule(passwords: List[str], rules: List[NewRule]) -> int:
    return sum([is_password_correct_new_rule(password, rule) for password, rule in zip(passwords, rules)])


assert how_many_passwords_are_correct_new_rule(PASSWORDS, NEW_RULES) == 1


with open("data/day02.txt") as f:
    data = f.readlines()
    data = list(map(lambda x: x.strip(), data))

    passwords = []
    rules = []
    new_rules = []
    for example in data:
        raw_rule, password = example.split(": ")
        minmax, char = raw_rule.split(" ")
        min_, max_ = minmax.split("-")
        rule = Rule(char, int(min_), int(max_))

        passwords.append(password)
        rules.append(rule)
        new_rules.append(NewRule(char, int(min_), int(max_)))

    print(how_many_passwords_are_correct(passwords, rules))
    print(how_many_passwords_are_correct_new_rule(passwords, new_rules))
