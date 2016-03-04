// 62. Unique Paths

class Solution {
public:
    int uniquePaths(int m, int n) {
        int path_cnt[m][n];
        if (m <= 0 || n <= 0) {
            return 0;
        }
        if (m == 1 || n == 1) {
            return 1;
        }
        for(int i = 0; i < m; i++) {
            path_cnt[i][0] = 1;
        }
        for (int i = 0; i < n; i++) {
            path_cnt[0][i] = 1;
        }
        path_cnt[0][0] = 0;
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                path_cnt[i][j] = path_cnt[i - 1][j] + path_cnt[i][j - 1];
            }
        }
        /*
        for (int i = 0; i < m; i++) {
            cout << endl;
            for (int j = 0; j < n; j++) {
                cout << path_cnt[i][j] <<'\t';
            }
        }
        */
        return path_cnt[m - 1][n - 1];
    }
};