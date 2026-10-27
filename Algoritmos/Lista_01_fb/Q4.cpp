#include <iostream>

void pontos(int x[], int y[], int n) {
    int menorDistancia = -1;
    int ponto1 = 0, ponto2 = 0;

    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            int dx = x[i] - x[j];
            int dy = y[i] - y[j];

            int distancia = dx * dx + dy * dy;

            if (menorDistancia == -1 || distancia < menorDistancia) {
                menorDistancia = distancia;
                ponto1 = i;
                ponto2 = j;
            }
        }
    }

    std::cout << "Pontos mais próximos: ("
              << x[ponto1] << ", " << y[ponto1] << ") e ("
              << x[ponto2] << ", " << y[ponto2] << ")\n";
}

int main() {
    int n;
    std::cin >> n;

    int x[n], y[n];

    for (int i = 0; i < n; i++) {
        std::cin >> x[i] >> y[i];
    }

    pontos(x, y, n);

    return 0;
}
