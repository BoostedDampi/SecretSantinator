import random
import os


names = []

dir_path = os.path.dirname(os.path.realpath(__file__)) + "/Secrets" #path to the folder where the names will be put in

def santa_gen(names): #Outputs a shuffled list of names

    while True:
        candidate = True
        r = random.sample(names, len(names)) #this shuffles the list
        for n in range(len(names)):
            print(f"Checking '{names[n]}' against '{r[n]}'")
            if names[n] == r[n]:
                candidate = False
                print()
                print("Reshuffling...")
                break
        if candidate == True:
            return r





def send_letter(names, random_names):

    try:
        os.makedirs(dir_path, exist_ok=True) #this will create a folder in the same location as the script

        for a in range(len(names)): #This bit creates a file for every name and writes his secret santa into it
            file = f"{dir_path}/{names[a]}.txt"
            f = open(file, "w")
            f.write(random_names[a])
            f.close()

    except:
        f.close()


debug = False

if debug == True:
    names = input(">> ").split(", ")
    santa = santa_gen(names)
    print(f"This is the original list: \n {names} \nThis is the new list: \n {santa}")


else:
    print("-"*50)
    print("Secret Santinator")
    print
    print("-"*50)
    print("Scrivi i nomi dei partecipanti seguiti da una virgola e uno spazio.\nEs. David, Usai, Lollo")
    names = input(">> ").split(", ")
    print()

    send_letter(names, santa_gen(names))

    print()
    print("Completed! Check your new 'Secret' folder, and send the files to your friends.")
    print("If you cant delete the folder in the future, delete the files in it first.")
    print("Have fun, David")
    input()
