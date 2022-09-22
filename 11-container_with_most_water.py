"""
Given an array of heights, which represents the heights of vertical lines drawn on a graph.
Find two lines that form a container that holds the most water when combined
with the horizontal axis.
The height of this container will be the shorter of the two lines:

Note: We cannot tilt any water containers.
"""

def max_water_area_container(height):
    print('height array: {0}'.format(height))

    area = -1
    for i in range(0, len(height) - 1):
        for j in range(i + 1, len(height)):
            temp_area = min(height[i], height[j]) * (j - i)
            if temp_area > area:
                area = temp_area

    print(' area: {0}'.format(area))
    return area

def max_water_area_container_1(height):
    print('height array: {0}'.format(height))

    left = 0
    right = len(height) - 1
    area = -1
    while left < right:
        temp_area = min(height[left], height[right]) * (right - left)
        if temp_area > area:
            area = temp_area

        if right == left + 1:
            break

        if height[left + 1] - height[left] >= height[right - 1] - height[right]:
            left += 1
        else:
            right -= 1

    print(' area: {0}'.format(area))
    return area

if __name__ == '__main__':
    max_water_area_container_1([1, 1])
    max_water_area_container_1([1, 8, 6, 2, 5, 4, 8, 3, 7])
    max_water_area_container([1, 8, 6, 2, 5, 4, 8, 3, 7])
    max_water_area_container([20, 30, 9, 69])
    max_water_area_container([13, 18, 12, 8])
    max_water_area_container([45, 32, 56, 99])
    max_water_area_container([23, 20])
