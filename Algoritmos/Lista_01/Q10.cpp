#include <iostream>
#include <iomanip>

double raizQuadrada(double n) {
    double r = n / 2.0;

    while (true) {
        double novoR = (r + n / r) / 2.0;

        if (novoR - r < 0.001 && r - novoR < 0.001) {
            return novoR;
        }

        r = novoR;
    }
}

int main() {
    double n;

    std::cin >> n;

    double resultado = raizQuadrada(n);

    std::cout << std::fixed << std::setprecision(3);
    std::cout << resultado << std::endl;

    return 0;
}