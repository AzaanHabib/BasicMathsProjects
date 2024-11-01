#include <iostream>
#include <cmath>


void ODE_calculator(int a, int b, int c, int d) {

    // Eigenvalues
    float z1 = (-(a - d) + sqrt(pow(a - d, 2) - 4 * ((a * d) - (b * c)))) / 2;
    float z2 = (-(a - d) - sqrt(pow(a - d, 2) - 4 * ((a * d) - (b * c)))) / 2;

    // Eigenvectors 
    float f12 = 1;
    float f22 = 1;
    float f11 = b / z1 - a;
    float f21 = b / z2 - a;

    // General solution (unsolved)
    float y1 = exp(z1);
    float y2 = exp(z2);

    // General solution (solved)
    float u11 = y1 * f11;
    float u12 = y2 * f21;
    float u13 = y1;
    float u14 = y2;

    std::cout << "k1(" << u11 << ")t + k2(" << u12 << ")t" << '\n';
    std::cout << "k1(" << u13 << ")t + k2(" << u14 << ")t";

    return;
}


