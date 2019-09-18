def is_in_mandelbrot(c, r=5, max_ite = 20):
    z = c
    i = 0
    if c.mod == 0:
        return i

    while (abs(c.re - z.re) <= r or abs(c.im - z.im) <= r) and i <= max_ite:
        z = z**2 + c
        i += 1

    return i