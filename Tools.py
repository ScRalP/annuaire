def trimNumber(number):
    trimmedNum = number.strip()
    for c in ".- ":
        trimmedNum = trimmedNum.replace(c, "")
    return trimmedNum