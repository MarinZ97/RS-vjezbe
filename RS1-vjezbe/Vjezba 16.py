def dijkstra(graph, start):
    import heapq

    udaljenosti = {node: float('inf') for node in graph}
    udaljenosti[start] = 0
    prioritetni_red = [(0, start)]

    while prioritetni_red:
        trenutna_udaljenost, trenutni_cvor = heapq.heappop(prioritetni_red)

        if trenutna_udaljenost > udaljenosti[trenutni_cvor]:
            continue

        for susjed, tezina in graph[trenutni_cvor]:
            nova_udaljenost = trenutna_udaljenost + tezina

            if nova_udaljenost < udaljenosti[susjed]:
                udaljenosti[susjed] = nova_udaljenost
                heapq.heappush(prioritetni_red, (nova_udaljenost, susjed))

    return udaljenosti

graph = {
'A': [('B', 1), ('C', 4)],
'B': [('A', 1), ('C', 2), ('D', 5)],
'C': [('A', 4), ('B', 2), ('D', 1)],
'D': [('B', 5), ('C', 1)]
}

print(dijkstra(graph, 'A'))