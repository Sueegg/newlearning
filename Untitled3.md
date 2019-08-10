

```python
import pandas as pd
import numpy as np
```


```python
from pandas import Series, DataFrame
```


```python
obj=pd.Series([4,7,-5,3])
obj
```




    0    4
    1    7
    2   -5
    3    3
    dtype: int64




```python
obj.values
```




    array([ 4,  7, -5,  3], dtype=int64)




```python
obj.index
```




    RangeIndex(start=0, stop=4, step=1)




```python
obj2=pd.Series([4,7,-5,3],index=['d','b','a','c'])
obj2
```




    d    4
    b    7
    a   -5
    c    3
    dtype: int64




```python
obj2.index
```




    Index(['d', 'b', 'a', 'c'], dtype='object')




```python
obj2['a']
```




    -5




```python
obj2['d']=6
```


```python
obj2[['c','a','d']]
```




    c    3
    a   -5
    d    6
    dtype: int64




```python
obj2[obj2>0]
```




    d    6
    b    7
    c    3
    dtype: int64




```python
obj2*2
```




    d    12
    b    14
    a   -10
    c     6
    dtype: int64




```python
np.exp(obj2)
```




    d     403.428793
    b    1096.633158
    a       0.006738
    c      20.085537
    dtype: float64




```python
'b' in obj2
```




    True




```python
'e' in obj2
```




    False




```python
sdata={'Ohio':35000,'Texas':71000,'Oregon':16000,'Utah':5000}
```


```python
obj3=pd.Series(sdata)
```


```python
obj3
```




    Ohio      35000
    Texas     71000
    Oregon    16000
    Utah       5000
    dtype: int64




```python
states=['California','Ohio','Oregon','Texas']
```


```python
obj4=pd.Series(sdata,index=states)
```


```python
obj4
```




    California        NaN
    Ohio          35000.0
    Oregon        16000.0
    Texas         71000.0
    dtype: float64




```python
pd.isnull(obj4)
```




    California     True
    Ohio          False
    Oregon        False
    Texas         False
    dtype: bool




```python
pd.notnull(obj4)
```




    California    False
    Ohio           True
    Oregon         True
    Texas          True
    dtype: bool




```python
obj4.isnull()
```




    California     True
    Ohio          False
    Oregon        False
    Texas         False
    dtype: bool




```python
obj3
```




    Ohio      35000
    Texas     71000
    Oregon    16000
    Utah       5000
    dtype: int64




```python
obj4
```




    California        NaN
    Ohio          35000.0
    Oregon        16000.0
    Texas         71000.0
    dtype: float64




```python
obj3+obj4
```




    California         NaN
    Ohio           70000.0
    Oregon         32000.0
    Texas         142000.0
    Utah               NaN
    dtype: float64




```python
obj4.name='population'
```


```python
obj4.index.name='state'
```


```python
obj4
```




    state
    California        NaN
    Ohio          35000.0
    Oregon        16000.0
    Texas         71000.0
    Name: population, dtype: float64




```python
obj
```




    0    4
    1    7
    2   -5
    3    3
    dtype: int64




```python
obj.index=['Bob','steve','Jeff','Ryan']
```


```python
obj
```




    Bob      4
    steve    7
    Jeff    -5
    Ryan     3
    dtype: int64




```python
data={'state':['Ohio','Ohio','Ohio','Nevada','Nevada','Nevade'],'year':[2000,2001,2002,2001,2002,2003],'pop':[1.5,1.7,3.6,2.4,2.9,3.2]}
```


```python
frame=pd.DataFrame(data)
```


```python
frame
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
      <th>state</th>
      <th>year</th>
      <th>pop</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Ohio</td>
      <td>2000</td>
      <td>1.5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Ohio</td>
      <td>2001</td>
      <td>1.7</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Ohio</td>
      <td>2002</td>
      <td>3.6</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Nevada</td>
      <td>2001</td>
      <td>2.4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Nevada</td>
      <td>2002</td>
      <td>2.9</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Nevade</td>
      <td>2003</td>
      <td>3.2</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame.head()
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
      <th>state</th>
      <th>year</th>
      <th>pop</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Ohio</td>
      <td>2000</td>
      <td>1.5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Ohio</td>
      <td>2001</td>
      <td>1.7</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Ohio</td>
      <td>2002</td>
      <td>3.6</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Nevada</td>
      <td>2001</td>
      <td>2.4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Nevada</td>
      <td>2002</td>
      <td>2.9</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.DataFrame(data,columns=['year','state','pop'])
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
      <th>year</th>
      <th>state</th>
      <th>pop</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2000</td>
      <td>Ohio</td>
      <td>1.5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2001</td>
      <td>Ohio</td>
      <td>1.7</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2002</td>
      <td>Ohio</td>
      <td>3.6</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2001</td>
      <td>Nevada</td>
      <td>2.4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2002</td>
      <td>Nevada</td>
      <td>2.9</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2003</td>
      <td>Nevade</td>
      <td>3.2</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame2=pd.DataFrame(data,columns=['year','state','pop','debt'],index=['one','two','three','four','five','six'])
```


```python
frame2
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
      <th>year</th>
      <th>state</th>
      <th>pop</th>
      <th>debt</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>one</th>
      <td>2000</td>
      <td>Ohio</td>
      <td>1.5</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>two</th>
      <td>2001</td>
      <td>Ohio</td>
      <td>1.7</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>three</th>
      <td>2002</td>
      <td>Ohio</td>
      <td>3.6</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>four</th>
      <td>2001</td>
      <td>Nevada</td>
      <td>2.4</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>five</th>
      <td>2002</td>
      <td>Nevada</td>
      <td>2.9</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>six</th>
      <td>2003</td>
      <td>Nevade</td>
      <td>3.2</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame2['state']
```




    one        Ohio
    two        Ohio
    three      Ohio
    four     Nevada
    five     Nevada
    six      Nevade
    Name: state, dtype: object




```python
frame2.loc['three']
```




    year     2002
    state    Ohio
    pop       3.6
    debt      NaN
    Name: three, dtype: object




```python
frame2['debt']=16.5
```


```python
frame2
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
      <th>year</th>
      <th>state</th>
      <th>pop</th>
      <th>debt</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>one</th>
      <td>2000</td>
      <td>Ohio</td>
      <td>1.5</td>
      <td>16.5</td>
    </tr>
    <tr>
      <th>two</th>
      <td>2001</td>
      <td>Ohio</td>
      <td>1.7</td>
      <td>16.5</td>
    </tr>
    <tr>
      <th>three</th>
      <td>2002</td>
      <td>Ohio</td>
      <td>3.6</td>
      <td>16.5</td>
    </tr>
    <tr>
      <th>four</th>
      <td>2001</td>
      <td>Nevada</td>
      <td>2.4</td>
      <td>16.5</td>
    </tr>
    <tr>
      <th>five</th>
      <td>2002</td>
      <td>Nevada</td>
      <td>2.9</td>
      <td>16.5</td>
    </tr>
    <tr>
      <th>six</th>
      <td>2003</td>
      <td>Nevade</td>
      <td>3.2</td>
      <td>16.5</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame2['debt']=np.arange(6.)
```


```python
frame2
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
      <th>year</th>
      <th>state</th>
      <th>pop</th>
      <th>debt</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>one</th>
      <td>2000</td>
      <td>Ohio</td>
      <td>1.5</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>two</th>
      <td>2001</td>
      <td>Ohio</td>
      <td>1.7</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>three</th>
      <td>2002</td>
      <td>Ohio</td>
      <td>3.6</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>four</th>
      <td>2001</td>
      <td>Nevada</td>
      <td>2.4</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>five</th>
      <td>2002</td>
      <td>Nevada</td>
      <td>2.9</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>six</th>
      <td>2003</td>
      <td>Nevade</td>
      <td>3.2</td>
      <td>5.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
val=pd.Series([-1.2,-1.5,-1.7],index=['two','four','five'])
```


```python
frame2['debt']=val
```


```python
frame2
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
      <th>year</th>
      <th>state</th>
      <th>pop</th>
      <th>debt</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>one</th>
      <td>2000</td>
      <td>Ohio</td>
      <td>1.5</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>two</th>
      <td>2001</td>
      <td>Ohio</td>
      <td>1.7</td>
      <td>-1.2</td>
    </tr>
    <tr>
      <th>three</th>
      <td>2002</td>
      <td>Ohio</td>
      <td>3.6</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>four</th>
      <td>2001</td>
      <td>Nevada</td>
      <td>2.4</td>
      <td>-1.5</td>
    </tr>
    <tr>
      <th>five</th>
      <td>2002</td>
      <td>Nevada</td>
      <td>2.9</td>
      <td>-1.7</td>
    </tr>
    <tr>
      <th>six</th>
      <td>2003</td>
      <td>Nevade</td>
      <td>3.2</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame2['eastern']=frame2.state=='Ohio'
```


```python
frame2
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
      <th>year</th>
      <th>state</th>
      <th>pop</th>
      <th>debt</th>
      <th>eastern</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>one</th>
      <td>2000</td>
      <td>Ohio</td>
      <td>1.5</td>
      <td>NaN</td>
      <td>True</td>
    </tr>
    <tr>
      <th>two</th>
      <td>2001</td>
      <td>Ohio</td>
      <td>1.7</td>
      <td>-1.2</td>
      <td>True</td>
    </tr>
    <tr>
      <th>three</th>
      <td>2002</td>
      <td>Ohio</td>
      <td>3.6</td>
      <td>NaN</td>
      <td>True</td>
    </tr>
    <tr>
      <th>four</th>
      <td>2001</td>
      <td>Nevada</td>
      <td>2.4</td>
      <td>-1.5</td>
      <td>False</td>
    </tr>
    <tr>
      <th>five</th>
      <td>2002</td>
      <td>Nevada</td>
      <td>2.9</td>
      <td>-1.7</td>
      <td>False</td>
    </tr>
    <tr>
      <th>six</th>
      <td>2003</td>
      <td>Nevade</td>
      <td>3.2</td>
      <td>NaN</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>




```python
del frame2['eastern']
```


```python
frame2.columns
```




    Index(['year', 'state', 'pop', 'debt'], dtype='object')




```python
pop={'Nevada':{2001:2.4,2002:2.9},'Ohio':{2000:1.5,2001:1.7,2002:3.6}}
```


```python

```
