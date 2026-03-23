#estrutura de seleção

mes = int(input("digite o mes em número: "))

match mes:
    case 1: 
        print("Janeiro")
    case 2: 
        print("Fevereiro")
    case 3: 
        print("Março")
    case 4: 
        print("Abril")
    case 5: 
        print("Maio")
    case 6: 
        print("Junho")
    case 7: 
        print("Julho")
    case _: 
        print("Valor Inválido")
    