// Clara está organizando as fotos da sua última viagem num álbum de fotos. Como ela tem muitas fotos, para economizar páginas do álbum ela quer colar duas fotos por página do álbum.
// Como as fotos são retangulares, as fotos podem ser coladas giradas (mas sempre com lados paralelos aos da página do álbum, para preservar o equilíbrio estético do álbum), mas elas devem sempre ficar inteiramente contidas no interior da página, e não devem se sobrepor.
// Em geral, das muitas formas de posicionar as fotos do álbum só algumas (ou nenhuma) satisfazem estas restrições, então pode ser difícil decidir se é possível colar as duas fotos em uma mesma página do álbum, e por isso Clara pediu a sua ajuda para escrever um programa que, dadas as dimensões da página e das fotos, decide se é possível colar as fotos na página.
// Por exemplo, cada página pode ser 5×7, e duas fotos são 3×4. Nesse caso, é possível colar as duas fotos:

#include <iostream>

void verificarFotos(int X, int Y, int L, int H, int L2, int H2) {
    int maiorH, maiorL;

    if (H >= H2) {
        maiorH = H;
    } else {
        maiorH = H2;
    }

    if (L >= L2) {
        maiorL = L;
    } else {
        maiorL = L2;
    }

    if ((X * Y) >= (L * H) + (L2 * H2)) {
        if ((L + L2 <= X && maiorH <= Y) || (H + H2 <= Y && maiorL <= X) || (L + H2 <= X && maiorH <= Y) || (H + L2 <= Y && maiorL <= X || L + H <= X && maiorH <= Y || H + L <= Y && maiorL <= X)) {
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