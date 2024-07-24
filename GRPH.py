def overlap_graph(sequences):
    adjacency_list = []
    for i in range(len(sequences)):
        for j in range(len(sequences)):
            if i != j and sequences[i][1][-3:] == sequences[j][1][:3]:
                adjacency_list.append((sequences[i][0], sequences[j][0]))
    return adjacency_list

sequences = [("Seq1", "AAATAAA"), ("Seq2", "AAATTTT"), ("Seq3", "TTTTCCC"), ("Seq4", "AAATCCC"), ("Seq5", "GGGTGGG")]
print(overlap_graph(sequences))