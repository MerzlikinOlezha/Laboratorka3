using System;

namespace ConsoleApplication6
{
    class Program
    {
        static void Main(string[] args)
        {
            Random rand = new Random();
            int[,] matrix = new int[9, 9];

            for (int i = 0; i < 9; i++)
                for (int j = 0; j < 9; j++)
                    matrix[i, j] = rand.Next(10, 100);

            for (int i = 0; i < 9; i++)
            {
                for (int j = 0; j < 9; j++)
                {
                    if (i - j <= 0 && j + i < 9 && i < 5)
                        Console.Write("   ");
                    else if (j + i > 7 && j <= i && i >= 5)
                        Console.Write("   ");
                    else
                        Console.Write(matrix[i, j] + " ");
                }
                Console.WriteLine();
            }
            Console.ReadKey();
        }
    }
}
