import csv
import pandas as pd 
import numpy
from sklearn.cluster import KMeans

def load_data():
	df = pd.read_csv('olympics.csv', skiprows=1)

	for col in df.columns:
		if col[:2]=='01':
			df.rename(columns={col:'Gold'+ col[4:]}, inplace=True)
		if col[:2]=='02':
			df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
		if col[:2]=='03':
			df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)


	name_ids = df.index.to_series().str.split('\s\(')

	df.index = name_ids.str[0]
	df['ID'] = name_ids.str[1].str[:3]
	df = df.drop('Total')
	print df[:1]

	def first_country():
		return df.iloc[0]

	def gold_medal():
		return df['Gold'].argmax()

	def biggest_difference_in_gold_medal():
		return (df['Gold']-df['Gold.1']).argmax()

	def get_points():
		df['points'] = df['Gold.2']*3 + df['Silver.2']*2 + df['Bronze.2']
		return df['points']

def k_means():
	data = pd.read_csv('olympics.csv')

	f1 = data['Gold.2'].values
	f2 = data['Silver.2'].values
	f3 = data['Bronze.2'].values
	X = np.array(list(zip(f1,f2,f3)))

	kmeans = KMeans(n_clusters=3)
	kmeans = kmeans.fit(X)
	lables = kmeans.predict(X)
	centroids = kmeans.cluster_centers_
	return centroids





