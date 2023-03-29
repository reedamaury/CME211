#ifndef MATVECOPS_HPP
#define MATVECOPS_HPP

#include <vector>

/* The following functions perform basic matrix-vector 
 * operations to assist the CGSolver in it's computations.
 * Each function assumes the use of standard library vectors,
 * and CSR formatted sparse matrices. The CSR sparse matrix 
 * should be constructed using three standard library vectors:
 * a row pointer vector, a column index vector, and a data vector. 
 */

// CSR matrix-vector multiplication -- A*u=b 
std::vector<double> sparse_vector_mult(const std::vector<double> &val, // data/values
             const std::vector<int>    &row_ptr,  // row pointer
             const std::vector<int>    &col_idx, // column indices (first three inputs collectively create sparse matrix)
             const std::vector<double> &u);  //vector u

// vector-vector multiplication (dot product)
double vector_vector_mult(const std::vector<double> &r,
            const std::vector<double> &p);
            
// scalar-vector multiplication 
std::vector<double> scalar_vector_mult(const double &a, const std::vector<double> &r);

// vector addition 
std::vector<double> vector_add(const std::vector<double> &r, const std::vector<double> &p);

// vector subtraction
std::vector<double> vector_sub(const std::vector<double> &r, const std::vector<double> &p);

// L2 norm 
double l2norm(const std::vector<double> &r);


#endif /* MATVECOPS_HPP */