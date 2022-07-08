from dendropy.calculate import treecompare as tc
import dendropy
import pandas as pd

tns = dendropy.TaxonNamespace()

tree_files = ["trees/tree"+str(x)+".tree" for x in range(1,11)]

original_trees = [dendropy.Tree.get_from_path(
    x,
    "newick",
    taxon_namespace = tns
) for x in tree_files]

estimated_tree = dendropy.Tree.get_from_path(
    "trees/tree.txt",
    "newick",
    taxon_namespace = tns
)


diffs = [tc.symmetric_difference(y,estimated_tree) for y in original_trees]
df = pd.DataFrame(diffs,columns=['difference']).describe()
print(df)
