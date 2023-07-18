# Leitura da quantidade de caixas compradas
quantidade_caixas = int(input())

# Cálculo da quantidade total de comprimidos
quantidade_total_comprimidos = quantidade_caixas * 35

# Cálculo da quantidade de dias que o estoque vai durar
quantidade_dias = quantidade_total_comprimidos // 4

# Cálculo da quantidade de comprimidos que sobrarão após os dias calculados
comprimidos_restantes = quantidade_total_comprimidos % 4

# Impressão da quantidade de dias e quantidade de comprimidos restantes
print(quantidade_dias)
print(comprimidos_restantes)
