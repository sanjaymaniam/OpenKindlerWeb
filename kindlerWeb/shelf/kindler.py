import os
from sys import argv
from shelf.models import Clipping

def getUnits(path_to_file):
    """Returns list of all 'units'.
    A unit is a tuple with (title, details, message), NOT a highlight. Highlights and notes are messages."""

    def getLines(path_to_file):
        "Returns list of all lines from file. Extra delimeter is added to beginning."
        file = open(path_to_file, 'r', encoding='utf-8-sig')
        return ['=========='] + [line.strip() for line in file]

    def delimeterIndices(delimeter='=========='):
        "Returns indices of lines with delimeter. We use this to identify individual highlights."
        lines = getLines(path_to_file)
        return [i for i, line in enumerate(lines) if line == '==========' and i != len(lines)-1]

    def breakTitleAuthor(titleline):
        "Breaks the line 'TITLE_NAME_HERE (AUTHOR)' to (title, author)"
        author = titleline.split('(')[-1][:-1]
        title = titleline[:titleline.find(f"({author})")-1]
        if title.startswith('\ufeff'):
            title = title.strip('\ufeff')
        split_name = author.split(',') #amazon stores authors as (Murakami, Haruki).
        if len(split_name) == 2:
            author = f"{split_name[1][1:]} {split_name[0]}"
        return (title, author)

    def parseDetails(details):
        "Returns tuple (kind_of_unit, location). For locations of type '100-123', we take 100."
        listed_details = details.split()
        return(listed_details[2], int(f"{listed_details[8] if 'on' not in listed_details[8] else listed_details[5]}".split('-')[0]))

    lines, units = getLines(path_to_file), []

    for delimeterIndex in delimeterIndices():
        title, author = breakTitleAuthor(lines[delimeterIndex+1])
        kind_of_unit, location = parseDetails(lines[delimeterIndex+2])
        message = lines[delimeterIndex+4]
        units.append((title, author, kind_of_unit, location, message))
    return units


def getTitles(path_to_file):
    "Returns alphabetically sorted list of titles. Removes duplicates."
    # to-do: allow sorting using keys- last read or alphabetically.
    from string import ascii_letters
    titles = []
    for unit in getUnits(path_to_file):
        title = unit[0]
        # handling titles that start with u'\ufeff'.
        if title[0] not in ascii_letters:
            titles.append(title[1:])
        else:
            titles.append(title)
    return sorted(list(set(titles)))