def gen_sq():
    squares = (x ** 2 for x in range(1, 11))
    for sqrs in squares:
         print(sqrs)

gen_sq()
