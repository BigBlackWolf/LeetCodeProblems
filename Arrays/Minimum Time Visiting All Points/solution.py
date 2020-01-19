class Solution:
    def minTimeToVisitAllPoints(self, points) -> int:
        location = points[0]
        counter = 0
        for i in points:
            x = (i[0] - location[0]) ** 2
            while location != i:
                if i[0] > location[0] and i[1] > location[1]:
                    location[0] += 1
                    location[1] += 1
                    counter += 1
                elif i[0] < location[0] and i[1] < location[1]:
                    location[0] -= 1
                    location[1] -= 1
                    counter += 1
                elif i[0] < location[0] and i[1] > location[1]:
                    location[0] -= 1
                    location[1] += 1
                    counter += 1
                elif i[0] > location[0] and i[1] < location[1]:
                    location[0] += 1
                    location[1] -= 1
                    counter += 1
                elif i[0] > location[0] and i[1] == location[1]:
                    location[0] += 1
                    counter += 1
                elif i[0] < location[0] and i[1] == location[1]:
                    location[0] -= 1
                    counter += 1
                elif i[0] == location[0] and i[1] < location[1]:
                    location[1] -= 1
                    counter += 1
                elif i[0] == location[0] and i[1] > location[1]:
                    location[1] += 1
                    counter += 1
        return counter
