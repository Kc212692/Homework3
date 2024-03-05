# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Agglomerative hierarchical clustering is like building a family tree for data points, combining them step by step based on closeness. K-means clustering puts each data point in the nearest group but can be misled by very distant points."

    # type: bool (True/False)
    answers["(b)"] = True

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "K-means clustering produces varying results due to the randomness in selecting initial centroids, while Agglomerative hierarchical clustering consistently yields the same result each time as it is deterministic."

    # type: bool (True/False)
    answers["(c)"] = False

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "K-means clustering is known for its efficiency in terms of time and memory usage compared to agglomerative hierarchical clustering. While K-means is considered one of the most efficient clustering algorithms, there are other algorithms like the leader algorithm that offer alternative approaches to clustering."


    # type: bool (True/False)
    answers["(d)"] = False

    # type: explanatory string (at least four words)
    answers["(d) explain"] = "Splitting a cluster into two lowers the total error because we now have two centers instead of one. This means each point is closer to its nearest center, reducing the overall distance."

    # type: bool (True/False)
    answers["(e)"] = True

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "The sum of squared errors (SSE) shows how tightly grouped a cluster is. When SSE goes down, it means the cluster is more cohesive. If SSE goes up, the cluster's cohesion decreases."

    # type: bool (True/False)
    answers["(f)"] = True

    # type: explanatory string (at least four words)
    answers["(f) explain"] = "In k-means, the sum of squares between (SSB) measures how far apart clusters are. So, if SSB goes up, it means clusters are more spread out from each other. If SSB goes down, clusters are closer together."

    # type: bool (True/False)
    answers["(g)"] = False

    # type: explanatory string (at least four words)
    answers["(g) explain"] = "In k-means, making clusters tighter (improving cohesion) doesn't necessarily mean they'll be further apart from each other (improving separation)."

    # type: bool (True/False)
    answers["(h)"] = True

    # type: explanatory string (at least four words)
    answers["(h) explain"] = "In k-means clustering, the total sum of squares (TSS) is the combination of the sum of squared errors (SSE) and the sum of squares between (SSB). Additionally, the TSS remains constant throughout the k-means clustering process."

    # type: bool (True/False)
    answers["(i)"] = True

    # type: explanatory string (at least four words)
    answers["(i) explain"] = "SSB measures how far apart clusters are, while SSE indicates how close together points within a cluster are, but in reverse. So, when clusters become tighter (more cohesive), SSE goes down and SSB, which shows separation, goes up."

    return answers




# -----------------------------------------------------------
def question2():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "The figure illustrates that the clusters are positioned too far from their centroids to draw points from neighboring clusters."

    # type: bool (True/False)
    answers["(b)"] = False

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "The figure shows that the shaded areas are near each other, meaning the clusters will include points from both shaded regions."

    # type: bool (True/False)
    answers["(c)"] = True

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "The centroid at 12.5 is too distant from all points, resulting in all other clusters being empty."

    return answers




# -----------------------------------------------------------
def question3():
    answers = {}

    # type: a string that evaluates to a float
    answers["(a) SSE"] = "(R^2)*4"

    # type: a string that evaluates to a float
    answers["(b) SSE"] = "4*((a*a) + (b*b) + (c*c))"

    # type: a string that evaluates to a float
    answers["(c) SSE"] = "4*((R^2) + ((R/2)^2))"

    return answers




# -----------------------------------------------------------
def question4():
    answers = {}

    # type: int
    answers["(a) Circle (a)"] = 1

    # type: int
    answers["(a) Circle (b)"] = 1

    # type: int
    answers["(a) Circle (c)"] = 1

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Because A and B both have the same number of points (100) and are equally distant, one centroid will be drawn towards A. Consequently, the right side of B, making up two-thirds of it, will then have two centroids. Circle C, with a significantly higher number of points (100,000) and equally spaced to B, will definitely secure a centroid because of its stronger attraction, despite not having one initially. The balanced distribution of points in A and B ensures that each will attract a centroid due to their comparable pull."

    # type: int
    answers["(b) Circle (a)"] = 1

    # type: int
    answers["(b) Circle (b)"] = 1

    # type: int
    answers["(b) Circle (c)"] = 1

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "The centroid will remain at A because of the points already there and the lack of a stronger attraction elsewhere. C's stronger pull will draw one centroid away from B. Therefore, each of the three circles, A, B, and C, will end up having one centroid each."

    # type: int
    answers["(c) Circle (a)"] = 0

    # type: int
    answers["(c) Circle (b)"] = 0

    # type: int
    answers["(c) Circle (c)"] = 2

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "Since circles A and B are near each other but distant from circle C, points from both A and B will be grouped with the centroid in A. Circle C's points will be split among two centroids, with each holding 50,000 points. Because A and B have an equal number of points, the centroid in A will shift between them. Meanwhile, the centroids in C will slightly separate but remain within C, each managing half of the points."

    return answers




# -----------------------------------------------------------
def question5():
    answers = {}

    # type: set
    answers["(a)"] = {'Group A', 'Group B'}

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Groups A and B can be combined because the rightmost point of A and the leftmost point of B are the closest to each other, indicating the shortest single-link distance between the two groups."

    # type: set
    answers["(b)"] = {'Group A', 'Group C'}

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Groups A and C can be merged because the rightmost point of A and the farthest point of C have the shortest complete-link distance between them, making them the closest pair for merging under this criterion."

    return answers




# -----------------------------------------------------------
def question6():
    answers = {}

    # type: set
    answers["(a) core"] = {'B', 'C', 'E', 'F', 'I', 'J', 'L', 'M'}

    # type: set
    answers["(a) boundary"] = {'D', 'G'}

    # type: set
    answers["(a) noise"] = {'A', 'H'}

    # type: set
    answers["(b) cluster 1"] = {'B','C','D','E','F','G'}

    # type: set
    answers["(b) cluster 2"] = {'I','J','L','M'}

    # type: set
    answers["(b) cluster 3"] = set()

    # type: set
    answers["(b) cluster 4"] = set()

    # type: set
    answers["(c)-a core"] = {'I', 'G', 'J', 'E', 'M', 'B', 'L', 'F', 'D', 'C'}

    # type: set
    answers["(c)-a boundary"] = {'A', 'H'}

    # type: set
    answers["(c)-a noise"] = set()

    # type: set
    answers["(c)-b cluster 1"] = {'G', 'I', 'H', 'J', 'E', 'M', 'B', 'D', 'F', 'L', 'C'}

    # type: set
    answers["(c)-b cluster 2"] = {'A'}

    # type: set
    answers["(c)-b cluster 3"] = set()

    # type: set
    answers["(c)-b cluster 4"] = set()

    return answers




# -----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    answers["(a)"] = "Cluster 4"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Cluster 4 has the highest entropy because its categories are more evenly distributed, leading to greater uncertainty or diversity within the cluster."

    # type: string
    answers["(b)"] = "Cluster 1"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Cluster 1 has low entropy because its data points are mostly from one category, making it very uniform or similar throughout." 
    return answers




# -----------------------------------------------------------
def question8():
    answers = {}

    # type: string
    answers["(a) Matrix 1"] = "Dataset Z"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 1"] = ""

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 1"] = ""

    # type: string
    answers["(a) Matrix 2"] = "Dataset X"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 2"] = ""

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 2"] = ""

    # type: string
    answers["(a) Matrix 3"] = "Dataset Y"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 3"] = ""

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 3"] = ""

    # type: string
    answers["(b) Row 1"] = "Cluster A"

    # type: string
    answers["(b) Row 2"] = "Cluster B"

    # type: string
    answers["(b) Row 3"] = "Cluster C"

    # type: string
    answers["(b) Row 4"] = "Cluster D"

    # type: explanatory string (at least four words)
    answers["(b) Row 1 explain"] = ""

    # type: explanatory string (at least four words)
    answers["(b) Row 2 explain"] = ""

    # type: explanatory string (at least four words)
    answers["(b) Row 3 explain"] = ""

    # type: explanatory string (at least four words)
    answers["(b) Row 4 explain"] = ""

    return answers




# -----------------------------------------------------------
def question9():
    answers = {}

    # type: list
    answers["(a)"] = ['Hierarchical', 'Partial', 'Overlapping']

    # type: list
    answers["(b)"] = ['Partitional', 'Exclusive', 'Complete']

    # type: list
    answers["(c)"] = ['Partitional', 'fuzzy', 'complete']


    # type: list
    answers["(d)"] = ['Hierarchical', 'overlapping', 'partial']

    # type: list
    answers["(e)"] = ['Partitional', 'Exclusive', 'Complete']

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "Letter grades are unique categories that don't overlap, meaning each category is exclusive. Each student gets only one grade per class, ensuring exclusivity. Additionally, every student in the class will be assigned a grade, making the system complete."

    return answers




# -----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    answers["(a) Figure (a)"] = "Yes"

    # type: string
    answers["(a) Figure (b)"] = "Yes"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = ""

    # type: string
    answers["(b) Figure (a)"] = "No"

    # type: string
    answers["(b) Figure (b)"] = "Yes"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = ""

    # type: string
    answers["(c)"] = ""

    return answers

# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()
    print('end code')

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
