from math import sqrt
def prod_non_zero_diag(x):
    """Compute product of nonzero elements from matrix diagonal.

    input:
    x -- 2-d numpy array
    output:
    product -- integer number


    Not vectorized implementation.
    """

    len_diag = min(len(x), len(x[0]))
    prod = 1
    for i in range(len_diag):
        if(x[i][i] != 0):
            prod *= x[i][i]
    return prod


def are_multisets_equal(x, y):
    """Return True if both vectors create equal multisets.

    input:
    x, y -- 1-d numpy arrays
    output:
    True if multisets are equal, False otherwise -- boolean

    Not vectorized implementation.
    """
    x.sort()
    y.sort()
    return x == y


def max_after_zero(x):
    """Find max element after zero in array.

    input:
    x -- 1-d numpy array
    output:
    maximum element after zero -- integer number

    Not vectorized implementation.
    """

    after_zero_list = list()
    for i in range(1, len(x)):
        if(not x[i - 1]):
            after_zero_list.append(x[i])
    if len(after_zero_list) == 0:
        return -100000
    return max(after_zero_list)


def convert_image(img, coefs):
    """Sum up image channels with weights from coefs array

    input:
    img -- 3-d numpy array (H x W x 3)
    coefs -- 1-d numpy array (length 3)
    output:
    img -- 2-d numpy array

    Not vectorized implementation.
    """
    height = len(img)
    width = len(img[0])
    result_img = list()
    for i in range(height):
        curr_str = list()
        for j in range(width):
            sum = 0
            for k in range(len(coefs)):
                sum += img[i][j][k] * coefs[k]
            curr_str.append(sum)
        result_img.append(curr_str)
    return result_img


def run_length_encoding(x):
    """Make run-length encoding.

    input:
    x -- 1-d numpy array
    output:
    elements, counters -- integer iterables

    Not vectorized implementation.
    """

    elements = [x[0]]
    counts = []
    cnt = 1
    for i in range(len(x)):
        if (x[i - 1] == x[i]):
            cnt += 1
        else:
            elements.append(x[i - 1])
            counts.append(cnt)
            cnt = 1
    counts.append(cnt)
    return (elements, counts)


def pairwise_distance(x, y):
    """Return pairwise object distance.

    input:
    x, y -- 2d numpy arrays
    output:
    distance array -- 2d numpy array

    Not vectorized implementation.
    """

    res = list()
    for i in range(len(x)):
        cur = list()
        for j in range(len(y)):
            dist = 0
            for k in range(len(x[0])):
                dist += (x[i][k] - y[j][k]) ** 2
            cur.append(sqrt(dist))
        res.append(cur)
    return res
