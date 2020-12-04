from dataclasses import dataclass
from typing import Optional
import re

DATA = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""


@dataclass
class Passport:
    byr: Optional[int] = None
    iyr: Optional[int] = None
    eyr: Optional[int] = None
    hgt: Optional[str] = None
    hcl: Optional[str] = None
    ecl: Optional[str] = None
    pid: Optional[int] = None
    cid: Optional[int] = None

    @classmethod
    def parse(cls, line: str) -> "Passport":
        line = line.replace("\n", " ").strip()
        elements = line.split()
        passport = {}
        for element in elements:
            key, val = element.split(":")
            passport[key] = val

        return cls(**passport)

    def is_valid(self) -> bool:
        for key in self.__annotations__:
            if getattr(self, key) is None and key != "cid":
                return False
        return True

    def is_valid2(self) -> bool:
        if self.is_valid():

            if not 1920 <= int(self.byr) <= 2002:
                return False

            if not 2010 <= int(self.iyr) <= 2020:
                return False

            if not 2020 <= int(self.eyr) <= 2030:
                return False

            try:
                height, unit = int(self.hgt[:-2]), self.hgt[-2:]
                if unit == "cm":
                    if not 150 <= height <= 193:
                        return False
                elif unit == "in":
                    if not 59 <= height <= 76:
                        return False
                else:
                    raise False
            except ValueError:
                return False

            if self.hcl[0] != "#" or re.findall(r"[^a-f0-9]", self.hcl[1:]):
                return False

            if self.ecl not in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}:
                return False

            if len(str(self.pid)) != 9:
                return False

            return True

        else:
            return False

    def __str__(self):

        return "\n".join(
            [
                f"Valid: {self.is_valid()}",
                f"Valid2: {self.is_valid2()}",
                f"Birth Year: {self.byr}",
                f"Issue Year: {self.iyr}",
                f"Expiration Year: {self.eyr}",
                f"Height: {self.hgt}",
                f"Hair Color: {self.hcl}",
                f"Eye Color: {self.ecl}",
                f"Passport ID: {self.pid}",
                f"Country ID: {self.cid}"
            ]
        )


passports = [Passport.parse(line) for line in DATA.split("\n\n")]
assert sum(passport.is_valid() for passport in passports) == 2


with open("data/day04.txt") as f:
    data = f.read()
    passports = [Passport.parse(line) for line in data.split("\n\n")]
    num_valid = sum(passport.is_valid() for passport in passports)
    print(num_valid)

    num_valid2 = sum(passport.is_valid2() for passport in passports)
    print(num_valid2)
