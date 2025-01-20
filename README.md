# AutoChartPy

AutoChartPy is a Python library to automatically generate beautiful charts and dashboards from raw datasets.

## Features
- **Automatic Chart Suggestions**: Recommends the best chart types for your data.
- **Customizable Visualizations**: Create line charts, bar charts, scatter plots, and histograms.
- **Interactive Dashboards**: Combine multiple charts into one layout.

## Installation

```bash
pip install autochartpy
```
## Usage
### Initialize
```bash
from autochartpy.core import AutoChartPy
import pandas as pd

data = pd.read_csv("data.csv")
ac = AutoChartPy(data)
```

### Suggest Chart Types
```bash
suggestions = ac.suggest_chart()
print(suggestions)
```

### Generate a Chart
```bash
fig = ac.generate_chart(x="Date", y="Sales", chart_type="line")
fig.show()
```

### Create a Dashboard
```bash
charts = [
    {"x": "Date", "y": "Sales", "chart_type": "line"},
    {"x": "Category", "y": "Sales", "chart_type": "bar"}
]
dashboard = ac.generate_dashboard(charts)
dashboard.show()
```