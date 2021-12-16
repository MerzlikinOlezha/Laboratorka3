using System;

namespace ConsoleApplication6
{
    class Program
    {
        static void Main(string[] args)
        {
            Random rand = new Random();
            int[,] matrix = new int[9, 9];

            for (int i = 0; i < 9; i++) // эти циклы для заполнения массива
                for (int j = 0; j < 9; j++)
                    matrix[i, j] = rand.Next(10, 100); //заполняем массив числами от 10 до 99 (100 не включается)

            for (int i = 0; i < 9; i++) // цикл для вывода матрицы
            {
                for (int j = 0; j < 9; j++)
                {
                    if (i - j <= 0 && j + i < 9 && i < 5) // условие, чтобы откинуть элемент, попадающий в верхний треугольник
                        Console.Write("   ");
                    else if (j + i > 7 && j <= i && i >= 5) // условие, чтобы откинуть элемент, попадающий в нижний треугольник
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
