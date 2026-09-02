#include <iostream>

int maior_do_array(int a[], unsigned int n) {
    int resultado = a[0];

    for (unsigned int i = 1; i < n; i++) {
        if (a[i] > resultado) {
            resultado = a[i];
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
    int maior = maior_do_array(a, n);
    std::cout << maior << std::endl;
    
    return 0;
}

/*

A) Feito

B) TESTES:

Teste 1:
Entrada:
5
1 2 3 4 5

Saída esperada:
5

Teste 2:
Entrada:
5
5 4 3 2 1

Saída esperada:
5

Teste 3:
Entrada:
6
10 25 3 8 17 4

Saída esperada:
25

Teste 4:
Entrada:
5
-10 -5 -20 -3 -8

Saída esperada:
-3

Teste 5:
Entrada:
5
7 7 7 7 7

Saída esperada:
7

C) 
#include <iostream>

int maior_do_array(int a[], unsigned int n) {
    int resultado = a[0];
    int index = 0;

    for (unsigned int i = 1; i < n; i++) {
        if (a[i] > resultado) {
            resultado = a[i];
            index = i;
        }
    }

    return index;
}

int main() {
    unsigned int n;

    std::cin >> n;
    int a[n];

    for (unsigned int i = 0; i < n; i++) {
        std::cin >> a[i];
    }

    int maior = maior_do_array(a, n);
    std::cout << maior << std::endl;

    return 0;
}

D) 
#include <iostream>

int menor_do_array(int a[], unsigned int n) {
    int resultado = a[0], index = 0;

    for (unsigned int i = 1; i < n; i++) {
        if (a[i] < resultado) {
            resultado = a[i];
            index = i;
        }
    }

    return index;
}

int main() {
    unsigned int n;
    

    std::cin >> n;
    int a[n];

    for (unsigned int i = 0; i < n; i++) {
        std::cin >> a[i];
    }
    int menor = menor_do_array(a, n);
    std::cout << menor << std::endl;
    
    return 0;
}
    
*/ 
