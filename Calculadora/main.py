from Calculadora.dividir import dividir as d
from Calculadora.multiplicar import multiplicar as m
from Calculadora.restar import restar as r
from Calculadora.sumar import sumar as s


def main():
    print("Resultado de la suma: ",s.suma(7,8))
    print("Resultado de la resta: ",r.resta(7,4))
    print("Resultado de la multiplicacion: ",m.multiplica(3,8))
    print("Resultado de la division: ",d.divide(24,8))

if __name__ == '__main__':
    main()