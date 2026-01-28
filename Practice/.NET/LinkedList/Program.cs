using System;

namespace Program
{
    public class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello, World");
            SinglyLinkedList<int> list = new SinglyLinkedList<int>();
            list.AddFirst(10);
            list.Print();
        }
    }
    public class Node<T>
    {
        public T? Data { get; set; }
        public Node<T>? Next { get; set; }
        public Node(T data)
        {
            Data = data;
            Next = null;
        }
    }
    public class SinglyLinkedList<T>
    {
        public Node<T>? Head { get; set; }
        public void AddFirst(T data)
        {
            Node<T> newNode = new Node<T>(data);
            newNode.Next = Head;
            Head = newNode;
        }
        // --- DELETING ELEMENTS ---
        public void Delete(T val)
        {
            if (Head == null) return;
            if (Head?.Data?.Equals(val) ?? false)
            {
                Head = Head.Next;
                return;
            }
            Node<T>? current = Head;
            while (current?.Next != null)
            {
                if (current?.Next?.Data?.Equals(val) ?? false)
                {
                    current.Next = current.Next.Next;
                    return;
                }
                current = current?.Next;
            }
        }
        // --- DISPLAY LIST ---
        public void Print()
        {
            Node<T>? current = Head;
            while (current != null)
            {
                Console.Write($"{current.Data} -> ");
                current = current.Next;
            }
            Console.WriteLine("null");
        }
    }
}