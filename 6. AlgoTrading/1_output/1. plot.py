import matplotlib.pyplot as plt
import pandas as pd


if __name__ == "__main__":    
    df = pd.read_csv('/Users/blenyesibalazs/DevProjects/MCCPython/6. AlgoTrading/1_output/ROJTO.csv').set_index('date')
    df[['open', 'high', 'low', 'close']].plot()
    plt.show()