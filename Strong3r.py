#

import random
import string

def gerar_senha(tamanho_senha, incluir_minusculas=True, incluir_maiusculas=True, incluir_numeros=True, incluir_simbolos=True):

#

  caracteres = []

  if incluir_minusculas:
    caracteres.extend(string.ascii_lowercase)
  if incluir_maiusculas:
    caracteres.extend(string.ascii_uppercase)
  if incluir_numeros:
    caracteres.extend(string.digits)
  if incluir_simbolos:
    caracteres.extend(string.punctuation)

  senha = "".join(random.choice(caracteres) for _ in range(tamanho_senha))
  return senha

# Função para interagir com o usuário

def interagir_usuario():

#  Interage com o usuário para obter as opções de senha.

  tamanho_senha = int(input("Tamanho da senha desejada: "))

  while True:
    incluir_minusculas = input("Incluir minúsculas? (s/n): ").lower() == "s"
    incluir_maiusculas = input("Incluir maiúsculas? (s/n): ").lower() == "s"
    incluir_numeros = input("Incluir números? (s/n): ").lower() == "s"
    incluir_simbolos = input("Incluir símbolos? (s/n): ").lower() == "s"

    if incluir_minusculas or incluir_maiusculas or incluir_numeros or incluir_simbolos:
      break
    else:
      print("Ao menos um grupo de caracteres deve ser selecionada.")

  return tamanho_senha, incluir_minusculas, incluir_maiusculas, incluir_numeros, incluir_simbolos

# Chamada da função interativa e geração da senha

tamanho_senha, incluir_minusculas, incluir_maiusculas, incluir_numeros, incluir_simbolos = interagir_usuario()
senha = gerar_senha(tamanho_senha, incluir_minusculas, incluir_maiusculas, incluir_numeros, incluir_simbolos)
print(f"Senha gerada: {senha}")
