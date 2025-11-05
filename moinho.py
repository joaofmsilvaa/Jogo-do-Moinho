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

    # VALIDADOR DE ARGUMENTOS
    
def validarArgumentos(coluna, linha):
    if not (isinstance(coluna, str) and isinstance(linha, str)):
        raise ValueError("cria_posicao: argumentos invalidos")
    if coluna not in ['a', 'b', 'c']:
        raise ValueError("cria_posicao: argumentos invalidos")
    if linha not in ['1', '2', '3']:
        raise ValueError("cria_posicao: argumentos invalidos")
    return True
# VALIDADOR DE ARGUMENTOS - FINISH

# CONSTRUTORES
def cria_posicao (coluna, linha):
    if validarArgumentos(coluna, linha):
        return {"linha": linha, "coluna": coluna}

def cria_copia_posicao(posicao):
    return cria_posicao(posicao["coluna"], posicao["linha"])
# CONSTRUTORES - FINISH

# SELECTORS
def obter_pos_c(posicao):
    return posicao["coluna"]

def obter_pos_l(posicao):
    return posicao["linha"]
# SELECTORS - FINISH

# RECONHECEDORES
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
    if posicao["coluna"] not in ["a","b","c"]:
        return False
    return True
# RECONHECEDORES - FINISH

# TESTES
def posicoes_iguais(posicao1, posicao2):    
    if not eh_posicao(posicao1) or not eh_posicao(posicao2):
        return False
    if posicao1["linha"] == posicao2["linha"] and posicao1["coluna"] == posicao2["coluna"]:
        return True
    
    return False
    # TESTES - FINISH

# TRANSFORMADORES
def posicao_para_str(posicao):
    return posicao["coluna"] + "" + posicao["linha"]
# TRANSFORMADORES - FINISH

def getColNumber(col):
    if col == 'a':
        return 1
    elif col == 'b':
        return 2
    else:
        return 3

# FUNCOES DE ALTO NIVEL
def obter_posicoes_adjacentes(posicao):
    if not eh_posicao(posicao):
        raise ValueError("obter_posicoes_adjacentes: argumento invalido")

    columnList = ['a', 'b', 'c']
    colNumber = getColNumber(posicao["coluna"])
    lineNumber = int(posicao["linha"])
    adjacentList = []
    for i in [colNumber - 1, colNumber, colNumber + 1]:
        for j in [lineNumber -1, lineNumber, lineNumber + 1]:
            if i >= 1 and i <= 3 and j >= 1 and j <= 3:
                if((j != lineNumber and i == colNumber) or (j == lineNumber and i != colNumber)):
                   adjacentList.append(cria_posicao(columnList[i - 1], str(j)))   


    return tuple(adjacentList)
# FUNCOES DE ALTO NIVEL - FINISH

p1 = cria_posicao('a', '2')
p2 = cria_posicao('b', '3')
posicoes_iguais(p1, p2)   # False
posicao_para_str(p1)      # 'a2'
print(tuple(posicao_para_str(p) for p in obter_posicoes_adjacentes(p2)))  
# ('b2', 'a3', 'c3')

# TAD Posicao - FINISH

#####################################

# TAD PECA

def eh_peca(arg):
    return isinstance(arg, str) and arg in ['X', 'O', ' ']

def cria_peca(s):
    if not eh_peca(s):
        raise ValueError("cria_peca: argumento invalido")
    return s

def cria_copia_peca(j):
    if not eh_peca(j):
        raise ValueError("cria_copia_peca: argumento invalido")
    return cria_peca(j)

def pecas_iguais(j1,j2):
    if not eh_peca(j1) or not eh_peca(j2):
        return False
    return j1 == j2

def peca_para_str(j):
    if not eh_peca(j):
        raise ValueError("peca_para_str: argumento invalido")
    return f'[{j}]'

def peca_para_inteiro(j):
    if j == 'X':
        return 1
    elif j == 'O':
        return -1
    else:
        return 0
    
#j1 = cria_peca('x')
j1 = cria_peca('X')
j2 = cria_peca('O')
print(pecas_iguais(j1, j2))
print(peca_para_str(j1))
print(peca_para_inteiro(cria_peca(' ')))

# TAD PECA - FINISH

#####################################

# TAD Tabuleiro - START

def eh_tabuleiro(arg):
    # 1️⃣ Tipo e estrutura base
    if not isinstance(arg, dict):
        return False
    if len(arg) != 9:
        return False

    pecasX = 0
    pecasO = 0

    # 2️⃣ Verificação das peças válidas e contagem
    for coluna in ['a', 'b', 'c']:
        for linha in ['1', '2', '3']:
            key = f"{coluna}{linha}"
            if key not in arg or not eh_peca(arg[key]):
                return False
            p = arg[key]
            if pecas_iguais(p, cria_peca('X')):
                pecasX += 1
            elif pecas_iguais(p, cria_peca('O')):
                pecasO += 1

    # 3️⃣ Restrições numéricas (máx. 3 peças por jogador)
    if pecasX > 3 or pecasO > 3:
        return False
    # diferença entre peças não pode ser maior que 1
    if abs(pecasX - pecasO) > 1:
        return False

    # 4️⃣ Ganhadores simultâneos não permitidos
    def linha_ganhadora(linha):
        pecas = [arg[f"{c}{linha}"] for c in ['a', 'b', 'c']]
        if all(pecas_iguais(p, cria_peca('X')) for p in pecas):
            return 'X'
        if all(pecas_iguais(p, cria_peca('O')) for p in pecas):
            return 'O'
        return None

    def coluna_ganhadora(coluna):
        pecas = [arg[f"{coluna}{l}"] for l in ['1', '2', '3']]
        if all(pecas_iguais(p, cria_peca('X')) for p in pecas):
            return 'X'
        if all(pecas_iguais(p, cria_peca('O')) for p in pecas):
            return 'O'
        return None

    ganhadores = set()

    # verificar linhas
    for l in ['1', '2', '3']:
        g = linha_ganhadora(l)
        if g:
            ganhadores.add(g)

    # verificar colunas
    for c in ['a', 'b', 'c']:
        g = coluna_ganhadora(c)
        if g:
            ganhadores.add(g)

    # apenas um ganhador é permitido
    if len(ganhadores) > 1:
        return False

    return True

def cria_tabuleiro():
    tabuleiro = {}
    for coluna in ['a', 'b', 'c']:
        for linha in ['1', '2', '3']:
            tabuleiro[f"{coluna}{linha}"] = cria_peca(' ')

    return tabuleiro

def cria_copia_tabuleiro(tabuleiro):
    if not eh_tabuleiro(tabuleiro):
        raise ValueError("cria_copia_tabuleiro: argumento invalido")
    
    novo_tabuleiro = {}
    for key, value in tabuleiro.items():
        novo_tabuleiro[key] = cria_copia_peca(value)

    return novo_tabuleiro

def obter_peca(tabuleiro, posicao):
    if not eh_tabuleiro(tabuleiro) or not eh_posicao(posicao):
        raise ValueError("obter_peca: argumentos invalidos")
    
    key = posicao_para_str(posicao)
    return tabuleiro[key]

def obter_vetor(tabuleiro, s):
    if not isinstance(tabuleiro, dict) or not isinstance(s, str):
        raise ValueError("obter_vetor: argumentos invalidos")
    
    if s in ['a', 'b', 'c']:
        return tuple(tabuleiro[f"{s}{l}"] for l in ['1', '2', '3'])
    elif s in ['1', '2', '3']:
        return tuple(tabuleiro[f"{c}{s}"] for c in ['a', 'b', 'c'])
    else:
        raise ValueError("obter_vetor: argumentos invalidos")

def coloca_peca(tabuleiro, peca, posicao):
    if not eh_tabuleiro(tabuleiro) or not eh_peca(peca) or not eh_posicao(posicao):
        raise ValueError("coloca_peca: argumentos invalidos")
    
    key = posicao_para_str(posicao)
    tabuleiro[key] = cria_copia_peca(peca)

    return tabuleiro

def remove_peca(tabuleiro, posicao):
    if not eh_tabuleiro(tabuleiro) or not eh_posicao(posicao):
        raise ValueError("remove_peca: argumentos invalidos")
    
    key = posicao_para_str(posicao)
    tabuleiro[key] = cria_peca(' ')

    return tabuleiro

def move_peca(tabuleiro,p1,p2):
    if not eh_tabuleiro(tabuleiro) or not eh_posicao(p1) or not eh_posicao(p2):
        raise ValueError("move_peca: argumentos invalidos")
    
    key1 = posicao_para_str(p1)
    key2 = posicao_para_str(p2)
    
    tabuleiro[key2] = cria_copia_peca(tabuleiro[key1])
    tabuleiro[key1] = cria_peca(' ')

    return tabuleiro

def eh_posicao_livre(tabuleiro, posicao):
    if not eh_tabuleiro(tabuleiro) or not eh_posicao(posicao):
        raise ValueError("eh_posicao_livre: argumentos invalidos")
    
    return obter_peca(tabuleiro, posicao) == ' '

def tabuleiros_iguais(tab1,tab2):
    if not eh_tabuleiro(tab1) or not eh_tabuleiro(tab2):
        return False
    
    for coluna in ['a', 'b', 'c']:
        for linha in ['1', '2', '3']:
            key = f"{coluna}{linha}"
            if not pecas_iguais(tab1[key], tab2[key]):
                return False
    
    return True

def tabuleiro_para_str(tabuleiro):
    if not eh_tabuleiro(tabuleiro):
        raise ValueError("tabuleiro_para_str: argumento invalido")
    
    linhas = []
    for linha in ['1', '2', '3']:
        linha_str = []
        for coluna in ['a', 'b', 'c']:
            key = f"{coluna}{linha}"
            linha_str.append(peca_para_str(tabuleiro[key]))
        linhas.append(" - ".join(linha_str))
        
        if linha == '1':
            linhas.append(" |  \\  |  /  |")
        elif linha == '2':
            linhas.append(" |  /  |  \\  |")
    
    return "\n".join(linhas)

def tuplo_para_tabuleiro(tuplo):
    if not isinstance(tuplo, tuple) or len(tuplo) != 3 or any(len(l) != 3 for l in tuplo):
        raise ValueError("tuplo_para_tabuleiro: argumento invalido")
    
    tabuleiro = {}
    index = 0
    subIndex = 0
    for coluna in ['a', 'b', 'c']:
        for linha in ['1', '2', '3']:
            key = f"{coluna}{linha}"
            peca = obter_peca_por_inteiro(tuplo[index][subIndex])
            if not eh_peca(peca):
                raise ValueError("tuplo_para_tabuleiro: argumento invalido")
            tabuleiro[key] = cria_copia_peca(peca)
            subIndex+= 1
        subIndex = 0
        index += 1
    
    return tabuleiro

def obter_ganhador(tabuleiro):
    if not eh_tabuleiro(tabuleiro):
        raise ValueError("obter_ganhador: argumento invalido")
    
    linhas = ['1', '2', '3']
    colunas = ['a', 'b', 'c']
    ganhadorInteiro = 0

    for linha in linhas:
        ganhadorValidado = validar_ganhador_linha(tabuleiro, linha)
        if ganhadorInteiro == 0 and ganhadorValidado != 0:
            ganhadorInteiro = ganhadorValidado
            break
    
    for coluna in colunas:
        ganhadorValidado = validar_ganhador_coluna(tabuleiro, coluna)
        if ganhadorInteiro == 0 and ganhadorValidado != 0:
            ganhadorInteiro = ganhadorValidado
            break
    
    return obter_peca_por_inteiro(ganhadorInteiro)

def obter_peca_por_inteiro(inteiro):
    if inteiro == 1:
        return 'X'
    elif inteiro == -1:
        return 'O'
    else:
        return ' '

def validar_ganhador_coluna(tabuleiro, coluna):
    if not eh_tabuleiro(tabuleiro) or coluna not in ['a', 'b', 'c']:
        raise ValueError("validar_ganhador_coluna: argumentos invalidos")
    
    vetor = obter_vetor(tabuleiro, coluna)
    if vetor.count('X') == 3:
        return 1
    elif vetor.count('O') == 3:
        return -1
    else:
        return 0

def validar_ganhador_linha(tabuleiro, linha):
    if not eh_tabuleiro(tabuleiro) or linha not in ['1', '2', '3']:
        raise ValueError("validar_ganhador_linha: argumentos invalidos")
    
    vetor = obter_vetor(tabuleiro, linha)
    if vetor.count('X') == 3:
        return 1
    elif vetor.count('O') == 3:
        return -1
    else:
        return 0

def obter_posicoes_livres(tabuleiro):
    if not eh_tabuleiro(tabuleiro):
        raise ValueError("obter_posicoes_livres: argumento invalido")
    
    posicoes_livres = []
    for coluna in ['a', 'b', 'c']:
        for linha in ['1', '2', '3']:
            key = f"{coluna}{linha}"
            if tabuleiro[key] == ' ':
                posicoes_livres.append(cria_posicao(coluna, linha))
    
    return tuple(posicoes_livres)

def obter_posicoes_jogador(tabuleiro, peca):
    if not eh_tabuleiro(tabuleiro) or not eh_peca(peca):
        raise ValueError("obter_posicoes_jogador: argumentos invalidos")
    
    posicoes_jogador = []
    for coluna in ['a', 'b', 'c']:
        for linha in ['1', '2', '3']:
            key = f"{coluna}{linha}"
            if pecas_iguais(tabuleiro[key], peca):
                posicoes_jogador.append(cria_posicao(coluna, linha))
    
    return tuple(posicoes_jogador)

# print(""" 
#    A     B     C
# 1  [ ] - [ ] - [ ]\n
#    |  \\  |  /  | \n
# 2  [ ] - [ ] - [ ]\n
#    |  /  |  \\  | \n
# 3  [ ] - [ ] - [ ]\n
# """)

t = cria_tabuleiro()
print(t)
print("\n")
tabuleiro_para_str(coloca_peca(t, cria_peca('X'), cria_posicao('a','1')))
print("\n")
print(tabuleiro_para_str(t))
print("\n")
print(tabuleiro_para_str(coloca_peca(t, cria_peca('O'),cria_posicao('b','2'))))
print("\n")
print(tabuleiro_para_str(move_peca(t, cria_posicao('a','1'), cria_posicao('b','1'))))
print("\n")
t = tuplo_para_tabuleiro(((0,1,-1),(-0,1,-1),(1,0,-1)))
print("\n")
print(tabuleiro_para_str(t))
print("\n")
peca_para_str(obter_ganhador(t))
print("\n")
tuple(posicao_para_str(p) for p in obter_posicoes_livres(t))
print("\n")
tuple(peca_para_str(peca) for peca in obter_vetor(t, 'a'))
print("\n")
tuple(peca_para_str(peca) for peca in obter_vetor(t, '2'))
print("\n")

# TAD Tabuleiro - FINISH
#####################################