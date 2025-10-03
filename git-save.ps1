param(
    [string]$msg = "Update"
)

# Adiciona todos os arquivos modificados
git add .

# Faz o commit com a mensagem passada
git commit -m "$msg"

# Envia para o GitHub
git push origin main
