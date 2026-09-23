"""Analisador educacional de requisitos de senhas.

O módulo verifica critérios básicos de composição. A análise é heurística e
não mede resistência real a ataques nem substitui políticas de segurança.
"""


def analisar_forca_senha(senha: str) -> dict[str, object]:
    """Analisa requisitos básicos sem armazenar ou exibir a senha."""
    if not isinstance(senha, str):
        raise TypeError("A senha deve ser uma string.")

    tamanho = len(senha)
    criterios = {
        "tamanho_minimo": tamanho >= 8,
        "maiuscula": any(caractere.isupper() for caractere in senha),
        "minuscula": any(caractere.islower() for caractere in senha),
        "numero": any(caractere.isdigit() for caractere in senha),
        "especial": any(not caractere.isalnum() for caractere in senha),
    }

    pontos = sum(criterios.values())

    if pontos <= 2:
        classificacao = "fraca"
    elif pontos <= 4:
        classificacao = "media"
    else:
        classificacao = "forte"

    return {
        "tamanho": tamanho,
        "criterios": criterios,
        "pontos": pontos,
        "classificacao": classificacao,
    }


def exibir_relatorio(resultado: dict[str, object]) -> None:
    """Exibe os critérios avaliados, sem revelar a senha analisada."""
    criterios = resultado["criterios"]

    print("\n" + "=" * 40)
    print("🛡️  RELATÓRIO DE ANÁLISE DE SENHA")
    print("=" * 40)
    print(f"Tamanho: {resultado['tamanho']} caracteres")
    print(f"Maiúsculas: {'OK' if criterios['maiuscula'] else 'Não'}")
    print(f"Minúsculas: {'OK' if criterios['minuscula'] else 'Não'}")
    print(f"Números: {'OK' if criterios['numero'] else 'Não'}")
    print(f"Caracteres especiais: {'OK' if criterios['especial'] else 'Não'}")
    print(f"Classificação heurística: {resultado['classificacao']}")
    print("=" * 40)


def main() -> None:
    """Executa o analisador pela linha de comando."""
    senha = input("Digite uma senha para analisar: ")
    resultado = analisar_forca_senha(senha)
    exibir_relatorio(resultado)


if __name__ == "__main__":
    main()
