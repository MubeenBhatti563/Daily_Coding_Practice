// See https://aka.ms/new-console-template for more information

using System;

namespace Program
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello, World!");
            MyQueue q1 = new MyQueue();
            DeQueue dq1 = new DeQueue();
            Console.WriteLine("Enter one of these:");
            // while (true)
            // {
            //     Console.WriteLine("1 => Insert value");
            //     Console.WriteLine("2 => Delete value");
            //     Console.WriteLine("3 => Show values");
            //     Console.WriteLine("4 => Quite the program");
            //     int val = Convert.ToInt32(Console.ReadLine());

            //     if (val == 1)
            //     {
            //         Console.Write("Enter value to insert: ");
            //         int item = Convert.ToInt32(Console.ReadLine());
            //         q1.Insert(item);
            //     }
            //     else if (val == 2)
            //     {
            //         Console.WriteLine("Deleted: " + q1.Del());
            //     }
            //     else if (val == 3)
            //     {
            //         q1.Show();
            //     }
            //     else if (val == 4)
            //     {
            //         break;
            //     }
            //     else
            //     {
            //         Console.WriteLine("Please select one of these!");
            //     }
            // }
            // For Dequeue
            //     while (true)
            //     {
            //         Console.WriteLine("1 => Insert value from Front");
            //         Console.WriteLine("2 => Insert value from Rear");
            //         Console.WriteLine("3 => Delete value from Front");
            //         Console.WriteLine("4 => Delete value from Rear");
            //         Console.WriteLine("5 => Show values");
            //         Console.WriteLine("6 => Quite the program");
            //         int val = Convert.ToInt32(Console.ReadLine());

            //         if (val == 1)
            //         {
            //             Console.Write("Enter value to insert: ");
            //             int item = Convert.ToInt32(Console.ReadLine());
            //             dq1.AddFront(item);
            //         }
            //         else if (val == 2)
            //         {
            //             Console.Write("Enter value to insert: ");
            //             int item = Convert.ToInt32(Console.ReadLine());
            //             dq1.AddRear(item);
            //         }
            //         else if (val == 3)
            //         {
            //             dq1.DelFront();
            //         }
            //         else if (val == 4)
            //         {
            //             dq1.DelRear();
            //         }
            //         else if (val == 5)
            //         {
            //             dq1.Show();
            //         }
            //         else if (val == 6)
            //         {
            //             Console.WriteLine("Thanks for using DeQueue!!!");
            //             Console.WriteLine("Good Bye!\t");
            //             break;
            //         }
            //         else
            //         {
            //             Console.WriteLine("Please select one of these!");
            //             continue;
            //         }
            //     }
            // For Priority Queue
            PriorityQueue pq1 = new PriorityQueue(10);
            pq1.Enqueue(10, 1);
            pq1.Enqueue(20, 2);
            pq1.Enqueue(30, 3);
            pq1.Enqueue(40, 2);
            pq1.Show();
            pq1.Dequeue();
            pq1.Show();
            pq1.Dequeue();
            pq1.Show();
            pq1.Dequeue();
            pq1.Show();
        }
    }
    public class MyQueue
    {
        private int front;
        private int rare;
        private int[] queue;
        public MyQueue()
        {
            this.front = -1;
            this.rare = -1;
            this.queue = new int[10];
        }
        public void Insert(int val)
        {
            if (rare >= queue.Length)
            {
                Console.WriteLine("Queue is full!");
                return;
            }
            else
            {
                queue[++rare] = val;
                if (front == -1) front++;
            }

        }
        public int Del()
        {
            if (front == -1)
            {
                Console.WriteLine("Queue is empty!");
                return 0;
            }
            else if (front == rare)
            {
                front = rare = -1;
                return 0;
            }
            int data = queue[front];
            if (front == rare) front = rare = -1;
            else front++;
            return data;
        }
        public void Show()
        {
            Console.WriteLine("Given Queue is: ");
            for (int val = front; val <= rare; val++)
            {
                Console.Write(queue[val] + "\t");
            }
            Console.WriteLine();
        }
    }
    public class DeQueue
    {
        private int F;
        private int R;
        private int[] DQ;
        private int size;

        public DeQueue(int capacity = 10)
        {
            DQ = new int[capacity];
            F = -1;
            R = -1;
            size = capacity;
        }

        private bool IsFull()
        {
            return (F == 0 && R == size - 1) || (F == R + 1);
        }

        private bool IsEmpty()
        {
            return F == -1;
        }

        public void AddFront(int val)
        {
            if (IsFull())
            {
                Console.WriteLine("DeQueue is full!");
                return;
            }

            if (IsEmpty())
            {
                F = R = 0;
            }
            else if (F == 0)
            {
                F = size - 1;
            }
            else
            {
                F--;
            }

            DQ[F] = val;
        }

        public void AddRear(int val)
        {
            if (IsFull())
            {
                Console.WriteLine("DeQueue is full!");
                return;
            }

            if (IsEmpty())
            {
                F = R = 0;
            }
            else if (R == size - 1)
            {
                R = 0;
            }
            else
            {
                R++;
            }

            DQ[R] = val;
        }

        public void DelFront()
        {
            if (IsEmpty())
            {
                Console.WriteLine("DeQueue is empty!");
                return;
            }

            int val = DQ[F];

            if (F == R)
            {
                F = R = -1;
            }
            else if (F == size - 1)
            {
                F = 0;
            }
            else
            {
                F++;
            }

            Console.WriteLine("Deleted value: " + val);
        }

        public void DelRear()
        {
            if (IsEmpty())
            {
                Console.WriteLine("DeQueue is empty!");
                return;
            }

            int val = DQ[R];

            if (F == R)
            {
                F = R = -1;
            }
            else if (R == 0)
            {
                R = size - 1;
            }
            else
            {
                R--;
            }

            Console.WriteLine("Deleted value: " + val);
        }

        public void Show()
        {
            if (IsEmpty())
            {
                Console.WriteLine("DeQueue is empty!");
                return;
            }

            Console.Write("DeQueue elements: ");
            int i = F;
            while (true)
            {
                Console.Write(DQ[i] + " ");
                if (i == R) break;
                i = (i + 1) % size;
            }
            Console.WriteLine();
        }
    }
    public class PriorityQueue
    {
        private int[] data;
        private int[] priority;
        private int size;
        public PriorityQueue(int capacity)
        {
            this.data = new int[capacity];
            this.priority = new int[capacity];
            this.size = 0;
        }
        public void Enqueue(int val, int pr)
        {
            if (size > data.Length - 1)
            {
                Console.WriteLine("Priority Queue is full!");
                return;
            }
            data[size] = val;
            priority[size] = pr;
            size++;
        }
        public int Dequeue()
        {
            if (size == 0)
            {
                Console.WriteLine("Priority Queue is empty!");
                return -1;
            }
            int highePr = 0;

            for (int i = 1; i < size; i++)
            {
                if (priority[i] > priority[highePr])
                {
                    highePr = i;
                }
            }
            int item = data[highePr];
            for (int i = highePr; i < size - 1; i++)
            {
                data[i] = data[i + 1];
                priority[i] = priority[i + 1];
            }
            size--;
            return item;
        }
        public void Show()
        {
            Console.WriteLine("Value  Priority");
            for (int i = 0; i < size; i++)
            {
                Console.WriteLine($"{data[i]}      {priority[i]}");
            }
        }
    }
}