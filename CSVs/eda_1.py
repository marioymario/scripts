from matplotlib import pyplot as plt
import math
import numpy as np 
import pandas as pd 
import seaborn as sns 
import pdb
from time import time
from sklearn import metrics
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from PIL import Image

""" EDA and visualization also the imports"""

df_sapo = pd.read_csv('/home/gato/SCRIPTS_001/CSVs/Frogs_MFCCs.csv')
print('\n First 5 rows:')
print(df_sapo.head())
print('\nData type and basic information')
print(df_sapo.info())

print('\n Statistical Analysis')
X = df_sapo.iloc[:, :-4]
print(X.describe())
print('\n No missing Values, all infomation has been normalized...')
print('looking into the distribution of some columns')
fig = plt.figure(figsize=(18,15))
# loop over all numerical columns
for i in range(1, X.shape[1]):
    plt.subplot(6, 6, i)
    f = plt.gca()
    f.axes.get_yaxis().set_visible(False)
    f.set_title(X.columns.values[i])
    #f.axes.set_ylim([0, X.shape[0]])
    plt.xticks(rotation = 45)

    vals = np.size(X.iloc[:, i].unique())
    if vals < 10:
        bins = vals
    else:
        vals = 10

    plt.hist(X.iloc[:, i], bins=30, color='#3f7d6a')

plt.tight_layout()

plt.savefig("histogram-distribution.png")
# open method used to open different extension image file
im = Image.open(r"/home/gato/SCRIPTS_001/CSVs/histogram-distribution.png") 
  # This method will show image in any image viewer 
im.show() 

# Prerequisitos for Sklearn, all to array
yyy = df_sapo.iloc[:, 22:-1]
Data = X.to_numpy(dtype=None, copy=True)
labels = yyy.Family.to_numpy(dtype=None, copy=True)
labels_Genus = yyy.Genus.to_numpy(dtype=None, copy=True)
labels_Species = yyy.Species.to_numpy(dtype=None, copy=True)

#@title Assignando el numero de clustars
seleccion = str(input('seleccionar Family,  Genus or  Species :'))
(n_samples, n_features), n_digits = df_sapo.shape, np.unique(df_sapo[seleccion]).size
print(f"# digits: {n_digits}; # samples: {n_samples}; # features {n_features}")

print('Metrics')
#@title metricas
def bench_k_means(kmeans, name, data, labels):
  
    t0 = time()
    estimator = make_pipeline(StandardScaler(), kmeans).fit(data)
    fit_time = time() - t0
    results = [name, fit_time, estimator[-1].inertia_]

    # Define the metrics which require only the true labels and estimator
    # labels
    clustering_metrics = [
        metrics.homogeneity_score,
        metrics.completeness_score,
        metrics.v_measure_score,
        metrics.adjusted_rand_score,
        metrics.adjusted_mutual_info_score,
    ]
    results += [m(labels, estimator[-1].labels_) for m in clustering_metrics]

    # The silhouette score requires the full dataset
    results += [
        metrics.silhouette_score(data, estimator[-1].labels_,
                                 metric="euclidean", sample_size=300,)
    ]

    # Show the results
    formatter_result = ("{:9s}\t{:.3f}s\t{:.0f}\t{:.3f}\t{:.3f}"
                        "\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}")
    print(formatter_result.format(*results))
    

print(82 * '_')
print('init\t\ttime\tinertia\thomo\tcompl\tv-meas\tARI\tAMI\tsilhouette')

kmeans = KMeans(init="k-means++", n_clusters=n_digits, n_init=4,
                random_state=111)
bench_k_means(kmeans=kmeans, name="k-means++", data=X, labels=labels)

kmeans = KMeans(init="random", n_clusters=n_digits, n_init=4, random_state=0)
bench_k_means(kmeans=kmeans, name="random", data=X, labels=labels)

pca = PCA(n_components=n_digits).fit(X)
kmeans = KMeans(init=pca.components_, n_clusters=n_digits, n_init=1)
bench_k_means(kmeans=kmeans, name="PCA-based", data=X, labels=labels) #Benchmark to evaluate the KMeans initialization methods.

print(82 * '_')

reduced_data = PCA(n_components=2).fit_transform(X)
kmeans = KMeans(init="k-means++", n_clusters=n_digits, n_init=4)
kmeans.fit(reduced_data)

# Step size of the mesh. Decrease to increase the quality of the VQ.
h = .005     # point in the mesh [x_min, x_max]x[y_min, y_max].

# Plot the decision boundary. For that, we will assign a color to each
x_min, x_max = reduced_data[:, 0].min() - 1, reduced_data[:, 0].max() + 1
y_min, y_max = reduced_data[:, 1].min() - 1, reduced_data[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

# Obtain labels for each point in mesh. Use last trained model.
Z = kmeans.predict(np.c_[xx.ravel(), yy.ravel()])

# Put the result into a color plot
Z = Z.reshape(xx.shape)
plt.figure(1, figsize = [20, 20])

plt.clf()
plt.imshow(Z, interpolation="nearest",
           extent=(xx.min(), xx.max(), yy.min(), yy.max()),
           cmap=plt.cm.Paired, aspect="auto", origin="lower")

plt.plot(reduced_data[:, 0], reduced_data[:, 1], 'k.', markersize=2)
# Plot the centroids as a white X
centroids = kmeans.cluster_centers_
plt.scatter(centroids[:, 0], centroids[:, 1], marker="X", s=180, linewidths=1,
            color="w", zorder=10)
plt.title("K-means clustering on the Anuran Calls data set (PCA-reduced data)\n"
          "Centroids are marked with white cross")
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())
plt.show()