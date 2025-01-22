"""
----- Without using numpy -----
"""
import matplotlib.pyplot as plt
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

sq_cord_1 = [x1_b, x1_b, x2_b, x2_b, x1_b]
sq_cord_2 = [y1_b, y2_b, y2_b, y1_b, y1_b]

start_time = time.time()
line_cord = [[
            r.randint(0, MAX_X), r.randint(0, MAX_Y), r.randint(0, MAX_X), r.randint(0, MAX_Y)
        ] for _ in range(LINES)
    ]

cnt = 0
for l in range(LINES):
    x1 = line_cord[l][0]
    y1 = line_cord[l][1]
    x2 = line_cord[l][2]
    y2 = line_cord[l][3]
    axis[0].plot([x1, x2], [y1, y2])
    check_x_axis = x1_b < x1 < x2_b and x1_b < x2 < x2_b
    check_y_axis = y1_b < y1 < y2_b and y1_b < y2 < y2_b
    if check_x_axis and check_y_axis:
        cnt += 1
        axis[1].plot([x1, x2], [y1, y2])

axis[1].plot(sq_cord_1, sq_cord_2, label='Square Bound')
axis[0].set_title('All lines')
axis[1].set_title(f'Filtered {cnt} lines')
end_time = time.time()
print(f"Program time: {end_time - start_time}")

plt.show()

# End of file
