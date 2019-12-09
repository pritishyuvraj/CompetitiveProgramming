class checkUniqueStrings:
    def __init__(self, sample_string):
        self.sample_string = sample_string

    def checkIfStringsAreUnique(self):
        string = self.sample_string
        characters = {}
        for char in string:
            if char in characters:
                return False
            else:
                characters[char] = 1
        return True

    def checkIfStringsAreUniqueNoDictionary(self):
        string = self.sample_string
        string = ''.join(sorted(string))
        length_of_string = len(string)
        for index, c in enumerate(string):
            if index + 1 < length_of_string:
                if string[index] == string[index+1]:
                    return False
        return True

if __name__ == '__main__':
    # Test cases
    check_unique_strings = checkUniqueStrings("abcd")

    result = check_unique_strings.checkIfStringsAreUnique()
    print("Strings have all unique characters -> ", result)

    result_no_dic = check_unique_strings.checkIfStringsAreUniqueNoDictionary()
    print("Strings have all unique characters without using data structure -> ", result_no_dic)

    assert result == result_no_dic, "Algorithms don't match"
