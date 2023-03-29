#ifndef CGSOLVER_HPP
#define CGSOLVER_HPP

#include <vector>

/* Function that implements the CG algorithm for a linear system
 *
 * Ax = b
 *
 * where A is in CSR format.  The starting guess for the solution
 * is provided in x, and the solver runs a maximum number of iterations
 * equal to the size of the linear system.  Function returns the
 * number of iterations to converge the solution to the specified
 * tolerance, or -1 if the solver did not converge.
 */

int CGSolver(const std::vector<double> &val,
             const std::vector<int>    &row_ptr,
             const std::vector<int>    &col_idx,
             const std::vector<double> &b,
             std::vector<double>       &x,
             const double              tol);

#endif /* CGSOLVER_HPP */
