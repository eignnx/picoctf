REV_INPUT_LIST = False
REV_KEY_STR = False
REV_ZIP = False


def main():
    input_list = [
        4,
        54,
        41,
        0,
        112,
        32,
        25,
        49,
        33,
        3,
        0,
        0,
        57,
        32,
        108,
        23,
        48,
        4,
        9,
        70,
        7,
        110,
        36,
        8,
        108,
        7,
        49,
        10,
        4,
        86,
        43,
        108,
        122,
        14,
        2,
        71,
        62,
        115,
        88,
        78,
    ]

    if REV_INPUT_LIST:
        input_list = list(reversed(input_list))

    # key_str = "J_o3t" if REV_KEY_STR else "t3o_J"
    key_str = "J"
    key_str = "_" + key_str
    key_str = key_str + "o"
    key_str = key_str + "3"
    key_str = "t" + key_str

    key_list = [ord(ch) for ch in key_str]

    # @134:
    # if not (len(input_list) < len(key_list)): goto @162
    # key_list.extend(key_list)
    # goto @134
    # @162:

    while len(key_list) < len(input_list):
        key_list.extend(key_list)

    result = [chr(a ^ b) for (a, b) in zip(input_list, key_list)]
    result_text = "".join(result)
    print(result_text)
    return None


if __name__ == "__main__":
    for a in [False, True]:
        for b in [False, True]:
            REV_INPUT_LIST = a
            REV_KEY_STR = b
            main()
