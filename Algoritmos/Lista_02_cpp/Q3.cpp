#include <iostream>

void conta_imparesPares(int a[], int n, int impares[], int pares[], int& qtd_impares, int& qtd_pares) {
    for (int i = 0; i < n; ++i) {
        if (a[i] % 2 == 1) {
            impares[qtd_impares] = a[i];
            qtd_impares = qtd_impares + 1;
        } else {
            pares[qtd_pares] = a[i];
            qtd_pares = qtd_pares + 1;
        }
    }
}

void conta_negativos (int a[], int n, int negativos[], int& qtd_negativos) {
    for (int i = 0; i < n; ++i) {
        if (a[i] < 0) {
            negativos[qtd_negativos] = a[i];
            qtd_negativos = qtd_negativos + 1;
        }
    }
}

int main() {
    int n, qtd_impares = 0, qtd_pares = 0, qtd_negativos = 0;
    std::cin >> n;
    int a[n], impares[n], pares[n], negativos[n]; // A quantidade máxima de números é n

    for (int i = 0; i < n; ++i) {
        std::cin >> a[i];
    }

    conta_imparesPares(a, n, impares, pares, qtd_impares, qtd_pares);

    std::cout << qtd_impares << std::endl;

    if (qtd_impares > 0) {
        std::cout << impares[0];
        for (int i = 1; i < qtd_impares; ++i) {
            std::cout << " " << impares[i];
        }
        std::cout << std::endl;
    }

    std::cout << qtd_pares << std::endl;

    if (qtd_pares > 0) {
        std::cout << pares[0];
        for (int i = 1; i < qtd_pares; ++i) {
            std::cout << " " << pares[i];
        }
        std::cout << std::endl;
    }

    conta_negativos(a, n, negativos, qtd_negativos);

    std::cout << qtd_negativos << std::endl;

    if (qtd_negativos > 0) {
        std::cout << negativos[0];
        for (int i = 1; i < qtd_negativos; ++i) {
            std::cout << " " << negativos[i];
        }
        std::cout << std::endl;
    }


    return 0;
}