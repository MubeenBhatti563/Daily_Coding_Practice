
// See https://aka.ms/new-console-template for more information
using System;

namespace Program
{
    public class Stack
    {
        private string exp { get; set; }
        private char[] stk { get; set; }       // char[] instead of string[]
        private char ch { get; set; }
        private int top { get; set; }

        public Stack()
        {
            this.top = -1;
            this.stk = new char[200]; // increase capacity; set to 15 if you want
        }

        public void Input()
        {
            Console.Write("Enter expression without space: ");
            this.exp = (Console.ReadLine() ?? string.Empty);
        }

        // Pushes the current 'ch' onto the stack
        public void Push()
        {
            if (top >= stk.Length - 1)
            {
                throw new InvalidOperationException("Stack overflow");
            }
            stk[++top] = ch;
        }

        // Pops based on the current 'ch'
        // - If ch == ')': pop until '(' and print operators
        // - If ch is operator: pop while top has higher precedence or equal precedence (left associative)
        public void Pop()
        {
            if (top == -1) return;

            if (ch == ')')
            {
                // Pop until '('
                while (top != -1 && stk[top] != '(')
                {
                    Console.Write($"{stk[top]}");
                    top--;
                }
                // Discard '(' if present
                if (top != -1 && stk[top] == '(')
                    top--;
                return;
            }

            // If current token is an operator, pop according to precedence/associativity
            if (IsOperator(ch))
            {
                while (top != -1 && stk[top] != '(')
                {
                    char topOp = stk[top];
                    if (!IsOperator(topOp)) break;

                    int pTop = Prec(topOp);
                    int pCur = Prec(ch);

                    // Pop while top has higher precedence,
                    // or equal precedence and current operator is left-associative
                    if (pTop > pCur || (pTop == pCur && !IsRightAssoc(ch)))
                    {
                        Console.Write($"{stk[top]}");
                        top--;
                    }
                    else
                    {
                        break;
                    }
                }
            }
        }

        // Converts and prints postfix with tabs
        public void Scan()
        {
            if (string.IsNullOrEmpty(exp))
            {
                Console.WriteLine("No input provided.");
                return;
            }

            foreach (char c in exp)
            {
                if (char.IsWhiteSpace(c)) continue;

                ch = c;

                if (char.IsLetterOrDigit(ch))
                {
                    // Operand: print directly
                    Console.Write($"{ch}");
                }
                else if (ch == '(')
                {
                    Push();
                }
                else if (ch == ')')
                {
                    Pop(); // will pop until '('
                }
                else if (IsOperator(ch))
                {
                    if (top == -1 || stk[top] == '(')
                    {
                        Push();
                    }
                    else
                    {
                        Pop();   // pop while higher/equal precedence on stack
                        Push();  // then push current operator
                    }
                }
                else
                {
                    // Unsupported character
                    Console.WriteLine($"\nWarning: Ignoring unsupported token '{ch}'");
                }
            }

            // Flush remaining operators
            FlushRemaining();
            Console.WriteLine(); // end line
        }

        // === Helpers ===

        private static bool IsOperator(char c) => c == '+' || c == '-' || c == '*' || c == '/' || c == '%' || c == '^';

        private static int Prec(char op) => op switch
        {
            '+' or '-' => 1,
            '*' or '/' or '%' => 2,
            '^' => 3,
            _ => -1
        };

        private static bool IsRightAssoc(char op) => op == '^';

        // Pop the rest of the stack and print
        private void FlushRemaining()
        {
            while (top != -1)
            {
                if (stk[top] == '(' || stk[top] == ')')
                {
                    // Mismatched parentheses; discard
                    top--;
                    continue;
                }
                Console.Write($"{stk[top]}");
                top--;
            }
        }
    }

    public class Program
    {
        public static void Main(string[] args)
        {
            Stack s1 = new Stack();
            s1.Input();
            s1.Scan();
        }
    }
}
