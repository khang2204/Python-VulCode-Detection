def summary(self):...
"""docstring"""
summary = 'Graphical model of order k = ' + str(self.order)
summary += '\n'
summary += 'Nodes:\t\t\t\t' + str(self.vcount()) + '\n'
summary += 'Links:\t\t\t\t' + str(self.ecount()) + '\n'
summary += 'Total weight (sub/longest):\t' + str(self.totalEdgeWeight()[0]
    ) + '/' + str(self.totalEdgeWeight()[1]) + '\n'
return summary
