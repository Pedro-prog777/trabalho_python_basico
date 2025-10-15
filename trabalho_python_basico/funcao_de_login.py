# Questão 1 - Verificação de login

def login(email, senha):
   
    if email == "admin" and senha == "admin":
        return True
    else:
        return False
    
print(login("admin", "admin"))  # Retorna True
print(login("user", "123"))     # Retorna False

