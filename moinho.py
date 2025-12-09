linhas = ["1","2","3"]
colunas = ["a","b","c"]

def avaliar_tabuleiro(tabuleiro):
    """ 
        Retorna 1 se X ganha, -1 se O ganha, 0 caso contrario.
        :param tabuleiro: tabuleiro
        :return: inteiro
    """
    ganhador = obter_ganhador(tabuleiro)
    if pecas_iguais(ganhador, cria_peca('X')):
        return 1
    elif pecas_iguais(ganhador, cria_peca('O')):
        return -1
    return 0

def minimax(tabuleiro, jogador, profundidade, seq_movimentos):
    """
        Implementacao direta do algoritmo fornecido no enunciado.
        :param tabuleiro: tabuleiro
        :param jogador: peca do jogador atual
        :param profundidade: profundidade maxima da pesquisa
        :param seq_movimentos: sequencia de movimentos ate ao momento
        :return: tuplo (valor do tabuleiro, sequencia de movimentos)
    """
    
    # 1 — Caso terminal: vitoria ou profundidade = 0
    resultado_terminal = avaliar_tabuleiro(tabuleiro)
    if resultado_terminal != 0 or profundidade == 0:
        return (resultado_terminal, seq_movimentos)

    # 2 — Caso nao terminal: preparar melhor resultado
    outro_jogador = cria_peca('O') if pecas_iguais(jogador, cria_peca('X')) else cria_peca('X')
    
    # X maximiza, O minimiza
    if pecas_iguais(jogador, cria_peca('X')):
        melhor_resultado = -999
    else:
        melhor_resultado = 999

    melhor_seq_movimentos = None

    # 3 — Percorrer pecas do jogador
    for peca_pos in obter_posicoes_jogador(tabuleiro, jogador):

        # 4 — Percorrer posicoes adjacentes
        for adj in obter_posicoes_adjacentes(peca_pos):

            # 5 — So interessa posicao livre
            if not eh_posicao_livre(tabuleiro, adj):
                continue

            # 6 — Criar nova copia e aplicar movimento
            novo_tab = cria_copia_tabuleiro(tabuleiro)
            move_peca(novo_tab, peca_pos, adj)
            movimento = (peca_pos, adj)

            # 7 — Calcular minimax recursivo
            novo_resultado, nova_seq = minimax(
                novo_tab,
                outro_jogador,
                profundidade - 1,
                seq_movimentos + (movimento,)
            )

            # 8 — Atualizar melhor resultado
            atualizar = False
            if melhor_seq_movimentos is None:
                atualizar = True

            elif pecas_iguais(jogador, cria_peca('X')) and novo_resultado > melhor_resultado:
                atualizar = True

            elif pecas_iguais(jogador, cria_peca('O')) and novo_resultado < melhor_resultado:
                atualizar = True

            if atualizar:
                melhor_resultado = novo_resultado
                melhor_seq_movimentos = nova_seq

    # 9 — Devolver melhor resultado encontrado
    return melhor_resultado, melhor_seq_movimentos

#####################################
# TAD Posicao - START
#####################################

# VALIDADOR DE ARGUMENTOS
    
def validarArgumentos(coluna, linha):
    """
        Validacao dos argumentos para a criacao de uma posicao.
        :param coluna: string igual a 'a', 'b' ou 'c'
        :param linha: string igual a '1', '2' ou '3'
        :return: True se os argumentos forem validos
    """
    if not (isinstance(coluna, str) and isinstance(linha, str)):
        raise ValueError("cria_posicao: argumentos invalidos")
    if coluna not in ['a', 'b', 'c']:
        raise ValueError("cria_posicao: argumentos invalidos")
    if linha not in ['1', '2', '3']:
        raise ValueError("cria_posicao: argumentos invalidos")
    return True

# CONSTRUTORES
def cria_posicao (coluna, linha):
    """
        Cria e devolve uma posicao como dicionario {'linha','coluna'}.
        :param coluna: coluna ('a'|'b'|'c')
        :param linha: linha ('1'|'2'|'3')
        :return: dicionario representando a posicao
    """
    if validarArgumentos(coluna, linha):
        return {"linha": linha, "coluna": coluna}

def cria_copia_posicao(posicao):
    """
        Retorna copia independente da posicao dada.
        :param posicao: posicao a copiar
        :return: nova posicao com mesma linha e coluna
    """
    return cria_posicao(obter_pos_c(posicao), obter_pos_l(posicao))
# CONSTRUTORES - FINISH

# SELECTORS
def obter_pos_c(posicao):
    """
        Retorna a coluna de uma posicao.
        :param posicao: posicao valida
        :return: coluna ('a'|'b'|'c')
    """
    return posicao["coluna"]

def obter_pos_l(posicao):
    """
        Retorna a linha de uma posicao.
        :param posicao: posicao valida
        :return: linha ('1'|'2'|'3')
    """
    return posicao["linha"]
# SELECTORS - FINISH

# RECONHECEDORES
def eh_posicao(posicao):
    """
        Verifica se o objeto e uma posicao valida.
        :param posicao: objeto a validar
        :return: True se for uma posicao valida, False caso contrario
    """
    if type(posicao) != dict:
        return False
    if len(posicao) != 2:
        return False
    if "linha" not in posicao or "coluna" not in posicao:
        return False
    if type(obter_pos_l(posicao)) != str or type(obter_pos_c(posicao)) != str:
        return False
    if obter_pos_l(posicao) not in linhas:
        return False
    if obter_pos_c(posicao) not in colunas:
        return False
    return True
# RECONHECEDORES - FINISH

# TESTES
def posicoes_iguais(posicao1, posicao2):    
    """
        Compara duas posicoes; True se tiverem mesma linha e coluna.
        :param posicao1: primeira posicao
        :param posicao2: segunda posicao
        :return: True se iguais, False caso contrario
    """
    if not eh_posicao(posicao1) or not eh_posicao(posicao2):
        return False
    if obter_pos_l(posicao1) == obter_pos_l(posicao2) and obter_pos_c(posicao1) == obter_pos_c(posicao2):
        return True
    
    return False
    # TESTES - FINISH

# TRANSFORMADORES
def posicao_para_str(posicao):
    """
        Converte posicao para string/chave do tabuleiro (ex.: 'a1').
        :param posicao: posicao valida
        :return: string com coluna+linha
    """
    c = obter_pos_c(posicao)
    l = obter_pos_l(posicao)
    return c + l
# TRANSFORMADORES - FINISH

# FUNCOES DE ALTO NIVEL
def obter_posicoes_adjacentes(posicao):
    """
        Devolve tupla com posicoes adjacentes a posicao dada.
        :param posicao: posicao valida
        :return: tupla de posicoes adjacentes
    """
    c_idx = colunas.index(obter_pos_c(posicao))
    l_idx = linhas.index(obter_pos_l(posicao))
    res = []

    adj_dict = {
        "00": ["b1", "a2", "b2"],
        "01": ["a1", "b2", "a3"],
        "02": ["b3", "a2", "b2"],

        "10": ["a1", "b2", "c1"],
        "11": ["a1","a2","a3", "b1", "b3", "c1", "c2", "c3"],
        "11": ["a1", "b1", "c1", "a2","c2","a3", "b3", "c3"],
        "12": ["b2", "a3", "c3"],

        "20": ["b1", "c2", "b2"],
        "21": ["c1", "b2", "c3"],
        "22": ["b3", "c2", "b2"],
    }

    chave = str(c_idx) + str(l_idx)

    for pos_str in adj_dict[chave]:
        res.append(cria_posicao(pos_str[0], pos_str[1]))

    return tuple(res)

# TAD Posicao - FINISH

#####################################

# TAD PECA

def eh_peca(arg):
    """
        Verifica se o argumento e uma peca valida.
        :param arg: objeto a verificar
        :return: True se for ['X'], ['O'] ou [' ']
    """
    return isinstance(arg, list) and arg in [["X"], ["O"], [" "]]

def cria_peca(s):
    """
        Cria uma peca a partir de um caracter 'X','O' ou ' '.
        :param s: caracter representando a peca
        :return: peca no formato lista, ex. ['X']
    """
    if not isinstance(s, str) or s not in ['X', 'O', ' ']:
        raise ValueError("cria_peca: argumento invalido")
    return [s]

def cria_copia_peca(j):
    """
        Retorna uma copia independente da peca dada.
        :param j: peca a copiar
        :return: nova peca equivalente
    """
    if not eh_peca(j):
        raise ValueError("cria_copia_peca: argumento invalido")
    return cria_peca(j[0])

def pecas_iguais(j1,j2):
    """
        Compara duas pecas e retorna True se forem iguais.
        :param j1: primeira peca
        :param j2: segunda peca
        :return: True se iguais, False caso contrario
    """

    return j1 == j2

def peca_para_str(j):
    """
        Converte peca para string no formato '[X]'/'[O]'/'[ ]'.
        :param j: peca valida
        :return: string formatada representando a peca
    """

    return "[" + j[0] + "]"

def peca_para_inteiro(j):
    """
        Mapeia peca para inteiro: X->1, O->-1, ' '->0.
        :param j: peca valida
        :return: inteiro correspondente
    """

    if j[0] == 'X':
        return 1
    if j[0] == 'O':
        return -1
    return 0


# TAD PECA - FINISH

#####################################

# TAD Tabuleiro - START

def eh_tabuleiro(arg):
    """
        Verifica se o objeto e um tabuleiro valido segundo as regras.
        :param arg: objeto a validar
        :return: True se for um tabuleiro valido, False caso contrario
    """
    if not isinstance(arg, dict):
        return False
    if len(arg) != 9:
        return False

    pecasX = 0
    pecasO = 0

    for coluna in ['a', 'b', 'c']:
        for linha in ['1', '2', '3']:
            key = f"{coluna}{linha}"
            if key not in arg or not eh_peca(arg[key]):
                #print(eh_peca(arg[key]), "3", key, arg[key], "<- arg key")
                return False
            p = arg[key]
            if pecas_iguais(p, cria_peca('X')):
                pecasX += 1
            elif pecas_iguais(p, cria_peca('O')):
                pecasO += 1

    # Restricoes numericas (max. 3 pecas por jogador)
    if pecasX > 3 or pecasO > 3:
        return False
    
    # diferenca entre pecas nao pode ser maior que 1
    if abs(pecasX - pecasO) > 1:
        return False

    # Ganhadores simultaneos nao permitidos
    def linha_ganhadora(linha):
        pecas = [arg[f"{c}{linha}"] for c in ['a', 'b', 'c']]
        if all(pecas_iguais(p, cria_peca('X')) for p in pecas):
            return '[X]'
        if all(pecas_iguais(p, cria_peca('O')) for p in pecas):
            return '[O]'
        return None

    def coluna_ganhadora(coluna):
        pecas = [arg[f"{coluna}{l}"] for l in linhas]
        if all(pecas_iguais(p, cria_peca('X')) for p in pecas):
            return '[X]'
        if all(pecas_iguais(p, cria_peca('O')) for p in pecas):
            return '[O]'
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
            
    return True

def cria_tabuleiro():
    """
        Cria um tabuleiro 3x3 inicial com todas as posicoes vazias.
        :return: tabuleiro (dicionario)
    """
    tabuleiro = {}
    for coluna in ['a', 'b', 'c']:
        for linha in ['1', '2', '3']:
            tabuleiro[f"{coluna}{linha}"] = cria_peca(' ')

    return tabuleiro

def cria_copia_tabuleiro(tabuleiro):
    """
        Retorna uma copia profunda do tabuleiro (novas pecas criadas).
        :param tabuleiro: tabuleiro valido a copiar
        :return: novo dicionario representando o tabuleiro copiado
    """

    novo_tabuleiro = {}
    for key, value in tabuleiro.items():
        novo_tabuleiro[key] = cria_copia_peca(value)

    return novo_tabuleiro

def obter_peca(tabuleiro, posicao):
    """
        Obtem a peca na posicao dada do tabuleiro.
        :param tabuleiro: tabuleiro valido
        :param posicao: posicao valida
        :return: peca na posicao
    """

    key = posicao_para_str(posicao)
    return tabuleiro[key]

def obter_vetor(tabuleiro, s):
    """
        Retorna tupla com as 3 pecas de uma coluna ('a'..'c') ou linha ('1'..'3').
        :param tabuleiro: tabuleiro valido
        :param s: coluna ('a'..'c') ou linha ('1'..'3')
        :return: tupla de 3 pecas
    """

    if s in ['a', 'b', 'c']:
        return tuple(tabuleiro[f"{s}{l}"] for l in ['1', '2', '3'])
    elif s in ['1', '2', '3']:
        return tuple(tabuleiro[f"{c}{s}"] for c in ['a', 'b', 'c'])
    else:
        raise ValueError("obter_vetor: argumentos invalidos")

def coloca_peca(tabuleiro, peca, posicao):
    """
        Coloca uma peca numa posicao do tabuleiro (modifica o tabuleiro).
        :param tabuleiro: tabuleiro valido
        :param peca: peca a colocar
        :param posicao: posicao onde colocar a peca
        :return: tabuleiro alterado
    """

    key = posicao_para_str(posicao)
    tabuleiro[key] = cria_copia_peca(peca)

    return tabuleiro

def remove_peca(tabuleiro, posicao):
    """
        Remove a peca numa posicao (substitui por espaco) e retorna o tabuleiro.
        :param tabuleiro: tabuleiro valido
        :param posicao: posicao a limpar
        :return: tabuleiro alterado
    """

    key = posicao_para_str(posicao)
    tabuleiro[key] = cria_peca(' ')

    return tabuleiro

def move_peca(tabuleiro,p1,p2):
    """
        Move peca de p1 para p2 (modifica e retorna o tabuleiro).
        :param tabuleiro: tabuleiro valido
        :param p1: posicao de origem
        :param p2: posicao de destino
        :return: tabuleiro alterado
    """

    key1 = posicao_para_str(p1)
    key2 = posicao_para_str(p2)
    
    tabuleiro[key2] = cria_copia_peca(tabuleiro[key1])
    tabuleiro[key1] = cria_peca(' ')

    return tabuleiro

def eh_posicao_livre(tabuleiro, posicao):
    """
        Verifica se uma posicao esta livre (contem [' ']).
        :param tabuleiro: tabuleiro valido
        :param posicao: posicao valida
        :return: True se estiver livre, False caso contrario
    """

    return obter_peca(tabuleiro, posicao) == [' ']

def tabuleiros_iguais(tab1,tab2):
    """
        Compara dois tabuleiros; True se todas as posicoes coincidirem.
        :param tab1: primeiro tabuleiro
        :param tab2: segundo tabuleiro
        :return: True se identicos, False caso contrario
    """
    if not eh_tabuleiro(tab1) or not eh_tabuleiro(tab2):
        return False
    
    for coluna in ['a', 'b', 'c']:
        for linha in ['1', '2', '3']:
            key = f"{coluna}{linha}"
            if not pecas_iguais(tab1[key], tab2[key]):
                return False
    
    return True

def tabuleiro_para_str(tabuleiro):
    """
        Gera string representando o tabuleiro para impressao.
        :param tabuleiro: tabuleiro valido
        :return: string formatada do tabuleiro
    """
    if not eh_tabuleiro(tabuleiro):
        raise ValueError("tabuleiro_para_str: argumento invalido")

    linhas = []
    linhas.append("   a   b   c")
    for l in ['1', '2', '3']:
        pecas = []
        for c in ['a', 'b', 'c']:
            pecas.append(peca_para_str(tabuleiro[c + l]))
        linhas.append(l + " " + "-".join(pecas))
        if l == '1':
            linhas.append("   | \\ | / |")
        elif l == '2':
            linhas.append("   | / | \\ |")
    return "\n".join(linhas)


# ALTERAcaO (feito para os testes publicos):
# Corrigi o mapeamento do tuplo 3x3 para o tabuleiro:
# o primeiro indice do tuplo passa a ser a linha (1–3) e o segundo a coluna (a–c),
# de forma a coincidir com a forma usada nos testes (tipo o teste 12).
def tuplo_para_tabuleiro(tuplo):
    """
        Converte um tuplo 3x3 de inteiros (-1,0,1) para o tabuleiro interno.
        :param tuplo: tuplo 3x3 de inteiros (-1,0,1)
        :return: tabuleiro (dicionario)
    """
    if (not isinstance(tuplo, tuple) or len(tuplo) != 3 or
        any(not isinstance(l, tuple) or len(l) != 3 for l in tuplo)):
        raise ValueError("tuplo_para_tabuleiro: argumento invalido")

    tabuleiro = {}
    colunas = ['a', 'b', 'c']
    linhas = ['1', '2', '3']

    # li = indice da linha, co = indice da coluna
    for li, linha in enumerate(linhas):          # 0→'1', 1→'2', 2→'3'
        for co, coluna in enumerate(colunas):    # 0→'a', 1→'b', 2→'c'
            inteiro = tuplo[li][co]              # primeiro indice = linha, segundo = coluna
            peca = obter_peca_por_inteiro(inteiro)
            tabuleiro[coluna + linha] = cria_copia_peca(peca)

    return tabuleiro

def obter_ganhador(tabuleiro):
    """
        Determina o ganhador do tabuleiro.
        :param tabuleiro: tabuleiro valido
        :return: peca vencedora ['X']/['O'] ou [' '] se nao houver vencedor
    """
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
    """
        Converte inteiro para peca: 1->['X'], -1->['O'], 0->[' '].
        :param inteiro: inteiro representando a peca
        :return: peca correspondente
    """
    if inteiro == 1:
        return ["X"]
    elif inteiro == -1:
        return ["O"]
    else:
        return [" "]

def validar_ganhador_coluna(tabuleiro, coluna):
    """
        Verifica se uma coluna tem vencedor; retorna 1, -1 ou 0.
        :param tabuleiro: tabuleiro valido
        :param coluna: coluna a verificar ('a'|'b'|'c')
        :return: 1 se X ganhar, -1 se O ganhar, 0 caso contrario
    """
    if not eh_tabuleiro(tabuleiro) or coluna not in ['a', 'b', 'c']:
        raise ValueError("validar_ganhador_coluna: argumentos invalidos")
    vetor = obter_vetor(tabuleiro, coluna)
    if all(pecas_iguais(p, cria_peca('X')) for p in vetor):
        return 1
    if all(pecas_iguais(p, cria_peca('O')) for p in vetor):
        return -1
    return 0

def validar_ganhador_linha(tabuleiro, linha):
    """
        Verifica se uma linha tem vencedor; retorna 1, -1 ou 0.
        :param tabuleiro: tabuleiro valido
        :param linha: linha a verificar ('1'|'2'|'3')
        :return: 1 se X ganhar, -1 se O ganhar, 0 caso contrario
    """
    if not eh_tabuleiro(tabuleiro) or linha not in ['1', '2', '3']:
        raise ValueError("validar_ganhador_linha: argumentos invalidos")
    vetor = obter_vetor(tabuleiro, linha)
    if all(pecas_iguais(p, cria_peca('X')) for p in vetor):
        return 1
    if all(pecas_iguais(p, cria_peca('O')) for p in vetor):
        return -1
    return 0

def obter_posicoes_livres(tabuleiro):
    """
        Retorna tupla com todas as posicoes livres no tabuleiro.
        :param tabuleiro: tabuleiro valido
        :return: tupla de posicoes livres
    """
    if not eh_tabuleiro(tabuleiro):
        raise ValueError("obter_posicoes_livres: argumento invalido")
    
    posicoes_livres = []
    for coluna in ['a', 'b', 'c']:
        for linha in ['1', '2', '3']:
            key = f"{coluna}{linha}"
            if tabuleiro[key] == [' ']:
                posicoes_livres.append(cria_posicao(coluna, linha))
    
    return tuple(posicoes_livres)

def obter_posicoes_jogador(tabuleiro, peca):
    """
        Retorna tupla com posicoes ocupadas pela peca indicada.
        :param tabuleiro: tabuleiro valido
        :param peca: peca a procurar
        :return: tupla de posicoes onde a peca esta presente
    """
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


# TAD Tabuleiro - FINISH
#####################################

def obter_movimento_manual(t, peca):
    """
        Le e valida o movimento escolhido pelo jogador (colocacao ou movimento).
        :param t: tabuleiro atual
        :param peca: peca do jogador
        :return: tuplo com o movimento: (pos,) para colocacao ou (origem,destino) para movimento
    """
    if not eh_tabuleiro(t) or not eh_peca(peca):
        raise ValueError("obter_movimento_manual: argumentos invalidos")
    posicoes_jogador = obter_posicoes_jogador(t, peca)
    eh_fase_colocacao = len(posicoes_jogador) < 3

    if eh_fase_colocacao:
        entrada = input("Turno do jogador. Escolha uma posicao: ").strip().lower()
        if len(entrada) != 2:
            raise ValueError("obter_movimento_manual: escolha invalida")
        try:
            posicao = cria_posicao(entrada[0], entrada[1])
        except ValueError:
            raise ValueError("obter_movimento_manual: escolha invalida")
        if not eh_posicao_livre(t, posicao):
            raise ValueError("obter_movimento_manual: escolha invalida")
        return (posicao,)
    else:
        entrada = input("Turno do jogador. Escolha um movimento: ").strip().lower()
        if len(entrada) != 4:
            raise ValueError("obter_movimento_manual: escolha invalida")
        try:
            posicao_origem = cria_posicao(entrada[0], entrada[1])
            posicao_destino = cria_posicao(entrada[2], entrada[3])
        except ValueError:
            raise ValueError("obter_movimento_manual: escolha invalida")

        if not pecas_iguais(obter_peca(t, posicao_origem), peca):
            raise ValueError("obter_movimento_manual: escolha invalida")

        if posicoes_iguais(posicao_origem, posicao_destino):
            # passar turno: origem == destino e sempre valido
            return (posicao_origem, posicao_destino)

        if not eh_posicao_livre(t, posicao_destino):
            raise ValueError("obter_movimento_manual: escolha invalida")

        if posicao_destino not in obter_posicoes_adjacentes(posicao_origem):
            raise ValueError("obter_movimento_manual: escolha invalida")

        return (posicao_origem, posicao_destino)



def obter_movimento_auto(tabuleiro, peca, dificuldade):
    """
    tabuleiro × peca × str → tuplo de posicoes
    Devolve um movimento automatico de acordo com o nivel de dificuldade.
    """

    if not eh_tabuleiro(tabuleiro) or not eh_peca(peca) or dificuldade not in ('facil', 'normal', 'dificil'):
        raise ValueError("obter_movimento_auto: argumentos invalidos")

    posicoes_jogador = obter_posicoes_jogador(tabuleiro, peca)
    fase_colocacao = len(posicoes_jogador) < 3

    # ============================================================
    # FASE DE COLOCAcaO
    # ============================================================
    if fase_colocacao:
        # 1) Vitoria
        for s in ['a', 'b', 'c', '1', '2', '3']:
            vetor = obter_vetor(tabuleiro, s)
            if sum(1 for p in vetor if pecas_iguais(p, peca)) == 2 and \
            sum(1 for p in vetor if pecas_iguais(p, cria_peca(' '))) == 1:
                for idx, p in enumerate(vetor):
                    if pecas_iguais(p, cria_peca(' ')):
                        if s in ['a', 'b', 'c']:
                            pos = cria_posicao(s, str(idx + 1))
                        else:
                            colunas = ['a', 'b', 'c']
                            pos = cria_posicao(colunas[idx], s)
                        return (pos,)

        # 2) Bloqueio
        adversario = cria_peca('O') if pecas_iguais(peca, cria_peca('X')) else cria_peca('X')
        for s in ['a', 'b', 'c', '1', '2', '3']:
            vetor = obter_vetor(tabuleiro, s)
            if sum(1 for p in vetor if pecas_iguais(p, adversario)) == 2 and \
            sum(1 for p in vetor if pecas_iguais(p, cria_peca(' '))) == 1:
                for idx, p in enumerate(vetor):
                    if pecas_iguais(p, cria_peca(' ')):
                        if s in ['a', 'b', 'c']:
                            pos = cria_posicao(s, str(idx + 1))
                        else:
                            colunas = ['a', 'b', 'c']
                            pos = cria_posicao(colunas[idx], s)
                        return (pos,)

        # 3) Centro
        centro = cria_posicao('b', '2')
        if eh_posicao_livre(tabuleiro, centro):
            return (centro,)

        # 4) Cantos
        for c, l in (('a', '1'), ('c', '1'), ('a', '3'), ('c', '3')):
            pos = cria_posicao(c, l)
            if eh_posicao_livre(tabuleiro, pos):
                return (pos,)

        # 5) Laterais
        for c, l in (('b', '1'), ('a', '2'), ('c', '2'), ('b', '3')):
            pos = cria_posicao(c, l)
            if eh_posicao_livre(tabuleiro, pos):
                return (pos,)

        # fallback (nao deve acontecer)
        livres = obter_posicoes_livres(tabuleiro)
        return (livres[0],)

    # ============================================================
    # FASE DE MOVIMENTO
    # ============================================================

    # FACIL
    if dificuldade == 'facil':
        for pos in posicoes_jogador:
            adjacentes = obter_posicoes_adjacentes(pos)
            for adj in adjacentes:
                if eh_posicao_livre(tabuleiro, adj):
                    return (pos, adj)
        return (posicoes_jogador[0], posicoes_jogador[0])

    # NORMAL / DIFICIL (minimax)
    profundidade = 1 if dificuldade == 'normal' else 5
    melhor_valor = -999 if pecas_iguais(peca, cria_peca('X')) else 999
    melhor_movimento = None
    adversario = cria_peca('O') if pecas_iguais(peca, cria_peca('X')) else cria_peca('X')

    for origem in posicoes_jogador:
        for destino in obter_posicoes_adjacentes(origem):
            if not eh_posicao_livre(tabuleiro, destino):
                continue
            novo_tab = cria_copia_tabuleiro(tabuleiro)
            move_peca(novo_tab, origem, destino)
            valor, _ = minimax(novo_tab, adversario, profundidade - 1, ())
            if pecas_iguais(peca, cria_peca('X')):
                if valor > melhor_valor:
                    melhor_valor = valor
                    melhor_movimento = (origem, destino)
            else:
                if valor < melhor_valor:
                    melhor_valor = valor
                    melhor_movimento = (origem, destino)

    if melhor_movimento is not None:
        return melhor_movimento

    # fallback para facil
    for pos in posicoes_jogador:
        for adj in obter_posicoes_adjacentes(pos):
            if eh_posicao_livre(tabuleiro, adj):
                return (pos, adj)

    # se tudo bloqueado, peca parada
    return (posicoes_jogador[0], posicoes_jogador[0])



# FUNcaO PRINCIPAL DO JOGO
def moinho(peca, nivel):
    """
        Funcao principal que realiza o jogo completo entre humano e CPU.
        :param peca: string '[X]' ou '[O]' indicando peca do jogador
        :param nivel: dificuldade ('facil','normal','dificil')
        :return: string representando a peca vencedora ('[X]'/'[O]')
    """
    if peca not in ('[X]', '[O]') or nivel not in ('facil', 'normal', 'dificil'):
        raise ValueError('moinho: argumentos invalidos')

    print(f"Bem-vindo ao JOGO DO MOINHO. Nivel de dificuldade {nivel}.")

    tabuleiro = cria_tabuleiro()
    jogador = cria_peca(peca[1])
    cpu = cria_peca('X' if peca == '[O]' else 'O')
    turno = cria_copia_peca(jogador)

    pecas_humano = 0
    pecas_cpu = 0

    # Fase de colocacao  (ALTEREI ESTE METODO TODO)
    while pecas_humano < 3 or pecas_cpu < 3:
        print(tabuleiro_para_str(tabuleiro))
        if pecas_humano < 3 and pecas_cpu < 3:
            # primeiro o humano, depois o computador, como no exemplo
            if pecas_humano == pecas_cpu:
                # turno do jogador (usa a auxiliar)
                try:
                    mov = obter_movimento_manual(tabuleiro, jogador)
                    pos = mov[0]
                    tabuleiro = coloca_peca(tabuleiro, jogador, pos)
                    pecas_humano += 1
                except ValueError:
                    continue
            else:
                print(f"Turno do computador ({nivel}):")
                mov = obter_movimento_auto(tabuleiro, cpu, nivel)
                pos = mov[0]
                tabuleiro = coloca_peca(tabuleiro, cpu, pos)
                pecas_cpu += 1
        elif pecas_humano < 3:
            # so humano ainda coloca
            try:
                mov = obter_movimento_manual(tabuleiro, jogador)
                pos = mov[0]
                tabuleiro = coloca_peca(tabuleiro, jogador, pos)
                pecas_humano += 1
            except ValueError:
                continue
        elif pecas_cpu < 3:
            print(f"Turno do computador ({nivel}):")
            mov = obter_movimento_auto(tabuleiro, cpu, nivel)
            pos = mov[0]
            tabuleiro = coloca_peca(tabuleiro, cpu, pos)
            pecas_cpu += 1

    # Fase de movimento  (alterei a parte da peca chamada, nao vai corromper nada dw)
    turno = cria_copia_peca(jogador)
    while pecas_iguais(obter_ganhador(tabuleiro), cria_peca(' ')):
        print(tabuleiro_para_str(tabuleiro))
        if pecas_iguais(turno, jogador):
            try:
                mov = obter_movimento_manual(tabuleiro, jogador)
                orig, dest = mov
                if not posicoes_iguais(orig, dest):
                    tabuleiro = move_peca(tabuleiro, orig, dest)
                turno = cpu
            except ValueError:
                continue
        else:
            print(f"Turno do computador ({nivel}):")
            orig, dest = obter_movimento_auto(tabuleiro, cpu, nivel)
            if not posicoes_iguais(orig, dest):
                tabuleiro = move_peca(tabuleiro, orig, dest)
            turno = jogador

    print(tabuleiro_para_str(tabuleiro))
    vencedor = obter_ganhador(tabuleiro)
    return peca_para_str(vencedor)



#moinho('[X]', 'facil')

################################################
# Escolha da dificuldade                       #
################################################ 
def obter_dificuldade():
    """
        Le e devolve uma dificuldade valida escolhida pelo utilizador.
        :return: nivel ('facil','normal','dificil')
    """
    while True: # Le a dificuldade escrita pelo utilizador e normaliza para minusculas sem espacos
        nivel = input("Escolha a dificuldade do jogo (facil, normal, dificil): ").strip().lower()
        # So aceita se for uma das opcoes permitidas
        if nivel in ('facil', 'normal', 'dificil'):
            return nivel
        # Caso contrario, mostra mensagem de erro e volta a pedir
        print("Dificuldade invalida. Por favor, escolha entre: facil, normal, dificil.")

def jogar_moinho():
    """
        Funcao auxiliar que pede opcoes ao utilizador e inicia o jogo.
    """
    # Pede ao utilizador o nivel de dificuldade para o CPU
    dificuldade = obter_dificuldade()

    # Pede ao utilizador para escolher o simbolo com que quer jogar
    simbolo = input("Escolha seu simbolo [X/O]: ").strip().upper()

    # Garante que o simbolo e valido; se nao for, volta a pedir
    while simbolo not in ('X', 'O'):
        print("Simbolo invalido. Escolha X ou O.")
        simbolo = input("Escolha seu simbolo [X/O]: ").strip().upper()

    # Constroi a peca no formato esperado pela funcao moinho, por exemplo "[X]" ou "[O]"
    peca = f'[{simbolo}]'

    # Inicia o jogo do moinho com a peca escolhida e a dificuldade selecionada
    moinho(peca, dificuldade)

#jogar_moinho()
