#include <iostream>
#include <queue>
#include <unordered_set>
#include <vector>

struct state {
    int length;
    long long qe;
    int remaining_part;
    unsigned int nums;

    state(const int& length, const long long& qe, const int& remaining_part, const int& nums)
    : length(length), qe(qe), remaining_part(remaining_part), nums(nums)
    {}

    bool operator>(const state& other) const {
        if(length == other.length) {
            if(qe == other.qe) {
                return remaining_part > other.remaining_part;
            }
            return qe > other.qe;
        }
        return length > other.length;
    }
};

long long BFS(int target, const std::vector<int>& all_nums) {
    std::priority_queue<state, std::vector<state>, std::greater<state>> Q;
    std::unordered_set<int> visited;
    Q.push(state(0, 1, target, 0));
    visited.insert(0);
    int N = all_nums.size();

    while(!Q.empty()) {
        state current_state = Q.top();
        Q.pop();

        if(current_state.remaining_part == 0) {
            return current_state.qe;
        }

        for(int i = 0; i < N; ++i) {
            int num = all_nums[i];
            int mask = (1 << i);
            if(num > current_state.remaining_part || (current_state.nums & mask != 0)) {
                continue;
            }
            unsigned int new_nums = current_state.nums | mask;
            if(visited.find(new_nums) == visited.end()) {
                state new_state = state(current_state.length + 1, current_state.qe * num, current_state.remaining_part - num, new_nums);
                visited.insert(new_state.nums);
                Q.push(new_state);
            }
        }
    }

    return -1;
}

int main() {
    std::vector<int> all_nums;
    int num;
    int sum = 0;
    while(std::cin >> num) {
        sum += num;
        all_nums.push_back(num);
    }
    int target = sum / 4;
    long long result = BFS(target, all_nums);
    std::cout << result << "\n";
}