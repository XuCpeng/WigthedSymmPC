import matplotlib
import pandas as pandas
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import cophenet, dendrogram, linkage
from scipy.spatial.distance import squareform


def save_wspc_figs(filename, method="average", corr="Pearson", fig="eps", out_path=""):
    if corr == "Pearson":
        data = pandas.read_csv("Rp_wspc_" + filename + ".csv")
    elif corr == "Spearman":
        data = pandas.read_csv("Rs_wspc_" + filename + ".csv")

    data = data.drop(data.columns[[0]], axis=1)

    x_rows, x_cols = data.shape

    data_features = data.columns

    data_dis = 1 - data

    y = squareform(data_dis)
    z = linkage(y, method=method)
    c, _ = cophenet(z, y)
    print(filename + '-wspc-' + method + '-' + corr + ': ' + str(c))
    plt.figure(figsize=(15, 8))
    dendrogram(z, labels=data_features, leaf_font_size=12)
    # plt.title(filename + ' ' + method + ' ' + corr + ' Correlations with W.Symm.pivot coord. ',fontdict={'size': 20})
    plt.ylabel("Distance cluster combine", fontdict={'size': 18})

    plt.savefig(out_path + filename + '_' +
                method + '_' +
                corr + ' Correlations with W_Symm_pivot coord' + '.' +
                fig,
                bbox_inches='tight', dpi=600)
    plt.close()


def save_spc_figs(filename, method="average", corr="Pearson", fig="eps", out_path=""):
    if corr == "Pearson":
        data = pandas.read_csv("Rp_" + filename + ".csv")
    elif corr == "Spearman":
        data = pandas.read_csv("Rs_" + filename + ".csv")

    data = data.drop(data.columns[[0]], axis=1)

    x_rows, x_cols = data.shape

    data_features = data.columns

    data_dis = 1 - data

    y = squareform(data_dis)
    z = linkage(y, method=method)
    c, _ = cophenet(z, y)
    print(filename + '-spc-' + method + '-' + corr + ': ' + str(c))
    plt.figure(figsize=(15, 8))
    dendrogram(z, labels=data_features, leaf_font_size=12)
    # plt.title(filename + ' ' + method + ' ' + corr + ' Correlations with W.Symm.pivot coord. ',fontdict={'size': 20})
    plt.ylabel("Distance cluster combine", fontdict={'size': 18, 'weight': 'bold'})

    plt.savefig(out_path + filename + '_' +
                method + '_' +
                corr + ' Correlations with Symm_pivot coord' + '.' +
                fig,
                bbox_inches='tight', dpi=600)
    plt.close()

 
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    matplotlib.rcParams['text.usetex'] = True
    matplotlib.rcParams['text.latex.unicode'] = True
    matplotlib.rcParams['pdf.fonttype'] = 42  # pdf.fonttype : 42 # Output Type 3 (Type3) or Type 42 (TrueType)
    matplotlib.rcParams['ps.fonttype'] = 42
    plt.rc('font', family='Times New Roman')
    save_wspc_figs("datanhao", method="average")
    save_wspc_figs("adaohai", method="average")
    save_wspc_figs("datanhao", method="single")
    save_wspc_figs("adaohai", method="single")
    save_wspc_figs("datanhao", method="complete")
    save_wspc_figs("adaohai", method="complete")

    print("print Success!")
