#include <iostream>

int get_present_count(int n) {
    int result = 0;
    for(int i = 1; i * i <= n; ++i) {
        if(n % i == 0) {
            int first = i;
            int second = n / first;
            result += first * 10;
            if(second != i) {
                result += second * 10;
            }
        }
    }
    return result;
}

int main() {
    int target;
    std::cin >> target;
    int i = 1;
    while(true) {
        int presents = get_present_count(i);
        if(presents >= target) {
            break;
        }
        ++i;
    }
    std::cout << i << "\n";
}