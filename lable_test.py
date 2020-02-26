import pandas as pd
import numpy as np

def readfile(acfile):
    df = pd.read_csv(acfile)
    return df

def findsync(recfile):
    df = pd.read_csv(recfile)
    timestamps = df['timestamp']
    return timestamps

def lable(df, syncs):
    i = 0
    j = i + 1
    if df['timestamp'] > syncs[i] and df['timestamp'] < syncs[j]:
        df.drop(df.index[0:9])
        print(df)

syncs = findsync('RecordingLog.csv')
df = readfile('Accelerometer.csv')
lable(df, syncs)