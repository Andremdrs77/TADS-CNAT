#include <iostream>

int menor(int a, int b) {
    int menor;

    if (a < b) {
        menor = a;
    } else {
        menor = b;
    }

    return menor;
}

bool primosConjuntos(int n, int m) {
    int range = menor(n, m);
    bool primos = true;

    for (int i = 2; i <= range; i++) {
        if (n % i == 0 && m % i == 0) {
            primos = false;
        }
    }

    return primos;
}

int main() {
    int num1, num2;

    std::cin >> num1 >> num2;
    bool num_primos = primosConjuntos(num1, num2);
    std::cout << num_primos << std::endl;

    return 0;
}
  // ---------------------------------
// | Caso | `a` | `b` | Saída esperada |
// | ---- | --- | --- | -------------- |
// |    1 |   6 |  10 |              0 |
// |    2 |   8 |  15 |              1 |
// |    3 |   7 |  13 |              1 |
// |    4 |  12 |  18 |              0 |
// |    5 |   9 |  25 |              1 |
  // Fiz o layout da tabela com o ChatGPT pra ficar legível no próprio arquivo .cpp