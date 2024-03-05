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
    answers["(a) explain diag entries, Matrix 1"] = "The two diagonal entries that are more blue and crisp suggest that clusters B and C are more tightly knit, showing higher cohesion, compared to the other two clusters, A and D."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 1"] = "The first and third rows represent clusters A and C because the colors of their off-diagonal entries differ, showing varying distances to other clusters. Specifically, A is closest to C (blue), then B (green), and farthest from D (yellow); the same pattern applies to C. The second row matches cluster B, with equal distances to A and C (green) and the greatest distance to D (red). The fourth row matches cluster D, with equal distances from A and C (yellow) and the greatest distance from B (red), illustrating the distinct spatial relationships between these clusters."

    # type: string
    answers["(a) Matrix 2"] = "Dataset X"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 2"] = "The presence of two diagonal entries that are more blue and crisp compared to the others suggests that two clusters, B and C, exhibit better cohesion, meaning they are more tightly grouped, than the other two clusters, A and D."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 2"] = "Rows with less crisp diagonal entries (rows 1 and 4) have all  different colors, indicating that all other clusters have different  distances from these clusters (e.g: Cluster A is the nearest to B,  followed by C and then D, no 2 clusters have same distance to cluster A).  2. Rows with more crisp diagonal entries have 2 same colors (other than  the diagonal), indicating that it has same distance to 2 clusters,  and is the furthest from 1 cluster (e.g: B’s distance to A and C is  similar, but is the furtherst from D)"

    # type: string
    answers["(a) Matrix 3"] = "Dataset Y"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 3"] = "The two diagonal entries that are more blue and crisp compared to the others indicate that clusters B and C have better cohesion, meaning they are more tightly knit or compact, compared to the other two clusters, A and D."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 3"] = "The presence of two similar and one different color in the off-diagonal entries of all rows indicates that each cluster is relatively closer to two other clusters than to the remaining one. For example, Cluster B is similarly close to Clusters A and C when compared to its distance from Cluster D."

    # type: string
    answers["(b) Row 1"] = "Cluster A"

    # type: string
    answers["(b) Row 2"] = "Cluster B"

    # type: string
    answers["(b) Row 3"] = "Cluster C"

    # type: string
    answers["(b) Row 4"] = "Cluster D"

    # type: explanatory string (at least four words)
    answers["(b) Row 1 explain"] = "A less crisp diagonal entry suggests the cluster is less cohesive, meaning its points are not as tightly grouped. The different colors in all off-diagonal entries indicate that the cluster has varying distances to other clusters, being closest to B, then to C, and furthest from A."

    # type: explanatory string (at least four words)
    answers["(b) Row 2 explain"] = "A more crisp diagonal entry indicates the cluster is cohesive, meaning its points are closely grouped. When two out of three off-diagonal entries share the same color, it shows that two other clusters (A and C, despite the entry for A being less crisp) are closer to this cluster. This arrangement suggests the cluster is furthest from one other cluster (D)."

    # type: explanatory string (at least four words)
    answers["(b) Row 3 explain"] = "The explanation is simimilar to row 2"

    # type: explanatory string (at least four words)
    answers["(b) Row 4 explain"] = "The explanation, similar to row 1 but in inverted order, suggests that while the cluster remains cohesive (indicated by a crisp diagonal entry), the distances to other clusters are reversed. This means the cluster is closest to what was previously the furthest (D) and furthest from what was previously the closest (A), with the middle distances to B and C also adjusting accordingly."

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
    answers["(a) explain"] = "DBSCAN can identify clusters matching patterns like the nose, eyes, and mouth because it's good at finding clusters in areas with varying densities and shapes, including both dense and sparse regions."

    # type: string
    answers["(b) Figure (a)"] = "No"

    # type: string
    answers["(b) Figure (b)"] = "Yes"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "K-means is better for datasets with clusters of similar density, not so much for areas with different densities. However, in high-density areas where clusters are tightly packed and clearly separated, K-means can still be effective."

    # type: string
    answers["(c)"] = "DBSCAN clustering is preferred for its flexibility in handling both high and low-density areas and its ability to identify clusters with irregular shapes, making it versatile for various data patterns."

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
