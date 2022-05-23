import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import processarDados as prod

def esconderEixos(axes):
    axes.set_frame_on(False)
    [n.set_visible(False) for n in axes.get_xticklabels() + axes.get_yticklabels()]
    [n.set_visible(False) for n in axes.get_xticklines() + axes.get_yticklines()]

hoje = prod.dataHoje()
ontem = prod.dataOntem()

def criarGrafico(figure, gs = None, dados = None, axes = None, submercado = None):
    if not axes:
        axes = figure.add_subplot(gs[0, 0])
    hora = dados['Hora']
    preco = dados[hoje]
    if submercado == "NORDESTE":
        color = '#D2691E'
    elif submercado == "NORTE":
        color = '#8B008B'
    elif submercado == "SUDOESTE":
        color = '#2E8B57'
    else:
        color = '#191970'
    axes.set_title(submercado, fontsize=20, color=color)
    axes.plot(hora, preco, linewidth=1, alpha=0.5, c=color, marker='o', markersize=4)
    axes.set_xticks(range(0, 23, 2))
    axes.set_xlabel("Hora", fontsize=10)
    axes.set_ylabel("Preço (R$/MWh)", fontsize=10)
    df=prod.obterEstatisticasHoje(dados)
    max = round(df['max'][submercado],2)
    min = round(df['min'][submercado],2)
    mean = round(df['mean'][submercado],2)
    axes.annotate("Máximo: "+str(max), xy=(5, 68), xycoords='axes points', size=8, alpha=0.75)
    axes.annotate("Mínimo: "+str(min), xy=(5, 5), xycoords='axes points', size=8, alpha=0.75)
    axes.annotate("Média: "+str(mean), xy=(270, 68), xycoords='axes points', size=8, alpha=0.75)
    if gs:
        gs.tight_layout(figure)
    return axes
