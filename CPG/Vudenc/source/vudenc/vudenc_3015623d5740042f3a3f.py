def _load_clusters(self):...
"""docstring"""
import soscollector.clusters
package = soscollector.clusters
supported_clusters = {}
clusters = self._load_modules(package, 'clusters')
for cluster in clusters:
supported_clusters[cluster[0]] = cluster[1](self)
return supported_clusters
