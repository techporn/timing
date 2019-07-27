import re

ERR_NONE = 0
ERR_IGNORE = 1
ERR_EXCEPTION = 2

        
class TimingParser:
    def __init__(self, token: tuple=("~", "_")):
        """ The parser to convert string to Signal object list.
        
        Keyword Arguments:
            token {tuple} -- String representing the high and low values of the signal. (default: {("~", "_")})
        """

        self.TOKEN_H, self.TOKEN_L = token
        self.pattern = re.compile("(\S+)\s*:(.*)")  # ラベルとシグナルを抽出する正規表現

    def parse(self, signals: str) -> list:
        """ Parse signal text. Return Signal object list.
 
        Arguments:
            signals {str} -- String representing signal and label.
        
        Returns:
            list -- Signal object list.
        """

        result = []

        for line in signals.splitlines():
            # ラベルとシグナルを取得
            label, s = self._parse_line(line)

            # シグナルを文字列から0, 1のリストにする
            signal = self._str_to_bin(s)
            result.append((label, signal))

        return result

    def _parse_line(self, line: str) -> tuple:
        """ parse the signal string actually.
        
        Arguments:
            line {[str]} -- String representing signal and label.
        
        Raises:
            ValueError: Will be raised when got invalid format.
        
        Returns:
            tuple -- tuple of label and signal string. e.g. ("label", "~__~~")
        """

        res = self.pattern.match(line)
        if res is None:
            raise ValueError("Invalid formtat")
        else:
            return res.groups()

    def _str_to_bin(self, signal: str, error=ERR_NONE) -> list:
        """ convert string to binary or None.
        
        Arguments:
            signal {str} -- String representing signal.
        
        Keyword Arguments:
            error {[type]} -- Error (default: {ERR_NONE})
        
        Raises:
            TypeError: Will be raised when this method gets a not a token and error is ERR_EXCEPTION.
        
        Returns:
            [list] -- List with 0, 1 or None.
        """

        binary = []
        for i in signal:
            if i == self.TOKEN_H:
                binary.append(1)
            elif i == self.TOKEN_L:
                binary.append(0)

            # トークン以外だった場合
            else:
                if error == ERR_NONE:        binary.append(None)
                elif error == ERR_IGNORE:    pass
                elif error == ERR_EXCEPTION: raise TypeError()

        return binary

def read_signal(filename) -> list:
    signals = []
    parser = TimingParser()

    with open(filename, "r") as f:
        t = f.read()
        for i in parser.parse(t):
            label, data = i
            signals.append((label, data))
            
    return signals

if __name__ == "__main__":
    print(read_signal("chart-ccw"))
