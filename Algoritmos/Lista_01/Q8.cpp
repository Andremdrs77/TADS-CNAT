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

int descobrirMDC(int a, int b) {
    int MDC = 1;

    for (int i = 2; i <= menor(a, b); i++) {
        if (a % i == 0 and b % i == 0) {
            MDC = i;
        }
    }
    
    return MDC;
}

int main() {
    int num1, num2;

    std::cin >> num1 >> num2;
    int MDC = descobrirMDC(num1, num2);
    std::cout << MDC << std::endl;

    return 0;
}