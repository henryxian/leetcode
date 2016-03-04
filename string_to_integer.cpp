// 8. String to Integer (atoi)

class Solution {
public:
    int myAtoi(string str) {
        string::size_type index = 0;
        while (str[index] == ' ' || str[index] == '\t' || str[index] == '\n')
            index++;
        if (index == str.size())
            return 0;
        
        int int_num = 0, tmp = 0;
        if (str == "") {
            return 0;
        }
        int sign = 1;
        if (str[index] == '-' || str[index] == '+') {
            if (str[index] == '-') {
                sign = -1;
            }
            index++;
            while (str[index] <= '9' and str[index] >= '0') {
                tmp = 10 * int_num + (str[index] - 48);
                if (tmp / 10 != int_num) {
                    if (sign == 1)
                        return INT_MAX;
                    else
                        return INT_MIN;
                }
                index++;
                int_num = tmp;
            }
            return int_num * sign;
        }
        else {
            while (str[index] <= '9' and str[index] >= '0') {
                tmp = 10 * int_num + (str[index] - 48);
                if (tmp / 10 != int_num) {
                    if (sign == 1)
                        return INT_MAX;
                    else
                        return INT_MIN;
                }
                index++;
                int_num = tmp;
            }
            return int_num;
            }
        } 
};