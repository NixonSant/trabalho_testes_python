def converte_F_para_C(temperatura):
    """
    Testes:

    >>> converte_F_para_C(32)
    0.0

    >>> converte_F_para_C(-40)
    -40.0
    """
    return ((temperatura - 32) / 9) * 5


def converte_C_para_F(temperatura):
    return temperatura * (9 / 5) + 32

opcao = input(
    'Digite F para Fahrenheit\n'
    'Digite C para Celsius: '
)

temperatura = float(input('Forneça a temperatura: '))

match (opcao):
    case 'F':
        resultado = converte_C_para_F(temperatura)
        print(f'A temperatura convertida é: {resultado}')
    case 'C':
        resultado = converte_F_para_C(temperatura)
        print(f'A temperatura convertida é: {resultado}')
    case _:
        print('Digite F ou C. Tá errado!!!!')