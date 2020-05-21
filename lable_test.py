# Import libraries
import numpy as np
import pandas as pd
import warnings

subwayfiles = ['Accelerometer-20200228-Subway.csv', 'Accelerometer-20200302-Subway-01.csv',
               'Accelerometer-20200302-Subway-02.csv']
carfiles = ['Accelerometer-20200318-Bil.csv', 'Accelerometer-20200322-Bil.csv']
walkingfiles = ['Accelerometer-20200331-Walking.csv']
standingfiles = ['Accelerometer-20200331-Standing.csv']
files = [subwayfiles, carfiles, walkingfiles, standingfiles]

warnings.filterwarnings("ignore")

dataAcc = pd.read_csv('Accelerometer.csv')
dataAcc = dataAcc.drop(dataAcc.index[0], axis=0)
dataAcc = dataAcc.drop("timestamp", axis=1)
dfAcc = pd.DataFrame(dataAcc)

# SUBWAY
for f in range(len(subwayfiles)):
    dataAcc2 = pd.read_csv(subwayfiles[f])
    dataAcc2 = dataAcc2.drop("timestamp", axis=1)
    dfAcc2 = pd.DataFrame(dataAcc2)

    # Lägger till activity och activitylabel
    dfAcc2.loc[:, 'Activity'] = '5'
    dfAcc2.loc[:, 'ActivityName'] = 'SUBWAY'

    # Lägger till andra dataframen till första
    dfAcc = dfAcc.append(dfAcc2, ignore_index=True)

print(len(dfAcc.index))

# DRIVING
for f in range(len(carfiles)):
    dataAcc2 = pd.read_csv(carfiles[f])
    dataAcc2 = dataAcc2.drop("timestamp", axis=1)
    dfAcc2 = pd.DataFrame(dataAcc2)

    # Lägger till activity och activitylabel
    dfAcc2.loc[:, 'Activity'] = '3'
    dfAcc2.loc[:, 'ActivityName'] = 'DRIVING'

    # Lägger till andra dataframen till första
    dfAcc = dfAcc.append(dfAcc2, ignore_index=True)

dfAcc = dfAcc.drop(dfAcc.index[range(144998, len(dfAcc.index))])

print(len(dfAcc.index))


# WALKING
for f in range(len(walkingfiles)):
    dataAcc2 = pd.read_csv(walkingfiles[f])
    dataAcc2 = dataAcc2.drop("timestamp", axis=1)
    dfAcc2 = pd.DataFrame(dataAcc2)

    # Lägger till activity och activitylabel
    dfAcc2.loc[:, 'Activity'] = '2'
    dfAcc2.loc[:, 'ActivityName'] = 'WALKING'

    # Lägger till andra dataframen till första
    dfAcc = dfAcc.append(dfAcc2, ignore_index=True)

dfAcc = dfAcc.drop(dfAcc.index[range(217497, len(dfAcc.index))])

print(len(dfAcc.index))


# STANDING
for f in range(len(standingfiles)):
    dataAcc2 = pd.read_csv(standingfiles[f])
    dataAcc2 = dataAcc2.drop("timestamp", axis=1)
    dfAcc2 = pd.DataFrame(dataAcc2)

    # Lägger till activity och activitylabel
    dfAcc2.loc[:, 'Activity'] = '1'
    dfAcc2.loc[:, 'ActivityName'] = 'STANDING'

    # Lägger till andra dataframen till första
    dfAcc = dfAcc.append(dfAcc2, ignore_index=True)

dfAcc = dfAcc.drop(dfAcc.index[range(289996, len(dfAcc.index))])
print(len(dfAcc.index))

# for i in range(289796, len(dfAcc.index)):
#     dfAcc = dfAcc.drop(dfAcc.index[i])
# print(len(dfAcc.index))

print(dfAcc)
# Skriver dataframen till Accelerometer-Total
dfAcc.to_csv('Accelerometer-Total.csv')
