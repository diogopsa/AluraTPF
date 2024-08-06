x = float(input('Digite a coordenada x: '))
y = float(input('Digite a coordenada y: '))
if x == 0 and y == 0:
    print('Está localizado no centro do eixo cartesiano.')
elif x == 0 and y != 0:
    print('Está localizado no eixo das ordenadas.')
elif x != 0 and y == 0:
    print('Está localizado no eixo das abscissas.')
elif x > 0 and y > 0:
    print('Está localizado no primeiro quadrante')
elif x < 0 and y > 0:
    print('Está localizado no segundo quadrante')
elif x < 0 and y < 0:
    print('Está localizado no terceiro quadrante.')
else:
    print('Está localizado no quarto quadrante.')