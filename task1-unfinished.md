

```python
import numpy as np
```


```python
print(np.__version__)
np.show_config()
```

    1.16.4
    mkl_info:
        libraries = ['mkl_rt']
        library_dirs = ['D:/sue/Download/Anaconda3\\Library\\lib']
        define_macros = [('SCIPY_MKL_H', None), ('HAVE_CBLAS', None)]
        include_dirs = ['C:\\Program Files (x86)\\IntelSWTools\\compilers_and_libraries_2019.0.117\\windows\\mkl', 'C:\\Program Files (x86)\\IntelSWTools\\compilers_and_libraries_2019.0.117\\windows\\mkl\\include', 'C:\\Program Files (x86)\\IntelSWTools\\compilers_and_libraries_2019.0.117\\windows\\mkl\\lib', 'D:/sue/Download/Anaconda3\\Library\\include']
    blas_mkl_info:
        libraries = ['mkl_rt']
        library_dirs = ['D:/sue/Download/Anaconda3\\Library\\lib']
        define_macros = [('SCIPY_MKL_H', None), ('HAVE_CBLAS', None)]
        include_dirs = ['C:\\Program Files (x86)\\IntelSWTools\\compilers_and_libraries_2019.0.117\\windows\\mkl', 'C:\\Program Files (x86)\\IntelSWTools\\compilers_and_libraries_2019.0.117\\windows\\mkl\\include', 'C:\\Program Files (x86)\\IntelSWTools\\compilers_and_libraries_2019.0.117\\windows\\mkl\\lib', 'D:/sue/Download/Anaconda3\\Library\\include']
    blas_opt_info:
        libraries = ['mkl_rt']
        library_dirs = ['D:/sue/Download/Anaconda3\\Library\\lib']
        define_macros = [('SCIPY_MKL_H', None), ('HAVE_CBLAS', None)]
        include_dirs = ['C:\\Program Files (x86)\\IntelSWTools\\compilers_and_libraries_2019.0.117\\windows\\mkl', 'C:\\Program Files (x86)\\IntelSWTools\\compilers_and_libraries_2019.0.117\\windows\\mkl\\include', 'C:\\Program Files (x86)\\IntelSWTools\\compilers_and_libraries_2019.0.117\\windows\\mkl\\lib', 'D:/sue/Download/Anaconda3\\Library\\include']
    lapack_mkl_info:
        libraries = ['mkl_rt']
        library_dirs = ['D:/sue/Download/Anaconda3\\Library\\lib']
        define_macros = [('SCIPY_MKL_H', None), ('HAVE_CBLAS', None)]
        include_dirs = ['C:\\Program Files (x86)\\IntelSWTools\\compilers_and_libraries_2019.0.117\\windows\\mkl', 'C:\\Program Files (x86)\\IntelSWTools\\compilers_and_libraries_2019.0.117\\windows\\mkl\\include', 'C:\\Program Files (x86)\\IntelSWTools\\compilers_and_libraries_2019.0.117\\windows\\mkl\\lib', 'D:/sue/Download/Anaconda3\\Library\\include']
    lapack_opt_info:
        libraries = ['mkl_rt']
        library_dirs = ['D:/sue/Download/Anaconda3\\Library\\lib']
        define_macros = [('SCIPY_MKL_H', None), ('HAVE_CBLAS', None)]
        include_dirs = ['C:\\Program Files (x86)\\IntelSWTools\\compilers_and_libraries_2019.0.117\\windows\\mkl', 'C:\\Program Files (x86)\\IntelSWTools\\compilers_and_libraries_2019.0.117\\windows\\mkl\\include', 'C:\\Program Files (x86)\\IntelSWTools\\compilers_and_libraries_2019.0.117\\windows\\mkl\\lib', 'D:/sue/Download/Anaconda3\\Library\\include']
    


```python
Z=np.zero(10)
print（Z）
```


      File "<ipython-input-3-1c97bce6f917>", line 2
        print（Z）
               ^
    SyntaxError: invalid character in identifier
    



```python
Z = np.zeros((10,10))
print("%d bytes" % (Z.size * Z.itemsize))
```

    800 bytes
    


```python
numpy.info(numpy.add)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-8-3ccd1fa36e8b> in <module>
    ----> 1 numpy.info(numpy.add)
    

    NameError: name 'numpy' is not defined



```python
Z = np.zeros(10)
Z[4] = 1
print(Z)
```

    [0. 0. 0. 0. 1. 0. 0. 0. 0. 0.]
    


```python
Z = np.arange(10,50)
print(Z)
```

    [10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33
     34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49]
    


```python
Z = np.arange(50)
Z = Z[::-1]
print(Z)
```

    [49 48 47 46 45 44 43 42 41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26
     25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10  9  8  7  6  5  4  3  2
      1  0]
    


```python
Z = np.arange(9).reshape(3,3)
print(Z)
```

    [[0 1 2]
     [3 4 5]
     [6 7 8]]
    


```python
nz = np.nonzero([1,2,0,0,4,0])
print(nz)
```

    (array([0, 1, 4], dtype=int64),)
    


```python
Z = np.eye(3)
print(Z)
```

    [[1. 0. 0.]
     [0. 1. 0.]
     [0. 0. 1.]]
    


```python
Z = np.random.random((3,3,3))
print(Z)
```

    [[[0.98784349 0.57186172 0.14992141]
      [0.05228159 0.93091362 0.7463116 ]
      [0.21301189 0.16746122 0.52710109]]
    
     [[0.45440811 0.26131855 0.28351118]
      [0.09773066 0.55454894 0.35467484]
      [0.52404514 0.64026131 0.08736051]]
    
     [[0.70980934 0.94188707 0.745482  ]
      [0.39122553 0.29528731 0.00137184]
      [0.48586857 0.20881671 0.4378545 ]]]
    


```python
Z = np.random.random((10,10))
Zmin, Zmax = Z.min(), Z.max()
print(Zmin, Zmax)
```

    0.029603183382481135 0.9935845773156272
    


```python
Z = np.random.random(30)
m = Z.mean()
print(m)
```

    0.4771700297956217
    


```python
Z = np.ones((10,10))
Z[1:-1,1:-1] = 0
print(Z)
```

    [[1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
     [1. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
     [1. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
     [1. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
     [1. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
     [1. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
     [1. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
     [1. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
     [1. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
     [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]]
    


```python
Z = np.ones((5,5))
Z = np.pad(Z, pad_width=1, mode='constant', constant_values=0)
print(Z)
```

    [[0. 0. 0. 0. 0. 0. 0.]
     [0. 1. 1. 1. 1. 1. 0.]
     [0. 1. 1. 1. 1. 1. 0.]
     [0. 1. 1. 1. 1. 1. 0.]
     [0. 1. 1. 1. 1. 1. 0.]
     [0. 1. 1. 1. 1. 1. 0.]
     [0. 0. 0. 0. 0. 0. 0.]]
    


```python
print(0 * np.nan)

```

    nan
    


```python
print(np.nan == np.nan)
```

    False
    


```python
print(np.nan - np.nan)
```

    nan
    


```python
print(0.3 == 3 * 0.1)
```

    False
    


```python
Z = np.diag(1+np.arange(4),k=-1)
print(Z)
```

    [[0 0 0 0 0]
     [1 0 0 0 0]
     [0 2 0 0 0]
     [0 0 3 0 0]
     [0 0 0 4 0]]
    


```python
Z = np.zeros((8,8),dtype=int)
Z[1::2,::2] = 1
Z[::2,1::2] = 1
print(Z)
```

    [[0 1 0 1 0 1 0 1]
     [1 0 1 0 1 0 1 0]
     [0 1 0 1 0 1 0 1]
     [1 0 1 0 1 0 1 0]
     [0 1 0 1 0 1 0 1]
     [1 0 1 0 1 0 1 0]
     [0 1 0 1 0 1 0 1]
     [1 0 1 0 1 0 1 0]]
    


```python
print(np.unravel_index(100,(6,7,8)))
```

    (1, 5, 4)
    


```python
Z = np.tile( np.array([[0,1],[1,0]]), (4,4))
print(Z)
```

    [[0 1 0 1 0 1 0 1]
     [1 0 1 0 1 0 1 0]
     [0 1 0 1 0 1 0 1]
     [1 0 1 0 1 0 1 0]
     [0 1 0 1 0 1 0 1]
     [1 0 1 0 1 0 1 0]
     [0 1 0 1 0 1 0 1]
     [1 0 1 0 1 0 1 0]]
    


```python
Z = np.random.random((5,5))
Zmax, Zmin = Z.max(), Z.min()
Z = (Z - Zmin)/(Zmax - Zmin)
print(Z)
```

    [[0.61907829 0.95605555 0.971256   0.12985533 0.81841064]
     [0.85021381 0.7655655  0.07019688 0.07413148 0.39569433]
     [0.94789989 1.         0.2383944  0.63465682 0.        ]
     [0.46822265 0.57624404 0.6492285  0.51120077 0.3793471 ]
     [0.0685865  0.48144133 0.32084535 0.06742664 0.9843294 ]]
    


```python
olor = np.dtype([("r", np.ubyte, 1),
                  ("g", np.ubyte, 1),
                  ("b", np.ubyte, 1),
                  ("a", np.ubyte, 1)])
color
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-31-009ed2f48842> in <module>
          3                   ("b", np.ubyte, 1),
          4                   ("a", np.ubyte, 1)])
    ----> 5 color
    

    NameError: name 'color' is not defined



```python
Z = np.dot(np.ones((5,3)), np.ones((3,2)))
print(Z)
```

    [[3. 3.]
     [3. 3.]
     [3. 3.]
     [3. 3.]
     [3. 3.]]
    


```python
Z = np.arange(11)
Z[(3 < Z) & (Z <= 8)] *= -1
print(Z)
```

    [ 0  1  2  3 -4 -5 -6 -7 -8  9 10]
    


```python
print(sum(range(5),-1))
```

    9
    


```python
print(sum(range(5),-1))
```

    9
    


```python

```
