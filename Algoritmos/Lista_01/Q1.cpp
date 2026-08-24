#include <iostream>

long soma(long a, long b) {
    long r = a + b;
    return r;
}

int main() {
    long a, b;
    std::cin >> a >> b;
    long s = soma (a, b);
    std::cout << s << std::endl;
    return 0;
}

// A) Feito
// B) 30, 0, -5, 2000000000, 4, -1294967296, 935362436
// C) O primeiro, quarto e sexto resultados apenas fazem uma soma comum, os demais somam números negativos, ou seja, algo como a + (-b), no entanto, os últimos dois resultados estão incorretos.
// D) Os últimos resultados estão incorretos pois passam de 32 bits (-2.147.483.647 a 2.147.483.647). A correção é usar 'long' ou 'long long' ao definir as variáveis para poder ter mais bits.