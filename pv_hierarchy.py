import matplotlib
import pandas as pandas
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import cophenet, dendrogram, linkage
from scipy.spatial.distance import pdist


def save_pv_figs(filename, method="average", distance="correlation", fig="eps", out_path="", figsize=(15, 8)):
    data = pandas.read_csv(filename + ".csv")
    data = data.drop(data.columns[[0]], axis=1)
    x_rows, x_cols = data.shape

    data_features = data.columns

    y = pdist(data.T, distance)

    z = linkage(y, method=method)
    c, _ = cophenet(z, y)
    print(filename + '-pv-' + method + '-' + distance + ': ' + str(c))
    plt.figure(figsize=figsize)
    dendrogram(z, labels=data_features, leaf_font_size=12)
    # plt.title(filename + ' ' + method + ' ' + corr + ' Correlations with W.Symm.pivot coord. ',fontdict={'size': 20})
    plt.ylabel("Distance cluster combine", fontdict={'size': 18, 'weight': 'bold'})

    plt.savefig(out_path + filename + '_' +
                method + '_' +
                distance + ' with Pivot Coord' + '.' +
                fig,
                bbox_inches='tight', dpi=600)
    plt.close()


matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams['text.latex.unicode'] = True
matplotlib.rcParams['pdf.fonttype'] = 42  # pdf.fonttype : 42 # Output Type 3 (Type3) or Type 42 (TrueType)
matplotlib.rcParams['ps.fonttype'] = 42
plt.rc('font', family='Times New Roman')
save_pv_figs("PV_adaohai", "average", "correlation")
save_pv_figs("PV_adaohai", "single", "correlation")
save_pv_figs("PV_adaohai", "complete", "correlation")

save_pv_figs("PV_adaohai", "average", "euclidean", figsize=(13, 8))
save_pv_figs("PV_adaohai", "single", "euclidean", figsize=(13, 8))
save_pv_figs("PV_adaohai", "complete", "euclidean", figsize=(13, 8))
save_pv_figs("PV_adaohai", "centroid", "euclidean", figsize=(13, 8))

save_pv_figs("PV_datanhao", "average", "correlation")
save_pv_figs("PV_datanhao", "single", "correlation")
save_pv_figs("PV_datanhao", "complete", "correlation")

save_pv_figs("PV_datanhao", "average", "euclidean", figsize=(13, 8))
save_pv_figs("PV_datanhao", "single", "euclidean", figsize=(13, 8))
save_pv_figs("PV_datanhao", "complete", "euclidean", figsize=(13, 8))
save_pv_figs("PV_datanhao", "centroid", "euclidean", figsize=(13, 8))
