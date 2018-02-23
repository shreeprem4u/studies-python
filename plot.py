import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()  # a new figure window
ax = fig.add_subplot(1, 1, 1)  # specify (nrows, ncols, axnum)
ax.set_title('Title of my subplot', fontsize=14)

# set tick labels for x-axis
ax.set_xticklabels(np.arange(10), rotation=45, fontsize=10 )
# set a title for x-axis
ax.set_xlabel("title for x-axis")
# choose where and how many ticks on the x-axes
#ax.set_xticks(np.arange(0, 10, 1.0))


# set tick labels for y-axis
ax.set_yticklabels(np.arange(10), rotation=45, fontsize=10 )
# set a title for y-axis
ax.set_ylabel("title for y-axis")
# choose where and how many ticks on the y-axes
#ax.set_yticks(np.arange(0, 5, 1.0))
ax.set_yticks(np.arange(-10, 5, 1.0))
x = [1,2,3,4,5,6,7,8,9,10]
y = [1,-2,3,-4,5,-6,7,-8,9,-10]

ax.set_xticks(x)
ax.plot(x,y)

plt.show()
