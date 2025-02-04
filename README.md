# Physics Free-Fall Time

This repository contains a simple script called `fall_time.py` that computes how long it takes for an object to fall from a given height under uniform gravity (ignoring air resistance). It is intentionally incomplete so that you can practice using Git and GitHub to add features or fix issues.

## Usage

1. Clone or fork this repository.
2. From the command line, run:  
   `python fall_time.py --height 10.0`
3. Modify the script to add new features or fix issues, then open a pull request with your changes.

## Suggested Exercises

1. **Final Velocity**  
   Implement a function `compute_final_velocity(height, gravity)` using the formula `v = sqrt(2 * g * h)`.  
   Add an optional command-line flag (for example, `--final-velocity`) to print the result at the end of the fall.

2. **Planetary Gravity**  
   Add a `--planet` argument letting users choose among `Earth`, `Moon`, or `Mars`. A dictionary in the code can store each planet’s gravitational acceleration.  
   Use the selected planet’s gravity when calculating fall time.

## Contributing

1. **Fork** this repository.
2. Create a **branch** for your feature or fix.
3. **Commit** your changes locally with a descriptive message.
4. **Push** your branch to your fork on GitHub.
5. Open a **pull request** against the main repository and request a **review**.  
6. Once approved, your changes can be **merged** into the main branch!

