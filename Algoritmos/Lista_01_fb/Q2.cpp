#include <iostream>

void verificarPar(int a[], int n, int s) {
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (a[i] + a[j] == s) {
                std::cout << a[i] << "+" << a[j] << "=" << (a[i] + a[j]) << std::endl;
            }
        }
    }
}


int main() {
    int n, s;

    std::cin >> n;
    std::cin >> s;

    int a[n];

    for (int i = 0; i < n; i++) {
        std::cin >> a[i];
    }

    verificarPar(a, n, s);

    return 0;
}