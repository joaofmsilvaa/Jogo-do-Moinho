
    "a1": ({"coluna":"b" ,"linha": "1"}, {"coluna":"a" ,"linha": "2"}, {"coluna":"b" ,"linha": "2"}),
    "b1": ({"coluna":"a" ,"linha": "1"}, {"coluna":"c" ,"linha": "1"}, {"coluna":"b" ,"linha": "2"}),
    "c1": ({"coluna":"b" ,"linha": "1"}, {"coluna":"c" ,"linha": "2"}, {"coluna":"b" ,"linha": "2"}),
    "a2": ({"coluna":"a" ,"linha": "1"}, {"coluna":"a" ,"linha": "3"}, {"coluna":"b" ,"linha": "2"}),
    "b2": ({"coluna":"a" ,"linha": "1"}, {"coluna":"b" ,"linha": "1"}, {"coluna":"c" ,"linha": "1"}, {"coluna":"a" ,"linha": "2"}, {"coluna":"c", "linha": "2"}, {"coluna":"a", "linha": "3"}, {"coluna":"b", "linha": "3"}, {"coluna":"c", "linha": "3"}),
    "c2": ({"coluna":"c" ,"linha": "1"}, {"coluna":"c" ,"linha": "3"}, {"coluna":"b" ,"linha": "2"}),
    "a3": ({"coluna":"a" ,"linha": "2"}, {"coluna":"b" ,"linha": "3"}, {"coluna":"b" ,"linha": "2"}),
    "b3": ({"coluna":"a" ,"linha": "3"}, {"coluna":"c" ,"linha": "3"}, {"coluna":"b" ,"linha": "2"}),
    "c3": ({"coluna":"c" ,"linha": "2"}, {"coluna":"b" ,"linha": "2"}, {"coluna":"b" ,"linha": "3"})
}

# print(""" 
#    A     B     C
# 1  [ ] - [ ] - [ ]\n
#    |  \\  |  /  | \n
# 2  [ ] - [ ] - [ ]\n
#    |  /  |  \\  | \n
# 3  [ ] - [ ] - [ ]\n
# """)

#####################################
# TAD Posicao - START
#####################################

adjacentes = {
    "a1": ({"coluna":"b" ,"linha": "1"}, {"coluna":"a" ,"linha": "2"}, {"coluna":"b" ,"linha": "2"}),
    "b1": ({"coluna":"a" ,"linha": "1"}, {"coluna":"c" ,"linha": "1"}, {"coluna":"b" ,"linha": "2"}),
    "c1": ({"coluna":"b" ,"linha": "1"}, {"coluna":"c" ,"linha": "2"}, {"coluna":"b" ,"linha": "2"}),
    "a2": ({"coluna":"a" ,"linha": "1"}, {"coluna":"a" ,"linha": "3"}, {"coluna":"b" ,"linha": "2"}),
    "b2": ({"coluna":"a" ,"linha": "1"}, {"coluna":"b" ,"linha": "1"}, {"coluna":"c" ,"linha": "1"}, {"coluna":"a" ,"linha": "2"}, {"coluna":"c", "linha": "2"}, {"coluna":"a", "linha": "3"}, {"coluna":"b", "linha": "3"}, {"coluna":"c", "linha": "3"}),
    "c2": ({"coluna":"c" ,"linha": "1"}, {"coluna":"c" ,"linha": "3"}, {"coluna":"b" ,"linha": "2"}),
    "a3": ({"coluna":"a" ,"linha": "2"}, {"coluna":"b" ,"linha": "3"}, {"coluna":"b" ,"linha": "2"}),
    "b3": ({"coluna":"a" ,"linha": "3"}, {"coluna":"c" ,"linha": "3"}, {"coluna":"b" ,"linha": "2"}),
    "c3": ({"coluna":"c" ,"linha": "2"}, {"coluna":"b" ,"linha": "2"}, {"coluna":"b" ,"linha": "3"})
}

def cria_posicao (coluna, linha):
    linha = linha.strip().lower()
    coluna = coluna.strip().lower()
    if valiarArgumentos(coluna, linha):
        return {"linha": linha, "coluna": coluna}

def valiarArgumentos(coluna, linha):
    if type(linha) != str or type(coluna) != str:
        raise ValueError("cria_posicao: argumentos invalidos")
    if linha not in ["1","2","3"]:
        raise ValueError("cria_posicao: argumentos invalidos")
    if coluna not in ["a","b","c"]:
        raise ValueError("cria_posicao: argumentos invalidos")
    return True

def cria_copia_posicao(posicao):
    return cria_posicao(posicao["coluna"], posicao["linha"])

def obter_pos_c(posicao):
    return posicao["coluna"]

def obter_pos_l(posicao):
    return posicao["linha"]

def eh_posicao(posicao):
    if type(posicao) != dict:
        return False
    if len(posicao) != 2:
        return False
    if "linha" not in posicao or "coluna" not in posicao:
        return False
    if type(posicao["linha"]) != str or type(posicao["coluna"]) != str:
        return False
    if posicao["linha"] not in ["1","2","3"]:
        return False
    if posicao["coluna"] not in ["A","B","C"]:
        return False
    return True

def posicoes_iguais(posicao1, posicao2):
    if not eh_posicao(posicao1) or not eh_posicao(posicao2):
        return False
    if posicao1["linha"] == posicao2["linha"] and posicao1["coluna"] == posicao2["coluna"]:
        return True
    
    return False

def posicao_para_str(posicao):
    return posicao["coluna"] + "" + posicao["linha"]

def obter_posicoes_adjacentes(posicao):
    if not eh_posicao(posicao):
        raise ValueError("obter_posicoes_adjacentes: argumento invalido")

    stringPos = posicao_para_str(posicao)
    adj = adjacentes[stringPos]
    return tuple(cria_posicao(p["coluna"], p["linha"]) for p in adj)

#####################################
# TAD Posicao - FINISH
#####################################

p1 = cria_posicao('a', '2')
p2 = cria_posicao('b', '3')
posicoes_iguais(p1, p2)   # False
posicao_para_str(p1)      # 'a2'
print(tuple(posicao_para_str(p) for p in obter_posicoes_adjacentes(p2)))  
# ('b2', 'a3', 'c3')