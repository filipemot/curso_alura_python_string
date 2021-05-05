from extrator_url import ExtratorURL

url = "bytebank.com/cambio?quantidade=100&moedaOrigem=dolar&moedaDestino=real"
extrator_url = ExtratorURL(url)

VALOR_DOLAR = 5.50  # 1 dólar = 5.50 reais
moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
quantidade = extrator_url.get_valor_parametro("quantidade")

valor = 0

if(moeda_origem == 'real' and moeda_destino == 'dolar'):
    valor = int(quantidade) / VALOR_DOLAR
elif(moeda_origem == 'dolar' and moeda_destino == 'real'):
    valor = int(quantidade) * VALOR_DOLAR

print(f"Valor:{valor}")