import pandas as pd
import json

# Caminho do Excel (ajuste conforme necessário)
excel_path = "modelo_painel_indicadores.xlsx"
json_path = "dados.json"

# Lê os dados da planilha
df = pd.read_excel(excel_path)

# Converte os dados em dicionário
dados = {
    "dias": df["dias"].tolist(),
    "sla": df["sla"].tolist(),
    "chamados": df["chamados"].tolist()
}

# Salva como JSON formatado
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(dados, f, indent=2, ensure_ascii=False)

print("Arquivo 'dados.json' gerado com sucesso.")
