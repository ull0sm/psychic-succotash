#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <stdlib.h>

void printupper()
{
    for (char ch = 'A'; ch <= 'Z'; ch++)
    {
        printf("%c\t", ch);
    }
    printf("\n");
}

void printlower()
{
    for (char ch = 'a'; ch <= 'z'; ch++)
    {
        printf("%c\t", ch);
    }
    printf("\n");
}

int main()
{
    pid_t child = fork();

    if (child < 0)
    {
        printf("fork failed\nchild process was not created");
    }
    else if (child == 0)
    {
        printlower();
    }
    else
    {
        usleep(5000000);
        printupper();
    }

    return 0;
}