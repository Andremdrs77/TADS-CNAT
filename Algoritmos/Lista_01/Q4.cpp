#include <iostream>

int quantidadePostes(int m, int p) {
    int qtd_postes = 1 + (m / p);
    int distancia_resto = m % p;

    if (distancia_resto != 0) {
        qtd_postes += 1;
    }

    return qtd_postes;
}

int distanciaUltimos(int m, int p) {
    int distancia_resto = m % p;

    if (distancia_resto == 0) {
        return p;
    }

    return distancia_resto;
}

int main() {
    int m, p;
    std::cin >> m >> p;
    int qtd_postes = quantidadePostes(m, p);
    int distancia_resto = distanciaUltimos(m, p);

    std::cout << qtd_postes << std::endl;
    std::cout << distancia_resto <<std::endl;
}