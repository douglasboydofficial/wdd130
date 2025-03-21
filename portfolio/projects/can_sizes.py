#imports the math function.
import math


def main():
    """Calls the compute_volume, compute_surface_area,
    and compute_cost_efficiency functions and stores them
    in functions. Then , computes the storage efficiency.
    prints each can, the storage efficiency, and cost of each can.
    """
    volume = compute_volume (6.83, 10.16)
    surface_area = compute_surface_area (6.83, 10.16)
    cost = compute_cost_efficiency (volume, 0.28)
    storage_efficiency = volume / surface_area
    print (f"#1 Picnic {storage_efficiency:.2f} ${cost:.6f}")

    volume = compute_volume (7.78, 11.91)
    surface_area = compute_surface_area (7.78, 11.91)
    cost = compute_cost_efficiency (volume, 0.43)
    storage_efficiency = volume / surface_area
    print (f"#1 Tall {storage_efficiency:.2f} ${cost:.6f}")

    volume = compute_volume (8.73, 11.59)
    surface_area = compute_surface_area (8.73, 11.59)
    cost = compute_cost_efficiency (volume, 0.45)
    storage_efficiency = volume / surface_area
    print (f"#2 {storage_efficiency:.2f} ${cost:.6f}")

    volume = compute_volume (10.32, 11.91)
    surface_area = compute_surface_area (10.32, 11.91)
    cost = compute_cost_efficiency (volume, 0.61)
    storage_efficiency = volume / surface_area
    print (f"#2.5 {storage_efficiency:.2f} ${cost:.6f}")

    volume = compute_volume (10.79, 17.78)
    surface_area = compute_surface_area (10.79, 17.78)
    cost = compute_cost_efficiency (volume, 0.86)
    storage_efficiency = volume / surface_area
    print (f"#3 Cylinder {storage_efficiency:.2f} ${cost:.6f}")

    volume = compute_volume (13.02, 14.29)
    surface_area = compute_surface_area (13.02, 14.29)
    cost = compute_cost_efficiency (volume, 0.83)
    storage_efficiency = volume / surface_area
    print (f"#5 {storage_efficiency:.2f} ${cost:.6f}")

    volume = compute_volume (5.40, 8.89)
    surface_area = compute_surface_area (5.40, 8.89)
    cost = compute_cost_efficiency (volume, 0.22)
    storage_efficiency = volume / surface_area
    print (f"#6Z {storage_efficiency:.2f} ${cost:.6f}")

    volume = compute_volume (6.83, 7.62)
    surface_area = compute_surface_area (6.83, 7.62)
    cost = compute_cost_efficiency (volume, 0.26)
    storage_efficiency = volume / surface_area
    print (f"#8Z short {storage_efficiency:.2f} ${cost:.6f}")

    volume = compute_volume (15.72, 17.78)
    surface_area = compute_surface_area (15.72, 17.78)
    cost = compute_cost_efficiency (volume, 1.53)
    storage_efficiency = volume / surface_area
    print (f"#10 {storage_efficiency:.2f} ${cost:.6f}")

    volume = compute_volume (6.83, 12.38)
    surface_area = compute_surface_area (6.83, 12.38)
    cost = compute_cost_efficiency (volume, 0.34)
    storage_efficiency = volume / surface_area
    print (f"#211 {storage_efficiency:.2f} ${cost:.6f}")

    volume = compute_volume (7.62, 11.27)
    surface_area = compute_surface_area (7.62, 11.27)
    cost = compute_cost_efficiency (volume, 0.38)
    storage_efficiency = volume / surface_area
    print (f"#300 {storage_efficiency:.2f} ${cost:.6f}")

    volume = compute_volume (8.10, 11.11)
    surface_area = compute_surface_area (8.10, 11.11)
    cost = compute_cost_efficiency (volume, 0.42)
    storage_efficiency = volume / surface_area
    print (f"#303 {storage_efficiency:.2f} ${cost:.6f}")


def compute_volume(radius, height):
    """Computes the volume of a can and returns the
    value to main function.
    """
    volume = math.pi * (radius ** 2) * height

    return volume


def compute_surface_area(radius, height):
    """Computes the surface area of a can and 
    returns the value to main function.
    """
    surface_area = 2 * math.pi * radius * (radius + height)

    return surface_area


def compute_cost_efficiency (volume, cost):
    """computes the cost efficiency of a can and
    returns the value to main function. #2 of the stretch
    challenges.
    """
    cost_efficiency = cost / volume
                       
    return cost_efficiency 


#Calls back to the main function.
main ()
