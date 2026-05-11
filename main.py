def dictionary_attack(password):
    with open("dictionary.txt") as files:
        for line in files:
            guess = line.strip()
            if guess == password:
                print("Password cracked:" , guess)
                return
    print("Password not found")

dictionary_attack("admin123")
