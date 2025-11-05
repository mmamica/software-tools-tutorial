#!/usr/bin/env python3
"""
data_simulation.py

A simple data simulation script using pandas and numpy.
Generates a CSV file with random data.
"""

import argparse
import numpy as np
import pandas as pd


def simulate_data(rows=100, cols=5, seed=42, output="simulated_data.csv"):
    """
    Generate a DataFrame with random data and save to CSV.

    Parameters:
        rows (int): Number of rows
        cols (int): Number of columns
        seed (int): Random seed for reproducibility
        output (str): Output CSV filename
    """
    np.random.seed(seed)

    # Generate column names
    columns = [f"feature_{i + 1}" for i in range(cols)]

    # Create random data
    data = np.random.randn(rows, cols)

    # Create DataFrame
    df = pd.DataFrame(data, columns=columns)

    # Save to CSV
    df.to_csv(output, index=False)
    print(f"Simulated data saved to {output}")


def main():
    parser = argparse.ArgumentParser(description="Simulate data with pandas and numpy.")
    parser.add_argument("--rows", type=int, default=100, help="Number of rows")
    parser.add_argument("--cols", type=int, default=5, help="Number of columns")
    parser.add_argument("--seed", type=int, default=42, help="Random seed")
    parser.add_argument("--output", type=str, default="simulated_data.csv", help="Output CSV file name")

    args = parser.parse_args()

    simulate_data(rows=args.rows, cols=args.cols, seed=args.seed, output=args.output)


if __name__ == "__main__":
    main()
