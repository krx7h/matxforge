class matrix:
    """
    A simple matrix class supporting basic matrix operations such as addition, 
    subtraction, multiplication, transpose, reshaping, flattening, and determinant 
    calculation. Also provides checks for square, identity, symmetric, and zero matrices.

    Attributes:
        matrix (list of lists): 2D list representing the matrix elements.
        rows (int): Number of rows in the matrix.
        columns (int): Number of columns in the matrix.
    """
    def __init__(self,matrix):
        """
        Initializes a matrix object.

        Args:
            matrix (list of lists or list of numbers): Input matrix as a 2D list or 
                a single row vector as a list.

        Raises:
            TypeError: If the input is not a list or contains incompatible types.
        """
        if isinstance(matrix[0], (int, float)):
            matrix = [matrix]
        self.matrix = matrix
        self.rows = len(matrix)
        self.columns = len(matrix[0])
    

    def __str__(self):
        """
        Returns a string representation of the matrix.

        Returns:
            str: A string where each row of the matrix is on a new line.
        """
        matrix = ""
        for row in self.matrix:
            matrix += f"{row}\n"
        return matrix
    
    
    def __eq__(self,other):
        """
        Checks if two matrices are equal.

        Args:
            other (matrix): Another matrix to compare.

        Returns:
            bool: True if matrices have the same shape and elements, False otherwise.
        """
        if not isinstance(other, matrix):
            return False

        if self.rows != other.rows or self.columns != other.columns:
            return False

        for i in range(self.rows):
            for j in range(self.columns):
                if self.matrix[i][j] != other.matrix[i][j]:
                    return False

        return True
    

    def __getitem__(self,index):
        """
        Retrieves a row of the matrix by index.

        Args:
            index (int): Index of the row to retrieve.

        Returns:
            list: The requested row.

        Raises:
            IndexError: If index is out of range.
        """
        try:
            return self.matrix[index]
        except:
            return IndexError("Index out of range.")
        

    def __add__(self,other):
        """
        Adds two matrices element-wise.

        Args:
            other (matrix): The matrix to add.

        Returns:
            matrix: New matrix representing the sum.

        Raises:
            ValueError: If matrices have different dimensions.
        """
        r1,c1 = self.rows,self.columns
        r2,c2 = other.rows,other.columns
        if r1 != r2 or c1 != c2:
            raise ValueError("Addition cannot be performed.(Size Mismatch)")
        else:
            sum = [[0 for _ in range(c1)] for _ in range(r1)]
            for i in range(r1):
                for j in range(c1):
                    sum[i][j] = self.matrix[i][j] + other.matrix[i][j]
            return matrix(sum)
        

    def __matmul__(self,other):
        """
        Performs matrix multiplication using the '@' operator.

        Args:
            other (matrix): The matrix to multiply.

        Returns:
            matrix: New matrix representing the product.

        Raises:
            ValueError: If number of columns in self does not match number of rows in other.
        """
        if self.columns != other.rows:
            raise ValueError("Matrix multiplication not possible")

        result = [[0 for _ in range(other.columns)] for _ in range(self.rows)]

        for i in range(self.rows):
            for j in range(other.columns):
                for k in range(self.columns):
                    result[i][j] += self.matrix[i][k] * other.matrix[k][j]

        return matrix(result)
    

    def __sub__(self,other):
        """
        Subtracts one matrix from another element-wise.

        Args:
            other (matrix): The matrix to subtract.

        Returns:
            matrix: New matrix representing the difference.

        Raises:
            ValueError: If matrices have different dimensions.
        """
        r1,c1 = self.rows,self.columns
        r2,c2 = other.rows,other.columns
        if r1 != r2 or c1 != c2:
            raise ValueError("Addition cannot be performed.(Size Mismatch)")
        else:
            sub = [[0 for _ in range(c1)] for _ in range(r1)]
            for i in range(r1):
                for j in range(c1):
                    sub[i][j] = self.matrix[i][j] - other.matrix[i][j]
            return matrix(sub)


    def __mul__(self, scalar):
        """
        Multiplies the matrix by a scalar.

        Args:
            scalar (int or float): The scalar value to multiply.

        Returns:
            matrix: New matrix with elements multiplied by scalar.
        """
        if isinstance(scalar, (int, float)):
            return matrix([[x * scalar for x in row] for row in self.matrix])
        return NotImplemented


    def __rmul__(self, scalar):
        """
        Enables scalar multiplication from the left.

        Args:
            scalar (int or float): The scalar value to multiply.

        Returns:
            matrix: New matrix with elements multiplied by scalar.
        """

        return self.__mul__(scalar)
    

    def transpose(self):
        """
        Transposes the matrix (rows become columns and vice versa).

        Returns:
            matrix: New matrix representing the transpose.
        """
        transpose = [[0 for i in range(self.rows)] for i in range(self.columns)]
        for i in range(self.columns):
            for j in range(self.rows):
                transpose[i][j] = self.matrix[j][i]
        return matrix(transpose)
    

    def reshape(self,new_rows,new_cols):
        """
        Reshapes the matrix to new dimensions.

        Args:
            new_rows (int): New number of rows.
            new_cols (int): New number of columns.

        Returns:
            matrix: New reshaped matrix.

        Raises:
            ValueError: If total elements do not match.
        """
        if (self.rows * self.columns) != (new_rows * new_cols):
            raise ValueError("Size Mismatch.")
        else:
            flat = []
            for i in range(self.rows):
                for j in range(self.columns):
                    flat.append(self.matrix[i][j])
            reshape = [[0 for i in range(new_cols)] for i in range(new_rows)]
            num = 0
            for i in range(new_rows):
                for j in range(new_cols):
                    reshape[i][j] = flat[num]
                    num += 1
            return matrix(reshape)


    def flatten(self):
        """
        Flattens the matrix into a single list.

        Returns:
            list: List of all elements row-wise.
        """
        flat = []
        for i in range(self.rows):
            for j in range(self.columns):
                flat.append(self.matrix[i][j])
            return flat
    

    def determinant(self):
        """
        Calculates the determinant of a square matrix.

        Returns:
            int or float: Determinant value.

        Raises:
            ValueError: If the matrix is not square.
        """
        # must be square
        if self.rows != self.columns:
            raise ValueError("Determinant only defined for square matrices")

        # 1×1 matrix
        if self.rows == 1:
            return self.matrix[0][0]

        # 2×2 matrix
        if self.rows == 2:
            return (self.matrix[0][0] * self.matrix[1][1] -
                    self.matrix[0][1] * self.matrix[1][0])

        # larger matrices (recursive expansion)
        det = 0
        for col in range(self.columns):
            # build minor matrix
            minor = []
            for i in range(1, self.rows):
                row = []
                for j in range(self.columns):
                    if j != col:
                        row.append(self.matrix[i][j])
                minor.append(row)

            sign = (-1) ** col
            det += sign * self.matrix[0][col] * matrix(minor).determinant()

        return det
    

    def is_square(self):
        """
        Checks if the matrix is square.

        Returns:
            bool: True if rows == columns, else False.
        """
        if (self.rows == self.columns):
            return True
        else:
            return False
    

    def is_identity(self):
        """
        Checks if the matrix is an identity matrix.

        Returns:
            bool: True if identity, else False.
        """
        if self.rows != self.columns:
            return False

        for i in range(self.rows):
            for j in range(self.columns):
                if i == j:
                    if self.matrix[i][j] != 1:
                        return False
                else:
                    if self.matrix[i][j] != 0:
                        return False
        return True
    

    def is_symmetric(self):
        """
        Checks if the matrix is symmetric.

        Returns:
            bool: True if symmetric, else False.
        """
        if (self == self.transpose()):
            return True
        else:
            return False
        
    
    def is_zero(self):
        """
        Checks if the matrix is a zero matrix.

        Returns:
            bool: True if all elements are zero, else False.
        """
        for i in range(self.rows):
            for j in range(self.columns):
                if self.matrix[i][j] != 0:
                    return False
        return True
    

    def __truediv__(self, scalar):
        """
        Divides the matrix by a scalar.

        Args:
            scalar (int or float): The scalar to divide by.

        Returns:
            matrix: New matrix with elements divided by scalar.

        Raises:
            ValueError: If scalar is not a number.
            ZeroDivisionError: If scalar is zero.
        """
        if not isinstance(scalar, (int, float)):
            raise ValueError("Can only divide by a scalar")
        if scalar == 0:
            raise ZeroDivisionError("Division by zero is not allowed")

        # multiply each element by 1/scalar
        new_matrix = [[x / scalar for x in row] for row in self.matrix]
        return matrix(new_matrix)
    

    def inverse(self):
        """
        Returns the inverse of a square, non-singular matrix.

        Returns:
            matrix: The inverse of the matrix.

        Raises:
            ValueError: If the matrix is not square or singular (determinant is 0).
        """
        if not self.is_square():
            raise ValueError("Only square matrices can have an inverse.")

        det = self.determinant()
        if det == 0:
            raise ValueError("Singular matrix; inverse does not exist.")

        # 1x1 matrix
        if self.rows == 1:
            return matrix([[1 / self.matrix[0][0]]])

        # 2x2 matrix
        if self.rows == 2:
            a, b = self.matrix[0]
            c, d = self.matrix[1]
            inv = [[d / det, -b / det],
                [-c / det, a / det]]
            return matrix(inv)

        # NxN matrix: use adjugate method
        cofactors = []
        for i in range(self.rows):
            cofactor_row = []
            for j in range(self.columns):
                # Build minor matrix by removing row i and column j
                minor = [[self.matrix[m][n] for n in range(self.columns) if n != j]
                        for m in range(self.rows) if m != i]
                # Cofactor = determinant of minor * (-1)^(i+j)
                cofactor_row.append(((-1) ** (i + j)) * matrix(minor).determinant())
            cofactors.append(cofactor_row)

        # Transpose cofactor matrix to get adjugate
        adjugate = matrix(cofactors).transpose()

        # Divide each element by determinant
        inv_matrix = [[x / det for x in row] for row in adjugate.matrix]

        return matrix(inv_matrix)
    

    def __pow__(self, power):
        """
        Raises the matrix to the given positive integer power.
        
        Args:
            power (int): The power to raise the matrix to. Must be >= 0.
        
        Returns:
            matrix: New matrix representing self ** power.
        
        Raises:
            ValueError: If matrix is not square or power is negative.
        """
        if not self.is_square():
            raise ValueError("Only square matrices can be raised to a power.")
        if power < 0:
            inv = self.inverse()
            return inv ** (-power)

        # Power = 0 , return identity matrix
        if power == 0:
            return matrix([[1 if i == j else 0 for j in range(self.columns)] for i in range(self.rows)])
        
        # Power = 1 , return a copy
        result = matrix([row[:] for row in self.matrix])
        
        for _ in range(1, power):
            result = result @ self
        
        return result


    



        



    




