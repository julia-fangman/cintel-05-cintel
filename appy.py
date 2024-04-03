from shiny import reactive, render
from shiny.express import ui
import random
from datetime import datetime
from collections import deque
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
from shinywidgets import render_plotly, render_widget
from scipy import stats
from faicons import icon_svg
from ipyleaflet import Map  

UPDATE_INTERVAL_SECS: int = 10
DEQUE_SIZE: int = 10
reactive_value_wrapper = reactive.value(deque(maxlen=DEQUE_SIZE))

@reactive.calc()
def reactive_calc_combined():
    reactive.invalidate_later(UPDATE_INTERVAL_SECS)
    temp = round(random.uniform(8, 10), 1)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_dictionary_entry = {"temp":temp, "timestamp":timestamp}
    reactive_value_wrapper.get().append(new_dictionary_entry)
    deque_snapshot = reactive_value_wrapper.get()
    df = pd.DataFrame(deque_snapshot)
    latest_dictionary_entry = new_dictionary_entry
    return deque_snapshot, df, latest_dictionary_entry

ui.page_opts(title="Julia's PyShiny: Live Data Example", fillable=True)

with ui.sidebar(open="open", style="background-color: lightblue; color: navy;"):
    ui.h2("St. Joseph, MO Weather", class_="text-center")
    ui.p(
        "A demonstration of real-time temperature readings in the St. Joe Area.",
        class_="text-center",
        style="color: navy;",
    )

    @render_widget
    def small_map(width="100%", height="200px"):
        return Map(center=(39.7675, -94.8467), zoom=10,)
    
    ui.hr(style="border-color: navy;")
    ui.h6("Links:", style="color: navy;")
    ui.a(
        "GitHub Source",
        href="https://github.com/julia-fangman/cintel-05-cintel/blob/main/app.py",
        target="_blank",
        style="color: yellow;",
    )
    ui.a(
        "GitHub App",
        href="https://github.com/julia-fangman/cintel-05-cintel",
        target="_blank",
        style="color: yellow;",
    )


with ui.div(class_="container-fluid"):
    with ui.div(class_="row"):
        with ui.div(class_="col"):
            with ui.card(style="background-color: lightblue; color: navy;"):
                ui.card_header("Current Date and Time", style="background-color: yellow; color: navy;")

                @render.text
                def display_time():
                    """Get the latest reading and return a timestamp string"""
                    deque_snapshot, df, latest_dictionary_entry = reactive_calc_combined()
                    return f"{latest_dictionary_entry['timestamp']}"

        with ui.div(class_="col"):
            with ui.card(style="background-color: lightblue; color: navy;"):
                ui.card_header("Current Temperature", style="background-color: yellow; color: navy;")

                @render.text
                def display_temp():
                    """Get the latest reading and return a temperature string"""
                    deque_snapshot, df, latest_dictionary_entry = reactive_calc_combined()
                    return f"{latest_dictionary_entry['temp']} C"

    with ui.div(class_="row"):
        with ui.div(class_="col"):
            with ui.card(style="background-color: lightblue; color: navy;"):
                ui.card_header("Most Recent Readings", style="background-color: yellow; color: navy;")

                @render.data_frame
                def display_df():
                    """Get the latest reading and return a dataframe with current readings"""
                    deque_snapshot, df, latest_dictionary_entry = reactive_calc_combined()
                    pd.set_option('display.width', None)        # Use maximum width
                    return render.DataGrid(df,width="100%")

        with ui.div(class_="col"):
            with ui.card(style="background-color: lightblue; color: navy;"):
                ui.card_header("Temperature Box Plot", style="background-color: yellow; color: navy;")

                @render_plotly
                def display_box_plot():
                    deque_snapshot, df, latest_dictionary_entry = reactive_calc_combined()
                    if not df.empty:
                        fig = px.box(df, y="temp", title="Temperature Distribution (Box Plot)")
                        fig.update_layout(
                            yaxis_title="Temperature (°C)",
                            showlegend=False
                        )
                        return fig

        with ui.div(class_="col"):
            with ui.card(style="background-color: lightblue; color: navy;"):
                ui.card_header("Chart with Current Trend", style="background-color: yellow; color: navy;")

                @render_plotly
                def display_plot():
                    deque_snapshot, df, latest_dictionary_entry = reactive_calc_combined()
                    if not df.empty:
                        df["timestamp"] = pd.to_datetime(df["timestamp"])
                        fig = px.scatter(df,
                                         x="timestamp",
                                         y="temp",
                                         title="Temperature Readings with Regression Line",
                                         labels={"temp": "Temperature (°C)", "timestamp": "Time"},
                                         color_discrete_sequence=["blue"])
                        sequence = range(len(df))
                        x_vals = list(sequence)
                        y_vals = df["temp"]
                        slope, intercept, r_value, p_value, std_err = stats.linregress(x_vals, y_vals)
                        df['best_fit_line'] = [slope * x + intercept for x in x_vals]
                    
                        fig.add_scatter(x=df["timestamp"], y=df['best_fit_line'], mode='lines', name='Regression Line')

                        fig.update_layout(xaxis_title="Time", yaxis_title="Temperature (°C)")

                        return fig
