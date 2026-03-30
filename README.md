# matrixceax

**matrixceax** is a simple Python library for performing matrix operations.  
It supports basic linear algebra operations, including addition, subtraction, multiplication, determinant, transpose, reshaping, and even negative powers (using matrix inverse).  

---
##Download From:
  ```python
https://pypi.org/project/matrixcea/0.1.0/
  ```

##Usage:
  ```python
from matrixceax import matrix
  ```

## **Features**

- Create matrices from lists of lists or single row.
- Matrix addition, subtraction, scalar multiplication, and matrix multiplication.
- Transpose, flatten, and reshape matrices.
- Determinant calculation for square matrices.
- Check for square, identity, symmetric, or zero matrices.
- Raise a matrix to a positive or negative integer power.
- Compute matrix inverse (for square, non-singular matrices).
- Element-wise division by a scalar.
- Operator overloading for Pythonic syntax:
  ```python
  A + B
  A - B
  A @ B      # matrix multiplication
  A * 3      # scalar multiplication
  3 * A      # scalar multiplication
  A ** -1    # matrix inverse
  A ** 3     # matrix power


# Create matrices
  ```python
A = matrix([[1, 2], [3, 4]])
B = matrix([[5, 6], [7, 8]])
  ```
# Arithmetic operations
  ```python
C = A + B
D = A - B
E = A @ B
F = A * 2
G = 2 * A
H = A / 2
  ```
# Properties
  ```python
print(A.is_square())    # True
print(A.is_identity())  # False
print(A.is_symmetric()) # False
print(A.is_zero())      # False
  ```
# Advanced
 ```python
det = A.determinant()
A_inv = A.inverse()
A_pow = A ** 3
A_neg = A ** -1
A_T = A.transpose()
flat = A.flatten()
reshaped = A.reshape(1, 4)
 ```
