# ⚠️ ARCHIVED - This repository is no longer maintained

**All functionality has been moved to [PyStataR](https://github.com/brycewang-stanford/PyStataR)**

---

# pandas-tabulate

[![PyPI version](https://badge.fury.io/py/pandas-tabulate.svg)](https://badge.fury.io/py/pandas-tabulate)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**⚠️ MIGRATION NOTICE**: This package has been integrated into the unified **PyStataR** package.

## 🔄 Migration Instructions

**Old:**
```bash
pip install pandas-tabulate
```
```python
import pandas_tabulate as ptab
result = ptab.tabulate(df['var1'], df['var2'])
```

**New:**
```bash
pip install pystatar
```
```python
from pystatar import tabulate
result = tabulate.tabulate(df['var1'], df['var2'])
```

## 🎯 Why the Change?

The new unified package provides:
- **Single installation** for all Stata-equivalent commands
- **Consistent API** across tabulate, egen, reghdfe, and winsor2
- **Better documentation** and examples
- **Easier maintenance** and updates

## 📖 New Documentation

Visit the new repository for complete documentation:
**https://github.com/brycewang-stanford/PyStataR**

---

*This repository is archived and will not receive further updates. Please migrate to the new package.*
