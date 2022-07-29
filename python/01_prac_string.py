""" 스트링 (String)
python 에서의 스트링 타입은 str
글자의 Unicode 로 이루어진 불변의 순서가 있는 집합
아래의 키워드로 문자열을 만들 수 있다.
""
''
""" """

# 이스케이프 (escape)
\\ : backslash
\' : single quote
\a : ASCII Bell
\b : ASCII Backspace
\f : ASCII Formfeed
\n : ASCII Linefeed
\r : ASCII Carriage Return
\t : ASCII Horizontal Tab
\v : ASCII Vertical Tab

# 변환
str() 내장 메소드 통해서
"""
# 유용한 스트링 함수들
# help() 내장 메소드 통해서 알아볼 수 있다.

if __name__ == '__main__':
    help(str)

    print('*' * 50)
    a = 'test, test, test'
    b = str(a)
    print(id(a)) # 같음
    print(id(b))

    print('*' * 50)
    a = 'test, test, test'
    a = a.__add__('a')
    print(a) # test, test, testa

    # capitalize(self, /)
    # |      Return a capitalized version of the string.

    # center(self, width, fillchar=' ', /)
    #  |      Return a centered string of length width.
    #  |
    #  |      Padding is done using the specified fill character (default is a space).

    # count(...)
    #  |      S.count(sub[, start[, end]]) -> int
    #  |
    #  |      Return the number of non-overlapping occurrences of substring sub in
    #  |      string S[start:end].  Optional arguments start and end are
    #  |      interpreted as in slice notation.

    # encode(self, /, encoding='utf-8', errors='strict')
    # |      Encode the string using the codec registered for encoding.

    # endswith(...)
    # | S.endswith(suffix[, start[, end]]) -> bool
    #     Return True if S ends with the specified suffix, False otherwise.
    #      |      With optional start, test S beginning at that position.
    #      |      With optional end, stop comparing S at that position.
    #      |      suffix can also be a tuple of strings to try.

    # find(...)
    #  |      S.find(sub[, start[, end]]) -> int
    #  |
    #  |      Return the lowest index in S where substring sub is found,
    #  |      such that sub is contained within S[start:end].  Optional
    #  |      arguments start and end are interpreted as in slice notation.
    #  |
    #  |      Return -1 on failure.

    # index(...)
    #  |      S.index(sub[, start[, end]]) -> int
    #  |
    #  |      Return the lowest index in S where substring sub is found,
    #  |      such that sub is contained within S[start:end].  Optional
    #  |      arguments start and end are interpreted as in slice notation.
    #  |
    #  |      Raises ValueError when the substring is not found.

    # isalnum(self, /)
    #  |      Return True if the string is an alpha-numeric string, False otherwise.
    #  |
    #  |      A string is alpha-numeric if all characters in the string are alpha-numeric and
    #  |      there is at least one character in the string.

    # isalpha(self, /)
    # |      Return True if the string is an alphabetic string, False otherwise.
    # |
    # |      A string is alphabetic if all characters in the string are alphabetic and there
    # |      is at least one character in the string.

    # isdecimal(self, /)
    # |      Return True if the string is a decimal string, False otherwise.
    # |
    # |      A string is a decimal string if all characters in the string are decimal and
    # |      there is at least one character in the string.

    # isdigit(self, /)
    # |      Return True if the string is a digit string, False otherwise.
    # |
    # |      A string is a digit string if all characters in the string are digits and there
    # |      is at least one character in the string.

    # islower(self, /)
    #  |      Return True if the string is a lowercase string, False otherwise.
    #  |
    #  |      A string is lowercase if all cased characters in the string are lowercase and
    #  |      there is at least one cased character in the string.

    # isnumeric(self, /)
    # |      Return True if the string is a numeric string, False otherwise.
    # |
    # |      A string is numeric if all characters in the string are numeric and there is
    # |      at least one character in the string .
