int solution(vector<int> a) {
    map<int, int> mp = {};
    for (int temp : a) {
        mp[temp]++;
        if (mp[temp] == 2) return temp;
    }
    return -1;
}
