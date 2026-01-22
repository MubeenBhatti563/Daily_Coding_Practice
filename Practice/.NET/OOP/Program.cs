// See https://aka.ms/new-console-template for more information
using System;
using System.Collections;
using System.Collections.Generic;

namespace Program
{
    internal class Program
    {
        static void Main(string[] args)
        {
            /*
            Rectangle r1 = new Rectangle(10, 10);
            r1.Formula();
            Animal a1 = new Pig("Piggy");
            a1.animalSound();
            Animal[] a2 = { new Pig("Piggy1"), new Pig("Piggy2"), new Pig("Piggy3") };
            foreach (Animal a in a2)
            {
                a.animalSound();
            } */
            // IElectronicDevice TV = TVRemote.GetDevice();
            // PowerButton powBut = new PowerButton(TV);
            // powBut.Execuate();
            // powBut.Undo();
            // powBut.Execuate();
            // powBut.Undo();
            #region ArrayList Code
            ArrayList aList = new ArrayList();
            aList.Add("Mubeen");
            aList.Add(21);
            // Console.WriteLine("Count: {0}", aList.Count);
            // Console.WriteLine("Capacity: {0}", aList.Capacity);

            ArrayList bList = new ArrayList();
            bList.AddRange(new object[] { "Husnain", "Usman", "Mubeen" });

            aList.AddRange(bList);
            aList.Insert(0, "Waqas Ahamd");
            bList.Sort();
            aList.RemoveAt(2);
            aList.Reverse();
            // Converting ArrayList to Simple Array
            string[] myArray = (string[])aList.ToArray(typeof(string));
            // Converting Array to ArrayList
            string[] customers = { "Bob", "John", "Tayler" };
            ArrayList custArray = new ArrayList();
            custArray.AddRange(customers);
            #endregion

            #region Dictionary
            Dictionary<string, string> superheroes = new Dictionary<string, string>();
            superheroes.Add("Beauty", "Mubeen");
            superheroes.Add("Benay", "M Mubeen");
            superheroes.Add("Clark Kent", "Superman");

            superheroes.Remove("Benay");
            // Console.WriteLine("Clark Kent : {0}", superheroes.ContainsKey("Clark Kent"));
            // superheroes.TryGetValue("Beauty", out string test);
            // Console.WriteLine($"Beauty: {test}");
            // foreach (KeyValuePair<string, string> item in superheroes)
            // {
            //     Console.WriteLine("{0} : {1}", item.Key, item.Value);
            // }
            #endregion
            #region Queue
            Queue q1 = new Queue();
            q1.Enqueue(1);
            q1.Enqueue(2);
            q1.Enqueue(3);
            // Console.WriteLine("1 in Queue : {0}", q1.Contains(1));
            // Console.WriteLine("Remove : {0}", q1.Dequeue());
            // Console.WriteLine("Peek in Queue : {0}", q1.Peek());

            object?[] numArray = q1.ToArray();
            // Console.WriteLine(String.Join(",", numArray));
            #endregion
            #region Generics
            List<Animal1> animalList = new List<Animal1>();
            List<int> numList = new List<int>();
            numList.Add(24);

            animalList.Add(new Animal1() { Name = "Doggy" });
            animalList.Add(new Animal1() { Name = "Paul" });
            animalList.Add(new Animal1() { Name = "Tommy" });

            animalList.Insert(1, new Animal1() { Name = "Steve" });
            animalList.RemoveAt(1);
            Console.WriteLine("No of Animals {0}", animalList.Count);
            foreach (Animal1 a in animalList)
            {
                Console.WriteLine(a.Name);
            }
            #endregion
        }
    }

    public class Animal1
    {
        public string Name { get; set; }
        public Animal1(string name = "No Name") { Name = name; }
        public static void GetSum<T>(ref T num1, ref T num2)
        {
            double dbX = Convert.ToDouble(num1);
            double dbY = Convert.ToDouble(num2);
            Console.WriteLine($"{dbX} + {dbY} = {dbX + dbY}");
        }
    }
    public class Rectangle
    {
        private int width { get; set; }
        private int length { get; set; }
        public Rectangle(int w, int l)
        {
            this.width = w;
            this.length = l;
        }
        public void Formula()
        {
            if (this.width == this.length)
            {
                Console.WriteLine("The Area of Square is {0}", this.width * this.length);
            }
            else
            {
                Console.WriteLine("The Area of Rectangle is {0}", this.width * this.length);
            }
        }
    }
    abstract class Animal
    {
        public static int inst = 0;
        protected string name;
        public Animal(string name)
        {
            this.name = name;
            Console.WriteLine("The animal name is {0}", this.name);
            inst += 1;
        }
        public abstract void animalSound();
        public void sleep()
        {
            Console.WriteLine("Zzz");
        }
    }
    class Pig : Animal
    {
        public Pig(string name) : base(name)
        {
            Console.WriteLine("This is child constructor! {0}", inst);
        }
        public override void animalSound()
        {
            Console.WriteLine("The {0} says: wee wee", this.name);
        }
    }
    interface IElectronicDevice
    {
        void On();
        void Off();
        void VolumeUp();
        void VolumeDown();
    }
    class Television : IElectronicDevice
    {
        public int volume { get; set; }
        public void Off()
        {
            Console.WriteLine("The TV is Off!");
        }

        public void On()
        {
            Console.WriteLine("The TV is On!");
        }

        public void VolumeDown()
        {
            if (volume != 0) volume--;
            Console.WriteLine("The TV volume is at {0}", volume);
        }

        public void VolumeUp()
        {
            if (volume != 100) volume++;
            Console.WriteLine("The TV volume is at {0}", volume);
        }
    }
    class TVRemote
    {
        public static IElectronicDevice GetDevice()
        {
            return new Television();
        }
    }
    interface ICommand
    {
        void Execuate();
        void Undo();
    }
    class PowerButton : ICommand
    {
        IElectronicDevice device;
        public PowerButton(IElectronicDevice device)
        {
            this.device = device;
        }
        public void Execuate()
        {
            device.On();
        }

        public void Undo()
        {
            device.Off();
        }
    }
}