#include <iostream>

bool remove(int value, int a[], int& n) {
    
    for (int i = 0; i < n; i++) {
        if (a[i] == value) {
            for (int j = i; j < n; j++) {
                a[j] = a[j + 1];
            }
            
            n -= 1;
            return true;
        }
    }
    std::cout << "Valor inválido" << std::endl;
    return false;
}

bool remove_at(int index, int a[], int& n) {
    if (index < n and index > 0) {
        for (int i = index; i < n; i++) {
        a[i] = a[i + 1];
        }
        
        n -= 1;
        return true;
    } else {
        std::cout << "Índice inválido" << std::endl;
        return false;
    }
}

int main() {
    int a[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0};
    int tam_logico = sizeof(a) / sizeof(a[0]);

    remove_at(3, a, tam_logico);
    remove_at(8, a, tam_logico);
    remove(6, a, tam_logico);
    remove(7, a, tam_logico);
    remove(6, a, tam_logico);
    remove_at(7, a, tam_logico);
    
    for (int i = 0; i < tam_logico; i++) {
        std::cout << a[i] << " ";
    }
    std::cout << std::endl;
    std::cout << tam_logico;
    
    return 0;
}