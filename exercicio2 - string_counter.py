def count_letter_a(input_string: str) -> int:
    """
    Conta a quantidade de vezes que a letra 'a' (maiúscula ou minúscula) ocorre em uma string.

    :param input_string: A string em que será feita a contagem.
    :return: O número de ocorrências de 'a' ou 'A' na string.
    """
    return input_string.lower().count('a')

def main() -> None:
    """Função principal para capturar a entrada do usuário e contar a ocorrência da letra 'a'."""
    input_string = input("Informe uma string: ")

    count = count_letter_a(input_string)
    if count > 0:
        print(f"A letra 'a' aparece {count} vezes na string informada.")
    else:
        print("A letra 'a' não aparece na string informada.")

if __name__ == "__main__":
    main()
