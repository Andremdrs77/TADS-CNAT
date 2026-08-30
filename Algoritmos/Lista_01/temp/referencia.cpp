#include <iostream>

struct cordenada {
    double x, y;
}

void mostra_cordenada(cordenada &c) {
    std::cout << "(" << c.x ", " << c.y << ")";
}

int main(){
    cordenada c1, c2;

    std::cin >> c1.x >> c1.y;
    std::cin >> c2.x >> c2.y;
    std::cout << "C1 = ";
    mostra_cordenada(c1);
    
    std::cout << std::endl;
    std::cout << "C2 = ";
    mostra_cordenada(c2);
    std::cout << std::endl;

    return 0;
}