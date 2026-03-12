import pandas as pd

def H(G,dt):
    """
    Comentar funci'on
    """

    G = G.dropna()
    meses = G.index.month.unique().values
    H = []
    F = []

    for mes in meses:
        dfmes = G[G.index.month == mes]
        dias = dfmes.index.day.unique().values
        for dia in dias:
            dfw = dfmes[dfmes.index.day == dia]
            h = dt * dfw.sum()/1E6
            H.append(h)
            f = str(dfw.index.year[0]) + '-' + str(mes) + '-' +str(dia)
            F.append(f)
    data = {'Fecha':F, 'H':H}
    df = pd.DataFrame(data)
    df.Fecha = pd.to_datetime(df.Fecha, format="%Y-%m-%d")
    df.set_index('Fecha', inplace = True)
    return(df)
