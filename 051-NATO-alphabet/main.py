import pandas

alphabet_data = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_df = pandas.DataFrame(alphabet_data)

alphabet_dict = {row["letter"]: row["code"] for (index, row) in alphabet_df.iterrows()}


def generate_nato_alphabet():
    user_input_word = input("Enter a word: ").upper()
    try:
        nato_alphabet = [alphabet_dict[letter] for letter in user_input_word]
    except KeyError:
        print("Sorry! Only the letters in alphabets are expected.")
        generate_nato_alphabet()
    else:
        print(nato_alphabet)


generate_nato_alphabet()
