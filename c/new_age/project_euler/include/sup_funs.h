 /* sup_funs.h is the header file providing the declarations for the
  * suplementary functions used during the projecteuler challenges */


// FUNCTION DECLARATIONS

/* PRINT_RESULT: 
 * The purpose of this function is to print the result needed for each one
 * of the levels in the projecteuler challenges. Used to automate the
 * process of printing  */
void print_result(unsigned long long result);

/* IS_PRIME: 
 * function used to determine wether the inputted number num
 * is a prime or not.  Initially designed for problem 3 of projecteuler
 * series */
bool is_prime(unsigned long num);

/* IS_PALINDROME:
 * The purpose of the function is to determine weather the inputted number
 * is a palindrome. Needed for projecteuler challenge 4. */
bool is_palindrome(unsigned long num);

/* SUMOSQ:
 * Returns the sum of squares from (and including) low to (and
 * including) high.*/
int sumOsq(unsigned long low, unsigned long high);

/* SQOSUM:
 * Returns the square of the sum from (and including) low to (and
 * including) high. */
int sqOsum(unsigned long low, unsigned long high);

/* C2D:
 * Returns the integer representation of a character */
int c2d(char c);

/* IS_PRIME2:
 * The function uses an array to index weather the number inputted (which has
 * to be in range of that array is a prime or not */
bool is_prime2(unsigned long long *nums_ar, size_t nums_ar_l, unsigned long long num);

/* INIT_ARRAY:
 * Initialize all the elements of a given array to a certain value */
void init_array(unsigned long long *arr, size_t length, int value);

/* PRIMES_SIEVE:
 * The function implements the Eratosthenous sieve to gain a list of the prime
 * numbers up to a certain limit (length) */
void primes_sieve(unsigned long long *arr, size_t length);



// MACROS 

//Adapted from K&R, p.135 of edition 2.
#define len(array) (sizeof((array))/sizeof((array)[0]))

