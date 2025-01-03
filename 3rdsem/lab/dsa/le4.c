#include <stdio.h>
#include <ctype.h>
#include <math.h>
#include <stdlib.h>

#define max 100

typedef struct
{
    int data[max];
    int top;
} Stack;

Stack s;

void initialize()
{
    s.top = -1;
}

int isFull()
{
    return s.top == max - 1;
}

int isEmpty()
{
    return s.top == -1;
}

void push(int value)
{
    if (isFull())
    {
        printf("stack overflow");
        return;
    }
    s.data[++(s.top)] = value;
}

int pop()
{
    if (isEmpty())
    {
        printf("stack is underflow");
        exit(0);
    }
    return s.data[(s.top)--];
}

int peek()
{
    if (isEmpty())
    {
        printf("stack is underflow");
        exit(0);
    }
    return s.data[s.top];
}

int isoperator(char ch)
{
    return ch == '+' || ch == '-' || ch == '*' || ch == '/' || ch == '^';
}
int precedence(char ch)
{
    if (isoperator(ch))
    {
        switch (ch)
        {
        case '+':
        case '-':
            return 1;
        case '*':
        case '/':
            return 2;
        case '^':
            return 3;
        default:
            return 0;
        }
    }
}

void infixtopostfix(char infix[], char postfix[])
{
    int i = 0, j = 0;
    char ch;
    while (infix[i] != '\0')
    {
        ch = infix[i];

        if (isalnum(ch))
        {
            postfix[j++] = ch;
        }
        else if (ch == '(')
        {
            push(ch);
        }
        else if (ch == ')')
        {
            while (!isEmpty() && peek() != '(')
            {
                postfix[j++] = pop();
            }
            pop();
        }
        else if (isoperator(ch))
        {
            while (!isEmpty() && precedence(peek()) >= precedence(ch))
            {
                postfix[j++] = pop();
            }
            push(ch);
        }
        i++;
    }
    while (!isEmpty())
    {
        postfix[j++] = pop();
    }
    postfix[j] = '\0';
}

int main()
{
    char infix[max], postfix[max];
    printf("enter the infix expression:");
    scanf("%s", infix);

    initialize();
    infixtopostfix(infix, postfix);

    printf("the postfix expression is %s\n", postfix);
    return 0;
}