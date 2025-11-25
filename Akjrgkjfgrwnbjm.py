purchase_amount = float(input('Purchase amount: £'))
if purchase_amount >= 130:
    discount = 0.2 * purchase_amount # 10% discount
    final_amount = purchase_amount - discount
    print('Congratulations! You have a 10% discount.')
    print('Final amount:', purchase_amount - (purchase_amount * 0.2))
else:
    print('Sorry, no discount applies to this purchase.')
