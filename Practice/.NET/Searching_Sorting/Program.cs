using System;
using System.Reflection.Metadata;

namespace Program
{
    internal class Program
    {
        static void SequentialSearch(int val, int[] arr)
        {
            int item = -1;
            bool found = false;
            for (int i = 0; i < arr.Length; i++)
            {
                item += 1;
                if (arr[i] == val)
                {
                    Console.WriteLine($"Value {arr[i]} found at index {item}");
                    found = true;
                    break;
                }
            }
            if (!found)
                Console.WriteLine("Value not found!");
        }
        static void Binary(int val, int[] arr)
        {
            int mid; int loc = -1;
            mid = arr.Length / 2;
            if (val == arr[mid])
            {
                Console.WriteLine($"Value {val} found at index {mid}");
                return;
            }
            if (val > arr[mid])
            {
                for (int i = mid + 1; i < arr.Length; i++)
                {
                    if (val == arr[i])
                    {
                        loc++;
                        break;
                    }
                }
            }
            else
            {
                for (int i = mid; i >= 0; i--)
                {
                    if (val == arr[i])
                    {
                        loc++;
                        break;
                    }
                }
            }
            if (loc == -1)
                Console.WriteLine("Value not found");
            else
                Console.WriteLine($"Value {val} found at index {mid}");
        }
        static void Main(string[] args)
        {
            int[] arr1 = { 9, 2, 3, 5, 7, 1 };
            Console.Write("Enter value to search: ");
            int val = Convert.ToInt32(Console.ReadLine());
            Binary(val, arr1);
        }
    }
}