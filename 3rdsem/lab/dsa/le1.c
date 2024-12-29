#include<stdio.h>
#include<stdlib.h>
#define max 3
typedef struct{
    char *name;
    int date;
    char *activity;
}Day;

Day* calendar[max];

void create(){
    for (int i = 0; i < max; i++)
    {
        calendar[i] = (Day*) malloc(sizeof(Day));
        calendar[i]->name = (char*) malloc(20*sizeof(char));
        calendar[i]->activity = (char*) malloc(100*sizeof(char));
    }
}
void read(){
    printf("\nenter the details");
    for (int i = 0; i < max; i++)
    {
        printf("\nenter the day:");
        scanf("%s",calendar[i]->name);
        printf("\nenter the date:");
        scanf("%d",&calendar[i]->date);
        printf("\nenter the activity:");
        scanf("%s",calendar[i]->activity);
    }
}
void display(){
    for (int i = 0; i < max; i++)
    {
        printf("Day:%s\t\tDate:%d\t\tActivity:%s\n",calendar[i]->name,calendar[i]->date,calendar[i]->activity);
    }
}
void main(){
    printf("creating the caledar..........\n");
    create();
    printf("\nreading the data...........\n");
    read();
    printf("\ndisplaying the schedule............\n");
    display();
}