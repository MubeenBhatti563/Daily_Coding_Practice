using System;

namespace Program
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello, World!");
            BinarySearchTree<int> list = new BinarySearchTree<int>();
            list.Insert(10);
            list.Insert(5);
            list.Insert(7);
            list.Insert(3);
            list.PrintSorted();
        }
    }
    public class TreeNode<T>
    {
        public T? Data { get; set; }
        public TreeNode<T>? Left { get; set; }
        public TreeNode<T>? Right { get; set; }
        public TreeNode(T data)
        {
            Data = data;
            Left = null;
            Right = null;
        }
    }
    public class BinarySearchTree<T>
    {
        public TreeNode<int>? Root { get; set; }
        public void Insert(int val)
        {
            Root = InsertRecursive(Root, val);
        }
        private TreeNode<int> InsertRecursive(TreeNode<int>? root, int val)
        {
            if (root == null)
            {
                return new TreeNode<int>(val);
            }
            if (val < root.Data)
            {
                root.Left = InsertRecursive(root.Left, val);
            }
            else if (val > root.Data)
            {
                root.Right = InsertRecursive(root.Right, val);
            }
            return root;
        }
        public void PrintSorted()
        {
            PrintRecursive(Root);
        }

        private void PrintRecursive(TreeNode<int>? node)
        {
            // THE MOST IMPORTANT LINE: Base Case
            if (node == null) return;

            PrintRecursive(node.Left);
            Console.Write(node.Data + " ");
            PrintRecursive(node.Right);
        }
        public bool SearchIterative(int target)
        {
            TreeNode<int>? current = Root;
            while (current != null)
            {
                if (target == current.Data) return true;
                if (target < current.Data) current = current.Left;
                else current = current.Right;
            }
            return false;
        }
    }
}