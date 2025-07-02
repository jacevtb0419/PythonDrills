def make_receipt(float):
    discount = float * .9
    print(float)
    print(discount)
    return discount

make_receipt(make_receipt(20.0))