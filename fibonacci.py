import math

def is_perfect_square(n: int) -> bool:
    """Verifica se um número é um quadrado perfeito."""
    sqrt_n = int(math.isqrt(n))
    return sqrt_n * sqrt_n == n

def is_fibonacci_number(num: int) -> bool:
    """
    Verifica se um número pertence à sequência de Fibonacci.
    
    Um número faz parte da sequência de Fibonacci se e somente se um ou ambos
    de (5 * n^2 + 4) ou (5 * n^2 - 4) forem quadrados perfeitos.
    """
    if num < 0:
        return False

    test_1 = 5 * (num ** 2) + 4
    test_2 = 5 * (num ** 2) - 4

    return is_perfect_square(test_1) or is_perfect_square(test_2)

def main() -> None:
    """Função principal para capturar a entrada do usuário e verificar se pertence à sequência de Fibonacci."""
    try:
        number = int(input("Informe um número: "))
    except ValueError:
        print("Por favor, insira um número inteiro válido.")
        return

    if is_fibonacci_number(number):
        print(f"O número {number} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {number} não pertence à sequência de Fibonacci.")

if __name__ == "__main__":
    main()
