def conversao(temperatura):
    return 5 * ((temperatura-32)/9)

if __name__ == '__main__':
    temperatura = float(input('Digite a temperatura em Fahrenheit: '))
    celsius = conversao(temperatura)
    print(f'A temperatura em Celsius é: {celsius}')