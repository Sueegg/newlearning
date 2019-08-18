

```python
import numpy as np
import pandas as pd
```


```python
!type C:\Users\Sueegg\Desktop\data\examples\ex1.csv
```

    a,b,c,d,message
    1,2,3,4,hello
    5,6,7,8,world
    9,10,11,12,foo
    


```python
df = pd.read_csv('C:/Users/Sueegg/Desktop/data/examples/ex1.csv')
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
      <th>message</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
      <td>hello</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
      <td>world</td>
    </tr>
    <tr>
      <th>2</th>
      <td>9</td>
      <td>10</td>
      <td>11</td>
      <td>12</td>
      <td>foo</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.read_table('C:/Users/Sueegg/Desktop/data/examples/ex1.csv', sep=',')


```

    D:\sue\Download\Anaconda3\lib\site-packages\ipykernel_launcher.py:1: FutureWarning: read_table is deprecated, use read_csv instead.
      """Entry point for launching an IPython kernel.
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
      <th>message</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
      <td>hello</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
      <td>world</td>
    </tr>
    <tr>
      <th>2</th>
      <td>9</td>
      <td>10</td>
      <td>11</td>
      <td>12</td>
      <td>foo</td>
    </tr>
  </tbody>
</table>
</div>




```python
!type C:\Users\Sueegg\Desktop\data\examples\ex2.csv
```

    1,2,3,4,hello
    5,6,7,8,world
    9,10,11,12,foo
    


```python
pd.read_csv('C:/Users/Sueegg/Desktop/data/examples/ex2.csv', header=None)

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
      <td>hello</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
      <td>world</td>
    </tr>
    <tr>
      <th>2</th>
      <td>9</td>
      <td>10</td>
      <td>11</td>
      <td>12</td>
      <td>foo</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.read_csv('C:/Users/Sueegg/Desktop/data/examples/ex2.csv', names=['a', 'b', 'c', 'd', 'message'])

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
      <th>message</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
      <td>hello</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
      <td>world</td>
    </tr>
    <tr>
      <th>2</th>
      <td>9</td>
      <td>10</td>
      <td>11</td>
      <td>12</td>
      <td>foo</td>
    </tr>
  </tbody>
</table>
</div>




```python
names = ['a', 'b', 'c', 'd', 'message']
pd.read_csv('C:/Users/Sueegg/Desktop/data/examples/ex2.csv', names=names, index_col='message')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
    </tr>
    <tr>
      <th>message</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>hello</th>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
    </tr>
    <tr>
      <th>world</th>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
    </tr>
    <tr>
      <th>foo</th>
      <td>9</td>
      <td>10</td>
      <td>11</td>
      <td>12</td>
    </tr>
  </tbody>
</table>
</div>




```python
import os
os.chdir('C:/Users/Sueegg/Desktop/data/examples')
```


```python
!type csv_mindex.csv
```

    key1,key2,value1,value2
    one,a,1,2
    one,b,3,4
    one,c,5,6
    one,d,7,8
    two,a,9,10
    two,b,11,12
    two,c,13,14
    two,d,15,16
    


```python
parsed = pd.read_csv('csv_mindex.csv',index_col=['key1', 'key2'])
parsed
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>value1</th>
      <th>value2</th>
    </tr>
    <tr>
      <th>key1</th>
      <th>key2</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="4" valign="top">one</th>
      <th>a</th>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>b</th>
      <td>3</td>
      <td>4</td>
    </tr>
    <tr>
      <th>c</th>
      <td>5</td>
      <td>6</td>
    </tr>
    <tr>
      <th>d</th>
      <td>7</td>
      <td>8</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">two</th>
      <th>a</th>
      <td>9</td>
      <td>10</td>
    </tr>
    <tr>
      <th>b</th>
      <td>11</td>
      <td>12</td>
    </tr>
    <tr>
      <th>c</th>
      <td>13</td>
      <td>14</td>
    </tr>
    <tr>
      <th>d</th>
      <td>15</td>
      <td>16</td>
    </tr>
  </tbody>
</table>
</div>




```python
list(open('ex3.txt'))
```




    ['            A         B         C\n',
     'aaa -0.264438 -1.026059 -0.619500\n',
     'bbb  0.927272  0.302904 -0.032399\n',
     'ccc -0.264273 -0.386314 -0.217601\n',
     'ddd -0.871858 -0.348382  1.100491\n']




```python
result = pd.read_table('ex3.txt', sep='\s+')#匹配空白符号
result
```

    D:\sue\Download\Anaconda3\lib\site-packages\ipykernel_launcher.py:1: FutureWarning: read_table is deprecated, use read_csv instead.
      """Entry point for launching an IPython kernel.
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>aaa</th>
      <td>-0.264438</td>
      <td>-1.026059</td>
      <td>-0.619500</td>
    </tr>
    <tr>
      <th>bbb</th>
      <td>0.927272</td>
      <td>0.302904</td>
      <td>-0.032399</td>
    </tr>
    <tr>
      <th>ccc</th>
      <td>-0.264273</td>
      <td>-0.386314</td>
      <td>-0.217601</td>
    </tr>
    <tr>
      <th>ddd</th>
      <td>-0.871858</td>
      <td>-0.348382</td>
      <td>1.100491</td>
    </tr>
  </tbody>
</table>
</div>




```python
!type ex4.csv
pd.read_csv('ex4.csv', skiprows=[0, 2, 3])
```

    # hey!
    a,b,c,d,message
    # just wanted to make things more difficult for you
    # who reads CSV files with computers, anyway?
    1,2,3,4,hello
    5,6,7,8,world
    9,10,11,12,foo
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
      <th>message</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
      <td>hello</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
      <td>world</td>
    </tr>
    <tr>
      <th>2</th>
      <td>9</td>
      <td>10</td>
      <td>11</td>
      <td>12</td>
      <td>foo</td>
    </tr>
  </tbody>
</table>
</div>




```python
!type ex5.csv
```

    something,a,b,c,d,message
    one,1,2,3,4,NA
    two,5,6,,8,world
    three,9,10,11,12,foo
    


```python
result=pd.read_csv('ex5.csv')
result
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>something</th>
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
      <th>message</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>one</td>
      <td>1</td>
      <td>2</td>
      <td>3.0</td>
      <td>4</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>two</td>
      <td>5</td>
      <td>6</td>
      <td>NaN</td>
      <td>8</td>
      <td>world</td>
    </tr>
    <tr>
      <th>2</th>
      <td>three</td>
      <td>9</td>
      <td>10</td>
      <td>11.0</td>
      <td>12</td>
      <td>foo</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.isnull(result)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>something</th>
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
      <th>message</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>1</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>




```python
result = pd.read_csv('ex5.csv',na_values=['NULL'])
result
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>something</th>
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
      <th>message</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>one</td>
      <td>1</td>
      <td>2</td>
      <td>3.0</td>
      <td>4</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>two</td>
      <td>5</td>
      <td>6</td>
      <td>NaN</td>
      <td>8</td>
      <td>world</td>
    </tr>
    <tr>
      <th>2</th>
      <td>three</td>
      <td>9</td>
      <td>10</td>
      <td>11.0</td>
      <td>12</td>
      <td>foo</td>
    </tr>
  </tbody>
</table>
</div>




```python
sentinels = {'message': ['foo', 'NA'], 'something': ['two']}
pd.read_csv('ex5.csv', na_values=sentinels)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>something</th>
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
      <th>message</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>one</td>
      <td>1</td>
      <td>2</td>
      <td>3.0</td>
      <td>4</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NaN</td>
      <td>5</td>
      <td>6</td>
      <td>NaN</td>
      <td>8</td>
      <td>world</td>
    </tr>
    <tr>
      <th>2</th>
      <td>three</td>
      <td>9</td>
      <td>10</td>
      <td>11.0</td>
      <td>12</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
