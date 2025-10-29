def arrange_matrix(matrix):
    arranged_matrix = []
    for i in range(len(matrix)):
        for j, row in enumerate(matrix):
            if row[i] == matrix[0][0]:
                arranged_matrix.append([j, row])
                break
    return arranged_matrix

def main():
    notes = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]
    series = [0,1,2,3,4,5,6,7,8,9,10,11] # Change series here
    assert len(set(series)) == len(series), "ERROR: Series has repeated notes!"
    assert len(series) == 12, "ERROR: Length of series is not 12!"
    reversed = series[::-1]
    inverted = []
    for i in range(len(series)):
        if i == 0:
            inverted.append(series[0])
        else:
            inverted.append((inverted[i-1]- (series[i]-series[i-1]))%12)
    inverted_reversed = inverted[::-1]
    print("PRIME:                       ", series)
    print("REVERSED:                    ", reversed)
    print("INVERTED:                    ", inverted)
    print("INVERTED REVERSED:           ", inverted_reversed)
    print("PRIME NOTES:                 ", [notes[series[i]] for i in range(len(series))])
    print("REVERSED NOTES:              ", [notes[reversed[i]] for i in range(len(series))])
    print("INVERTED NOTES:              ", [notes[inverted[i]] for i in range(len(series))])
    print("REVERSED INVERTED NOTES:     ", [notes[inverted_reversed[i]] for i in range(len(series))])
    #Matrix calculation
    matrix = [[notes[(series[i]+offset)%12] for i in range(len(series))] for offset in range(0,12)]
    arranged_matrix = arrange_matrix(matrix)
    print("Pseudo Matrix:")
    for line in arranged_matrix:
        print(f"P{line[0]}: {line[1]}")
    #User query
    while True:
        while True:
            print("What's the type of series?")
            type_of_series = input()
            if type_of_series in ["P", "R", "I", "RI"]:
                break
            print("Valid types: P,R,I,RI")
        while True:
            print("What's the shift?")
            shift = input()
            if shift.isdigit() and int(shift) in range(0, 12):
                shift = int(shift)
                break
            print("Shift must be a number between 0 and 11.")
        if type_of_series == "P":
            print(f"P{shift}:               ", [notes[(series[i]+shift)%12] for i in range(len(series))])
        if type_of_series == "R":
            print(f"R{shift}:               ", [notes[(reversed[i]+shift)%12] for i in range(len(series))])
        if type_of_series == "I":
            print(f"I{shift}:               ", [notes[(inverted[i]+shift)%12] for i in range(len(series))])
        if type_of_series == "RI":
            print(f"RI{shift}:              ", [notes[(inverted_reversed[i]+shift)%12] for i in range(len(series))])
        ans = input("Do you want to do another? (y/n) ")
        if ans == "n":
            break

if __name__ == "__main__":
    main()
