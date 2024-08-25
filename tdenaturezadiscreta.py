def leitura(arquivo):
    ## essa função lê o arquivo por linhas
    with open(arquivo, 'r') as file:
        leitura = file.readlines()
    return leitura

def operacoes(leitura, index):
    # essa função pega as linhas do texto e separa em uma operação e dois conjuntos
    operacao = leitura[index].strip().upper()
    conjunto1 = set(leitura[index + 1].strip().split(","))
    conjunto2 = set(leitura[index + 2].strip().split(","))

    if operacao == 'U':
        return "União", conjunto1.union(conjunto2)
    elif operacao == 'I':
        return "Interseção", conjunto1.intersection(conjunto2)
    elif operacao == 'D':
        return "Diferença", conjunto1.difference(conjunto2)
    elif operacao == 'C':
        return "Produto Cartesiano", {(x, y) for x in conjunto1 for y in conjunto2}
    else:
        return "Inválido", "operação inválida"

def processamento_das_operacoes(arquivo):
    linhas_lidas = leitura(arquivo)
    total_operacoes = int(linhas_lidas[0].strip())
    resultados = []

    ## acessa as linhas com os elementos de cada conjunto
    for i in range(total_operacoes):
        index = 1 + i * 3
        nome_operacao, resultado = operacoes(linhas_lidas, index)
        conjunto1 = set(linhas_lidas[index + 1].strip().split(","))
        conjunto2 = set(linhas_lidas[index + 2].strip().split(","))
        resultados.append((nome_operacao, conjunto1, conjunto2, resultado))


    return resultados

def main():
    nome_arquivo = input("Digite o caminho do arquivo para usar como entrada: ")
    saida = processamento_das_operacoes(nome_arquivo)

    for nome_operacao, conjunto1, conjunto2, resultado in saida:
        print(f"{nome_operacao}: Conjunto 1: {conjunto1}, conjunto 2: {conjunto2}. Resultado: {resultado}")

if __name__ == "__main__":
    main()