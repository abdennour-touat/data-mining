import sys
import numpy as np
import pandas as pd

arr = []


# qst1
def chargerData(path):
    data = []
    with open(path, "r") as file:
        for line in file:
            data.append(line.split(","))
    return data


def classifyData(data):
    newData = np.array(data)

    return newData.T[:-1].astype("float")


data = chargerData("dataset.txt")
data = classifyData(data)


# qst2
def dataInfo(data):
    print(len(data), "line")
    print(sys.getsizeof(data), "bytes")


# dataInfo(data)
# qst3
def moyenne(data):
    dataSize = len(data)
    sum = 0
    for i in data:
        sum += i
    return sum / dataSize


def mediane(data):
    sortedData = np.sort(data)
    middle_elements = 0
    if len(sortedData % 2 == 0):
        middle_elements = sortedData[
            len(sortedData) // 2 - 1 : len(sortedData) // 2 + 1
        ]
        middle_elements = (middle_elements[0] + middle_elements[1]) / 2
    else:
        middle_elements = sortedData[len(sortedData) // 2]
    return middle_elements


def mode(data):
    counts = []
    unique = np.unique(data)
    for i in range(len(unique)):
        count = 0
        for j in range(1, len(data)):
            if data[i] == data[j]:
                count += 1
        counts.append(count)
    occurence = 0
    max = 0
    for count in counts:
        if max < count:
            max = count
            occurence = 0
        elif max == count:
            occurence += 1
    return occurence


def tendanceCentrale(data: np.array):
    # mode moyenne mediane
    moy = moyenne(data)
    print("moy ", moy)
    med = mediane(data)
    print("mediane ", med)
    mod = mode(data)
    print("mode ", mod)


# print(data[0])


# qst4
def quartile(data):
    q0 = np.min(data)
    q2 = mediane(data)
    q4 = np.max(data)
    if len(data) % 2 == 0:
        q1 = mediane(data[0 : len(data) // 2])
        q3 = mediane(data[len(data) // 2 + 1 : len(data)])
    else:
        q1 = mediane(data[0 : len(data) // 2])
        q3 = mediane(data[len(data) // 2 + 1 : len(data)])
    return q0, q1, q2, q3, q4


# qst5
def nbPercentage(data):
    count = 0
    for i in data:
        if i == None:
            count += 1
    print("les valeurs null ", count)
    return count


# print("attr 1:\n")

# tendanceCentrale(data[0])
# quartile(data[0])
# nbPercentage(data[0])
# print("attr 2")
# tendanceCentrale(data[1])
# quartile(data[1])
# nbPercentage(data[1])
# print("attr 3")
# tendanceCentrale(data[2])
# quartile(data[2])
# nbPercentage(data[2])
# print("attr 4")
# tendanceCentrale(data[3])
# quartile(data[3])
# nbPercentage(data[3])


# Exo 2
import matplotlib.pyplot as plt


# qst1
def diagrammeDispersion(data, xlabel, ylabel):
    plt.title("digramme de dispersion")
    plt.xlabel(xlabel=xlabel)
    plt.ylabel(ylabel=ylabel)
    plt.scatter(data[0], data[1])
    plt.show()


# qst2
# histogramme
def histogram(data, title):
    plt.title(title)
    plt.hist(data)
    plt.show()


# qst3
def boxPlot(data, title):
    # calculer les quartiles
    q0, q1, q2, q3, q4 = quartile(data)
    # calculer outliers
    min_range = 1.5 * q1
    max_range = q3 * 1.5
    iqr = q3 - q1
    min_range = iqr * 1.5

    new_data = []
    for i in data:
        if i < q1 - min_range or i > q3 + max_range:
            # remove the outlier from the data
            continue
        else:
            new_data.append(i)
    # print(new_data)
    # print(data)
    plt.title(title)
    plt.boxplot(new_data)
    # plt.boxplot(data)
    plt.show()


# diagrammeDispersion((data[0],data[1]),"attr1","attr2")
# diagrammeDispersion((data[2],data[3]),"attr3","attr4")
# diagrammeDispersion((data[0],data[2]),"attr1","attr3")
# diagrammeDispersion((data[1],data[3]),"attr2","attr4")
# histogram(data[0],"attr1")
# histogram(data[1],"attr2")
# histogram(data[2],"attr3")
# histogram(data[3],"attr4")
# boxPlot(data[0],"attr1")
# boxPlot(data[1],"attr2")
# boxPlot(data[2],"attr3")
boxPlot(data[3], "attr4")


# exo 3
def discretiser(data):
    # calculate K
    k = 1 + 3.3 * np.log10(len(data))
    largeur = (np.max(data) - np.min(data)) / k
    print(k)
    # discretiser
    new_data = []
    for i in data:
        new_data.append(np.floor((i - np.min(data)) / largeur))
    # bins = [np.min(data[0])+i*largeur for i in range(int(8)+1)]
    # discretized_data = np.digitize(data, bins)
    # print(discretized_data)
    # print(new_data)
    return new_data


def normaliser(data, new_data):
    new_list = []
    for i in range(len(data)):
        new_val = (data[i] - np.min(data)) / (np.max(data) - np.min(data))
        new_val = new_val * 1 + np.min(new_data)
        new_list.append(new_val)
    return new_list


new_list = discretiser(data[0])
# print("discretiser")
# print(new_list)
normalized_list = normaliser(data[0], new_list)
print("normaliser")
print(normalized_list)


def zscore2(data):
    new_data = data - np.mean(data)
    s = (np.sum(data - np.mean(data)) ** 2) / len(data)
    print(s)
    new_data = new_data / s
    return data


print(zscore2(data[0]))
