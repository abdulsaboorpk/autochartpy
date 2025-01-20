import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

class AutoChartPy:
    def __init__(self, data: pd.DataFrame):
        """
        Initialize the AutoChartPy with a Pandas DataFrame.

        :param data: A Pandas DataFrame containing the dataset.
        """
        if not isinstance(data, pd.DataFrame):
            raise ValueError("Data must be a Pandas DataFrame.")
        self.data = data

    def suggest_chart(self):
        """
        Suggest the best chart type based on the dataset.

        :return: A dictionary containing suggested chart types and columns.
        """
        suggestions = []
        for col in self.data.columns:
            if pd.api.types.is_numeric_dtype(self.data[col]):
                suggestions.append({"column": col, "chart": "Histogram"})
            elif pd.api.types.is_datetime64_any_dtype(self.data[col]):
                suggestions.append({"column": col, "chart": "Time Series"})
            elif isinstance(self.data[col].dtype, pd.CategoricalDtype):
                suggestions.append({"column": col, "chart": "Bar Chart"})
            else:
                suggestions.append({"column": col, "chart": "Scatter Plot"})
        return suggestions

    def generate_chart(self, x: str, y: str = None, chart_type: str = "line"):
        """
        Generate a chart based on the specified type.

        :param x: Column for the x-axis.
        :param y: Column for the y-axis (optional for some chart types).
        :param chart_type: Type of chart to generate (e.g., line, bar, scatter).
        :return: A Plotly Figure object.
        """
        if chart_type == "line":
            fig = px.line(self.data, x=x, y=y, title=f"Line Chart: {x} vs {y}")
        elif chart_type == "bar":
            fig = px.bar(self.data, x=x, y=y, title=f"Bar Chart: {x} vs {y}")
        elif chart_type == "scatter":
            fig = px.scatter(self.data, x=x, y=y, title=f"Scatter Plot: {x} vs {y}")
        elif chart_type == "histogram":
            fig = px.histogram(self.data, x=x, title=f"Histogram: {x}")
        else:
            raise ValueError(f"Unsupported chart type: {chart_type}")
        return fig

    def generate_dashboard(self, charts: list):
        """
        Generate a dashboard with multiple charts.

        :param charts: A list of dictionaries, where each dictionary contains
                       x, y, and chart_type keys.
        :return: A Plotly dashboard layout.
        """
        fig = go.Figure()
        for idx, chart in enumerate(charts):
            chart_fig = self.generate_chart(chart["x"], chart.get("y"), chart["chart_type"])
            fig.add_trace(chart_fig.data[0])
        fig.update_layout(title="Dashboard", showlegend=True)
        return fig
