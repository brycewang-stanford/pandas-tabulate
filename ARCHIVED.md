# ⚠️ This Repository Has Been Archived

This repository has been **archived** and is no longer maintained. 

All functionality from `pandas-tabulate` has been integrated into the unified **Py-Stata-Commands** package.

## 🔗 New Repository

Please use the new unified repository:
**https://github.com/brycewang-stanford/Py-Stata-Commands**

## 🚀 New Installation

```bash
pip install py-stata-commands
```

## 📖 New Usage

```python
from py_stata_commands import tabulate

# Same functionality, new location
result = tabulate.tabulate(df['var1'], df['var2'])
```

## 📚 Benefits of the New Package

- **Unified installation**: All Stata-equivalent commands in one package
- **Consistent API**: Familiar syntax across all modules
- **Better maintenance**: Single repository for all related functionality
- **Comprehensive documentation**: Complete examples and guides

---

**Migration**: Replace `import pandas_tabulate` with `from py_stata_commands import tabulate`