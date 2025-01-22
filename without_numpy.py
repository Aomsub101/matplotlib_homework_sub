"""
----- Without using numpy -----
"""
import matplotlib.pyplot as plt
import random as r
import time

MAX_X = 100 # Just random IDK
MAX_Y = 150 # Same here
LINES = 1000 # numbers of lines

x1_b = r.randint(0, MAX_X)
x2_b = r.randint(x1_b, MAX_X)
y1_b = r.randint(0, MAX_Y)
y2_b = r.randint(y1_b, MAX_Y)   

sq_cord_1 = [x1_b, x1_b, x2_b, x2_b, x1_b]
sq_cord_2 = [y1_b, y2_b, y2_b, y1_b, y1_b]

start_time = time.time()
line_cord = [[[
            r.randint(0, MAX_X), r.randint(0, MAX_Y)
            ] for _ in range(2)
        ] for _ in range(LINES)
    ]

end_time = time.time()
print(f"Program time: {end_time - start_time}")

for l in range(LINES):
    x1 = line_cord[l][0][0]
    y1 = line_cord[l][0][1]
    x2 = line_cord[l][1][0]
    y2 = line_cord[l][1][1]
    check_x_axis = (x1 >= x1_b and x1 <= x2_b) and (x2 <= x2_b and x2 >= x1_b)
    check_y_axis = (y1 >= y1_b and y1 <= y2_b) and (y2 <= y2_b and y2 >= y1_b)
    if check_x_axis and check_y_axis:
        plt.plot([x1, x2], [y1, y2])

plt.plot(sq_cord_1, sq_cord_2, label='Square Bound')
plt.title(f'Filter {LINES} lines plots.')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()



# End of file
