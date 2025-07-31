#Funções de carregamento de dados
#Script chamado apos conectada a conta e extraido os dados
import pandas as pd
from datetime import datetime

def transform_tracks_data(tracks_data):
    #Lista para armazenar os dados transformados
    transformed_data = []

    for track in tracks_data:
        played_at = track['played_at']
        track_info = track['track']

        tracks_data = {
            'played_at' : datetime.strptime(played_at,'%Y-%m-%dT%H:%M:%S.%fZ'),
            'track_id' : track_info['id'],
            'track_name' : track_info['name'],
            'artist_name' : track_info['artists'][0]['name'],
            'album_name' : track_info['album']['name'],
            'duration_ms' : track_info['duration_ms'],
            'popularity' : track_info['popularity'],
            'day_of_week' : datetime.strptime(played_at,'%Y-%m-%dT%H:%M:%S.%fZ').strftime('%A'),
            'hour_of_day' : datetime.strptime(played_at,'%Y-%m-%dT%H:%M:%S.%fZ').strftime('%H')

        }

        #Adiciona os dados transformados a lista
        transformed_data.append(tracks_data)

    df = pd.DataFrame(transformed_data)

    df = df.sort_values(by='played_at', ascending=False)

    df = df.drop_duplicates(subset=['track_id', 'played_at'])

    return df


def clean_data(df):
    # Removendo linhas com valores nulos
    df = df.dropna()
    
    # Convertendo duração de milissegundos para minutos
    df['duration_min'] = df['duration_ms'] / 60000
    
    # Arredondando para 2 casas decimais
    df['duration_min'] = df['duration_min'].round(2)
    
    return df

