#include <stdio.h>
#include <string.h>

#define MAXLEN 1000

/* Struct Definitions */
struct package_struct { //bit field specifications!! 
    unsigned int f1:2;
    unsigned int f2:1;
    unsigned int f3:1;
    unsigned int f4:1;
    unsigned int four_bit:4;
    unsigned int another:9;
};
struct book {
    char title[MAXLEN];
    char author[MAXLEN];
    char about[MAXLEN];
    int year;
};

void print_book(struct book *my_book) {
    printf("***Printing book contents***\n");
    printf("Year of the book is %d\n", my_book->year);
    printf("Title of the book is %s\n", my_book->title);
    printf("About of the book is %s\n", my_book->about);
}

int main(int argc, const char *argv[])
{
    struct book first_book, *book_ptr;
    book_ptr = &first_book;


    book_ptr->year = 1949;
    /*my_book.title = &"Marx's own Revolution" WROONNGG!! */
    strcpy(book_ptr->title, "1984");
    strcpy(book_ptr->author, "George Orwell");
    strcpy(book_ptr->about, "This is a great distopia of Goerge Orwell written after the second War.");

    /*print_book(book_ptr);*/

    struct package_struct my_packet, *ptr_packet;
    ptr_packet = &my_packet;

    ptr_packet->f1 = 3; //this is a valid value for f1 as it can hold up to this value;
    printf("f1's contents are the following: %d\n", ptr_packet->f1);

       
    return 0;
}
