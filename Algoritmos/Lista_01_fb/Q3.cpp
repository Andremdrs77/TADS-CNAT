#include <iostream>

void sublistaContigua(int a[], int n) {
    int maiorSublista = a[0], temp = 0;

    for (int i = 0; i < n; i++) {
        temp = 0;
        for (int j = i; j < n; j++) {
            temp += a[j];
            if (temp > maiorSublista) {
                maiorSublista = temp;
            }
        }
    }
    std::cout << maiorSublista;
}


int main() {
    int n;
    std::cin >> n;

    int a[n];

    for (int i = 0; i < n; i++) {
        std::cin >> a[i];
    }

    sublistaContigua(a, n);


    return 0;
}