#include <iostream>
#include <iomanip>

float calcularCirculo(int d) {
    const double pi = 3.14159;
    int r = d/2;
    float circulo = pi * r * r;
    return circulo;
}

int main() {
    float diametro;
    std::cin >> diametro;
    float resultado = calcularCirculo(diametro);
    std::cout << std::fixed << std::setprecision(5) << resultado;
    return 0;
}


