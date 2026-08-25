#include <iostream>

int divisores(int n) {
    int cont = 0;
    for (int i = 1; i <= n; i++) {
        if (n % i == 0) {
            cont += 1;
        }
    }
    return cont;
}

int main() {
    int num;
    std::cin >> num;
    int qtd_divisores = divisores(num);
    std::cout << qtd_divisores << std::endl;
    
    return 0;
}