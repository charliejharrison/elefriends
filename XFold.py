from sklearn.cross_validation import KFold

class XFold:

    def __init__(self, _pos, _neg, _n_folds=10):
        self.pos = _pos
        self.neg = _neg
        self.n_folds = _n_folds

        self.pos_folds = KFold(len(pos), n_folds=self.n_folds)
        self.neg_folds = KFold(len(neg), n_folds=self.n_folds)


    def next_fold():
        try:
            pos_train, pos_test = pos_folds.next()
            neg_train, neg_test = neg_folds.next()
        except StopIteration:
            return None

        return (pos[pos_train], neg[neg_train], pos[pos_test], neg[neg_test])

