"""
Example usage of pandas-tabulate package.

This script demonstrates the main functionality of pandas-tabulate,
showing how to use it for frequency analysis and cross-tabulation.
"""

import pandas as pd
import numpy as np
import pandas_tabulate as ptab


def main():
    """Run example analysis."""
    print("pandas-tabulate Examples")
    print("=" * 50)
    
    # Create sample data
    np.random.seed(42)
    n = 200
    
    df = pd.DataFrame({
        'gender': np.random.choice(['Male', 'Female'], n),
        'education': np.random.choice(['High School', 'College', 'Graduate'], n),
        'income_category': np.random.choice(['Low', 'Medium', 'High'], n),
        'age_group': np.random.choice(['18-30', '31-50', '51+'], n),
        'satisfaction': np.random.choice(['Satisfied', 'Neutral', 'Dissatisfied'], n)
    })
    
    # Add some missing values
    missing_indices = np.random.choice(n, size=20, replace=False)
    df.loc[missing_indices[:10], 'education'] = np.nan
    df.loc[missing_indices[10:], 'income_category'] = np.nan
    
    print(f"Sample data created: {len(df)} observations")
    print(f"Variables: {list(df.columns)}")
    print("\n")
    
    # Example 1: One-way tabulation
    print("Example 1: One-way Tabulation")
    print("-" * 40)
    result = ptab.oneway(df['gender'], percent=True, cumulative=True)
    print(result)
    print("\n")
    
    # Example 2: Two-way tabulation
    print("Example 2: Two-way Cross-tabulation")
    print("-" * 40)
    result = ptab.twoway(df['gender'], df['education'])
    print(result)
    print("\n")
    
    # Example 3: Two-way with percentages
    print("Example 3: Cross-tabulation with Percentages")
    print("-" * 40)
    result = ptab.twoway(df['gender'], df['education'], 
                        row_percent=True, col_percent=True)
    print(result)
    print("\n")
    
    # Example 4: Statistical tests
    print("Example 4: Cross-tabulation with Statistical Tests")
    print("-" * 40)
    result = ptab.twoway(df['gender'], df['education'], 
                        chi2=True, exact=False, cramers_v=True)
    print(result)
    print("\n")
    
    # Example 5: Missing value handling
    print("Example 5: Handling Missing Values")
    print("-" * 40)
    print("Excluding missing values:")
    result_exclude = ptab.twoway(df['education'], df['income_category'], 
                                missing=False)
    print(f"Total observations: {result_exclude.data['core_table'].sum().sum()}")
    
    print("\nIncluding missing values:")
    result_include = ptab.twoway(df['education'], df['income_category'], 
                                missing=True)
    print(f"Total observations: {result_include.data['core_table'].sum().sum()}")
    print(result_include)
    print("\n")
    
    # Example 6: Using main tabulate function
    print("Example 6: Main tabulate() Function")
    print("-" * 40)
    
    # One-way using main function
    result_one = ptab.tabulate(df['satisfaction'])
    print("One-way tabulation:")
    print(result_one)
    print("\n")
    
    # Two-way using main function
    result_two = ptab.tabulate(df['age_group'], df['satisfaction'], 
                              chi2=True, row_percent=True)
    print("Two-way tabulation:")
    print(result_two)


if __name__ == "__main__":
    main()
