import random
import string

print("Generez votre mot de passe. ")

z = int(input("Combien de lettres minuscules doit-il avoir? "))
y = int(input("Combien de lettres majuscules doit-il avoir? "))
a = int(input("Combien de chiffres doit-il avoir? "))
x = int(input("Combien de signes de ponctuation doit-il avoir? "))

mot_de_passe = ""

for i in range(z):
    mot_de_passe += random.choice(string.ascii_lowercase)

for i in range(y):
    mot_de_passe += random.choice(string.ascii_uppercase)

for i in range(a):
    mot_de_passe += random.choice(string.digits)

for i in range(x):
    mot_de_passe += random.choice(string.punctuation)

mot_de_passe_melange = ''.join(random.sample(mot_de_passe, len(mot_de_passe)))

print(mot_de_passe_melange)


