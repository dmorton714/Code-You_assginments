// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");

// Assigning values to variables A and B
double A = 40;
int B = 60;

// Adding variables A and B together
Double sum = A + B;

// Printing the result
Console.WriteLine("The sum of A and B is: " + sum);

//if (A > B)
//{
//    Console.WriteLine("A is greater than B");
//}

//if (B > A)
//{
//    Console.WriteLine("B is greater than A");
//}

if (A > B)
{
    Console.WriteLine("A is greater than B");
}
else if (A == B)
{
    Console.WriteLine("A is equal to B");
}
else
{
    Console.WriteLine("B is greater than A");
}