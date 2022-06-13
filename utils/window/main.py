import sys
from ctypes import windll
from tkinter import Tk
from tkinter.messagebox import askokcancel

from utils.constant import NAME_WITH_SPACE, WINDOW, PATH
from utils.window import frames


class Main(Tk):
    PACK_KWARGS = {
        'fill': 'both',
        'padx': 15,
        'pady': 15
    }

    def __init__(self):
        super().__init__()
        self.geometry(WINDOW.SIZE)
        self.minsize(WINDOW.WIDTH, WINDOW.HEIGHT)
        self.title(NAME_WITH_SPACE)
        self.iconbitmap(PATH.ICON_PATH)

        # High DPI
        # https://stackoverflow.com/questions/62794931/high-dpi-tkinter-re-scaling-when-i-run-it-in-spyder-and-when-i-run-it-direct-in
        windll.shcore.SetProcessDpiAwareness(2)
        scale_factor = windll.shcore.GetScaleFactorForDevice(0) / 75
        self.tk.call('tk', 'scaling', scale_factor)

        self.title_frame = frames.Title(self)
        self.search_frame = frames.Search(self)
        self.show_frame = frames.Show(self)
        self.filters_frame = frames.Filters(self)
        self.buttons_frame = frames.Buttons(self)

        self.title_frame.pack(**self.PACK_KWARGS)
        self.search_frame.pack(**self.PACK_KWARGS)
        self.show_frame.pack(**self.PACK_KWARGS, expand=True)
        self.filters_frame.pack(**self.PACK_KWARGS)
        self.buttons_frame.pack(**self.PACK_KWARGS)

        self.ask_license()

        self.mainloop()

    @staticmethod
    def ask_license():
        """
        Ask to accept license.
        :return:
        """
        if '--no-license' not in sys.argv and not askokcancel(
                '版权声明',
                'Copyright © 2022 Andy Zhang\n'
                '本程序是自由软件：你可以再分发之和/或依照由自由软件基金会发布的 GNU 通用公共许可证修改之，无论是版本 3 许可证，还是（按你的决定）任何以后版都可以。\n'
                '发布该程序是希望它能有用，但是并无保障；甚至连可销售和符合某个特定的目的都不保证。请参看 GNU 通用公共许可证，了解详情。\n'
                '你应该随程序获得一份 GNU 通用公共许可证的复本。如果没有，请看 https://www.gnu.org/licenses/。'
        ):
            exit()