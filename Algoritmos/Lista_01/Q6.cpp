#include <iostream>

bool verificarPrimo(int n) {
    int cont = 0;
    bool resultado = false;
    for (int i = 1; i <= n; i++) {
        if (n % i == 0) {
            cont += 1;
        }
    }
    
    if (cont == 2) {
        resultado = true;
    }
    
    return resultado;
}

int main() {
    int num;
    std::cin >> num;
    bool resultado = verificarPrimo(num);
    std::cout << resultado << std::endl;
    
    return 0;
}