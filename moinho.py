# print(""" 
#    A     B     C
# 1  [ ] - [ ] - [ ]\n
#    |  \\  |  /  | \n
# 2  [ ] - [ ] - [ ]\n
#    |  /  |  \\  | \n
# 3  [ ] - [ ] - [ ]\n
# """)

def avaliar_tabuleiro(tabuleiro):
    """Retorna 1 se X ganha, -1 se O ganha, 0 caso contrário."""
    ganhador = obter_ganhador(tabuleiro)
    if pecas_iguais(ganhador, cria_peca('X')):
        return 1
    elif pecas_iguais(ganhador, cria_peca('O')):
        return -1
    return 0


def minimax(tabuleiro, jogador, profundidade, seq_movimentos):
    """Implementação direta do algoritmo fornecido no enunciado."""
    
    # 1 — Caso terminal: vitória ou profundidade = 0
    resultado_terminal = avaliar_tabuleiro(tabuleiro)
    if resultado_terminal != 0 or profundidade == 0:
        return (resultado_terminal, seq_movimentos)

    # 2 — Caso não terminal: preparar melhor resultado
    outro_jogador = cria_peca('O') if pecas_iguais(jogador, cria_peca('X')) else cria_peca('X')
    
    # X maximiza, O minimiza
    if pecas_iguais(jogador, cria_peca('X')):
        melhor_resultado = -999
    else:
        melhor_resultado = 999

    melhor_seq_movimentos = None

    # 3 — Percorrer peças do jogador
    for peca_pos in obter_posicoes_jogador(tabuleiro, jogador):

        # 4 — Percorrer posições adjacentes
        for adj in obter_posicoes_adjacentes(peca_pos):

            # 5 — Só interessa posição livre
            if not eh_posicao_livre(tabuleiro, adj):
                continue

            # 6 — Criar nova cópia e aplicar movimento
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
    return posicao["coluna"] + posicao["linha"]
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

    colunas = ['a', 'b', 'c']
    linhas = ['1', '2', '3']
    c_idx = colunas.index(posicao["coluna"])
    l_idx = linhas.index(posicao["linha"])
    res = []

    for j in range(len(linhas)):      # linhas (1,2,3)
        for i in range(len(colunas)): # colunas (a,b,c)
            if i == c_idx and abs(j - l_idx) == 1:
                res.append(cria_posicao(colunas[i], linhas[j]))
            elif j == l_idx and abs(i - c_idx) == 1:
                res.append(cria_posicao(colunas[i], linhas[j]))

    return tuple(res)
# FUNCOES DE ALTO NIVEL - FINISH

# TAD Posicao - FINISH

#####################################

# TAD PECA

def eh_peca(arg):
    return isinstance(arg, list) and arg in [["X"], ["O"], [" "]]

def cria_peca(s):
    if not isinstance(s, str) or s not in ['X', 'O', ' ']:
        raise ValueError("cria_peca: argumento invalido")
    return [s]

def cria_copia_peca(j):
    if not eh_peca(j):
        raise ValueError("cria_copia_peca: argumento invalido")
    return cria_peca(j[0])

def pecas_iguais(j1,j2):
    if not eh_peca(j1) or not eh_peca(j2):
        return False
    return j1 == j2

def peca_para_str(j):
    if not eh_peca(j):
        raise ValueError("peca_para_str: argumento invalido")
    return "[" + j[0] + "]"

def peca_para_inteiro(j):
    if not eh_peca(j):
        raise ValueError("peca_para_inteiro: argumento invalido")
    if j[0] == 'X':
        return 1
    if j[0] == 'O':
        return -1
    return 0


# TAD PECA - FINISH

#####################################

# TAD Tabuleiro - START

def eh_tabuleiro(arg):
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

    # Restrições numéricas (máx. 3 peças por jogador)
    if pecasX > 3 or pecasO > 3:
        return False
    
    # diferença entre peças não pode ser maior que 1
    if abs(pecasX - pecasO) > 1:
        return False

    # Ganhadores simultâneos não permitidos
    def linha_ganhadora(linha):
        pecas = [arg[f"{c}{linha}"] for c in ['a', 'b', 'c']]
        if all(pecas_iguais(p, cria_peca('X')) for p in pecas):
            return '[X]'
        if all(pecas_iguais(p, cria_peca('O')) for p in pecas):
            return '[O]'
        return None

    def coluna_ganhadora(coluna):
        pecas = [arg[f"{coluna}{l}"] for l in ['1', '2', '3']]
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
    
    return obter_peca(tabuleiro, posicao) == [' ']

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


# ALTERAÇÃO (feito para os testes públicos):
# Corrigi o mapeamento do tuplo 3x3 para o tabuleiro:
# o primeiro índice do tuplo passa a ser a linha (1–3) e o segundo a coluna (a–c),
# de forma a coincidir com a forma usada nos testes (tipo o teste 12).
def tuplo_para_tabuleiro(tuplo):
    if (not isinstance(tuplo, tuple) or len(tuplo) != 3 or
        any(not isinstance(l, tuple) or len(l) != 3 for l in tuplo)):
        raise ValueError("tuplo_para_tabuleiro: argumento invalido")

    tabuleiro = {}
    colunas = ['a', 'b', 'c']
    linhas = ['1', '2', '3']

    # li = índice da linha, co = índice da coluna
    for li, linha in enumerate(linhas):          # 0→'1', 1→'2', 2→'3'
        for co, coluna in enumerate(colunas):    # 0→'a', 1→'b', 2→'c'
            inteiro = tuplo[li][co]              # primeiro índice = linha, segundo = coluna
            if inteiro not in (-1, 0, 1):
                raise ValueError("tuplo_para_tabuleiro: argumento invalido")
            peca = obter_peca_por_inteiro(inteiro)
            tabuleiro[coluna + linha] = cria_copia_peca(peca)

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
        return ["X"]
    elif inteiro == -1:
        return ["O"]
    else:
        return [" "]

def validar_ganhador_coluna(tabuleiro, coluna):
    if not eh_tabuleiro(tabuleiro) or coluna not in ['a', 'b', 'c']:
        raise ValueError("validar_ganhador_coluna: argumentos invalidos")
    vetor = obter_vetor(tabuleiro, coluna)
    if all(pecas_iguais(p, cria_peca('X')) for p in vetor):
        return 1
    if all(pecas_iguais(p, cria_peca('O')) for p in vetor):
        return -1
    return 0

def validar_ganhador_linha(tabuleiro, linha):
    if not eh_tabuleiro(tabuleiro) or linha not in ['1', '2', '3']:
        raise ValueError("validar_ganhador_linha: argumentos invalidos")
    vetor = obter_vetor(tabuleiro, linha)
    if all(pecas_iguais(p, cria_peca('X')) for p in vetor):
        return 1
    if all(pecas_iguais(p, cria_peca('O')) for p in vetor):
        return -1
    return 0

def obter_posicoes_livres(tabuleiro):
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
            # passar turno: origem == destino é sempre válido
            return (posicao_origem, posicao_destino)

        if not eh_posicao_livre(t, posicao_destino):
            raise ValueError("obter_movimento_manual: escolha invalida")

        if posicao_destino not in obter_posicoes_adjacentes(posicao_origem):
            raise ValueError("obter_movimento_manual: escolha invalida")

        return (posicao_origem, posicao_destino)



def obter_movimento_auto(tabuleiro, peca, dificuldade):
    """
    tabuleiro × peca × str → tuplo de posicoes
    Devolve um movimento automático de acordo com o nível de dificuldade.
    """

    if not eh_tabuleiro(tabuleiro) or not eh_peca(peca) or dificuldade not in ('facil', 'normal', 'dificil'):
        raise ValueError("obter_movimento_auto: argumentos invalidos")

    posicoes_jogador = obter_posicoes_jogador(tabuleiro, peca)
    fase_colocacao = len(posicoes_jogador) < 3

    # ============================================================
    # FASE DE COLOCAÇÃO
    # ============================================================
    if fase_colocacao:
        # 1) Vitória
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

        # fallback (não deve acontecer)
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

    # se tudo bloqueado, peça parada
    return (posicoes_jogador[0], posicoes_jogador[0])



# FUNÇÃO PRINCIPAL DO JOGO
def moinho(peca, nivel):

    if peca not in ('[X]', '[O]') or nivel not in ('facil', 'normal', 'dificil'):
        raise ValueError('moinho: argumentos invalidos')

    print(f"Bem-vindo ao JOGO DO MOINHO. Nivel de dificuldade {nivel}.")

    tab = cria_tabuleiro()
    jogador = cria_peca(peca[1])
    cpu = cria_peca('X' if peca == '[O]' else 'O')
    turno = cria_copia_peca(jogador)

    pecas_humano = 0
    pecas_cpu = 0

    # Fase de colocacao  (ALTEREI ESTE METODO TODO)
    while pecas_humano < 3 or pecas_cpu < 3:
        print(tabuleiro_para_str(tab))
        if pecas_humano < 3 and pecas_cpu < 3:
            # primeiro o humano, depois o computador, como no exemplo
            if pecas_humano == pecas_cpu:
                # turno do jogador (usa a auxiliar)
                try:
                    mov = obter_movimento_manual(tab, jogador)
                    pos = mov[0]
                    tab = coloca_peca(tab, jogador, pos)
                    pecas_humano += 1
                except ValueError:
                    continue
            else:
                print(f"Turno do computador ({nivel}):")
                mov = obter_movimento_auto(tab, cpu, nivel)
                pos = mov[0]
                tab = coloca_peca(tab, cpu, pos)
                pecas_cpu += 1
        elif pecas_humano < 3:
            # só humano ainda coloca
            try:
                mov = obter_movimento_manual(tab, jogador)
                pos = mov[0]
                tab = coloca_peca(tab, jogador, pos)
                pecas_humano += 1
            except ValueError:
                continue
        elif pecas_cpu < 3:
            print(f"Turno do computador ({nivel}):")
            mov = obter_movimento_auto(tab, cpu, nivel)
            pos = mov[0]
            tab = coloca_peca(tab, cpu, pos)
            pecas_cpu += 1

    # Fase de movimento  (alterei a parte da peça chamada, nao vai corromper nada dw)
    turno = cria_copia_peca(jogador)
    while pecas_iguais(obter_ganhador(tab), cria_peca(' ')):
        print(tabuleiro_para_str(tab))
        if pecas_iguais(turno, jogador):
            try:
                mov = obter_movimento_manual(tab, jogador)
                orig, dest = mov
                if not posicoes_iguais(orig, dest):
                    tab = move_peca(tab, orig, dest)
                turno = cpu
            except ValueError:
                continue
        else:
            print(f"Turno do computador ({nivel}):")
            orig, dest = obter_movimento_auto(tab, cpu, nivel)
            if not posicoes_iguais(orig, dest):
                tab = move_peca(tab, orig, dest)
            turno = jogador

    print(tabuleiro_para_str(tab))
    print(peca_para_str(obter_ganhador(tab)))
    return peca_para_str(obter_ganhador(tab))



moinho('[X]', 'facil')