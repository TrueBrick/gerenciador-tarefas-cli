import csv

with open("investimentos.csv", "r") as arquivo:
    leitor = csv.DictReader(arquivo)
    investimentos = []
    for linha in leitor:
        investimentos.append(linha)

print(f"Total de investimentos: {len(investimentos)}")
print("=" * 40)

for inv in investimentos:
    nome = inv["nome"]
    tipo = inv["tipo"]
    aquisicao = float(inv["valor_aquisicao"])
    atual = float(inv["valor_atual"])
    resultado = atual - aquisicao
    rentabilidade = (atual - aquisicao) / aquisicao * 100
    status = "LUCRO" if resultado > 0 else "PREJUÍZO"

    print(f"Nome: {nome}")
    print(f"Tipo: {tipo}")
    print(f"Aquisição: R$ {aquisicao:,.2f}")
    print(f"Atual: R$ {atual:,.2f}")
    print(f"Resultado: R$ {resultado:,.2f}")
    print(f"Rentabilidade: {rentabilidade:,.2f}%")
    print(f"Status: {status}")
    print("=" * 40)