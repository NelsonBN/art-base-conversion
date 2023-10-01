def fromDecimalTo(num: int, base: int) -> str:
    result = ""

    while num > 0:
        remainder = num % base

        if(remainder > 9):
            result = chr(ord('A') + remainder - 10) + result
        else:
            result = str(remainder) + result

        num //= base

    return result


def toDecimal(num: str, base: int) -> int:
    result = 0
    power = 0

    for i in range(len(num) - 1, -1, -1):
        if num[i].isdigit():
            result += int(num[i]) * base ** power
        else:
            result += (ord(num[i]) - ord('A') + 10) * base ** power

        power += 1

    return result

fromDecimalTests = [
    [1, 2, "1"],
    [2, 2, "10"],
    [10, 2, "1010"],
    [10, 8, "12"],
    [10, 16, "A"]]

toDecimalTests = [
    ["1", 2, 1],
    ["10", 2, 2],
    ["1010", 2, 10],
    ["12", 8, 10],
    ["A", 16, 10]]




for num, base, expected in fromDecimalTests:
    assert fromDecimalTo(num, base) == expected, f"{num} {base} {expected}"

for num, base, expected in toDecimalTests:
    assert toDecimal(num, base) == expected, f"{num} {base} {expected}"