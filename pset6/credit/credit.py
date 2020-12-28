import cs50

#************************************
#    Validate card with checksum
#************************************
def validateCardNumber():
    userPrompt = cs50.get_int("Number: ")

    if (userPrompt is None):
        validateCardNumber()

    divider = 0;
    modulo = 0;
    digit = 0
    sumEven = 0;
    sumOdd = 0;
    cardNumberLength = len(str(userPrompt))

    # loop through the digits composing the card number, following Luhn’s Algorithm
    for i in str(userPrompt):

        if int(i) % 2 == 0:
            #do Luhn's algorithm calculations
            digitTimesTwo = digit * 2
            if (digitTimesTwo) > 9:
                sumEven = sumEven + digitTimesTwo % 10
                sumEven = sumEven + digitTimesTwo / 10 % 10
            else:
                sumEven = sumEven + digitTimesTwo
        else:
            sumOdd = sumOdd + digit

    sum = sumEven + sumOdd
    itValidatesLuhnsAlgorithm = sum % 10 == 0

    #determine card provider
    AMEX_LENGTH = 15
    MASTERCARD_LENGTH = 16
    VISA_LENGTH = 13

    firstTwoDigits = str(userPrompt)[0] + str(userPrompt)[1]
    firstDigit = str(userPrompt)[0]

    if (itValidatesLuhnsAlgorithm and cardNumberLength == AMEX_LENGTH or (firstTwoDigits == "34" or firstTwoDigits == "37")):
        print("AMEX")
    elif (itValidatesLuhnsAlgorithm and cardNumberLength == MASTERCARD_LENGTH and
        (firstTwoDigits == "51" or firstTwoDigits == "52" or firstTwoDigits == "53" or firstTwoDigits == "54" or firstTwoDigits == "55")):
        print("MASTERCARD")
    elif (itValidatesLuhnsAlgorithm and (cardNumberLength == VISA_LENGTH or cardNumberLength == MASTERCARD_LENGTH) and firstDigit == "4"):
        print("VISA")
    else:
        print("INVALID")

validateCardNumber()
