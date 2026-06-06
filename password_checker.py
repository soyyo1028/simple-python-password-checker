import os
import time

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

cls()
print("Bienvenido a Password Strong Checker | Soyyo\n\n" + "="*45 + "\n\nEste programa está diseñado para verificar la seguridad de su contraseña.")

passw = input('\nIngrese su contraseña: ')
score = 10
hasErrors = False
common = {'123456', 
          'admin', 
          '12345678', 
          '12345', 
          'aa123456', 
          '1234567890', 
          'pass@123', 
          'admin123', 
          '1234567', 
          '123123', 
          '111111', 
          '12345678910', 
          'p@ssw0rd', 
          'aa@123456', 
          'admintelecom', 
          'admin@123', 
          '112233', 
          '102030', 
          '654321', 
          'abcd1234', 
          'abc123', 
          'qwerty123', 
          'abcd@1234', 
          'pass@1234', 
          '11223344', 
          '87654321', 
          'secret', 
          'qwerty', 
          'iloveyou', 
          'dragon', 
          'monkey', 
          'qwertyuiop', 
          'password', 
          'contrasena', 
          'contrasena123', 
          '123contrasena',
          'password123'}

time.sleep(1)
cls()
time.sleep(0.5)

if "ñ" in passw.lower():    
    cls()
    print('Error: La contraseña no puede contener la letra ñ.')
    time.sleep(1)
    quit()

if len(passw)<4:
    print('➔  Su contraseña es demasiado corta.')
    score -= 6
    hasErrors = True
elif len(passw)<8:
    print('➔  Su contraseña debe contener al menos 8 caracteres.')
    score -= 4
    hasErrors = True
if not any(char.isupper() for char in passw):
    print('➔  Su contraseña debe contener al menos una mayúscula.')
    score -= 2
    hasErrors = True
if not any(char.islower() for char in passw):
    print('➔  Su contraseña debe contener al menos una minúscula.')
    score -= 2
    hasErrors = True
if not any(not char.isalnum() for char in passw):
    print('➔  Su contraseña debe contener al menos un caracter especial.')
    score -= 2
    hasErrors = True
if not any(char.isdigit() for char in passw):
    print('➔  Su contraseña debe contener al menos un número.')
    score -= 2
    hasErrors = True
if passw.lower() in common:
    print('➔  Contraseña muy común.')
    score -= 5

if hasErrors:
    print('⬆️   Flags encontradas. ⬆️')
else:
    print('¡Bien hecho, no se encontraron flags! 🥳')

score = max(score, 0)

if score<=2:
    strength = "muy débil"
elif score<=4:
    strength = "débil"
elif score<=7:
    strength = "moderada"
else:
    strength = "fuerte"   

print(f'\nPunteo: {score}/10 (Contraseña {strength})')