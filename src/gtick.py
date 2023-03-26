from warnings import warn
from matplotlib import ticker, dates


class JDayHourFormatter(ticker.Formatter):
    def __init__(self, start_pos: int = 0, ji: bool = False, year: bool = True):
        """日本語の年月日時フォーマッター

        先頭は、(年)月日時を表示される。
        残りは、時のみが表示されるが、年、月、日が変わる場合は、時と合わせて(年)月日表示される。
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

        if dt.minute != 0 or dt.second != 0:
            warn("00分以外のところに置かれています。matplotlib.dates.HourLocatorと組み合わせるべきです")

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
        return dt.strftime(f"{hour}")
