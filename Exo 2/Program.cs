int somme = 0;
int temp;
int a = 0;
int b = 1;
while (somme < 4000000)
{
    temp = b;
    b = a + b;
    a = temp;
    if (b % 2 == 0)
    {
        somme += b;
        Console.WriteLine(somme);
    }
}




