// See https://aka.ms/new-console-template for more information
using System;

public interface IClean
{
    void Clean();
}
public class Pool: IClean
{
    public int cholorinLevel;
    public int waterLevel;
    public Pool(int chlorin, int water)
    {
        cholorinLevel = chlorin;
        waterLevel = water;
    }
    public void PoolInfo()
    {
        Console.WriteLine($"Pool: {cholorinLevel} {waterLevel}");
    }
    public virtual void Clean()
    {
        Console.WriteLine("Cleaning pool water...");
    }
}

public class Spa : Pool
{
    public int heatLevel;
    public Spa(int chlorin, int water, int heat) : base(chlorin, water)
    {
        heatLevel = heat;
    }
    public void SpaInfo()
    {
        Console.WriteLine($"Spa: {cholorinLevel} {waterLevel} {heatLevel}");
    }
    public override void Clean()
    {
        Console.WriteLine("Cleaning spa water with heat system...");
    }
}

public class Database
{
    private static Database instance;
    private static readonly object lockObject = new object();

    // Private constructor prevents instantiation from other classes
    private Database() { }

    public static Database GetInstance()
    {
        if (instance == null)
        {
            lock (lockObject)
            {
                if (instance == null)
                {
                    instance = new Database();
                }
            }
        }
        return instance;
    }

    public void Connect()
    {
        Console.WriteLine("Database connected.");
    }
}

// Target interface
public interface ITarget
{
    void Request();
}

// Adaptee class
public class Adaptee
{
    public void SpecificRequest()
    {
        Console.WriteLine("Specific request is called.");
    }
}

// Adapter class
public class Adapter : ITarget
{
    private Adaptee adaptee;

    public Adapter(Adaptee adaptee)
    {
        this.adaptee = adaptee;
    }

    public void Request()
    {
        // Convert the interface of Adaptee to the Target interface
        adaptee.SpecificRequest();
    }
}

public class OOP1
{
    public static void Main(string[] args)
    {
        Spa s1 = new Spa(10, 30, 31);
        Pool p1 = new Pool(21, 34);
        Pool p2 = new Spa(21, 40 ,12);
        Database db1 = Database.GetInstance();
        Database db2 = Database.GetInstance();

        db1.Connect();
        Console.WriteLine(object.ReferenceEquals(db1, db2)); // Outputs: True
        
        Adaptee adaptee = new Adaptee();
        ITarget target = new Adapter(adaptee);

        target.Request(); // Outputs: Specific request is called.
    }
}