FACE_COUNT = {
    'Tetrahedron': 4,
    'Cube': 6,
    'Octahedron': 8,
    'Dodecahedron': 12,
    'Icosahedron': 20,
}

n = int(input())

total = 0
while n > 0:
    polyhedron = input()
    total += FACE_COUNT[polyhedron]
    n -= 1

print(total)