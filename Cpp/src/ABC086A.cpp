#include <iostream>

int main() {
    // 入力 (a, b) from std::cin
    int a, b;
    std::cin >> a >> b;
    std::cout << (a * b % 2 == 0 ? "Even" : "Odd") << std::endl;
    return 0;
}
