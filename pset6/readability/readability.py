import cs50

def main():
    num_of_letters = 0
    num_of_words = 0
    num_of_sentences = 0
    index = 0
    user_input = cs50.get_string("Text: ")

    if (user_input is None):
        main()

    for char in user_input:
        # loop through the text and use ctype to count only letters

        if (char.isalpha()):
            num_of_letters += 1;

        # words are separated by spaces (e.g. "hello," is a word)
        if (char == " "):
            num_of_words += 1

        # sentences are separated by . ? !
        if (char == '.' or char == '?' or char == '!'):
            num_of_sentences += 1

    # the total number of words is equal to numbers of empty spaces + 1;
    if (num_of_words > 0):
        num_of_words += 1

    index = findColemanLiauIndex(num_of_letters, num_of_words, num_of_sentences)

    if (index < 1):
        print("Before Grade 1")
        return 0

    if (index >= 16):
        print("Grade 16+")
        return 0

    print(f"Grade {index}")

def findColemanLiauIndex(num_of_letters, num_of_words, num_of_sentences):
    divider = num_of_words if num_of_words > 0 else 1

    # L is the average number of letters per 100 words in the text
    L = num_of_letters / divider * 100.00

    # S is the average number of sentences per 100 words in the text
    S = num_of_sentences / divider * 100.00

    # Coleman Liau index = 0.0588 * L - 0.296 * S - 15.8;
    index = (0.0588 * L) - (0.296 * S) - 15.8

    return round(index)

main()
