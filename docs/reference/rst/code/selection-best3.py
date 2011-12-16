# Description: Ranking and selection of best N attributes
# Category:    feature selection
# Uses:        voting
# Referenced:  Orange.feature.html#selection
# Classes:     Orange.feature.scoring.score_all, Orange.feature.selection.bestNAtts

import Orange
table = Orange.data.Table("voting")

n = 3
ma = Orange.feature.scoring.score_all(table)
best = Orange.feature.selection.bestNAtts(ma, n)
print 'Best %d features:' % n
for s in best:
    print s