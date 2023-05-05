import os
import wget

# data from https://www.sciencedirect.com/science/article/pii/S2352340920303048

# Download the zipped dataset
url = 'https://drive.google.com/drive/u/2/folders/1qUnqnkjwpvb9_HZrV7AwHgsapscjBvCy'
file_name = "creditCard.csv"
wget.download(url, file_name)
