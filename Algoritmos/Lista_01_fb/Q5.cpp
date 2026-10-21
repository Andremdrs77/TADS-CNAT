
#include <iostream>

int quantidadeTriangulos(int x[], int y[], int n) {
    int quantidade = 0;

    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            for (int k = j + 1; k < n; k++) {
                int a = (x[i] - x[j]) * (x[i] - x[j])
                      + (y[i] - y[j]) * (y[i] - y[j]);

                int b = (x[i] - x[k]) * (x[i] - x[k])
                      + (y[i] - y[k]) * (y[i] - y[k]);

                int c = (x[j] - x[k]) * (x[j] - x[k])
                      + (y[j] - y[k]) * (y[j] - y[k]);

                if (a + b == c || a + c == b || b + c == a) {
                    quantidade++;
                }
            }
        }
    }

    return quantidade;
}

int main() {
    int n;
    std::cin >> n;

    int x[n], y[n];

    for (int i = 0; i < n; i++) {
        std::cin >> x[i] >> y[i];
    }

    std::cout << quantidadeTriangulos(x, y, n) << std::endl;

    return 0;
}
