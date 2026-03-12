"""Julia set generator without optional PIL-based image drawing"""
import time
from PIL import Image
import array

# area of complex space to investigate
x1, x2, y1, y2 = -1.8, 1.8, -1.8, 1.8
c_real, c_imag = -0.62772, -.42193


def show_greyscale(output_raw, width, height, max_iterations):
    """Convert list to array, show using PIL"""
    # convert our output to PIL-compatible input
    # scale to [0...255]
    max_iterations = float(max(output_raw))
    # print(max_iterations)
    scale_factor = float(max_iterations)
    scaled = [int(o / scale_factor * 255) for o in output_raw]
    # print(scaled[500000:500030])
    output = array.array('B', scaled)  # array of unsigned ints
    # print(output[500000:500030])
    # print(max(output))
    # display with PIL
    im = Image.new("L", (width, height))
    # EXPLAIN RAW L 0 -1
    im.frombytes(output.tobytes(), "raw", "L", 0, -1)
    im.show()


def show_false_greyscale(output_raw, width, height, max_iterations):
    """
    Pillow Image.frombytes() 範例

    需求
    1. RGB 模式
    2. raw data 值 0 ~ 300
    3. 0 → 白色
    4. 300 → 黑色
    5. 中間值使用彩虹七色
    6. 影像大小 1000x1000
    """

# ------------------------------------
# 定義彩虹七色
# ------------------------------------
# 彩虹順序
# Red → Orange → Yellow → Green → Blue → Indigo → Violet
    rainbow_colors = [
        (255, 0, 0),     # Red
        (255, 127, 0),   # Orange
        (255, 255, 0),   # Yellow
        (0, 255, 0),     # Green
        (0, 0, 255),     # Blue
        (75, 0, 130),    # Indigo
        (148, 0, 211)    # Violet
    ]

# 將 0~300 分成 7 段
    STEP = max_iterations / len(rainbow_colors)

# ------------------------------------
# 建立 bytearray 儲存 RGB bytes
# ------------------------------------
    pixel_bytes = bytearray()

# ------------------------------------
# 產生測試 raw data
# 這裡使用 x+y 做漸層示範
# ------------------------------------
    for value in output_raw:

        # ------------------------------
        # 特殊值處理
        # ------------------------------
        if value == 0:
            r, g, b = (255, 255, 255)  # 白色

        elif value >= 300:
            r, g, b = (0, 0, 0)        # 黑色

        else:
            # --------------------------
            # 計算彩虹階段
            # --------------------------
            index = int(value / STEP)

            # 防止 index 超出範圍
            if index >= len(rainbow_colors):
                index = len(rainbow_colors) - 1

            r, g, b = rainbow_colors[index]

        # ------------------------------
        # 加入 RGB bytes
        # ------------------------------
        pixel_bytes.extend([r, g, b])

# ------------------------------------
# 使用 Image.frombytes 建立影像
# ------------------------------------
    img = Image.frombytes(
        mode="RGB",
        size=(width, height),
        data=bytes(pixel_bytes)
    )

# ------------------------------------
# 儲存與顯示影像
# ------------------------------------
    img.save("julia2.png")
    img.show()


def calculate_z_serial_purepython(maxiter, zs, cs):
    """Calculate output list using Julia update rule"""
    output = [0] * len(zs)
    for i in range(len(zs)):
        n = 0
        z = zs[i]
        c = cs[i]
        while abs(z) < 2 and n < maxiter:
            z = z * z + c
            n += 1
        output[i] = n
    return output


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
    width = len(x)
    height = len(y)
    # build a list of co-ordinates and the initial condition for each cell.
    # Note that our initial condition is a constant and could easily be removed,
    # we use it to simulate a real-world scenario with several inputs to our function
    zs = []
    cs = []
    for ycoord in y:
        for xcoord in x:
            zs.append(complex(xcoord, ycoord))
            cs.append(complex(c_real, c_imag))

    print("Length of x:", len(x))
    print("Total elements:", len(zs))
    start_time = time.time()
    output = calculate_z_serial_purepython(max_iterations, zs, cs)
    end_time = time.time()
    secs = end_time - start_time
    print(calculate_z_serial_purepython.__name__ + " took", secs, "seconds")

    assert sum(output) == 33219980  # this sum is expected for 1000^2 grid with 300 iterations

    if draw_output:
        show_greyscale(output, width, height, max_iterations)
    else:
        show_false_greyscale(output, width, height, max_iterations)


if __name__ == "__main__":
    # Calculate the Julia set using a pure Python solution with
    # reasonable defaults for a laptop
    # set draw_output to True to use PIL to draw an image
    calc_pure_python(draw_output=False, desired_width=1000, max_iterations=300)
