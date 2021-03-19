beer = {'하이트': 2000, '카스': 2100, '칭따오': 2500, '하이네켄': 4000, '버드와이저': 500}
beerup = {x: beer[x] * 1.05 for x in beer}

print("{0}            # 인상 전".format(beer))
print("{0}  # 인상 후".format(beerup))