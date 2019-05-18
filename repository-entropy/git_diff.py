import re


class GitDiff:
    """Representation of a git diff"""

    __additions = None
    __removals = None
    __change_regex = None

    def __init__(self, diff_text):
        self.__additions = []
        self.__removals = []
        self.__change_regex = re.compile(r"@@\s+\-\d+,\d+ \+\d+,\d+\s+@@$")
        self.__parse_diff(diff_text)

    def __parse_diff(self, text):
        split_text = text.split("\n")
        reached_change = False

        for line in split_text:
            if self.__change_start(line):
                reached_change = True

            if not reached_change:
                continue

            self.__parse_line(line)

    def __parse_line(self, line):
        if self.__addition_line(line):
            self.__additions += [line[1:]]

        if self.__removal_line(line):
            self.__removals += [line[1:]]

    def __change_start(self, line):
        return self.__change_regex.match(line) is not None

    @staticmethod
    def __addition_line(line):
        return len(line) > 0 and line[0] == "+"

    @staticmethod
    def __removal_line(line):
        return len(line) > 0 and line[0] == "-"

    def additions(self):
        return self.__additions

    def removals(self):
        return self.__removals

    def all(self):
        return self.__additions+self.__removals
