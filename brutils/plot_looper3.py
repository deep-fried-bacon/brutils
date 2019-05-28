

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

class PlotLooper3 :

    def __init__(self, data_groups, some_condition_func=None, title=None, plot_func=None) :
        # each data_group in data_groups must have plot(self,axis)


        # if data_groups has len() and getitem[]
        # self.data_group_iter = BidirectionalIter(data_groups)

        # if data_groups has get_max() and iget()
        self.data_group_iter = BiIterM(data_groups)

        self.some_condition_func = some_condition_func
        self.title = title
        self.plot_func = plot_func

        self.set_up_plot_gui()
        #self.cur_group = self.data_group_iter.next()
        self.next_plot()


    def plot(self) :
        #     ax = plt.gca()
        #     ax.cla()
        if self.plot_func == None :
            print("plot_func = None")
            self.cur_group.plot(self.fig)
        else :
            print("have plot_func")
            p = self.plot_func
            self.cur_group.p(plt.gca())
        plt.draw()

        self.fig.canvas.mpl_connect("key_press_event", self.on_key_press)

    def next(self, direct=1) :
        self.cur_group = self.data_group_iter.next(direct)

        if self.some_condition_func is not None :
            #while not some_condition_func(self.cur_group)
            if not self.some_condition_func(self.cur_group) : self.next(direct)


    def next_plot(self,*event) :
        self.next(1)
        self.plot()

    def prev_plot(self,*event) :
        self.next(-1)
        self.plot()

    def on_key_press(self, event) :
        if event.key == "left":
            self.prev_plot(self)
        elif event.key == "right":
            self.next_plot(self)


    def set_up_plot_gui(self) :

        DEFAULTS = {'next_button_loc': [0.7, 0.05, 0.1, 0.075],
                    'prev_button_loc': [0.81, 0.05, 0.1, 0.075],
                    'figsize': [10, 5]}

        self.fig = plt.figure(figsize=DEFAULTS['figsize'])

        if self.title != None:
            self.fig.suptitle(self.title)
        self.fig.show()


        # self.ax_prev = plt.axes(DEFAULTS['next_button_loc'])
        # self.ax_next = plt.axes(DEFAULTS['prev_button_loc'])
        # self.b_next = Button(self.ax_next, 'Next')
        # self.b_prev = Button(self.ax_prev, 'Prev')
        # self.b_next.on_clicked(self.next_plot)
        # self.b_prev.on_clicked(self.prev_plot)

        try :
            matplotlib.rcParams['keymap.back'].remove('left')
            matplotlib.rcParams['keymap.forward'].remove('right')
        except Exception :
            pass
        self.fig.canvas.mpl_connect("key_press_event", self.on_key_press)

        # self.fig.add_subplot(1,1,1)
        ipython_interactive = True
        if not ipython_interactive :
            plt.show()