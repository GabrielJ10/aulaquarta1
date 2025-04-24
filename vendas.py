vendas = []

while True:
    produto = input("Nome do produto: ")
    quantidade = int(input("Quantidade vendida: "))
    preco_unitario = float(input("Preço unitário: R$ "))

    vendas.append({
        "produto": produto,
        "quantidade": quantidade,
        "preco_unitario": preco_unitario,
        "total": quantidade * preco_unitario
    })

    cont = input("Deseja continuar? (s/n): ")
    if cont.lower() != 's':
        break

print("\n--- Vendas Realizadas ---")
for venda in vendas:
    print(f"{venda['produto']} - {venda['quantidade']} unidades x R$ {venda['preco_unitario']:.2f} = R$ {venda['total']:.2f}")
