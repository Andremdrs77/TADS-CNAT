#include <iostream>

struct fracao {
    int numerador;
    int denominador;
};

int maior(int a, int b) {
    if (a > b) {
        return a;
    } else {
        return b;
    }
}

int menor(int a, int b) {
    if (a < b) {
        return a;
    } else {
        return b;
    }
}

int descobrirMMC(int a, int b) {
    int MMC;

    for (int i = maior(a, b); ; i++) {
        if (i % a == 0 and i % b == 0) {
            MMC = i;
            break;
        }
    }

    return MMC;
}

int descobrirMDC(int a, int b) {
    int MDC = 1;

    for (int i = 2; i <= menor(a, b); i++) {
        if (a % i == 0 and b % i == 0) {
            MDC = i;
        }
    }

    return MDC;
}

fracao soma(fracao &f1, fracao &f2) {
    int MMC = descobrirMMC(f1.denominador, f2.denominador);

    int numerador = (f1.numerador * (MMC / f1.denominador))
                  + (f2.numerador * (MMC / f2.denominador));

    int denominador = MMC;

    int MDC = descobrirMDC(numerador, denominador);

    numerador = numerador / MDC;
    denominador = denominador / MDC;

    fracao f3;
    f3.numerador = numerador;
    f3.denominador = denominador;

    return f3;
}

int main() {
    fracao f1, f2;

    std::cin >> f1.numerador >> f1.denominador;
    std::cin >> f2.numerador >> f2.denominador;

    fracao f3 = soma(f1, f2);

    std::cout << f3.numerador << "/" << f3.denominador << std::endl;

    return 0;
}