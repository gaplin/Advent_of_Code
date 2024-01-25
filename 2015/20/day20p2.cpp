#include <iostream>

int get_present_count(int n) {
    int result = 0;
    for(int i = 1; i * i <= n; ++i) {
        if(n % i == 0) {
            int first = i;
            if(first * 50 >= n) {
                result += first * 11;
            }
            int second = n / first;
            if(second != i && second * 50 >= n) {
                result += second * 11;
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