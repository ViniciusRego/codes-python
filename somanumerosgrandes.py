def sum_large_numbers(digits_a, digits_b):
    len_a = len(digits_a)
    len_b = len(digits_b)
    
    # Verificar o maior tamanho e ajustar os tamanhos dos arrays se necessário
    max_len = max(len_a, len_b)
    if len_a < max_len:
        digits_a = [0] * (max_len - len_a) + digits_a
    if len_b < max_len:
        digits_b = [0] * (max_len - len_b) + digits_b
    
    result = [0] * (max_len + 1)
    carry = 0
    
    # Somar os dígitos da direita para a esquerda
    for i in range(max_len - 1, -1, -1):
        current_sum = digits_a[i] + digits_b[i] + carry
        carry = current_sum // 10
        result[i + 1] = current_sum % 10
    
    result[0] = carry
    
    # Remover zeros à esquerda do resultado
    if result[0] == 0:
        result = result[1:]
    
    return result

# Receber a entrada do usuário
len_a = int(input())
digits_a = list(map(int, input().split()))
len_b = int(input())
digits_b = list(map(int, input().split()))

# Realizar a soma e obter o resultado
result = sum_large_numbers(digits_a, digits_b)

# Imprimir o resultado
print("".join(map(str, result)))
