import pandas

alphabet_data = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_df = pandas.DataFrame(alphabet_data)

# TODO 1. Create a dictionary in this format {"A": "Alfa", "B": "Bravo"}:
alphabet_dict = {row["letter"]: row["code"] for (index, row) in alphabet_df.iterrows()}
# print(alphabet_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input_word = input("Enter a word: ").upper()
nato_alphabet = [alphabet_dict[letter] for letter in user_input_word]
print(nato_alphabet)
