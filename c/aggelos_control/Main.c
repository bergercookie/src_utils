// LIBRARIES
#include <stdio.h>
#include <math.h>
#include <stdlib.h>

// DEFINITIONS
#define MAX 10000 // maximum length of array

int main(int argc, const char *argv[])
{
    FILE *ifp, *ofp;
    char *mode = "r";

    // Problem variables
    double dt, t0, t;
    double a, b, c;
    int Nt;
    int i, j;
    double time[MAX], sin_vals[MAX];
    char fname_in[] = "data.txt";
    char fname_out[] = "t_y_values.txt";

    /*char outputFilename[] = "out.list";*/

    // Input file
    ifp = fopen(fname_in, mode);
    if (ifp == NULL) {
          fprintf(stderr, "Can't open input file %s!\n", fname_in);
            exit(1);
    }


    // Output file
    ofp = fopen(fname_out, "w");
    if (ofp == NULL) {
          fprintf(stderr, "Can't open output file %s!\n",fname_out);
            exit(1);
    }

    // Read the first line
    fscanf(ifp, "%d,%lf,%lf\n", &Nt, &t0, &dt);
    
    // Print for verification reasons...
    // Remove it afterwards.. 
    printf("Size of samples: %d\n", Nt);
    printf("Initial Value:\t %.2f [s]\n", t0);
    printf("Step Size:\t %.2f [s]\n", dt);

    // Read the second line
    fscanf(ifp, "%lf\n,%lf\n,%lf\n", &a, &b, &c);

    // Print for verification reasons...
    // Remove it afterwards.. 
    printf("\n");
    printf("Polynomial parameters:\n");
    printf("\t\t a = %.2f\n", a);
    printf("\t\t b = %.2f\n", b);
    printf("\t\t c = %.2f\n", c);

    // Store the series in matrix
    for(i=0; i<Nt; i++) {
        // current time
        t = t0 + dt * i;

        time[i] = t;
        sin_vals[i] = sin(t);
    }

    // Printing the values for verification
    for(i=0; i<Nt; i++) {
        // current time
        fprintf(ofp, "%.2f\t%.2f\n", time[i], sin_vals[i]);
    }



    // Closing files, exiting..
    fclose(ifp);
    fclose(ofp);
    return 0;
}
