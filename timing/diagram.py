import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


class Diagram:
    def __init__(self):
        self.timing = []
        self.x_length = 0

    def add_timing(self, label: str, data: list):
        self.timing.append((label, data))
        self.x_length = len(data)

        # l = len(data)
        # if self.x_length < l:
        #     self.x_length = l

    def save(self, path: str):
        self.fig.savefig(path)

    def plot(self):
        """ plot timing diagram
        
        Arguments:
            signals {list} -- Signal object list. 
        """

        self.fig, axis = plt.subplots(len(self.timing), sharex=True)  # 複数グラフを表示するときに使う.この場合は縦に3つ並べて、x軸を共有
        self.x = list(range(self.x_length))

        print(type(axis))
        # axisが複数
        if isinstance(axis, np.ndarray):
            for i, a in enumerate(axis):
                label, data = self.timing[i]
                self._plot_signal(a, label, data)   # オプションを設定する

        # axisがひとつ
        else:
            label, data = self.timing[0]
            self._plot_signal(axis, label, data)    # オプションを設定する

        plt.show()


    def _plot_signal(self, axes: plt.Axes, label: str, data: list):
        """ set detaile diagram
        
        Arguments:
            axes {matplotlib.Axes} -- Target to set.
            signal {Signal} -- Signal object to plot.
        """

        axes.step(self.x, data, label=label, where="post")    # データをステップでプロット

        # 四方の枠を非表示にする
        axes.spines['right'].set_visible(False)    # 左枠非表示
        axes.spines['left'].set_visible(False)     # 右枠非表示
        axes.spines['top'].set_visible(False)      # 上枠非表示
        axes.spines['bottom'].set_visible(False)   # 下枠非表示

        # axes.grid(which="both", linestyle='--')                   # グリッド線表示
        axes.set_ylabel(label, rotation=0)         # デフォルトだと回転してしまうのでrotation=0とする
        axes.yaxis.set_label_coords(-0.1, 0.5)     # y軸のラベルの位置を調整する

        axes.set_xticks(np.linspace(start=0, stop=1, num=2))     # 0か1の2値で軸を取る
        axes.set_yticks(np.linspace(start=0, stop=1, num=2))     # 0か1の2値で軸を取る
        axes.tick_params(labelbottom=False, labelleft=False, color='white')   # 下と左の目盛りを消す


def main():
    d = Diagram()
    d.add_timing("Q1", [0,1,0,1,0,1,1])
    d.add_timing("Q2", [0,0,1,1,0,0,0])
    d.add_timing("Q3", [0,0,0,1,1,0,0])
    d.plot()

main()