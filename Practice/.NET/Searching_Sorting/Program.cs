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
        // Selection sort for sorting an array
        static void SelectionSort(ref int[] arr)
        {
            for (int i = 0; i < arr.Length; i++)
            {
                for (int j = i + 1; j < arr.Length; j++)
                {
                    if (arr[i] > arr[j])
                    {
                        int temp = arr[i];
                        arr[i] = arr[j];
                        arr[j] = temp;
                    }
                }
            }
        }
        static void InsertionSort(ref int[] arr)
        {
            int i; int j;
            for (i = 0; i < arr.Length; i++)
            {
                int temp = arr[i];
                for (j = i; j > 0 && temp < arr[j - 1]; j--)
                {
                    arr[j] = arr[j - 1];
                }
                arr[j] = temp;
            }
        }
        static void Main(string[] args)
        {
            int[] arr1 = { 9, 2, 6, 3, 5, 7, 1 };
            Console.Write("Enter value to search: ");
            int val = Convert.ToInt32(Console.ReadLine());
            InsertionSort(ref arr1);
            Binary(val, arr1);
        }
    }
}