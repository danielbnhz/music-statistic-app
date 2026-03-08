import gradio as gr

from analysis.queries import load_top_tracks, top_streamed
from analysis.charts import streams_bar_chart


def analyze_dataset(csv_file):

    if csv_file is None:
        raise gr.Error("Please upload a CSV")

    file_path = csv_file if isinstance(csv_file, str) else csv_file.name

    df = load_top_tracks(file_path)

    top_df = top_streamed(df)

    fig = streams_bar_chart(top_df)

    return top_df, fig


def build_interface():

    with gr.Blocks() as demo:

        gr.Markdown("# 🎵 Music Stream Analyzer")

        file_input = gr.File(label="Upload CSV", type="filepath")

        run_button = gr.Button("Run Analysis")

        table_output = gr.Dataframe()

        chart_output = gr.Plot()

        run_button.click(
            analyze_dataset,
            inputs=file_input,
            outputs=[table_output, chart_output]
        )

    return demo