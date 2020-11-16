def trimNumber(number):
    trimmedNum = number.strip()
    for c in ".- ":
        trimmedNum = trimmedNum.replace(c, "")
    return trimmedNum

def formatTelNumberDisplay(number):
        index = 0;
        formated = ""
        for c in str(number):
            formated += " "+str(number[index]) if (index%2 == 0 and index != 0) else str(number[index])
            index += 1
        return formated

SaveFileName = "contacts"