import re
import pandas as pd
import plotly.graph_objects as go
import plotly.subplots


if __name__ == '__main__':
    df = pd.read_excel('graph-data.xlsx', skiprows=1, index_col=0)

    titles = []
    for i in range(12, 18):
        sub = df.iloc[:, [i, i + 6]]
        titles.append(re.search('[^\.]+', sub.columns[0]).group(0))

    # Consolidated figure
    fig2 = plotly.subplots.make_subplots(rows=6, cols=1, shared_xaxes=True, subplot_titles=titles)
    fig2.update_layout(title_text='Failure Patterns', showlegend=False)
    for _ in range(1, 7):
        fig2.update_layout({f'yaxis{_}': {'range': [0, 0.1]}})

    # ignore first 12 columns. After that column and column + 6 have probability and severity for a type.
    for i in range(12, 18):
        sub = df.iloc[:, [i, i + 6]]
        title = re.search('[^\.]+', sub.columns[0]).group(0)

        # Enable fig for individual graphs
        # fig = go.Figure()
        trace = go.Bar(
            # name=title,
            x=sub.index.values,
            y=sub.iloc[:, 0],
            marker=dict(
                color=sub.iloc[:, 1],
                colorscale="BlueRed"
            )
        )
        # fig.add_trace(trace)
        # fig.update_layout(title=title)
        # fig.show

        # trace.update({'layout': })
        fig2.add_trace(trace, row=i-11, col=1)

    fig2.show()
