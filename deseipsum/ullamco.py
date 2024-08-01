import matplotlib.pyplot as plt

# Create a figure with subplots
fig, axs = plt.subplots(2, 2)

# Add some plots to the subplots
axs[0, 0].plot([1, 2, 3], [1, 4, 9])
axs[0, 1].plot([1, 2, 3], [1, 2, 3])
axs[1, 0].plot([1, 2, 3], [3, 2, 1])
axs[1, 1].plot([1, 2, 3], [1, 0.5, 0.33])

# Adjust layout and save the figure with tight bounding box
plt.tight_layout()
plt.savefig('subplots_example.png', bbox_inches='tight')

# Show the plot
plt.show()
