import random


class Generator():

    @staticmethod
    def generate() -> str:
        password = []
        special_chars = "!@#$"
        password.append(chr(random.randint(65,90)))
        password.append(chr(random.randint(65,90)))
        password.append(chr(random.randint(97,122)))
        password.append(chr(random.randint(97,122)))
        password.append(str(random.randint(0, 9)))
        password.append(str(random.randint(0 , 9)))
        password.append(random.choice(special_chars))
        password.append(random.choice(special_chars))
        random.shuffle(password)
        return "".join(password)

if __name__ == "__main__":
    generator = Generator()
    print(generator.generate())
