class Solution {
public:
    void reverseString(vector<char>& s);
};
/*********************************************************************/
void Solution::reverseString(vector<char>& s) {
    int size = s.size(), left, right;
    char aux;
    for (left = 0, right = size-1; left < right; ++left, --right) {
        aux = s[left];
        s[left] = s[right];
        s[right] = aux;
    }
    
}
/*********************************************************************/