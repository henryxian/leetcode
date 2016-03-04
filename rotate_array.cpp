// Rotate Array

#include <stdlib.h>
#include <stdio.h>

void rotate(int nums[], int n, int k){
	int i;
	int temp;

	// attention
	if (k > n){
		k = k % n;
	}

	for (i = 0; i < (n / 2); ++i)
	{
		temp = nums[i];
		nums[i] = nums[n - i - 1];
		nums[n - i - 1] = temp;
	}

	// consider the edge situation
	for (i = 0; i < ((k ) / 2); i++){
		temp = nums[i];
		nums[i] = nums[k - i - 1];
		nums[k - i - 1] = temp;
	}

	//consider the edge situation
	for (i = k; i < ((k + n ) / 2); ++i)
	{
		temp = nums[i];
		nums[i] = nums[n - i - 1 + k];
		nums[n - i - 1 + k] = temp;
	}
}

int main(int argc, char const *argv[])
{
	int i;
	int a[] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
	int b[] = {1, 1, 1, 1, 2, 3, 3, 3, 3};
	int c[] = {1, 2, 3, 4, 5, 6, 7};
	int d[] = {2, 2, 1, 1};
	int e[] = {1, 2, 3, 4, 5, 6};

	rotate(a, 9, 2);
	rotate(c, 7, 3);
	rotate(d, 4, 2);
	rotate(e, 6, 3);
	// for (i = 0; i < 9; ++i)
	// {
	// 	printf("%d\t", a[i]);
	// }

	// for (i = 0; i < 7; ++i){
	// 	printf("%d\t", c[i]);
	// }

	for (i = 0; i < 6; i++){
		printf("%d\t", e[i]);
	}

	// for (i = 0; i < 4; ++i)
	// {
	// 	printf("%d\n", d[i]);
	// }
	return 0;
}