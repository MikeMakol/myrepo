def ask_ok(prompt, retries=4, reminder="Please try again!"):
    while True:
        ok = input(prompt)
        if ok in ('y', 'yes', 'ye'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError("Invalid user response.")
        #print(reminder)

#ask_ok("Do you really wana quit? ")
i = 5
def cheeseshop(kind, *arguments, **keywords):
    print('__Do you have any', kind,'?')
    print("__I'm sorry, we're out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
