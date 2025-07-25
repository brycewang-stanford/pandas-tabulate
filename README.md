# pandas-tabulate

[![PyPI version](https://badge.fury.io/py/pandas-tabulate.svg)](https://badge.fury.io/py/pandas-tabulate)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Python implementation of Stata's tabulate command for pandas DataFrames.

pandas-tabulate brings the power and familiarity of Stata's `tabulate` command to Python, providing comprehensive cross-tabulation and frequency analysis tools that seamlessly integrate with pandas DataFrames.

## Key Features

- **Comprehensive tabulation**: One-way and two-way frequency tables
- **Statistical analysis**: Chi-square tests, Fisher exact tests, and other statistical measures
- **Flexible formatting**: Multiple output formats and customization options
- **Missing value handling**: Configurable treatment of missing data
- **Stata compatibility**: Familiar syntax and output format for Stata users
- **Performance optimized**: Efficient implementation using pandas and NumPy

## Installation

```bash
pip install pandas-tabulate
```

## Quick Start

```python
import pandas as pd
import pandas_tabulate as ptab

# Create sample data
df = pd.DataFrame({
    'gender': ['M', 'F', 'M', 'F', 'M', 'F', 'M', 'F'],
    'education': ['High', 'Low', 'High', 'High', 'Low', 'Low', 'High', 'Low'],
    'income': [50000, 30000, 60000, 45000, 35000, 25000, 55000, 28000]
})

# One-way tabulation
result = ptab.tabulate(df['gender'])
print(result)

# Two-way tabulation with statistics
result = ptab.tabulate(df['gender'], df['education'], 
                      chi2=True, exact=True)
print(result)
```

## Available Functions

### Core Tabulation Functions
- **`tabulate(var1, var2=None, **kwargs)`** - Main tabulation function
- **`oneway(variable, **kwargs)`** - One-way frequency tables
- **`twoway(var1, var2, **kwargs)`** - Two-way cross-tabulation

### Statistical Tests
- **Chi-square test** - Test of independence for categorical variables
- **Fisher exact test** - Exact test for small sample sizes
- **Likelihood ratio test** - Alternative test of independence
- **Cramér's V** - Measure of association strength

### Output Options
- **Frequencies** - Raw counts
- **Percentages** - Row, column, and total percentages
- **Cumulative** - Cumulative frequencies and percentages
- **Missing handling** - Include/exclude missing values

## Detailed Examples

### One-way Tabulation

```python
import pandas as pd
import pandas_tabulate as ptab

# Basic frequency table
df = pd.DataFrame({'status': ['A', 'B', 'A', 'C', 'B', 'A', 'C']})
result = ptab.oneway(df['status'])
print(result)

# With percentages and cumulative statistics
result = ptab.oneway(df['status'], 
                    percent=True, 
                    cumulative=True)
print(result)
```

### Two-way Cross-tabulation

```python
# Basic cross-tabulation
result = ptab.twoway(df['gender'], df['education'])
print(result)

# With row and column percentages
result = ptab.twoway(df['gender'], df['education'],
                    row_percent=True,
                    col_percent=True)
print(result)

# With statistical tests
result = ptab.twoway(df['gender'], df['education'],
                    chi2=True,
                    exact=True,
                    cramers_v=True)
print(result)
```

### Missing Value Handling

```python
import numpy as np

# Data with missing values
df_missing = pd.DataFrame({
    'var1': ['A', 'B', np.nan, 'A', 'C'],
    'var2': ['X', np.nan, 'Y', 'X', 'Y']
})

# Exclude missing values (default)
result = ptab.twoway(df_missing['var1'], df_missing['var2'])

# Include missing values
result = ptab.twoway(df_missing['var1'], df_missing['var2'], 
                    missing=True)
```

## Stata to Python Translation Guide

| Stata Command | pandas-tabulate Equivalent |
|---------------|----------------------------|
| `tabulate var1` | `ptab.oneway(df['var1'])` |
| `tabulate var1, missing` | `ptab.oneway(df['var1'], missing=True)` |
| `tabulate var1 var2` | `ptab.twoway(df['var1'], df['var2'])` |
| `tabulate var1 var2, chi2` | `ptab.twoway(df['var1'], df['var2'], chi2=True)` |
| `tabulate var1 var2, exact` | `ptab.twoway(df['var1'], df['var2'], exact=True)` |
| `tabulate var1 var2, row col` | `ptab.twoway(df['var1'], df['var2'], row_percent=True, col_percent=True)` |

## Function Reference

### tabulate(var1, var2=None, **kwargs)

Main tabulation function that automatically determines whether to perform one-way or two-way tabulation.

**Parameters:**
- `var1`: pandas Series - First variable
- `var2`: pandas Series, optional - Second variable for cross-tabulation
- `percent`: bool, default False - Show percentages
- `cumulative`: bool, default False - Show cumulative statistics
- `chi2`: bool, default False - Perform chi-square test
- `exact`: bool, default False - Perform Fisher exact test
- `missing`: bool, default False - Include missing values

**Returns:**
- TabulationResult object with tables and statistics

### Statistical Tests

All statistical tests return results with:
- Test statistic
- p-value
- Degrees of freedom (where applicable)
- Critical value
- Interpretation

## Contributing

We welcome contributions! Please see our Contributing Guide for details.

### Development Setup
```bash
git clone https://github.com/brycewang-stanford/pandas-tabulate.git
cd pandas-tabulate
pip install -e ".[dev]"
python -m pytest tests/
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Inspired by Stata's tabulate command
- Built on pandas, NumPy, and SciPy
- Thanks to the open-source community for feedback and contributions

## Support

- Bug Reports: [GitHub Issues](https://github.com/brycewang-stanford/pandas-tabulate/issues)
- Feature Requests: [GitHub Discussions](https://github.com/brycewang-stanford/pandas-tabulate/discussions)
- Email: brycew6m@stanford.edu

---

If this package helps your research, please consider starring the repository!
