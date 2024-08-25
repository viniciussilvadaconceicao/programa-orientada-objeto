def distribuir_convites():
    fralda = ['P', 'M', 'G', 'GG']

    pessoas = ['marcos rodrigo','francine','filho de marcos', 'thiago nupicias','manu','filho de thiago','sogra de thiago', 'renan brasil','esposa renan', 'jean mega','esposa jean', 'elias', 'fabio alves','esposa do fabio', 'julio','esposa do julio', 'vitor barbeiro', 'esposa do vitor', 'ruan', 'aline', 'theo','celma', 'irinete', 'nilsa', 'marido da nilsa', 'breno','altinei', 'juliana', 'mulher da juliana', 'silvana', 'maicon', 'mae da silvana', 'aline amiga da andreza', 'sabrina', 'marido da sabrina', 'filho sabrina', 'yasmin','filha de yasmin','julia', 'filho de julia', 'filha de julia','andriele','amanda', 'leo', 'camila', 'samuel','jeferson', 'rafael','marcos de cachoeira', 'esposa do marcos', 'filho do marcos','raul','esposa do raul','filha do raul','pablo','esposa do pablo','sogra do pablo','roni','esposa do roni','fulano']

    familia = ['raul e sua familia','marcos rodrigo e sua familia', 'thiago nupicias e sua familia', 'renan brasil e sua familia', 'jean mega e sua familia', 'fabio alves e sua familia','elias e sua familia','ruan e sua familia','irinete e sua familia','julio e sua familia', 'vitor barbeiro e sua familia', 'nilsa e sua familia', 'juliana e sua familia', 'silvana e sua familia','aline e sua familia', 'sabrina e sua familia', 'yasmin e sua familia', 'julia e sua familia','andriele e sua familia','amanda e sua familia','camila e sua familia','jeferson e sua familia','rafael e sua familia', 'marcos de cachoeira e sua familia', 'pablo e sua familia', 'roni e sua familia']
    print('-'*50)
    for i, fam in enumerate(familia):
        salgado = 97 * 4
        mesa = len(pessoas) / 4
        bebida = len(pessoas)
        refrig = (bebida / 2) / 2 + 5
        suco = (bebida / 4) - 5
        doce = len(pessoas) * 4
        print(f'a fralda é {fralda[i % len(fralda)]} para a {fam} ')
    print('-'*50)
    print(f'vai ter um total de {len(familia)} familias')
    print('-'*50)
    print(f'vai ter um total de {len(pessoas)} pessoas vou precisar de {mesa} mesas de 4 lugares em dinheiro da {mesa * 9}R$')
    print('-'*70)   
    print(f'vai ter um total de {len(pessoas)} pessoas vou precisar de {len(pessoas) * 10 } salgados em dinheiro da {salgado}R$')
    print('-'*70)
    print(f'mini cachorro quente 2 por convidado {len(pessoas) * 2} mini cachorro quente')
    print('-'*50)
    print(f'sopa de ervilha 2 pratos por convidado {len(pessoas)}')
    print('-'*50)
    print(f'1 litro de refrigerante e suco por pessoa {len(pessoas)} litros em media {refrig} garrafas de 2 litros e {suco} de 1 litro')
    print('-'*70)
    print(f'doce 4 por pessoa, em media {doce} doces')
    print('-'*50)
distribuir_convites()

def salgado_tio():
    salgado = 150
    valor = 97
    cont = valor / salgado
    print(cont)

def bentido_sabor():
    salgado = 100
    valor = 70
    cont = valor / salgado
    print(cont)

