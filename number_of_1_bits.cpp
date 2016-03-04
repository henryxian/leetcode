// 191. Number of 1 Bits

#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>

uint32_t reverseBits(uint32_t n){
	uint32_t mask_f = 0x00000001;
	uint32_t mask_b = 0x80000000;
	uint32_t result = 0x00000000;

	int i;
	for(i = 0; i < 32; i++){
		if (1 == (mask_f & (n >> i)))
		{
			result |= mask_b;
		}
		mask_b >>= 1;
	}

	return result;
}

int main(int argc, char const *argv[])
{
	printf("%ud\n", reverseBits(43261596));
	printf("%ud\n", reverseBits(0x00000001));
	printf("%d\n", 0x00000000 | 0x00000001);
	printf("%d\n", 0x00000001 >> 1);
	// printf("%ud\n", 0x00000000 | 0x8000000);
	return 0;
}