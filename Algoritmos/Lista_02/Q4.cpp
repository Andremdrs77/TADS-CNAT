#include <iostream>

int maiorSoma(int a[], unsigned int n) {
    int resultado = a[0] + a[1];

    for (unsigned int i = 2; i < n; i++) {
        if (a[i - 1] + a[i] > resultado) {
            resultado = a[i - 1] + a[i];
        }
    }

    return resultado;
}

int main() {
    unsigned int n;
    std::cin >> n;
    int a[n];

    for (unsigned int i = 0; i < n; i++) {
        std::cin >> a[i];
    }

    int resultado = maiorSoma(a, n);
    std::cout << resultado << std::endl;
    
    return 0;
}