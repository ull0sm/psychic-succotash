#include <stdio.h>
#include <stdlib.h>
#define max 5

void push(int);
int pop();
void display();
void ispalindrome();

int a[max], top = -1;

int main()
{
    int choice;
    do
    {
        printf("\nenter your choice:\n1.push\n2.pop\n3.plaindrome\n4.display\n5.exit\n:");
        scanf("%d", &choice);
        switch (choice)
        {
        case 1:
            printf("enter the element:");
            int element;
            scanf("%d", &element);
            push(element);
            break;
        case 2:
            printf("the element which was poped was:%d", pop());
            break;
        case 3:
            ispalindrome();
            break;
        case 4:
            display();
            break;
        case 5:
            exit(0);

        default:
            printf("something went wrong");
            break;
        }
    } while (1);
}

void push(int element)
{
    if (top == max)
    {
        printf("element cannot be pushed\n");
    }
    else
    {
        top = top + 1;
        a[top] = element;
    }
}

int pop()
{
    int temp;
    if (top == -1)
    {
        return -1;
    }
    temp = a[top];
    top = top - 1;
    return temp;
}

void display()
{
    printf("the elements of the stack are:");
    for (int z = top; z >= 0; z--)
    {
        printf("|%d|\n", a[z]);
    }
}

void ispalindrome()
{
    for (int z = 0; z < top / 2; z++)
    {
        if (a[z] != a[top-z])
        {
            printf("it is not a palindrome");
            break;
        }
        printf("it is a palindrome");
    }
}