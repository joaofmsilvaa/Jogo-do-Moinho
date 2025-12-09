from moinho import *

# imports para simular a stream de input/output
import io
import sys

num_tests = 0
total_score = 0

print("Inicio dos testes publicos")
print("---------------------")

# TAD posicao
# Teste 1: testa cria_posicao com argumentos invalidos (espera ValueError)
num_tests += 1
try:
    p1 = cria_posicao('a', '4')
    print("Teste " + str(num_tests) + ": Falhou")
except ValueError as inst:
    if str(inst) == "cria_posicao: argumentos invalidos":
        total_score += 1
        print("Teste " + str(num_tests) + ": Passou")
    else:
        print("Teste " + str(num_tests) + ": Falhou")
except:
    print("Teste " + str(num_tests) + ": Falhou")
    pass

# Teste 2: testa posicoes_iguais entre 'a2' e 'b3'
num_tests += 1
p1 = cria_posicao('a', '2')
p2 = cria_posicao('b', '3')
if not posicoes_iguais(p1, p2):
    total_score += 1
    print("Teste " + str(num_tests) + ": Passou")
else:
    print("Teste " + str(num_tests) + ": Falhou")

# Teste 3: testa posicao_para_str para 'a2'
num_tests += 1
p1 = cria_posicao('a', '2')
if posicao_para_str(p1) == "a2":
    total_score += 1
    print("Teste " + str(num_tests) + ": Passou")
else:
    print("Teste " + str(num_tests) + ": Falhou")

 # Teste 4: testa obter_posicoes_adjacentes de 'b3'
num_tests += 1
p2 = cria_posicao('b', '3')
t = tuple(posicao_para_str(p) for p in obter_posicoes_adjacentes(p2))
if t == ('b2', 'a3', 'c3'):
    total_score += 1
    print("Teste " + str(num_tests) + ": Passou")
else:
    print("Teste " + str(num_tests) + ": Falhou")

# TAD peca
 # Teste 5: testa cria_peca com argumento invalido (minuscula)
num_tests += 1
try:
    j1 = cria_peca('x')
    print("Teste " + str(num_tests) + ": Falhou")
except ValueError as inst:
    if str(inst) == "cria_peca: argumento invalido":
        total_score += 1
        print("Teste " + str(num_tests) + ": Passou")
    else:
        print("Teste " + str(num_tests) + ": Falhou")
except:
    print("Teste " + str(num_tests) + ": Falhou")
    pass

 # Teste 6: testa pecas_iguais entre 'X' e 'O'
num_tests += 1
j1 = cria_peca('X')
j2 = cria_peca('O')
if not pecas_iguais(j1, j2):
    total_score += 1
    print("Teste " + str(num_tests) + ": Passou")
else:
    print("Teste " + str(num_tests) + ": Falhou")

 # Teste 7: testa peca_para_str para 'X'
num_tests += 1
j1 = cria_peca('X')
if peca_para_str(j1) == "[X]":
    total_score += 1
    print("Teste " + str(num_tests) + ": Passou")
else:
    print("Teste " + str(num_tests) + ": Falhou")

 # Teste 8: testa peca_para_inteiro para espaco (vazio)
num_tests += 1
if peca_para_inteiro(cria_peca(' ')) == 0:
    total_score += 1
    print("Teste " + str(num_tests) + ": Passou")
else:
    print("Teste " + str(num_tests) + ": Falhou")

# TAD tabuleiro
 # Teste 9: testa coloca_peca em 'a1' e tabuleiro_para_str
num_tests += 1
t = cria_tabuleiro()
str_tab = tabuleiro_para_str(coloca_peca(t, cria_peca('X'), cria_posicao('a', '1')))
if str_tab == "   a   b   c\n1 [X]-[ ]-[ ]\n   | \ | / |\n2 [ ]-[ ]-[ ]\n   | / | \ |\n3 [ ]-[ ]-[ ]":
    total_score += 1
    print("Teste " + str(num_tests) + ": Passou")
else:
    print("Teste " + str(num_tests) + ": Falhou")

 # Teste 10: testa coloca_peca em 'b2' mantendo 'a1'
num_tests += 1
t = cria_tabuleiro()
t1 = coloca_peca(t, cria_peca('X'), cria_posicao('a', '1'))
str_tab = tabuleiro_para_str(coloca_peca(t, cria_peca('O'), cria_posicao('b', '2')))
if str_tab == "   a   b   c\n1 [X]-[ ]-[ ]\n   | \ | / |\n2 [ ]-[O]-[ ]\n   | / | \ |\n3 [ ]-[ ]-[ ]":
    total_score += 1
    print("Teste " + str(num_tests) + ": Passou")
else:
    print("Teste " + str(num_tests) + ": Falhou")

 # Teste 11: testa move_peca de 'a1' para 'b1'
num_tests += 1
t = cria_tabuleiro()
t1 = coloca_peca(t, cria_peca('X'), cria_posicao('a', '1'))
t1 = coloca_peca(t, cria_peca('O'), cria_posicao('b', '2'))
str_tab = tabuleiro_para_str(move_peca(t, cria_posicao('a', '1'), cria_posicao('b', '1')))
if str_tab == "   a   b   c\n1 [ ]-[X]-[ ]\n   | \ | / |\n2 [ ]-[O]-[ ]\n   | / | \ |\n3 [ ]-[ ]-[ ]":
    total_score += 1
    print("Teste " + str(num_tests) + ": Passou")
else:
    print("Teste " + str(num_tests) + ": Falhou")

 # Teste 12: testa tuplo_para_tabuleiro e tabuleiro_para_str (exibicao)
num_tests += 1 # 12
t = tuplo_para_tabuleiro(((0, 1, -1), (-0, 1, -1), (1, 0, -1)))
str_tab = tabuleiro_para_str(t)
print(str_tab, "AQUI")
if str_tab == "   a   b   c\n1 [ ]-[X]-[O]\n   | \ | / |\n2 [ ]-[X]-[O]\n   | / | \ |\n3 [X]-[ ]-[O]":
    total_score += 1
    print("Teste " + str(num_tests) + ": Passou")
else:
    print("Teste " + str(num_tests) + ": Falhou")

 # Teste 13: testa obter_ganhador em tabuleiro especifico
num_tests += 1
t = tuplo_para_tabuleiro(((0, 1, -1), (-0, 1, -1), (1, 0, -1)))
str_j = peca_para_str(obter_ganhador(t))
if str_j == "[O]":
    total_score += 1
    print("Teste " + str(num_tests) + ": Passou")
else:
    print("Teste " + str(num_tests) + ": Falhou")

 # Teste 14: testa obter_posicoes_livres
num_tests += 1 # 14
t = tuplo_para_tabuleiro(((0, 1, -1), (-0, 1, -1), (1, 0, -1)))
tuplo = tuple(posicao_para_str(p) for p in obter_posicoes_livres(t))
if tuplo == ('a1', 'a2', 'b3'):
    total_score += 1
    print("Teste " + str(num_tests) + ": Passou")
else:
    print("Teste " + str(num_tests) + ": Falhou")

 # Teste 15: testa obter_vetor coluna 'a'
num_tests += 1
t = tuplo_para_tabuleiro(((0, 1, -1), (-0, 1, -1), (1, 0, -1)))
tuplo = tuple(peca_para_str(peca) for peca in obter_vetor(t, 'a'))
if tuplo == ('[ ]', '[ ]', '[X]'):
    total_score += 1
    print("Teste " + str(num_tests) + ": Passou")
else:
    print("Teste " + str(num_tests) + ": Falhou")

 # Teste 16: testa obter_vetor linha '2'
num_tests += 1
t = tuplo_para_tabuleiro(((0, 1, -1), (-0, 1, -1), (1, 0, -1)))
tuplo = tuple(peca_para_str(peca) for peca in obter_vetor(t, '2'))
if tuplo == ('[ ]', '[X]', '[O]'):
    total_score += 1
    print("Teste " + str(num_tests) + ": Passou")
else:
    print("Teste " + str(num_tests) + ": Falhou")
# obter_movimento_manual


def obter_movimento_manual_teste(t, j, p):
    sys.stdin = io.StringIO(p)
    m = obter_movimento_manual(t, j)
    for line in sys.stdin:
        print(line)
    return m


 # Teste 17: testa obter_movimento_manual com input 'a1' (colocar)
num_tests += 1
try:
    t = cria_tabuleiro()
    m = obter_movimento_manual_teste(t, cria_peca('X'), 'a1')
    if posicao_para_str(m[0]) == "a1":
        total_score += 1
        print("\nTeste " + str(num_tests) + ": Passou")
    else:
        print("\nTeste " + str(num_tests) + ": Falhou")
except:
    print("\nTeste " + str(num_tests) + ": Falhou")
    pass

 # Teste 18: testa obter_movimento_manual com input 'b1a1' (mover)
num_tests += 1
try:
    t = tuplo_para_tabuleiro(((0, 1, -1), (1, -1, 0), (1, -1, 0)))
    m = obter_movimento_manual_teste(t, cria_peca('X'), 'b1a1')
    if posicao_para_str(m[0]) == "b1" and posicao_para_str(m[1]) == "a1" and len(m) == 2:
        total_score += 1
        print("\nTeste " + str(num_tests) + ": Passou")
    else:
        print("\nTeste " + str(num_tests) + ": Falhou")
except:
    print("\nTeste " + str(num_tests) + ": Falhou")
    pass

 # Teste 19: testa obter_movimento_manual invalido (escolha invalida)
num_tests += 1
try:
    t = tuplo_para_tabuleiro(((0, 1, -1), (1, -1, 0), (1, -1, 0)))
    m = obter_movimento_manual_teste(t, cria_peca('O'), 'a2a1')
    print("\nTeste " + str(num_tests) + ": Falhou")
except ValueError as inst:
    if str(inst) == "obter_movimento_manual: escolha invalida":
        total_score += 1
        print("\nTeste " + str(num_tests) + ": Passou")
    else:
        print("\nTeste " + str(num_tests) + ": Falhou")
except:
    print("\nTeste " + str(num_tests) + ": Falhou")
    pass

# obter_movimento_auto
# Teste 20: testa obter_movimento_auto nivel 'facil' em tabuleiro vazio
num_tests += 1
t = cria_tabuleiro()
m = obter_movimento_auto(t, cria_peca('X'), 'facil')
if posicao_para_str(m[0]) == "b2":
    total_score += 1
    print("Teste " + str(num_tests) + ": Passou")
else:
    print("Teste " + str(num_tests) + ": Falhou")

# Teste 21: testa obter_movimento_auto 'facil' em tabuleiro especifico
num_tests += 1
t = tuplo_para_tabuleiro(((1, 0, -1), (0, 1, -1), (1, -1, 0)))
m = obter_movimento_auto(t, cria_peca('X'), 'facil')
if posicao_para_str(m[0]) == "a1" and posicao_para_str(m[1]) == "b1" and len(m) == 2:
    total_score += 1
    print("Teste " + str(num_tests) + ": Passou")
else:
    print("Teste " + str(num_tests) + ": Falhou")

# Teste 22: testa obter_movimento_auto 'normal' (primeiro caso)
num_tests += 1
t = tuplo_para_tabuleiro(((1, 0, -1), (0, 1, -1), (1, -1, 0)))
m = obter_movimento_auto(t, cria_peca('X'), 'normal')
if posicao_para_str(m[0]) == "b2" and posicao_para_str(m[1]) == "a2" and len(m) == 2:
    total_score += 1
    print("Teste " + str(num_tests) + ": Passou")
else:
    print("Teste " + str(num_tests) + ": Falhou")

# Teste 23: testa obter_movimento_auto 'normal' (outro tabuleiro)
num_tests += 1
t = tuplo_para_tabuleiro(((1, -1, -1), (-1, 1, 0), (0, 0, 1)))
m = obter_movimento_auto(t, cria_peca('X'), 'normal')
if posicao_para_str(m[0]) == "b2" and posicao_para_str(m[1]) == "c2" and len(m) == 2:
    total_score += 1
    print("Teste " + str(num_tests) + ": Passou")
else:
    print("Teste " + str(num_tests) + ": Falhou")

# Teste 24: testa obter_movimento_auto 'dificil'
num_tests += 1
t = tuplo_para_tabuleiro(((1, -1, -1), (-1, 1, 0), (0, 0, 1)))
m = obter_movimento_auto(t, cria_peca('X'), 'dificil')
if posicao_para_str(m[0]) == "c3" and posicao_para_str(m[1]) == "c2" and len(m) == 2:
    total_score += 1
    print("Teste " + str(num_tests) + ": Passou")
else:
    print("Teste " + str(num_tests) + ": Falhou")

# moinho


def moinho_teste(jogador, modo, jogadas):
    sys.stdin = io.StringIO(jogadas)
    fim = moinho(jogador, modo)
    for line in sys.stdin:
        print(line)
    return fim


 # Teste 25: testa funcao moinho com jogadas simuladas (resultado esperado '[O]')
num_tests += 1
try:
    fim = moinho_teste('[X]', 'facil', 'a2\na1\nc1\nb2\nc2\na2\nc1c2\na1b1\nb1b2')
    if fim == "[O]":
        total_score += 1
        print("\nTeste " + str(num_tests) + ": Passou")
    else:
        print("\nTeste " + str(num_tests) + ": Falhou")
except:
    print("\nTeste " + str(num_tests) + ": Falhou")
    pass

print("---------------------")
print("Pontuacao final do projeto: ", total_score, "/", num_tests, "(" + "{:.2f}".format((total_score / num_tests) * 100) + "% )")
