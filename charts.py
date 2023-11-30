#%%
# #Document to Graph
import matplotlib.pyplot as plt

def generate_bar_char(key, value):
    fig, ax = plt.subplots()
    ax.bar(key, value)
    plt.show()
    
    
if __name__ == '__main__':
    generate_bar_char(key, value)
#%%