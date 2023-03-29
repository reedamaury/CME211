#include <vector>
#include <cmath>

#include "matvecops.hpp"

// CSR matrix-vector vector multiplication -- A*u=b 
std::vector<double> sparse_vector_mult(const std::vector<double> &val, // data/values
            const std::vector<int>    &row_ptr,  // row pointer
            const std::vector<int>    &col_idx, // column indices (first three inputs collectively create sparse matrix)
            const std::vector<double> &u) { //vector u

            std::vector<double> b; 
            for (unsigned int i=0; i<u.size(); i++) {
                b.push_back(0.0);
                for (int j=row_ptr[i]; j<row_ptr[i+1]; j++){
                    b[i] += val[j]*u[col_idx[j]];
                }
            }
            return b; 
        }

// vector-vector multiplication (dot product)
double vector_vector_mult(const std::vector<double> &r, const std::vector<double> &p) {
            double a = 0; 
            for(unsigned int i=0;i<r.size();i++){
                a += r.at(i)*p.at(i);
            }
            return a; 
        }

// scalar-vector multiplication
std::vector<double> scalar_vector_mult(const double &a, const std::vector<double> &r) {
            std::vector<double> v; 
            for(unsigned int i=0;i<r.size();i++){
                v.push_back(a*r[i]);
            }
            return v; 
        }

// vector addition 
std::vector<double> vector_add(const std::vector<double> &r, const std::vector<double> &p) {
            std::vector<double> v; 
            for(unsigned int i=0;i<r.size();i++){
                v.push_back(r[i]+p[i]);
            }
            return v; 
        }

// vector subtraction
std::vector<double> vector_sub(const std::vector<double> &r, const std::vector<double> &p) {
            std::vector<double> v; 
            for(unsigned int i=0;i<r.size();i++){
                v.push_back(r[i]-p[i]);
            }
            return v; 
        }

// L2 norm 
double l2norm(const std::vector<double> &r) {
            double a, b; 
            a = 0;
            for(unsigned int i=0;i<r.size();i++){
                a += r[i]*r[i];
            }
            b = sqrt(a);
            return b; 
        }
