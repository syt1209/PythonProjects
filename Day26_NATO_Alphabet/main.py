import pandas
nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row[0]: row[1] for (index, row) in nato_df.iterrows()}


def generate_phonetic():
    try:
        user_input = input("Enter a word: ").upper()
        code_words = [nato_dict[letter] for letter in user_input]
    except KeyError:
        print("Please type alphabet only.")
        generate_phonetic()
    else:
        print(code_words)


generate_phonetic()


