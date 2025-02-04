#!/usr/bin/env python3

"""
Compute the time it takes for an object to fall from a given height
under constant gravitational acceleration, ignoring air resistance.

Exercise Features:
1) Implement a final velocity calculation using v = sqrt(2*g*h).
2) Add an argument --planet (Earth, Moon, Mars), each with different gravity.

Usage Example:
    python fall_time.py --height 10.0

C.D. Tunnell 2025
"""

import argparse
import math

# Dictionary of planetary gravities (m/s^2) - we only use metric mofo!
planetary_gravity = {
    "Earth": 9.8,
    "Moon": 1.62,
    "Mars": 3.71
}
def compute_fall_time(height, gravity=10):
    """
    Compute the time (in seconds) for an object to fall
    from a given height under constant gravity.
    Equation: time = sqrt(2 * height / gravity).
    """
    return math.sqrt(2 * height / gravity)

# TODO Feature A: Implement a function compute_final_velocity(height, gravity).
def compute_final_velocity(height, gravity=9.8):
    return (2 * gravity * height)**0.5

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Calculate time for an object to fall from a given height."
    )
    parser.add_argument(
        "--height",
        type=float,
        default=10.0,
        help="Height in meters from which the object is dropped."
    )
    parser.add_argument(
        "--planet",
        choices=["Earth", "Moon", "Mars"]
        help="Select which planet's gravity to use (Earth=9.8, Moon=1.62, Mars=3.71)."
    )

    # TODO Feature B: add optional '--planet' argument to choose Earth, Moon, or Mars
    # parser.add_argument(
    #     "--planet",
    #     choices=["Earth", "Moon", "Mars"],
    #     help="Select which planet's gravity to use (Earth=9.8, Moon=1.62, Mars=3.71)."
    # )

    # Also consider an optional '--gravity' float argument as a fallback

    args = parser.parse_args()

    # If planet is specified, override gravity
    gravity = planetary_gravity[args.planet]
    # e.g., if args.planet: gravity = planetary_gravity[args.planet]

    time_to_fall = compute_fall_time(args.height, gravity)
    final_vel = compute_final_velocity(args.height, gravity)
    print(f"Height: {args.height} m")
    print(f"Gravity: {gravity} m/s^2")
    print(f"Time to fall: {time_to_fall:.2f} seconds")
    print(f"Final velocity: {final_vel:.2f} meter/seconds")
    # If final velocity is implemented, optionally print that, too.
