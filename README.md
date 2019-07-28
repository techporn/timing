# timing
 simple plot app for digital timing diagram.
 
 タイミングチャートを描くためのモジュールです

# Usage
簡単にプロットする例: 
``` {.sourceCode .python}
>>> import timing
>>> d = timing.Diagram()
>>> d.add_timing("test", [0,1,0,1,0])
>>> d.plot()
<class 'matplotlib.axes._subplots.AxesSubplot'>
```

# Load text
以下のようなテキストファイルからタイミングチャートを作成できます。
``` :test_chart
A:~~__~~__~~_
B:~~__~~__~~__
```


``` {.sourceCode .python}
>>> import timing as tim
>>> data = tim.parser.read_timing("test_chart")
>>> d = tim.Diagram()
>>> for i in data:
...     d.add_timing(*i)
... 
>>> d.plot()
<class 'numpy.ndarray'>
```

## Result
![Result](./Figure_1.png "Figure 1") 