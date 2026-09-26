#include <iostream>

void contarPrimos(int a[], int n, int primos[], int& qtd_primos) {
    for (int i = 0; i < n; i++) {
        int cont = 0;

        for (int c = 2; c < a[i]; c++) {
            if (a[i] % c == 0) {
                cont += 1;
            }
        }

        if (cont == 0 && a[i] >= 2) {
            qtd_primos += 1;
            primos[qtd_primos - 1] = a[i];
        }
    }
}

int main() {
    int n, qtd_primos = 0;
    std::cin >> n;
    int a[n], primos[n];

    for (int i = 0; i < n; i++) {
        std::cin >> a[i];
    }

    contarPrimos(a, n, primos, qtd_primos);

    if (qtd_primos > 0) {
        std::cout << qtd_primos << std::endl;
        std::cout << primos[0];

        for (int i = 1; i < qtd_primos; i++) {
            std::cout << " " << primos[i];
        }
    }

    return 0;
}