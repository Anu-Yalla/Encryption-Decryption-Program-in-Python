
def translate(from_letters, to_letters, text):
    """
    The translate function does a letter to letter translation.
    The from_letters and to_letters parameters are expected to
    be strings of uppercase letters and both strings need to be 
    the same length. The from_letters and to_letters strings define
    a mapping such that from_letters[i] found in the text string 
    parameter will be converted to to_letters[i].  All characters in 
    the text parameter not found in from_letters are left as-is.
    Case of letters in the text parameter are preserved in the result.
    For example translate("ABC","CAB","C3PO-aBA") will return the 
    string "B3PO-cAC".  Likewise, translate("CAB","ABC","B3PO-cAC")
    will return the string "C3PO-aBA".   
    """
    # Check that parameters meet assumptions. The only assumption not
    # tested is that each character in from_letters should occur once.
    # Students should not change this code.  It is here to catch mistakes.
    if not(from_letters.isupper() and from_letters.isalpha() and 
           to_letters.isupper() and to_letters.isalpha()):
        raise ValueError("from_letters and to_letters must be all uppercase letters")
    if len(from_letters) != len(to_letters):
        raise ValueError("from_letters and to_letters must be the same length")
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    # Students should add their code below for the translate function


    for i in range(len(text)):
        current = text[i]
        index = from_letters.find(current.upper())

        if index != -1: # If a valid letter, just add the og char to the end
            if current.isupper():
                # Keep the begining to before the current letter and add the uppercase version
                # of the current letter and lastly add the sliced remaning of the original text.
                text = text[0:i] + to_letters[index].upper() + text[i+1:len(text)]
            else:
                text = text[0:i] + to_letters[index].lower() + text[i+1:len(text)]
    return text


def main():
    # .strip is to handle the test cases where there is white spaces. 
    commands_file = open("commands.txt", "r")
    key_file =  commands_file.readline().strip()
    task =  commands_file.readline().strip()
    input_file = commands_file.readline().strip()
    output_file = commands_file.readline().strip()
    commands_file.close()

    # Define the alphabet 
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    key_file = open(key_file, "r")
    key = key_file.readline()
    key_file.close()

    text = ""
    input_file = open(input_file, "r")
    line = input_file.readline()
    while line != "":
        text = text + line
        line = input_file.readline()
    input_file.close()

    # Perform encryption or decryption depending on what the commands.txt file says.
    if task == "encrypt":
        encrypted_text = translate(alphabet, key, text)
    elif task == "decrypt":
        encrypted_text = translate(key, alphabet, text)

    # Write the result to the output file.
    output_file = open(output_file, "w")
    output_file.write(encrypted_text)
    output_file.close()


if __name__ == "__main__":
    main()
