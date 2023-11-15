def point(x, y):
    return x, y

def line_equation_of(p1, M):
    C = p1[1] - M * p1[0]
    return f"y = {M:.2f}x + {C:.2f}"

point_p1 = point(3, 9)
gradien_M = 5


persamaan_garis = line_equation_of(point_p1, gradien_M)

print("Persamaan garis yang melalui titik (3,9) dan bergradien 5:")
print(persamaan_garis)
