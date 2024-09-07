using System;
using System.IO;
using System.Runtime.InteropServices;

namespace Program
{
    class lab_1
    {
        static void Main()
        {
            int Num1;
            int Num2;

            //Домашнее Задание

            //Задание 1
            Console.WriteLine("Введите Число:"); 
            Num1 = Convert.ToInt32(Console.ReadLine());
            for (int i = 1;i < Num1+1;i++)
            {
                Console.WriteLine(i);
            }

            
            
            Console.WriteLine("============================================================================================="); //Отступ
            

            //Задание 2
            Console.WriteLine("Введите Первое Число:"); 
            Num1 = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Введите Второе Число:");
            Num2 = Convert.ToInt32(Console.ReadLine());

            if (Num1 >= Num2)
            {
                Console.WriteLine(Num1);
            }
            else
            {
                Console.WriteLine("Большее: "+Num2);
            }
        }
    }
}
