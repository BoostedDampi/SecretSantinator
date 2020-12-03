import random
import os

try:
    names = []

    dir_path = os.path.dirname(os.path.realpath(__file__)) + "/Secrets" #path to the folder where the names will be put in

    def santa_gen(names): #Outputs a shuffled list of names

        same_name = False
        r = random.sample(names, len(names)) #this shuffles the list

        for n in range(len(names)): #this checks if some names picked themselves
            if names[n] == r[n]:
                same_name = True

        if same_name == True: #if some names picked themselves the function repeats
            santa_gen(names)

        return r #If all names are different the list will be returned


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

    print("-"*50)
    print("Secret Santinator")
    print
    print("-"*50)
    print("Scrivi i nomi dei partecipanti seguiti da una virgola e uno spazio.\n Es. David, Usai, Lollo")
    names = input(">> ").split(", ")


    send_letter(names, santa_gen(names))
    print()
    print("Completed! Check your new 'Secret' folder, and send the files to your friends.")
    print("If you cant delete the folder in the future, delete the files in it first.")
    print("Have fun, David")
    input()

except:

    print("I don´t know what you have done, but please don´t do it again.")
    input()
