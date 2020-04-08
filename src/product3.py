'''
MIT License

Copyright (c) 2020 Sebastian Cornejo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import csv
import pandas as pd
from os import listdir
from os.path import isfile, join

# product3 simplemente es una compilacion de los casos confirmados por dia en una tabla.

if __name__ == '__main__':

    mypath = "../output/producto4/"
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    print(type(onlyfiles))
    cumulativo = pd.DataFrame({'Region':[],
                               'Casos nuevos':[]})

    for eachfile in onlyfiles:
        date = eachfile.replace("CasosConfirmados-totalRegional-", "").replace(".csv", "")
        dataframe = pd.read_csv(mypath + eachfile)
        # sanitize headers
        dataframe.rename(columns={'Región': 'Region'}, inplace=True)
        dataframe.rename(columns={'Casos  nuevos': 'Casos nuevos'}, inplace=True)
        dataframe.rename(columns={' Casos nuevos': 'Casos nuevos'}, inplace=True)
        tomerge = dataframe[['Region', 'Casos nuevos']]
        if cumulativo['Region'].empty:
            cumulativo[['Region', 'Casos nuevos']] = dataframe[['Region', 'Casos nuevos']]
            cumulativo.rename(columns={'Casos nuevos': date}, inplace=True)
        else:
            cumulativo[date] = dataframe['Casos nuevos']

    print(cumulativo.columns)
    cumulativo.to_csv("../output/producto3/CasosConfirmadosCumulativo.csv", index=False)