#include <iostream>
#include <algorithm>

void verificarFotos(int X, int Y, int L, int H, int L2, int H2) {

    if ((X * Y) >= (L * H) + (L2 * H2)) {
        if ((L + L2 <= X && std::max(H, H2) <= Y) || (H + H2 <= Y && std::max(L, L2) <= X) || (L + H2 <= X && std::max(L2, H) <= Y) || (H + L2 <= X && std::max(L, H2) <= Y || L + L2 <= Y && std::max(H, H2) <= X || H + H2 <= X && std::max(L, L2) <= Y) || (L + H2 <= Y && std::max(H, L2) <= X) || (H + L2 <= Y && std::max(L, H2) <= X)) {
            std::cout << "S" << std::endl;
        } else {
            std::cout << "N" << std::endl;
        }
    } else {
        std::cout << "N" << std::endl;
    }
}

int main() {
    int X, Y, L, H, L2, H2;
    std::cin >> X >> Y;
    std::cin >> L >> H;
    std::cin >> L2 >> H2;

    verificarFotos(X, Y, L, H, L2, H2);
    
    return 0;
}

// Eu poderia ter criado alguma funçãozinha pra substituir std::max(), no entanto, achei mais prático usá-la, se não houver problema.