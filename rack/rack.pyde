from math import sin, cos, radians, sqrt

size_list  = [1000, 1000]
center = [ size_list[0]/2 - 1, size_list[1]/2 - 1]
tri_p = {'x': [center[0]], 'y': [center[1]]}

rotations = {'0': [60, 60, 120, 120],
             '45': [105, 105, 165, 165],
             '90': [150, 150, 210, 210],
             '135': [195, 195, 255, 255],
             '180': [240, 240, 300, 300],
             '225': [285, 285, 345, 345],
             '270': [330, 330, 30, 30],
             '315': [5, 5, 75, 75] }
            
def fabs(x):
    return sqrt(x**2)

def draw_triangle(angles = rotations['0'], edge = 150):
    i = 0
    for angle in angles:
        if i == 0 or i % 2 == 0:
             tri_p['x'].append(center[0] + edge * cos(radians(angles[i])))
             i += 1
        else:
            tri_p['y'].append(center[0] + edge * sin(radians(angles[i])))
            i += 1
            
    return triangle(tri_p['x'][0], tri_p['y'][0], tri_p['x'][1], tri_p['y'][1], tri_p['x'][2], tri_p['y'][2])


def draw_dashes(d_len = 15, d_gap = 15, angles = rotations['0']):
    
    if round(tri_p['y'][1], 2) == round(tri_p['y'][2], 2):
        base_len = fabs(tri_p['x'][2] - tri_p['x'][1])
        
        if tri_p['x'][1] > tri_p['x'][2]:
            while(base_len >= 0):
                line(tri_p['x'][1] - base_len, 
                     tri_p['y'][1], 
                     tri_p['x'][1] - base_len + d_len * cos(radians(145)), 
                     tri_p['y'][1] + d_len * sin(radians(145)))
                base_len -= d_gap
        else:
            while (base_len >= 0):
                line(tri_p['x'][1] + base_len, 
                     tri_p['y'][1], 
                     tri_p['x'][1] + base_len + d_len * cos(radians(35)), 
                     tri_p['y'][1] - d_len * sin(radians(35)))
                base_len -= d_gap
                
    if round(tri_p['x'][1], 2) == round(tri_p['x'][2], 2):
        base_len = fabs(tri_p['y'][2] - tri_p['y'][1])
        
        if tri_p['y'][1] > tri_p['y'][2]:
            while(base_len >= 0):
                line(tri_p['x'][1],
                     tri_p['y'][1] - base_len,
                     tri_p['x'][1] + d_len * sin(radians(305)),
                     tri_p['y'][1] - base_len + d_len * cos(radians(305)))
                base_len -= d_gap
            
        else:
            while(base_len >= 0):
                line(tri_p['x'][1],
                     tri_p['y'][1] + base_len,
                     tri_p['x'][1] + d_len * sin(radians(45)),
                     tri_p['y'][1] + base_len + d_len * cos(radians(45)))
                base_len -= d_gap

    else:
        temp_dict = {'x': [], 'y': []}
        for x in range(size_list[0]):
            for y in range(size_list[1]):
                if round((x - tri_p['x'][1]) / (tri_p['x'][2] - tri_p['x'][1]), 2) == round((y - tri_p['y'][1]) / (tri_p['y'][2] - tri_p['y'][1]), 2) and x not in temp_dict['x'] and (tri_p['x'][1] <= x <= tri_p['x'][2] or tri_p['x'][2] <= x <= tri_p['x'][1]):
                    temp_dict['y'].append(y)
                    temp_dict['x'].append(x)
                        
        n = 0
        for x in temp_dict['x']:
            if n == 0 or n % d_gap == 0:
                line(x, temp_dict['y'][n], x + d_len * cos(radians(angles[0] + 70)), temp_dict['y'][n] + d_len * sin(radians(angles[0] + 70)))
            n += 1
    
    
def draw_complete(angles = rotations['135'], edge = 150, d_len = 15, d_gap = 10):
    return draw_triangle(angles, edge), draw_dashes(d_len, d_gap, angles), circle(center[0], center[1], 20)

def setup():
    size(size_list[0], size_list[1])
    draw_complete()
    
