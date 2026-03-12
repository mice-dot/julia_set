"""Julia set generator without optional PIL-based image drawing"""
import time

# area of complex space to investigate
x1, x2, y1, y2 = -1.8, 1.8, -1.8, 1.8
c_real, c_imag = -0.62772, -.42193


@profile
def calculate_z_serial_purepython(maxiter, x, y, d_w):
    """Calculate output list using Julia update rule"""
    global c_real, c_imag
    time.sleep(0.25)
    with profile.timestamp("creat_output_list"):
        output = [0] * (d_w ** 2)
    time.sleep(0.25)
    with profile.timestamp("calculate_output"):
        c = complex(c_real, c_imag)
        i = 0
        for ycoord in y:
            for xcoord in x:
                z = complex(xcoord, ycoord)
                n = 0
                while n < maxiter and abs(z) < 2:
                    z = z * z + c
                    n += 1
                output[i] = n
                i = i + 1
    time.sleep(0.25)
    return output


@profile
def calc_pure_python(draw_output, desired_width, max_iterations):
    """Create a list of complex co-ordinates (zs) and complex parameters (cs), build Julia set and display"""
    x_step = (x2 - x1) / desired_width
    y_step = (y1 - y2) / desired_width
    x = []
    y = []
    ycoord = y2
    while ycoord > y1:
        y.append(ycoord)
        ycoord += y_step
    xcoord = x1
    while xcoord < x2:
        x.append(xcoord)
        xcoord += x_step
    # set width and height to the generated pixel counts, rather than the
    # pre-rounding desired width and height
    # build a list of co-ordinates and the initial condition for each cell.
    # Note that our initial condition is a constant and could easily be removed,
    # we use it to simulate a real-world scenario with several inputs to our function

    print("Length of x:", len(x))
    time.sleep(0.25)
    start_time = time.time()
    output = calculate_z_serial_purepython(max_iterations, x, y, desired_width)
    end_time = time.time()
    secs = end_time - start_time
    print("Total elements:", len(output))
    print(calculate_z_serial_purepython.__name__ + " took", secs, "seconds")

    assert sum(output) == 33219980  # this sum is expected for 1000^2 grid with 300 iterations


# Calculate the Julia set using a pure Python solution with
# reasonable defaults for a laptop
# set draw_output to True to use PIL to draw an image
calc_pure_python(draw_output=False, desired_width=1000, max_iterations=300)
