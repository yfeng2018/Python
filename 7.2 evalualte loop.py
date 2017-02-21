def eval_loop():
    while True:
        f=input('Input your math operation here...\n')
        if f=='done':
            break
        print(eval(f))
    return f

eval_loop()
