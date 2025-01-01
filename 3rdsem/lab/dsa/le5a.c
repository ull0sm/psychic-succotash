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

void initailize()
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
        exit(0);
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

int evaluatepostfix(char *expression)
{
    int i = 0;
    char ch;
    int op1, op2, res;
    while (expression[i] != '\0')
    {
        ch = expression[i];
        if (isdigit(ch))
        {
            push(ch - '0');
        }
        else
        {
            op2 = pop();
            op1 = pop();

            switch (ch)
            {
            case '+':
                res = op1 + op2;
                break;
            case '-':
                res = op1 - op2;
                break;
            case '*':
                res = op1 * op2;
                break;
            case '/':
                res = op1 / op2;
                break;
            case '%':
                res = op1 % op2;
                break;
            case '^':
                res = pow(op1,op2);
                break;

            default:
                printf("invalid operator!!!");
                exit(-1);
            }
            push(res);
        }
    }
}