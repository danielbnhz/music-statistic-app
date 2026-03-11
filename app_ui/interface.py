import gradio as gr
from analysis.queries import load_top_tracks, top_streamed
from analysis.charts import streams_bar_chart


DATA_PATH = "data/processed/top50_global.csv"   # adjust to your actual dataset path


def analyze_dataset():
    try:
        print("Loading dataset from:", DATA_PATH)

        df = load_top_tracks(DATA_PATH)
        print("columns:", list(df.columns))

        top_df = top_streamed(df)
        fig = streams_bar_chart(top_df)

        return top_df, fig

    except Exception as e:
        print("ERROR:", repr(e))
        raise gr.Error(str(e))


def build_interface():
    with gr.Blocks() as demo:
        gr.Markdown("# 🎵 Music Stream Analyzer")

        run_button = gr.Button("Run Analysis")

        table_output = gr.Dataframe()
        chart_output = gr.Plot()

        run_button.click(
            analyze_dataset,
            inputs=None,
            outputs=[table_output, chart_output]
        )

    return demo