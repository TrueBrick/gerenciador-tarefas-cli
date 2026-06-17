import requests

resposta = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=brl")
dados = resposta.json()
preco = dados["bitcoin"]["brl"]
preco_eth = dados["ethereum"]["brl"]
preco_sol = dados["solana"]["brl"]
print(f"Bitcoin hoje: R$ {preco:,}")
print(f"Ethereum hoje: R$ {preco_eth:,}")
print(f"Solana hoje: R$ {preco_sol:,}")