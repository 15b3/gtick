from matplotlib import ticker, dates


class JDayHourFormatter(ticker.Formatter):
    def __init__(self, start_pos=0, ji=False, year=True):
        """日本語の年月日時フォーマッター

        最初は、(年)月日時を表示させて、残りは時のみを表示される。
        年、月、日が変わる場合は、日や月が表示される。
        (年)月日時を表示させる最初の場所は、変更可能。

        Parameters
        ----------
        start_pos : int (default: 0)
            月日を表示させる場所を指定する。0 だと先頭。負の場合は先頭でも表示しない。
        ji : bool (default: False)
            Falseの場合は、時が、06と表示される。Trueの場合は、6時と表示される。
        year : bool (default: True)
            年を表示させるか否か。
        """
        self.start_pos = start_pos
        self.ji = ji
        self.year = year

    def __call__(self, x, pos=0) -> str:
        dt = dates.num2date(x)

        if self.ji:
            hour = f"{dt.hour}時"
        else:
            hour = "%H"
        if self.year:
            year = "\n%Y年"
        else:
            year = ""

        if pos == self.start_pos:
            return dt.strftime(f"{hour}\n{dt.month}月{dt.day}日{year}")
        if dt.hour == 0:
            if dt.day == 1:
                if dt.month == 1:
                    return dt.strftime(f"{hour}\n{dt.month}月{dt.day}日{year}")
                else:
                    return dt.strftime(f"{hour}\n{dt.month}月{dt.day}日")
            else:
                return dt.strftime(f"{hour}\n{dt.day}日")
        else:
            return dt.strftime(f"{hour}")
