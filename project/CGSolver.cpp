#include <iostream>
#include <fstream>
#include <vector>

#include "CGSolver.hpp"
#include "matvecops.hpp"

int CGSolver(const std::vector<double> &val,
            const std::vector<int>     &row_ptr,
            const std::vector<int>     &col_idx,
            const std::vector<double>  &b,
            std::vector<double>        &x,
            const double               tol) {
             
             // declare initial variables 
            std::vector<double> Ax, r0, p0; 
            double L2normr0; 
            
             // initialize initial variables
            Ax = sparse_vector_mult(val,row_ptr,col_idx,x); // A*x
            r0 = vector_sub(b,Ax); // r0 = b-A*x
            L2normr0 = l2norm(r0);
             
             
             // declare variables to be used in while loop 
            double rdot, rdot1, pAp, alpha, L2normr;
            std::vector<double> alphaAp, alphap, beta, betap, Ap; 
            std::vector<std::vector<double> > r, p, xn; 
            r.push_back(r0); 
            p.push_back(r0); // p0 = r0
            xn.push_back(x);
            unsigned int n, nmax; 
            n = 0; 
            nmax = x.size();
             
            while(n < nmax){
                rdot = vector_vector_mult(r[n],r[n]); // rt*r 
                Ap =  sparse_vector_mult(val,row_ptr,col_idx,p[n]); // A*p
                pAp = vector_vector_mult(p[n],Ap); // pt*A*p 
                alpha = rdot/pAp; // alpha = (rt*r)/(pt*A*p)
                alphap = scalar_vector_mult(alpha,p[n]); // alpha*p[n]
                xn.push_back(vector_add(xn[n],alphap)) ; // x[n+1] = x[n] + alpha*p[n]
                alphaAp = scalar_vector_mult(alpha,Ap); // alpha*A*p[n]
                r.push_back(vector_sub(r[n],alphaAp)); // r[n+1] = r[n] - alpha*A*p[n]
                L2normr = l2norm(r[n+1]);
                 
                if (L2normr/L2normr0 < tol) { // check for convergence 
                    std::cout << "SUCCESS: CG solver converged in " << n+1 << " iterations" << std::endl;
                    x = xn[n+1]; // modify reference to initial guess to the new solution 
                    return n+1; 
                    break;
                }
                 
                rdot1 = vector_vector_mult(r[n+1],r[n+1]); // rt[n+1]*r[n+1]
                beta.push_back(rdot1/rdot); // beta = (rt[n+1]*r[n+1])/(rt*r)
                betap = scalar_vector_mult(beta[n],p[n]); // beta[n]*p[n]
                p.push_back(vector_add(r[n+1],betap)); // p[n+1] = r[n+1] + beta[n]*p[n]
                n++;
                }
                
            if (n == nmax) { // if solver did not coverge, notify user
                std::cout << "FAILURE: CG solver did not converge in " << nmax << " iterations" << std::endl;
            }
            return -1;
        }
             
