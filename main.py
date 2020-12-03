import random

names = ["David", "Alina", "Betta", "Chiara", "Fefo", "Giada", "Matilda", "Carlotta", "Raffa", "Ricky", "Usai"]

attempts = 1

def santa_gen(names):
    global attempts
    same_name = False
    r = random.sample(names, len(names))
    for n in range(len(names)):
        if names[n] == r[n]:
            same_name = True
    if same_name == True:
        attempts += 1
        santa_gen(names)
    else:
        print(attempts)
        return r


def send_letter(names, secret_kids):
    for a in range(len(names)):
        file = "D:/Dropbox/Dropbox/Code/Python/Secret Santinator/Secrets/" + names[a] + ".txt"
        f = open(file, "w")
        f.write(secret_kids[a])
        f.close()

send_letter(names, santa_gen(names))




