import gradio as gr
from src.analysis.queries import load_top_tracks, top_streamed
from src.analysis.charts import streams_bar_chart


def analyze_dataset(csv_file):

    df = load_top_tracks(csv_file.name)

    top_df = top_streamed(df, 20)

    fig = streams_bar_chart(top_df)

    return top_df, fig


def build_interface():

    with gr.Blocks() as demo:

        gr.Markdown("# 🎵 Music Stream Analyzer")

        file_input = gr.File(label="Upload Dataset (CSV)")

        run_button = gr.Button("Run Analysis")

        table_output = gr.Dataframe()
        chart_output = gr.Plot()

        run_button.click(
            analyze_dataset,
            inputs=file_input,
            outputs=[table_output, chart_output]
        )

    return demo