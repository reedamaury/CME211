#include <iomanip>
#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>

#include "COO2CSR.hpp"
#include "CGSolver.hpp"
#include "matvecops.hpp"

int main(int argc, char* argv[]){
    
    // ensure appropriate number of command line arguments are provided
    if (argc < 2) {
      std::cout << "Not enough command line arguments" << std::endl;
      return 0;  // exit the program if not enough
    }
    
    // declare matrix file to stream in from
    std::ifstream f; 
    f.open(argv[1]);
    
    if (f.is_open()) { 
        // stream in first line 
        unsigned int row_size;
        unsigned int col_size;
        f >> row_size; 
        f >> col_size;
        
        // declare COO vectors 
        std::vector<double> val;
        std::vector<int> i_idx;
        std::vector<int> j_idx;
        double v; 
        int i, j;
        
        // populate row, column, and corresponding value vectors (COO format)
        while(f >> i >> j >> v) { 
            val.push_back(v);
            i_idx.push_back(i);
            j_idx.push_back(j);
        }
        f.close();
        
        // convert matrix from COO format to CSR format 
        COO2CSR(val,i_idx,j_idx);
        
        
        
        // CGSolver
        
        // construct initial guess vectors
        std::vector<double> b;
        std::vector<double> x;
        for (unsigned int k=0; k<row_size; k++) {
            b.push_back(0);
            x.push_back(1);
        }
        
        // Utilize CGSolver function 
        double tol = 1.e-5; // define tolerance
        int iter = CGSolver(val, i_idx, j_idx, b, x, tol); 
       
        // print solution vector to output file
        std::ofstream fo(argv[2]);
        if (fo.is_open()) {  
            for (unsigned int i=0; i<x.size(); i++) {
                fo << std::scientific << std::setprecision(4) << x[i] << std::endl;
            }
        }
    }
    return 0;
}
