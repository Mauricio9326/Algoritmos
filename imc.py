altura = float(input('Informe sua altura (cm): '))
peso = float(input('Informe seu peso (kg): '))
imc = peso/(altura * altura)
if imc < 18.5:
    print('Você está abaixo do seu peso ideal.')
elif 24.9 > imc > 18.5:
    print('Você está em seu peso ideal')
elif 30 > imc > 24.9:
    print('Você está acima do peso.')
elif imc < 30:
    print('Você está obeso')

