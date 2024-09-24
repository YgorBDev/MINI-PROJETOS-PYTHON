import random as rnd

palpipe = 999
sorteado = rnd.randint(0,10)
cont = 0

while palpipe != sorteado:
  palpipe = int(input("Digite um número entre 0 e 10 para testar sua sorte! : "))
  print(" ")
  if palpipe == sorteado:
    print("Parabéns você acertou!!")
    print(f"O número sorteado era: {sorteado}")
  else:
    cont=cont+1
    print(f"Você errou pela {cont}°!")
