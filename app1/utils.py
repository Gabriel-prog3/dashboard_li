import matplotlib.pyplot as plt
import base64
from io import BytesIO


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode("utf-8")
    buffer.close()
    return graph


def get_plot(x, y, y2, title, size=(5.5, 3), label_1="", label_2=""):
    # plt.switch_backend("AGG")
    # plt.figure(figsize=size)
    # plt.title(title)

    # plt.plot(x, y2, label="cccc")
    # plt.plot(x, y, label="9999")
    # plt.xticks(rotation=45)
    # plt.tight_layout()
    fig, ax = plt.subplots(figsize=size)
    ax.set_title(title)
    ax.plot(x, y2, label=label_2)
    ax.plot(x, y, label=label_1)
    ax.legend(loc="upper right")

    graph = get_graph()
    return graph
