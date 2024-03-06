class Arrows:

    def find_min_arrow_shots(self, points):
        points.sort(key=lambda x: x[1])
        arrow = 1
        n = len(points)
        end = points[0][1]
        for i in range(1, n):
            if points[i][0] > end:
                arrow += 1
                end = points[i][1]
        return arrow


a = Arrows()
points = [[10, 16], [2, 8], [1, 6], [7, 12]]
res = a.find_min_arrow_shots(points)
print(res)
