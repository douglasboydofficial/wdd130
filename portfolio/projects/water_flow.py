

def water_column_height (tower_height, tank_height):
    """Calculates and returns the height of a column of water
    from a tower height and a tank wall height.
    """
    # t is the height of the tower.
    # w is the height of the walls of the tank that is on top of the tower.

    t = tower_height
    w = tank_height

    # h is the height of the water column.
    h = t + 3 * w / 4

    return h


def pressure_gain_from_water_height (height):
    """Calculates and returns the pressure caused
    by Earth's gravity pulling on the water stored in
    an elevator tank.
    """
    # Pp is the pressure in kilopascals.
    # p is the density of water (998.2 kilogram / meter cubed).
    # g is the acceleration from Earths gravity (9.80665 meter / second squared).
    # h is the height of the water column in meters.

    p = WATER_DENSITY
    g = EARTH_ACCELERATION_OF_GRAVITY
    h = height

    Pp = p * g * h / 1000

    return Pp


def pressure_loss_from_pipe (pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """Calculates and returns the water pressure lost because of the friction between the water
    and the walls of a pipe that it flows through.
    """
    # Plp is the lost pressure in kilopascals.
    # f is the pipe's friction factor.
    # L is the length of the pipe in meters.
    # p is the density of water (998.2 kilogram / meter cubed).
    # v is the velocity of the water flowing through the pipe in meters / second.
    # d is the diameter of the pipe in meters.

    f = friction_factor
    L = pipe_length
    p = WATER_DENSITY
    v = fluid_velocity
    d = pipe_diameter

    Plp = ( - f * L * p * v ** 2) / (2000 * d)

    return Plp


def pressure_loss_from_fittings (fluid_velocity, quantity_fittings):
    """Calculates the water pressure lost because of fittings such as 45° and 90°
    bends that are in a pipeline.
    """
    # Plf is the lost pressure in kilopascals.
    # p is the density of water (998.2 kilogram / meter cubed).
    # v is the velocity of the water flowing through the pipe in meters / second.
    # n is the quantity of fittings.

    p = WATER_DENSITY
    v = fluid_velocity
    n = quantity_fittings

    Plf = (-0.04 * p * (v ** 2) * n) / 2000

    return Plf


def reynolds_number (hydraulic_diameter, fluid_velocity):
    """Calculates and returns the Reynolds number for a pipe with water flowing through it.
    The Reynolds number is a unitless ratio of the intertial & viscous forces in a fluid that
    is useful for predicting fluid flow in different situations.
    """
    # R is the Reynolds number
    # p is the density of water (998.2 kilograms / meter cubed)
    # d is the hydraulic diameter of a pipe in meters. For a round pipe, the hydraulic diameter
    # is the same as the pipe's inner diameter.
    # v is the velocity of the water flowing through the pipe in meters / second
    # µ (You type ALT + 230 for the Mu symbol) is the dynamic viscosity of water (0.0010016 Pascal seconds)

    p = WATER_DENSITY
    d = hydraulic_diameter
    v = fluid_velocity
    µ = WATER_DYNAMIC_VISCOSITY

    R = p * d * v / µ

    return R


def pressure_loss_from_pipe_reduction (larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    """Calculates the water pressure lost because of water moving from a pipe with a large diameter into a pipe
    with a smaller diameter.
    """
    # k is a constant computed by the first formula & used in the second formula.
    # R is the Reynolds number that corresponds to the pipe with the larger diameter.
    # D is the diameter of larger pipe in meters.
    # d is the diameter of smaller pipe in meters.
    # Plpr is the lost pressure in kilopascals.
    # p is the density of water (998.2 kilogram / meter cubed).
    # v is the velocity of the water flowing throug the larger diameter pipe in meters / second.

    R = reynolds_number
    D = larger_diameter
    d = smaller_diameter
    p = WATER_DENSITY
    v = fluid_velocity

    k = (0.1 + 50 / R) * ((D / d ) ** 4 - 1)

    Plpr = (- k * p * v ** 2) / 2000

    return Plpr


def kPa_to_psi (tower_height, tank_height, length1, quantity_angles, length2):
    """Calculates and returns the pressure in terms of psi."""

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)
    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss
    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss
    loss = pressure_loss_from_pipe_reduction(diameter,
        velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss
    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss
    
    psi = pressure * 0.14503773773020923

    return psi


PVC_SCHED80_INNER_DIAMETER = 0.28687    # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013     # (unitless)
SUPPLY_VELOCITY = 1.65                  # (meters / second)
HDPE_SDR11_INNER_DIAMETER = 0.048692    # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018      # (unitless)
HOUSEHOLD_VELOCITY = 1.75               # (meters / second)
EARTH_ACCELERATION_OF_GRAVITY = 9.80665 # (meters / second (squared))
WATER_DENSITY = 998.2                   # (kilogram / meter (cubed))
WATER_DYNAMIC_VISCOSITY = 0.0010016     # Pascal seconds


def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    psi = kPa_to_psi (tower_height, tank_height, length1, quantity_angles, length2)

    
    print(f"Pressure at house: {pressure:.1f} kilopascals ({psi:.1f} psi)")


if __name__ == "__main__":
    main()