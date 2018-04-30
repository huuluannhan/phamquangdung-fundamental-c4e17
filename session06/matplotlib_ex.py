from matplotlib import pyplot
# 1. Prepare data
machine_counts=[18,4,2]
# 2. Prepare labels
machine_names=["PC","MAC","Linux"]
# 3. Draw piechart
pyplot.pie(machine_counts,labels=machine_names,autopct="%.1f%%",shadow=True,explode=[0,0.15,0])
pyplot.title("OS usage in C4E")
pyplot.axis("equal")
# 4. Show
pyplot.show()
