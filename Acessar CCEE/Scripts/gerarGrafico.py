import matplotlib as mpl
import matplotlib.pyplot as plt
import processarDados as prod
import plotarDados as pldd
import time
from fpdf import FPDF
import baixarDados
import caminhosArquivos as path

# Informando datas
hoje = prod.dataHoje()
ontem = prod.dataOntem()

figure = plt.figure(figsize=(13, 10), dpi=300, constrained_layout=True)
pH = prod.buscarDados(path.caminhoDiretorio()+path.nomeArquivoPreco())
pdf = FPDF()

def gerarPDF():
    # Gerando dados a partir do data frame
    # Dados para hoje
    pH_hoje = prod.dadosHoje(pH)
    pH_hoje_NE = prod.filtrarNE(pH_hoje)
    pH_hoje_N = prod.filtrarN(pH_hoje)
    pH_hoje_SE = prod.filtrarSE(pH_hoje)
    pH_hoje_S = prod.filtrarS(pH_hoje)

    # Dados para ontem
    pH_ontem = prod.dadosOntem(pH)
    pH_ontem_NE = prod.filtrarNE(pH_ontem)
    pH_ontem_N = prod.filtrarN(pH_ontem)
    pH_ontem_SE = prod.filtrarSE(pH_ontem)
    pH_ontem_S = prod.filtrarS(pH_ontem)

    # Construindo as camadas

    gs_master = mpl.gridspec.GridSpec(ncols=2, nrows=9, wspace=0.2, hspace=5)

    # Camada 1 - Titulo
    gs_1 = mpl.gridspec.GridSpecFromSubplotSpec(1, 1, subplot_spec=gs_master[0:1, :])
    title_axes = figure.add_subplot(gs_1[0])
    title_axes.set_title("Preço Horário do Dia: " +hoje, fontsize = 30, color = "#4682B4")
    pldd.esconderEixos(title_axes)

    # Camada 2 - Preço Hora dia - NORDESTE
    gs_2 = mpl.gridspec.GridSpecFromSubplotSpec(1, 2, subplot_spec=gs_master[1:3, :])
    NE_axes = figure.add_subplot(gs_2[0])
    pldd.criarGrafico(figure, dados=pH_hoje_NE, axes=NE_axes, submercado="NORDESTE")

    # Camada 3 - Preço Hora dia - NORTE
    gs_3 = mpl.gridspec.GridSpecFromSubplotSpec(1, 1, subplot_spec=gs_master[1:3, 1])
    N_axes = figure.add_subplot(gs_3[0])
    pldd.criarGrafico(figure, dados=pH_hoje_N, axes=N_axes, submercado="NORTE")

    # Camada 4 - Preço Hora dia - SUDESTE
    gs_4 = mpl.gridspec.GridSpecFromSubplotSpec(1, 2, subplot_spec=gs_master[3:5, :])
    SE_axes = figure.add_subplot(gs_4[0])
    pldd.criarGrafico(figure, dados=pH_hoje_SE, axes=SE_axes, submercado="SUDESTE")

    # Camada 5 - Preço Hora dia - SUL
    gs_5 = mpl.gridspec.GridSpecFromSubplotSpec(1, 1, subplot_spec=gs_master[3:5, 1])
    S_axes = figure.add_subplot(gs_5[0])
    pldd.criarGrafico(figure, dados=pH_hoje_S, axes=S_axes, submercado="SUL")

    # Camada 6 - Preço Hora dia - PANORAMA GERAL
    gs_6 = mpl.gridspec.GridSpecFromSubplotSpec(1, 1, subplot_spec=gs_master[5:7, :])
    T_axes = figure.add_subplot(gs_6[0])
    hora = range(0, 24)
    NE = pH_hoje_NE[hoje]
    N = pH_hoje_N[hoje]
    SE = pH_hoje_SE[hoje]
    S = pH_hoje_S[hoje]
    T_axes.set_title("PANORAMA - "+hoje, fontsize=15, color='#4682B4')
    T_axes.plot(hora, NE, linewidth=1, alpha=0.5, c='#D2691E', marker='o', markersize=4)
    T_axes.plot(hora, N, linewidth=1, alpha=0.5, c='#8B008B', marker='o', markersize=4)
    T_axes.plot(hora, SE, linewidth=1, alpha=0.5, c='#2E8B57', marker='o', markersize=4)
    T_axes.plot(hora, S, linewidth=1, alpha=0.5, c='#191970', marker='o', markersize=4)
    T_axes.set_xticks(range(0, 24))
    T_axes.set_xlabel("Hora", fontsize=10)
    T_axes.set_ylabel("Preço (R$/MWh)", fontsize=10)
    nordeste = mpl.patches.Patch(color='#D2691E', alpha=0.5, label="Nordeste")
    norte = mpl.patches.Patch(color='#8B008B', alpha=0.5, label="Norte")
    sudeste = mpl.patches.Patch(color='#2E8B57', alpha=0.5, label="Sudeste")
    sul = mpl.patches.Patch(color='#191970', alpha=0.3, label="Sul")
    T_axes.legend(handles=[nordeste, norte, sudeste, sul], loc=2, fontsize=5)

    # Camada 7 - Preço Hora dia (ONTEM) - PANORAMA GERAL

    gs_7 = mpl.gridspec.GridSpecFromSubplotSpec(1, 1, subplot_spec=gs_master[7:, :])
    T_axes = figure.add_subplot(gs_7[0])
    hora = range(0, 24)
    NE = pH_ontem_NE[ontem]
    N = pH_ontem_N[ontem]
    SE = pH_ontem_SE[ontem]
    S = pH_ontem_S[ontem]
    T_axes.set_title("PANORAMA - " +ontem, fontsize=15, color='#4682B4')
    T_axes.plot(hora, NE, linewidth=1, alpha=0.5, c='#D2691E', marker='o', markersize=4)
    T_axes.plot(hora, N, linewidth=1, alpha=0.5, c='#8B008B', marker='o', markersize=4)
    T_axes.plot(hora, SE, linewidth=1, alpha=0.5, c='#2E8B57', marker='o', markersize=4)
    T_axes.plot(hora, S, linewidth=1, alpha=0.5, c='#191970', marker='o', markersize=4)
    T_axes.set_xticks(range(0, 24))
    T_axes.set_xlabel("Hora", fontsize=10)
    T_axes.set_ylabel("Preço (R$/MWh)", fontsize=10)
    nordeste = mpl.patches.Patch(color='#D2691E', alpha=0.5, label="Nordeste")
    norte = mpl.patches.Patch(color='#8B008B', alpha=0.5, label="Norte")
    sudeste = mpl.patches.Patch(color='#2E8B57', alpha=0.5, label="Sudeste")
    sul = mpl.patches.Patch(color='#191970', alpha=0.3, label="Sul")
    T_axes.legend(handles=[nordeste, norte, sudeste, sul], loc=2, fontsize=5)

    # Unindo as camadas
    gs_master.tight_layout(figure)
    data = time.strftime("%d-%m-%Y")
    figure.savefig(path.caminhoDiretorio() + 'panorama_' + data + '.png')
    figura = path.caminhoDiretorio()+'panorama_'+data+'.png'
    print("\nCRIANDO PDF\n")
    pdf.add_page(orientation='L')
    pdf.image(figura, w = 260, h = 200)
    pdf.output(path.caminhoDiretorio()+'panorama_'+data+'.pdf', 'F')
    print("\nPDF CRIADO\n")




