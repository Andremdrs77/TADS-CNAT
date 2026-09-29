#include <iostream>

void soma_arrays(int a[], int n, int x) {
    bool encontrou = false;
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            if (a[i] + a[j] == x and i != j){
                encontrou = true;
                std::cout << a[i] << " + " << a[j] << " = " << a[i] + a[j] << std::endl;
            }
        }
    }
    if (!encontrou) {
        std::cout << "Não há valores que, somados, deem " << x << ".";
    }
}

int main(){
    int n, x;
    
    std::cout << "Tamanho do array:" << std::endl;
    std::cin >> n;
    
    std::cout << "Número a ser comparado:" << std::endl;
    std::cin >> x;
    int a[n];
    
    std::cout << "Preencha o array:" << std::endl;
    for (int i = 0; i < n; i++) {
        std::cin >> a[i];
    }
    
    soma_arrays(a, n, x);
    
    return 0;
}

