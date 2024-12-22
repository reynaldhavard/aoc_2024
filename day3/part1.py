import re


if __name__ == "__main__":
    with open("sample.txt", "r") as f:
        seq = ''.join(f.read().splitlines())

    matches = re.findall(r'mul\(\d+,\d+\)', seq)
    result = 0
    for match in matches:
        a, b = [int(x) for x in match[4:-1].split(',')]
        result += a * b

    print(result)
