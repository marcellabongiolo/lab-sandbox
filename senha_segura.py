"""
Módulo: Validador e Analisador de Força de Senhas
Autor: Marcella Bongiolo
Descrição: Script experimental criado para o lab-sandbox para analisar 
           a robustez de senhas baseada em critérios de segurança.
"""

def analisar_forca_senha(senha):
    tamanho = len(senha)
    tem_maiuscula = any(c.isupper() for c in senha)
    tem_minuscula = any(c.islower() for c in senha)
    tem_numero = any(c.isdigit() for c in senha)
    tem_especial = any(not c.isalnum() for c in senha)
    
    pontos = sum([tamanho >= 8, tem_maiuscula, tem_minuscula, tem_numero, tem_especial])
    
    print("\n" + "="*40)
    print(" 🛡️  RELATÓRIO DE ANÁLISE DE SEGURANÇA")
    print("="*40)
    print(f"🔹 Tamanho da senha: {tamanho} caracteres")
    print(f"🔹 Letras maiúsculas: {'✅' if tem_maiuscula else '❌'}")
    print(f"🔹 Letras minúsculas: {'✅' if tem_minuscula else '❌'}")
    print(f"🔹 Números: {'✅' if tem_numero else '❌'}")
    print(f"🔹 Caracteres especiais: {'✅' if tem_especial else '❌'}")
    print("-" * 40)
    
    if pontos <= 2:
        print("⚠️ Status: SENHA FRACA — Risco alto de vulnerabilidade.")
    elif pontos <= 4:
        print("⚠️ Status: SENHA MÉDIA — Pode ser melhorada.")
    else:
        print("🚀 Status: SENHA FORTE — Excelente nível de segurança!")
    print("="*40 + "\n")

if __name__ == "__main__":
    print("--- Laboratório de Testes: Lab-Sandbox ---")
    usuario_senha = input("Digite uma senha para testar a robustez: ")
    analisar_forca_senha(usuario_senha)
