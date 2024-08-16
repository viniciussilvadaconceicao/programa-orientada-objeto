def temperatura():
    '''função para saber a temperatura'''
    temp = float(input("digite a temperatura:"))
    if temp < 35:
        print("Está congelando")

    elif temp >= 35 and temp <= 37.5:
        print(f"Está normal sua temperatura é: {temp}") 

    elif temp > 37.5 and temp <= 38:
        print(f"Está febril sua temperatura é: {temp}")
    
    else:
        print(f"Está com febre alta sua temperatura é: {temp}")
        
temperatura()