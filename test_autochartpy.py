import pandas as pd
from autochartpy.core import AutoChartPy

# Create a sample DataFrame
data = pd.DataFrame({
    "Date": pd.date_range(start="2023-01-01", periods=10, freq="D"),
    "Sales": [100, 200, 150, 300, 250, 400, 500, 450, 550, 600],
    "Category": ["A", "B", "A", "B", "A", "B", "A", "B", "A", "B"]
})

def test_suggest_chart():
    ac = AutoChartPy(data)
    suggestions = ac.suggest_chart()
    assert len(suggestions) == 3

def test_generate_chart():
    ac = AutoChartPy(data)
    fig = ac.generate_chart(x="Date", y="Sales", chart_type="line")
    assert fig.layout.title.text == "Line Chart: Date vs Sales"
