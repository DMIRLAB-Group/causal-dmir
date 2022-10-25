from causaldmir.utils.independence import ConditionalIndependentTest

from .adjacency_search import adjacency_search


class PC(object):
    def __init__(self,
                 alpha: float = 0.05,
                 adjacency_search_method=adjacency_search,
                 verbose: bool = False
                 ):
        self.causal_graph = None
        self.sep_set = None
        self.alpha = alpha
        self.indep_test = None
        self.adjacency_search_method = adjacency_search_method
        self.verbose = verbose

    def fit(self, indep_test: ConditionalIndependentTest):
        self.indep_test = indep_test
        self.causal_graph, self.sep_set = self.adjacency_search_method(self.indep_test, self.indep_test.var_names,
                                                                       self.alpha, verbose=self.verbose)
        self.causal_graph.rule0(sep_set=self.sep_set, verbose=self.verbose)
        changed = True
        while changed:
            changed = False
            changed |= self.causal_graph.rule1(verbose=self.verbose)
            changed |= self.causal_graph.rule2(verbose=self.verbose)
            changed |= self.causal_graph.rule3(verbose=self.verbose)
            changed |= self.causal_graph.rule4(verbose=self.verbose)

    def set_alpha(self, alpha):
        self.alpha = alpha

    def get_alpha(self):
        return self.alpha

    def set_verbose(self, verbose):
        self.verbose = verbose

    def get_verbose(self):
        return self.verbose
