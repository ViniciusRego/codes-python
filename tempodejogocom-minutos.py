def calcular_duracao_jogo(hora_inicial, minuto_inicial, hora_final, minuto_final):
    # Calcula a diferença entre as horas e minutos de início e fim
    minutos_inicio = hora_inicial * 60 + minuto_inicial
    minutos_fim = hora_final * 60 + minuto_final

    # Verifica se o jogo passou da meia-noite
    if minutos_fim <= minutos_inicio:
        minutos_fim += 24 * 60

    duracao_total_minutos = minutos_fim - minutos_inicio

    # Calcula as horas e minutos de duração do jogo
    duracao_horas = duracao_total_minutos // 60
    duracao_minutos = duracao_total_minutos % 60

    return duracao_horas, duracao_minutos


# Entrada de dados
hora_inicial, minuto_inicial, hora_final, minuto_final = map(int, input().split())

# Calcula a duração do jogo
duracao_horas, duracao_minutos = calcular_duracao_jogo(hora_inicial, minuto_inicial, hora_final, minuto_final)

# Saída de dados
print(f"O JOGO DUROU {duracao_horas} HORA(S) E {duracao_minutos} MINUTO(S)")
