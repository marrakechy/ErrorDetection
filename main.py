def credit_card_check(card_number):
    card_number = list(map(int, card_number))
    t_sum = 0

    for i in range(len(card_number) - 2, -1, -2):
        doubled_digit = card_number[i] * 2
        if doubled_digit > 9:
            doubled_digit -= 9
        card_number[i] = doubled_digit

    t_sum = sum(card_number)

    if t_sum % 10 == 0:
        return True
    else:
        return False

card_number = input("Enter a 14-digit credit card number: ")

if len(card_number) == 14 and card_number.isdigit():
    if credit_card_check(card_number):
        print("Valid card number")
    else:
        print("this is not a valid card number")
else:
    print("Invalid input")


