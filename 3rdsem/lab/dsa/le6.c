#include <stdio.h>
#include <stdlib.h>
#define max 5

void insert(int);
int delete();
void display();

int a[max], front = 0, rear = -1;

int main()
{
    int choice;
    do
    {
        printf("\nenter your choice:\n1.insert\n2.delete\n3.display\n4.exit\n:");
        scanf("%d", &choice);
        switch (choice)
        {
        case 1:
            printf("enter the element:");
            int element;
            scanf("%d", &element);
            insert(element);
            break;
        case 2:
            printf("the element which was poped was:%d", delete ());
            break;
        case 3:
            display();
            break;
        case 4:
            exit(0);

        default:
            printf("something went wrong");
            break;
        }
    } while (1);
}

void insert(int element)
{
    if (rear == max)
    {
        printf("overflow");
    }
    else {
        a[++rear] = element;
    }
}

int delete()
{
    if (rear == -1)
    {
        printf("underflow");
    }
    else{
        return a[front++];
    }
    
}

void display()
{
    printf("the elements of the stack are:");
    if (rear != front)
    {
        for (int z = front; z <= rear; z++)
        {
            printf("\n|%d|", a[z]);
        }
    }
}
