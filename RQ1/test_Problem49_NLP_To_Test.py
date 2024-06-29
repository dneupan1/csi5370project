from typing import List

def isRectangleCover(rectangles: List[List[int]]) -> bool:
    """
    This function returns true if all the rectangles together form an exact cover of a rectangular region, otherwise false.
    
    :param rectangles: List[List[int]] - List of rectangles where each rectangle is represented by [xi, yi, ai, bi]
    :return: bool - True if the rectangles form an exact cover, False otherwise
    """
    
    def add_point(point_set, point):
        if point in point_set:
            point_set.remove(point)
        else:
            point_set.add(point)
    
    # Variables to keep track of the corners of the overall rectangle
    min_x = min_y = float('inf')
    max_x = max_y = float('-inf')
    
    # Set to track unique points
    point_set = set()
    # Variable to keep track of the total area of small rectangles
    total_area = 0
    
    for x1, y1, x2, y2 in rectangles:
        # Update the overall bounding box
        min_x = min(min_x, x1)
        min_y = min(min_y, y1)
        max_x = max(max_x, x2)
        max_y = max(max_y, y2)
        
        # Add area of the current rectangle to the total area
        total_area += (x2 - x1) * (y2 - y1)
        
        # Add or remove the corners of the current rectangle to/from the set
        add_point(point_set, (x1, y1))
        add_point(point_set, (x1, y2))
        add_point(point_set, (x2, y1))
        add_point(point_set, (x2, y2))
    
    # The area of the bounding box
    bounding_box_area = (max_x - min_x) * (max_y - min_y)
    
    # The area covered by all rectangles should be equal to the area of the bounding box
    if total_area != bounding_box_area:
        return False
    
    # The set should contain exactly 4 points: the corners of the bounding box
    if len(point_set) != 4 or \
       (min_x, min_y) not in point_set or \
       (min_x, max_y) not in point_set or \
       (max_x, min_y) not in point_set or \
       (max_x, max_y) not in point_set:
        return False
    
    return True