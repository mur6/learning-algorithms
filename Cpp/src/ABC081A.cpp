#include <iostream>
#include <istream>
#include <ostream>
#include <string>

int main() {
    std::istream& input = std::cin;
    std::string word;
    input >> word;
    int count = 0;
    for (char c : word) {
        if (c == '1') {
            count++;
        }
    }
    std::cout << count << std::endl;
}
