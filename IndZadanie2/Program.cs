using System;

namespace ConsoleApplication6
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] arr = new int[100];
            Random r = new Random();
            int firstHalf = 0;
            int secondHalf = 0;

            for (int i = 0; i < arr.Length; i++)
                arr[i] = r.Next(-50, 50);

            for (int i = 0; i < arr.Length; i++)
            {
                if (i < arr.Length / 2)
                    if (arr[i] < 0)
                        firstHalf++;

                if (i > arr.Length / 2)
                    if (arr[i] < 0)
                        secondHalf++;
            }

            if (firstHalf > secondHalf)
                Console.WriteLine("1");

            if (firstHalf < secondHalf)
                Console.WriteLine("2");

            if (firstHalf == secondHalf)
                Console.WriteLine("0");

            Console.ReadKey();

        }
    }
}