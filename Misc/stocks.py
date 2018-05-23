import csv
import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt

dates = []
prices = []

def get_data(filename):
    with open(filename, "r") as csvfile:
        csvFileReader = csv.reader(csvfile)
        next(csvFileReader) #Skip the first row of data

        for row in csvFileReader:
            dates.append(int(row[0].split("-")[0]))
            prices.append(float(row[1]))
        
        return

#def predict_prices(dates, prices, x):
 #   dates = np.reshape