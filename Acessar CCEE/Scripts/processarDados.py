import pandas as pd
import time
import datetime

def buscarDados(data_file):
    return pd.read_csv(data_file, sep=';', encoding='UTF-8', decimal=',', header=[0])

def indexar(dados):
    return dados.set_index(['Submercado', 'Hora'])

def dataHoje():
    return time.strftime("%#d/%#m/%Y")

def dataOntem():
    data = datetime.datetime.now() - datetime.timedelta(days=1)
    return data.strftime("%#d/%#m/%Y")

def obterEstatisticasHoje(dados):
    dados = indexar(dados)
    min_data = dados.groupby(level="Submercado")[hoje].min()
    mean_data = dados.groupby(level="Submercado")[hoje].mean()
    max_data = dados.groupby(level="Submercado")[hoje].max()
    data = {'min': [0, 0, 0, 0],
            'mean': [0, 0, 0, 0],
            'max': [0, 0, 0, 0]}
    linhas = ['NORDESTE', 'NORTE', 'SUDESTE', 'SUL']
    df = pd.DataFrame(data, linhas)
    df['min'] = min_data
    df['mean'] = mean_data
    df['max'] = max_data
    return df

def obterEstatisticasOntem(dados):
    dados = indexar(dados)
    min_data = dados.groupby(level="Submercado")[ontem].min()
    mean_data = dados.groupby(level="Submercado")[ontem].mean()
    max_data = dados.groupby(level="Submercado")[ontem].max()
    data = {'min': [0, 0, 0, 0],
            'mean': [0, 0, 0, 0],
            'max': [0, 0, 0, 0]}
    linhas = ['NORDESTE', 'NORTE', 'SUDESTE', 'SUL']
    df = pd.DataFrame(data, linhas)
    df['min'] = min_data
    df['mean'] = mean_data
    df['max'] = max_data
    return df

def dadosHoje(dados):
    return dados[['Hora', 'Submercado', hoje]]

def dadosOntem(dados):
    return dados[['Hora', 'Submercado', ontem]]

def filtrarNE(dados):
    return dados[dados['Submercado'] == 'NORDESTE']

def filtrarN(dados):
    return dados[dados['Submercado'] == 'NORTE']

def filtrarSE(dados):
    return dados[dados['Submercado'] == 'SUDESTE']

def filtrarS(dados):
    return dados[dados['Submercado'] == 'SUL']

hoje = dataHoje()
ontem = dataOntem()