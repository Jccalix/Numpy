# NumPy Examples

A collection of Python scripts demonstrating various NumPy operations and concepts. This repository contains practical examples for learning and understanding NumPy functionality.

## Overview

This repository includes examples covering:
- Scalar arithmetic operations
- Vectorized mathematical functions
- Array slicing and indexing
- Multi-dimensional array manipulation

## Prerequisites

- Python 3.x
- NumPy library

## Installation

To run these examples, you'll need to install NumPy:

```bash
pip install numpy
```

## Examples

### 1. Scalar Arithmetic (`scalarArithmetic.py`)

Demonstrates basic arithmetic operations between arrays and scalar values.

**Operations covered:**
- Addition, subtraction, multiplication, division
- Exponentiation and modulus operations

**Example output:**
```python
[6 7 8]    # [1,2,3] + 5
[-1  0  1] # [1,2,3] - 2
[3 6 9]    # [1,2,3] * 3
```

**Run:** `python3 scalarArithmetic.py`

### 2. Vectorized Math Functions (`vectorizedMathFunctions.py`)

Shows how NumPy applies mathematical functions element-wise to arrays.

**Functions demonstrated:**
- Square root (`np.sqrt`)
- Rounding (`np.round`)
- Mathematical constants (`np.pi`)

**Example output:**
```python
[1.         1.41421356 1.73205081]  # Square roots
[1 2 3]                             # Rounded values
[3.14159265 6.28318531 9.42477796]  # Pi multiplication
```

**Run:** `python3 vectorizedMathFunctions.py`

### 3. Array Slicing (`slicing.py`)

Demonstrates 2D array slicing and indexing techniques.

**Concepts covered:**
- Basic slicing syntax `[start:end:step]`
- Multi-dimensional array slicing
- Row and column selection

**Example output:**
```python
[[3 4]
 [7 8]]     # First 2 rows, last 2 columns

[[ 6  7  8]
 [10 11 12]] # Rows 1-2, columns 1-3
```

**Run:** `python3 slicing.py`

### 4. Multi-dimensional Arrays (`multidimensionalArray.py`)

Explores 3D array creation and element access.

**Features:**
- 3D array construction
- Element selection by coordinates
- String concatenation from array elements

**Example output:**
```python
KLX  # Concatenated characters from specific array positions
```

**Run:** `python3 multidimensionalArray.py`

## Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/Jccalix/Numpy.git
   cd Numpy
   ```

2. Install NumPy:
   ```bash
   pip install numpy
   ```

3. Run any example:
   ```bash
   python3 <filename>.py
   ```

## Learning Path

For beginners, we recommend exploring the examples in this order:
1. `scalarArithmetic.py` - Learn basic operations
2. `vectorizedMathFunctions.py` - Understand vectorization
3. `slicing.py` - Master array indexing
4. `multidimensionalArray.py` - Work with complex structures

## Contributing

Feel free to add more NumPy examples or improve existing ones. Each example should:
- Be well-commented
- Demonstrate a specific NumPy concept
- Include clear output examples

## License

This project is open source and available under the MIT License.