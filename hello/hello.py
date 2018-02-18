from couchbase.cluster import Cluster
from couchbase.cluster import PasswordAuthenticator



cluster = Cluster('couchbase://localhost')
authenticator = PasswordAuthenticator('aanghour', 'pass123')
cluster.authenticate(authenticator)
bucket = cluster.open_bucket('travel-sample')

res = bucket.get('airline_10')
print(res)