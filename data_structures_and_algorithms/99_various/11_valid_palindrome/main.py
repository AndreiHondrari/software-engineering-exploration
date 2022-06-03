import string


def valid_palindrome(s: str) -> bool:
    non_letters = string.punctuation + string.whitespace

    normalized_s = s.lower()

    for character in non_letters:
        normalized_s = normalized_s.replace(character, '')

    length = len(normalized_s)
    for i in range(length // 2):
        if normalized_s[i] != normalized_s[length - i - 1]:
            return False

    return True


def main() -> None:
    s1 = "A man, a plan, a canal: Panama"

    res = valid_palindrome("0P")
    print("RES", res)


if __name__ == "__main__":
    main()
