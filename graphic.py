import plotly.graph_objects as go 

def create_performance_analysis_plot(
    number_invest_cli, investimento_diario, resultado,
    cliques_diario, leads_diario, leads_mensal
):
    fig = go.Figure()

    # Gráfico de investimento
    fig.add_trace(go.Bar(
        x=['Diário', 'Mensal'],
        y=[round(investimento_diario), number_invest_cli],
        name='Investimento',
        marker_color='indianred'
    ))

    # Gráfico de cliques
    fig.add_trace(go.Bar(
        x=['Diário', 'Mensal'],
        y=[round(cliques_diario), resultado],
        name='Cliques',
        marker_color='lightsalmon'
    ))

    # Gráfico de leads
    fig.add_trace(go.Bar(
        x=['Diário', 'Mensal'],
        y=[round(leads_diario), round(leads_mensal)],
        name='Leads',
        marker_color='lightseagreen'
    ))

    fig.update_layout(
        title='Investimento, Cliques e Leads (Diário e Mensal)',
        xaxis=dict(
            tickfont=dict(size=15)
        ),
        yaxis=dict(
            title=dict(
                text="Valores",
                font=dict(size=17)
            ),
            tickfont=dict(size=15)
        ),
        barmode='group',
        bargap=0.15,
        bargroupgap=0.2
    )
    return fig
