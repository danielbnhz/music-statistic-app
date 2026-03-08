import plotly.express as px


def streams_bar_chart(df):
    """
    Create bar chart of streams.
    """

    fig = px.bar(
        df,
        x="title",
        y="streams",
        color="artist",
        title="Top Streamed Tracks"
    )

    fig.update_layout(
        xaxis_title="Track",
        yaxis_title="Streams",
        template="plotly_dark"
    )

    return fig