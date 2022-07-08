from dendropy.calculate import treecompare as tc
import dendropy
import pandas as pd

tns = dendropy.TaxonNamespace()


orig_trees = [f"new_trees/tree{x}.tree" for x in range(100)]

est_trees =  [f"est_tree/est{x}.tree" for x in range(100)]

orig_trees = [dendropy.Tree.get_from_path(
    x,
    'newick'
    ,taxon_namespace=tns) for x in orig_trees]

est_trees = [dendropy.Tree.get_from_path(
    x,
    'newick'
    ,taxon_namespace=tns) for x in est_trees]

diffs = [tc.symmetric_difference(x[0],x[1]) for x in zip(orig_trees,est_trees)]

print(pd.DataFrame(diffs,columns=['difference']).describe())