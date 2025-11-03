from textual.app import App, ComposeResult
from textual_plot import PlotWidget, HiResMode


class BarPlotApp(App[None]):
    def compose(self) -> ComposeResult:
        yield PlotWidget()

    def on_mount(self) -> None:
        plot = self.query_one(PlotWidget)

        # Example data
        x = [1, 2, 3, 4, 5, 6, 7, 8]
        bar_y = [1, 4, 9, 16, 25, 36, 49, 34]

        # Add a bar plot
        plot.bar(x=x, y=bar_y, label="Foobar", marker_style="#5e5ea7")

        # Show a legend
        plot.show_legend()


BarPlotApp().run()
