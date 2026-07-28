def getRanking(query):...
ngrams = makeNGrams(query)
print(ngrams)
ranking = Ranking()
ids = set()
for ngram in ngrams:
records = sendIndexReq(' '.join(ngram))
additionalStatList = sendIndexDocumentReq(ids)
ranking.addNgram(records)
for additionalStat in additionalStatList:
for record in records:
ranking.addMoreStats(additionalStat)
rankedList = ranking.getDocuments()
ids.add(record[1])
return rankedList
