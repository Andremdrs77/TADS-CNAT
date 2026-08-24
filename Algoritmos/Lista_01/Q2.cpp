#include <iostream>

long retangulo(int l1, int l2) {
    long perimetro = 2LL * l1 + 2LL * l2;
    return perimetro;
}

int main() {
    int l1, l2;
    std::cin >> l1 >> l2;
    long p = retangulo(l1, l2);
    std::cout << p << std::endl;
    return 0;
}

// A) Usamos long pois, mesmo os dois inputs indo até 1 bilhão, o perímetro pode chegar a 4 bilhões, que sai da margem dos 32 bits.

// B)
// long retangulo(int l1, int l2) {
//     long perimetro = 2LL * l1 + 2LL * l2;
//     return perimetro;
// }

// C)
  // | Caso |          `l1` |          `l2` | Perímetro esperado |
  // | ---- | ------------- | ------------- | ------------------ |
  // |    1 |             1 |             1 |                  4 |
  // |    2 |             5 |            10 |                 30 |
  // |    3 |           100 |           200 |                600 |
  // |    4 |   999.999.999 | 1.000.000.000 |      3.999.999.998 |
  // |    5 | 1.000.000.000 | 1.000.000.000 |      4.000.000.000 |
// Fiz o layout da tabela com o ChatGPT pra ficar legível no próprio arquivo .cpp



