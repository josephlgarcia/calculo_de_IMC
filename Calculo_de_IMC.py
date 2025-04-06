
print("==============================================")
print("                BIENVENIDO")
print("==============================================")

nombre= input("\nCómo es su nombre: ")

print(f"\nHola, {nombre}\n")

while True:
    try:
        masa = input("Ingrese su peso (en kg): ")
        masa = float(masa)
        break
    except ValueError:
        print("Ingrese un caracter válido")


while True:
    try:
        altura = input("Ingrese su altura (en metros): ")
        altura = float(altura)
        break
    except ValueError:
        print("Ingrese un caracter válido")



IMC = masa / (altura)**2

print(f"Su Índice de masa corporal es: {IMC: .2f}")

if IMC < 18.5:
    print("Está es bajo peso")
elif IMC >= 18.5 and IMC <= 24.5:
    print("Está en peso normal")
elif IMC > 24.5 and IMC <= 29.9:
    print("Está en sobrepeso")
else:
    print("Tiene obesidad")


print("Recuerde que el índice de masa corporal no es")
print("un indicador de salud sino un estandar")

print("")
