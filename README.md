# gtick

Matplotlibの年月日時の日本語フォーマッター

2,3日程度の期間を「時」ごとに表示する際の利用を想定した日本語表示です。
表示が「H時(HH)」「M月D日」「Y年」のようになります。

## 特徴

- 「時」は全ての場所で表示される。
- 最初の場所（``start_pos=0`` ）では、「時」だけではなく、年・月・日が表示される。
- 年、月、日は、変わったタイミングのみで、表示される。
- 月や日が0埋めされずに、「3月21日」のように表示される。
- 「年」は省略可能 (year=False)
- 「時」は、「06」から「6時」(``ji=True``)に切り替え可能。

です。

## クイックスタート

``matplotlib.dates.HourLocator`` と組み合わせて使うことを想定しています。

```python
from gtick import JDayHourFormatter

import matplotlib.dates as mdates

# 何かデータをプロット
# plt.plot(x, y)

# HourLocatorを利用する: この例だと3時間ごとにおく。
# Locatorを調整することで、軸のラベル間隔などは調整可能。
axes.xaxis.set_major_locator(mdates.HourLocator(byhour=[i for i in range(0, 24, 3)]))
# major locatorの場所に、JDayHourFormatterを利用する
axes.xaxis.set_major_formatter(JDayHourFormatter())
```


## Examples

### A

先頭には、時・月日・年が表示される。日が変わると、日が表示される。
![Sample A](png/sample_a.png)


### B

「0時」じゃなくても、先頭には、時・月日・年が表示される。
また、日だけではなく、年や月が変わると、年や月が表示される。
![Sample B](png/sample_b.png)


### C

先頭と0時が近いと、詰まってしまうことがあるので、その場合は、オプションで、年・月・日の表示をずらすことができる。
![Sample C](png/sample_c.png)


### D

年は非表示にすることが可能。また、時は、6時の表示もできる。
![Sample D](png/sample_d.png)
