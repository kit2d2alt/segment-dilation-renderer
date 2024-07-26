import matplotlib.pyplot as plt

# Line segment endpoints
original_x1 = 6
original_y1 = 9
original_x2 = 9
original_y2 = 9

# Scale factor
scale_factor = 2/3

new_x1 = original_x1 * scale_factor
new_y1 = original_y1 * scale_factor
new_x2 = original_x2 * scale_factor
new_y2 = original_y2 * scale_factor

plt.figure(figsize=(5, 5))  # Set the figure size

plt.plot([original_x1, original_x2], [original_y1, original_y2], 'b-', label='Original')

plt.plot([new_x1, new_x2], [new_y1, new_y2], 'r-', label='Dilated (2/3)')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Segment Dilation')

plt.legend()

plt.grid(True)
plt.show()
