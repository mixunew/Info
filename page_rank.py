# pages and links
links = {
    "A": ["B","C","D"],
    "B": ["C","E"],
    "C": ["A","D"],
    "D": [],
    "E": []
}

# initial rank
rank = {p:1 for p in links}

# one iteration of PageRank
new_rank = {p:0 for p in links}

for page in links:
    if links[page]:
        share = rank[page] / len(links[page])
        for link in links[page]:
            new_rank[link] += share

print("PageRank Values:\n")
for p,r in new_rank.items():
    print(p,"=",round(r,2))