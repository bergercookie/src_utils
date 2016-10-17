#include <stdio.h>
#include <stdbool.h>
#include "stdlib.h"
#include <math.h>
#include <errno.h>        /* errno */
#include <string.h>       /* strerror */

bool is_prime(unsigned long num) {

    int i;
    bool it_is = true;

    for (i = 2; i <= num/2; i++) {
        if (num % i == 0) {
            it_is = false;
        }
    }
    return it_is;
}

void print_result(unsigned long long result) {

    printf("\n");
    printf("============================\n");
    printf("---- RESULT COMPUTED -------\n");
    printf("Result = %llu\n", result);
    printf("============================\n");
    printf("Exiting... \n");
    fflush(stdout);

    return;
}

bool is_palindrome(unsigned long num) {

    /*ndigits = floor (log10 (abs (num))) + 1;*/

    int reverse = 0, temp;
    bool it_is;

    temp = num;
    while (temp != 0)
    {
        reverse = reverse * 10;
        reverse = reverse + temp%10;
        temp    = temp/10;
    }

    if (reverse == num) {
        it_is = true;
    }
    else {
        it_is = false;
    }
    return it_is;
}

int sumOsq(unsigned long low, unsigned long high) {

    int sum = 0;
    for (int i=low; i<= high; i++) {
        sum += pow(i, 2);

    }
    return sum;
}

int sqOsum(unsigned  long low, unsigned long high) {
    int sum, i;

    sum = 0;
    for (i=low; i<= high; i++) {
        sum += i;
    }
    return pow(sum, 2);
}

int c2d(char c) {
    return c - '0';
}

bool is_prime2(unsigned long long *nums_ar, size_t nums_ar_l, unsigned long long num) {

    bool it_is=false;

    if (nums_ar_l < num) {
        printf("Please specify a valid number (smaller than %lu)\n", nums_ar_l);
        exit(EXIT_FAILURE);
    }

    // valid input is further assumed
    if (nums_ar[num] == 1) {
        it_is = true;
    }

    return it_is;
}
    
void init_array(unsigned long long *arr, size_t length, int value) {
    for (int i = 0; i< length; i++) {
        arr[i] = value;
    }
    return;
}

void primes_sieve(unsigned long long *arr, size_t length) {
    
    // zero, one are not considered as primes
    arr[0] = 0; 
    arr[1] = 0;

    for (unsigned long long i=2; i < length; i++) {
        for (unsigned long long j=2*i; j < length; j+=i) {
            arr[j] = 0;
        }
    }
    return;
}
