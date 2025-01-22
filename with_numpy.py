"""
----- Without using numpy -----
"""
import matplotlib.pyplot as plt
import numpy as np
import random as r
import time

MAX_X = 100 # Just random IDK
MAX_Y = 150 # Same here
LINES = 10000 # numbers of lines
figure, axis = plt.subplots(1, 2)

x1_b = r.randint(0, MAX_X)
x2_b = r.randint(x1_b, MAX_X)
y1_b = r.randint(0, MAX_Y)
y2_b = r.randint(y1_b, MAX_Y)

rect_cord_1 = np.array([x1_b, x1_b, x2_b, x2_b, x1_b])
rect_cord_2 = np.array([y1_b, y2_b, y2_b, y1_b, y1_b])

start_time = time.time()
line_cord = np.random.randint(0, [MAX_X, MAX_Y, MAX_X, MAX_Y], size=(LINES, 4))

all_x1 = line_cord[:, 0]
all_y1 = line_cord[:, 1]
all_x2 = line_cord[:, 2]
all_y2 = line_cord[:, 3]

check_x = (x1_b < all_x1) & (all_x1 < x2_b) & (x1_b < all_x2) & (all_x2 < x2_b)
check_y = (y1_b < all_y1) & (all_y1 < y2_b) & (y1_b < all_y2) & (all_y2 < y2_b)

filtered_line = line_cord[(check_x & check_y)]

axis[0].plot([all_x1, all_x2],[all_y1, all_y2])
axis[0].set_title('All lines')
axis[1].plot(rect_cord_1, rect_cord_2, label='rectangle Bound')
axis[1].plot([filtered_line[:, 0], filtered_line[:, 2]], [filtered_line[:, 1], filtered_line[:, 3]])
axis[1].set_title(f'Filtered {len(filtered_line)} lines')
end_time = time.time()
print(f"Program time: {end_time - start_time}")

plt.show()

# End of file
