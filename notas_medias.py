nota1 = float(input('Primeira Nota: '))
nota2 = float(input('Segunda Nota: '))
nota3 = float(input('Terceira Nota: '))
nota4 = float(input('Quarta Nota: '))
media = (nota1 + nota2 + nota3 + nota4) / 2
print('Tirando {} e {} a média do aluno é {}'.format(nota1,nota2,nota3,nota4))

if media > 7:
    print('Parabéns, você foi aprovado')
if media < 7 and media > 5.5:
    print('Você está de recuperação')
if media > 5.5:
    print('Você está reprovado')