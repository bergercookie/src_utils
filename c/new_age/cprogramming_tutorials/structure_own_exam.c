#include <stdio.h>
#include <stdbool.h>

/*This example is a brief introduction to the basic usage of a struct in C.*/

// DECLARATION OF STRUCT
struct Person {
    /* data */
    int age;
    char *hair_c;
    const char *Name, *Surname;
    double height_m;
};

// MAIN ROUTINE
int main(int argc, const char *argv[])
{
    char *STR1 = "Red";
    const char *STR2 = "Patrick";
    const char *STR3 = "Henry";

    // CLASSIC STRUCT
    struct Person prs1;

    prs1.age = 21;
    prs1.hair_c = STR1;
    prs1.Name = STR2;
    prs1.Surname = STR3;
    prs1.height_m = 1.85;

    printf("For the created person, the following fields exist:\n");
    printf("Name = %s, Surname = %s\n", prs1.Name, prs1.Surname);
    printf("Age = %d\n", prs1.age);
    printf("Height = %g\n", prs1.height_m);


    // POINTER STRUCT
    printf("==================\n");
    struct Person *pointer_prs;
    pointer_prs->age = 45;
    pointer_prs->hair_c = "kalimera";
    pointer_prs->Name = "Kalinuxta";
    pointer_prs->Surname = "Kalo Mesimeri";
    pointer_prs->height_m = 1.50;

    printf("For the created person, the following fields exist:\n");
    printf("Name = %s, Surname = %s\n", pointer_prs->Name, pointer_prs->Surname);
    printf("Age = %d\n", pointer_prs->age);
    printf("Height = %g\n", pointer_prs->height_m);

    printf("-----------------\n\nExiting..\n");
    return 0;
}
