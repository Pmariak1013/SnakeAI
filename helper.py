import matplotlib.pyplot as plt
from IPython import display

plt.ion()

def plot(scores, mean):
    plt.show(block=False)
    plt.clf()
    plt.title('Training')
    plt.xlabel('Number of games')
    plt.ylabel('Score')
    plt.plot(scores, label='Score')
    plt.plot(mean, label='Mean Score')
    plt.ylim(ymin=0)

    if len(scores) > 0:
        plt.text(len(scores)-1, scores[-1], str(scores[-1]))
    if len(mean) > 0:
        plt.text(len(mean)-1, mean[-1], str(mean[-1]))

    plt.legend()
    plt.pause(0.1)