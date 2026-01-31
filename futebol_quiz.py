#futebol_quiz
import json
import random

MAX_TRIES = 5

with open("data_futebol_quiz.json", encoding="utf8") as f:
    words = json.load(f)

computer_c = random.choice(list(words.keys()))

print("Que comecem os jogos!!")
print("Adivinhe a data! DDMMAAAA")
print("✅ dígito correto | ⬆️ menor que o correto | ⬇️ maior que o correto")
print("#########################################")


user_tries = MAX_TRIES
win = False

while user_tries > 0 and not win:
    print("Dica:", words[computer_c])
    user_pontuation = 0
    user_answer = input("DDMMAAAA:\n")

    if not user_answer.isdigit():
        print("Resposta inválida, insira apenas números.\n")
        continue

    if len(user_answer) != 8:
        print("Resposta inválida, use o formato DDMMAAAA.\n")
        continue

    user_tries -= 1
    check = []

    for i in range(8):
        if user_answer[i] == computer_c[i]:
            check.append("✅")
            user_pontuation += 1
        elif int(user_answer[i]) > int(computer_c[i]):
            check.append("⬇️ ")
        else:
            check.append("⬆️ ")

    print("Resposta:")
    print("|".join(check))
    print(" |".join(user_answer))
    print("#########################################")

    if user_pontuation == 8:
        win = True

tentativas_usadas = MAX_TRIES - user_tries

if win:
    print(f"Parabéns! Você acertou em {tentativas_usadas} tentativa(s)!")
else:
    print("Mais sorte na próxima vez!")
    print("A data correta era:", computer_c)


