"""
CP1404/CP5632 Practical 07 - File reading and class example.
Reads a CSV file of programming language details into objects.
Estimate: 10 min
Actual: 10 min
"""
from programming_language import ProgrammingLanguage

def main():
    languages = []
    in_file = open('languages.csv', 'r')
    header = in_file.readline()
    for line in in_file:
        line = line.strip()
        if not line:
            continue
        parts = line.split(',')
        name = parts[0]
        typing = parts[1]
        reflection = (parts[2] == "Yes")
        year = int(parts[3])
        pointer_arithmetic = (parts[4] == "Yes")
        language = ProgrammingLanguage(name, typing, reflection, year, pointer_arithmetic)
        languages.append(language)
    in_file.close()
    for language in languages:
        print(language)

if __name__ == "__main__":
    main()
