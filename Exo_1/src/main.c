#include <stdio.h>


int main()
{
	int somme = 0;

	for (size_t i = 1; i < 1000; i++)
	{
		if(i % 3 == 0 || i % 5 == 0)
		{
			somme += i;
		}
	}
	printf("La somme totale est: %d \n",somme);
	
}