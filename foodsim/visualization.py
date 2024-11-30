import matplotlib.pyplot as plt

def plot_results(data, title, xlabel, ylabel):
    """
    Simple function to visualize data.
    """
    plt.figure(figsize=(8, 5))
    plt.plot(data)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid()
    plt.show()