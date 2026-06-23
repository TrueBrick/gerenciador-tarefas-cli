import json

with open("colecao_relogios.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)
    colecao = dados["colecao"]
print(f"Coleção de relógios — {len(colecao)} itens")
print("=" * 45)

for relogio in colecao:
    print(f"{relogio['marca']} {relogio['modelo']} ({relogio['ano']})")
    print(f"  Preço pago: R$ {relogio['preco_pago']:,.2f}")
    print(f"  Movimento: {relogio['especificacoes']['movimento']}")
    print(f"  Diâmetro: {relogio['especificacoes']['diametro_mm']}mm")
    print("=" * 45)

# Atualizar preço do G-Shock
colecao[3]["preco_pago"] = 950.00

# Salvar de volta no arquivo
with open("colecao_relogios.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, indent=4, ensure_ascii=False)

print("Arquivo atualizado com sucesso!")