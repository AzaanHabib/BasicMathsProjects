#include <stdio.h>
#include <math.h>

void determinantcalculator(int x1, int x2, int x3, int x4) {

    float det = (x1 * x4) - (x2 * x3);
    printf("%f", det);

    return; 
}

void matrixinverse(float x1, float x2, float x3, float x4) {

    float y = 1 / ((x1 * x4) - (x2 * x3));
    float z1 = x4 / y;
    float z2 = - x3 / y;
    float z3 = - x2 / y;
    float z4 = x1 / y;

    printf("%f", z1);
    printf(" %f\n", z2);
    printf("%f", z3);
    printf(" %f", z4);    

    return;
}

void matrixmultiplier(int x11, int x12, int x13, int x14, int y11, int y12, int y13, int y14) {
    
    int z11 = (x11 * y11) + (x12 * y13);
    int z12 = (x11 * y12) + (x12 * y14); 
    int z13 = (x13 * y11) + (x14 * y13);
    int z14 = (x13 * y12) + (x14 * y14);

    printf("%d", z11); 
    printf(" %d\n", z12);
    printf("%d", z13);
    printf(" %d", z14);

    return;
}

void innerproduct(int x1, int x2, int x3, int y1, int y2, int y3) {

    int z = (x1 * y1) + (x2 * y2) + (x3 * y3);

    printf("%d", z);
    
    return;
}

void crossproduct(int x11, int x12, int x13, int y11, int y12, int y13) {

    int z1 = (x12 * y13) - (x13 * y12);
    int z2 = (x11 * y13) - (x13 * y11);
    int z3 = (x11 * y12) - (x12 * y11);

    printf("%d\n", z1);
    printf("%d\n", z2);
    printf("%d\n", z3);

    return;
}


