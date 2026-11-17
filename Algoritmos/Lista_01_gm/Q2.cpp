#include <iostream>

void VetorX(int a[], int x, int y) {
    bool encontrado = false;
    
    for (int i = 0; i < y; i++) {
        if (a[i] == x){
        std::cout << i << std::endl;
        encontrado = true;
        break;
        }
    }
    
    if (encontrado == false) {
        std::cout << "-1" << std::endl;
    }
    
}

int main() {
    int a[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int y = sizeof(a) / sizeof(a[0]);
    
    int x = 0;
    VetorX(a, x, y);
    
    x = 8;
    VetorX(a, x, y);

    x = 10;
    VetorX(a, x, y);

    x = 11;
    VetorX(a, x, y);
    
    return 0;
}