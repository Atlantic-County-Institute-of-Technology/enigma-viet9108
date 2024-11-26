# enigma.py
# description: a simple rotational ciphertext program that can create
# custom encoded messages, as well as encode and decode from file.
# author: YOUR_NAME_HERE
# created: MM.DD.YYYY
# last update:  MM.DD.YYYY
import random

# we'll be using this string for the majority of our translations
alphabet = "abcdefghijklmnopqrstuvwxyz"

key = 0


# user inputs a message and selects a key (or random), the message is then translated using the cipher
def encode_message(scrabbled=None):
    message = input("Input your message here : ")
    cypher = input("How many letters would you like to shift by? : ")
    if 1 > int(cypher) > 26:
        cypher = random.randint(1, 26)
    print(f"This is your cypher : {cypher}")

    for x in range(len(message)):
        y = alphabet.find(message[x])
        z = (y+int(cypher)) % 26
        print(f'{alphabet[z]}', end="")
        # if ' ' in message:
        #     print(f' ', end="")
    pass


# encodes a target file, similarly to encode_message, except now targeting a filename
def encode_file():
    pass


# decodes target file using a user-specified key. If key is unknown, a keypress should
# call decode_unknown_key()
def decode_file():

    pass


# runs if the key is unknown. If this is true, print out all possible decoding combinations.
def decode_unknown_key():
    unknown = input("Enter your encoded message : ")
    for i in range(len(alphabet)):
        print(f'{i}: ', end="")
        for x in range(len(unknown)):
            y = alphabet.find(unknown[x])
            z = (y-i) % 26
            print(f'{alphabet[z]}', end="")
        print("\n")
    pass


# main method declaration
def main():
    while True:
        print(f"\nWelcome to the Enigma Machine!\n"
              f"Please select an option:\n"
              f"[1]: Encode a custom message.\n"
              f"[2]: Encode file.\n"
              f"[3]: Decode file.\n"
              f"[5]: Decode message.\n"
              f"[4]: Exit.")

        selection = input("Choose an option:")

        if selection == "1":
            encode_message()
        elif selection == "2":
            encode_file()
        elif selection == "3":
            decode_file()
        elif selection == "4":
            print("Goodbye.")
            exit()
        elif selection == "5":
            decode_unknown_key()
        else:
            print("Invalid choice. Please try again.")


# runs on program start
if __name__ == "__main__":
    main()
