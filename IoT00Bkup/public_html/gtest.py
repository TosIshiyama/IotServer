@app.route('/graph2')
def graph2():
    import matplotlib.pyplot
    from matplotlib.backends.backend_agg import FigureCanvasAgg
    import random
    import string
    import os

    class TempImage(object):

        def __init__(self, file_name):
            self.file_name = file_name

        def create_png(self):
            fig, ax = matplotlib.pyplot.subplots()
            ax.set_title(u'IMINASHI GRAPH 2')
            x_ax = range(1, 284)
            y_ax = [x * random.randint(436, 875) for x in x_ax]
            ax.plot(x_ax, y_ax)

            canvas = FigureCanvasAgg(fig)
            canvas.print_figure(self.file_name)

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_value, traceback):
            os.remove(self.file_name)

    chars = string.digits + string.letters
    img_name = ''.join(random.choice(chars) for i in xrange(64)) + '.png'

    with TempImage(img_name) as img:
        img.create_png()
        return send_file(img_name, mimetype='image/png')

graph2()

