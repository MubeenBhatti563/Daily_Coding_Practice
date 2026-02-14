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
            list.AddFirst(20);
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
    public class ListNode
    {
        public int val;
        public ListNode next;
        public ListNode(int val = 0, ListNode next = null)
        {
            this.val = val;
            this.next = next;
        }
    }
    public class Solution
    {
        public ListNode? Head { get; set; }
        public ListNode AddTwoNumbers(ListNode l1, ListNode l2)
        {
            ListNode newList = new ListNode(0);
            ListNode current = newList;
            int carry = 0;
            while (l1 != null || l2 != null || carry != 0)
            {
                int val1 = (l1 != null) ? l1.val : 0;
                int val2 = (l2 != null) ? l2.val : 0;
                int sum = val1 + val2 + carry;
                carry = sum / 10;
                current.next = new ListNode(sum % 10);
                current = current.next;
                if (l1 != null) l1 = l1.next;
                if (l2 != null) l2 = l2.next;
            }
            return newList;
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
        public void Swap()
        {
            if (Head == null || Head.Next == null)
            {
                Console.WriteLine("Value can't be swapped");
                return;
            }
            Node<T>? first = Head;
            Node<T>? second = Head.Next;
            first.Next = second.Next;
            second.Next = first;
            Head = second;
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
    public class NodeDLL<T>
    {
        public T? Data { get; set; }
        public NodeDLL<T>? Next { get; set; }
        public NodeDLL<T>? Prev { get; set; }
        public NodeDLL(T data)
        {
            Data = data;
            Next = null;
            Prev = null;
        }
    }
    public class DoublyLinkedList<T>
    {
        public NodeDLL<T>? Head { get; set; }
        public NodeDLL<T>? Tail { get; set; }
        public void AddFirst(T data)
        {
            NodeDLL<T> newNode = new NodeDLL<T>(data);
            if (Head == null)
            {
                Head = Tail = newNode;
            }
            else
            {
                newNode.Next = Head;
                Head.Prev = newNode;
                Head = newNode;
            }
        }
        public void AddLast(T data)
        {
            NodeDLL<T> newNode = new NodeDLL<T>(data);
            if (Tail == null)
            {
                Head = Tail = newNode;
            }
            else
            {
                Tail.Next = newNode;
                newNode.Prev = Tail;
                Tail = newNode;
            }
        }
        public void Delete(T val)
        {
            if (Head == null)
            {
                Console.WriteLine("LinkedList is empty!");
                return;
            }
            NodeDLL<T>? current = Head;
            while (current != null)
            {
                if (current.Data?.Equals(val) ?? false)
                {
                    if (current == Head)
                    {
                        Head = Head?.Next;
                        if (Head != null) Head.Prev = null;
                        else Tail = null;
                    }
                    else if (current == Tail)
                    {
                        Tail = Tail.Prev;
                        if (Tail != null) Tail.Next = null;
                    }
                    else
                    {
                        current.Prev!.Next = current.Next;
                        current.Next!.Prev = current.Prev;
                    }
                    return;
                }
                current = current?.Next;
            }
        }
        public void PrintForward()
        {
            NodeDLL<T>? current = Head;
            Console.Write("Head <-> ");
            while (current != null)
            {
                Console.Write($"{current.Data} <-> ");
                current = current.Next;
            }
            Console.WriteLine("null");
        }

        // 5. Print Backward (The DLL Superpower!)
        public void PrintBackward()
        {
            NodeDLL<T>? current = Tail;
            Console.Write("Tail <-> ");
            while (current != null)
            {
                Console.Write($"{current.Data} <-> ");
                current = current.Prev;
            }
            Console.WriteLine("null");
        }
    }
    public class CircularLinkedList<T>
    {
        public Node<T>? Head { get; set; }
        public Node<T>? Tail { get; set; }
        public void AddFirst(T data)
        {
            Node<T> newNode = new Node<T>(data);
            if (Head == null)
            {
                Head = newNode;
                Tail = newNode;
                newNode.Next = Head;
            }
            else
            {
                Tail!.Next = newNode;
                newNode.Next = Head;
                Tail = newNode;
            }
        }
        public void Print()
        {
            Node<T>? current = Head;
            if (Head == null)
            {
                Console.WriteLine("List is empty.");
                return;
            }
            Console.Write("Start -> ");
            do
            {
                Console.Write($"{current!.Data} -> ");
                current = current.Next;
            } while (current != Head);
            Console.WriteLine("(Back to Start)");
        }
    }
}