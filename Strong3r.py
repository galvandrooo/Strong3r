import random
import string

def gerar_senha(tamanho_senha, incluir_minusculas=True, incluir_maiusculas=True, incluir_numeros=True, incluir_simbolos=True):

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

def interagir_usuario():

 tamanho_senha = int(input("TAMANHO DA SENHA: "))

 while True:
    print('=' * 26)
    incluir_minusculas = input("INCLUIR MINUSCULAS? (s/n): ").lower() == "s"
    print('=' * 26)
    incluir_maiusculas = input("INCLUIR MAIUSCULAS? (s/n): ").lower() == "s"
    print('=' * 26)
    incluir_numeros = input("INCLUIR NUMEROS? (s/n): ").lower() == "s"
    print('=' * 23)
    incluir_simbolos = input("INCLUIR SIMBOLOS? (s/n): ").lower() == "s"
    print('=' * 24)
    
    if incluir_minusculas or incluir_maiusculas or incluir_numeros or incluir_simbolos:
      break
    else:
      print("""
            ERRO!!!
            
            AO MENOS UM GRUPO DE CARACTERES DEVE SER INCLUIDO...
            """)

 return tamanho_senha, incluir_minusculas, incluir_maiusculas, incluir_numeros, incluir_simbolos

tamanho_senha, incluir_minusculas, incluir_maiusculas, incluir_numeros, incluir_simbolos = interagir_usuario()
senha = gerar_senha(tamanho_senha, incluir_minusculas, incluir_maiusculas, incluir_numeros, incluir_simbolos)
print(f"""
{'=' * (tamanho_senha + 7)}
SENHA: {senha}
{'=' * (tamanho_senha + 7)}
""")
