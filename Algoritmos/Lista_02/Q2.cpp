#include <iostream>

int descobrirMenor(int a[], unsigned int n) {
    int cont = 0;

    for (unsigned int i = 0; i < n; i++) {
        if (a[i] % 2 != 0) {
            cont += 1;
        }
    }

    return cont;
}

int main() {
    unsigned int n;
    std::cin >> n;
    std::cout << std::endl;
    int a[n];

    for (unsigned int i = 0; i < n; i++) {
        std::cin >> a[i];
    }

    int qtdImpares = descobrirMenor(a, n);
    std::cout << qtdImpares << std::endl;

    return 0;
}