def fileToList(filename):
    """
    Reads a file and returns a list of lines with newlines removed.
    Returns an empty list if the file is empty or does not exist.
    """
    lines = []
    try:
        with open(filename) as file:
            for line in file:
                lines.append(line.strip('\n'))
    except FileNotFoundError:
        return []
    return lines

def returnFirstString(strings):
    """
    Returns the first string in a list, or an empty string if the list is empty.
    """
    for string in strings:
        return strings[0]
    if not strings:
        return ""

def strandsAreNotEmpty(strand1, strand2):
    """
    Returns True if both strands are non-empty, False otherwise.
    """
    if strand1 and strand2:
        return True
    else:
        return False

def strandsAreEqualLengths(strand1, strand2):
    """
    Returns True if both strands are the same length, False otherwise.
    """
    if len(strand1) == len(strand2):
        return True
    else:
        return False
    
def candidateOverlapsTarget(target, candidate, overlap):
    """
    Checks if the last 'overlap' characters of target match the first 'overlap' characters of candidate.
    Returns True if they match, False otherwise.
    """
    return (
        overlap > 0
        and overlap <= len(target)
        and overlap <= len(candidate)
        and target[-overlap:] == candidate[:overlap]
    )

def findLargestOverlap(target, candidate):
    """
    Finds the largest overlap between target and candidate.
    Returns the size of the overlap, or -1 if strands are empty or not the same length.
    """
    if not strandsAreNotEmpty(target, candidate):
        return -1
    if not strandsAreEqualLengths(target, candidate):
        return -1
    for overlap in range(len(target), 0, -1):
        if candidateOverlapsTarget(target, candidate, overlap):
            return overlap
    return 0

def findBestCandidate(target, candidate):
    """
    Finds the candidate with the largest overlap with the target.
    Returns a tuple (best_candidate, max_overlap).
    If no overlap, returns ('', 0).
    """
    best_candidate = ''
    max_overlap = 0
    for string in candidate:
        overlap = findLargestOverlap(target, string)
        if overlap > max_overlap:
            max_overlap = overlap
            best_candidate = string
    return (best_candidate, max_overlap)

def joinTwoStrands(target, candidate, overlap):
    """
    Joins the target and candidate strands, merging at the overlap.
    If overlap is 0, simply concatenates the two strands.
    """
    if overlap == 0:
        joined_strand = target + candidate
    elif overlap > 0:
        joined_strand = target + candidate[overlap:]
    return joined_strand

def main():
    """
    Main function to run the DNA sequencing process:
    - Asks user for filenames
    - Reads files and finds the best candidate
    - Joins the strands and prints the result
    """
    target_filename = input("Target strand filename: ")
    candidate_filename = input("Candidate strands filename: ")

    target_list = fileToList(target_filename)
    candidate_list = fileToList(candidate_filename)

    target_strand = returnFirstString(target_list)
    best_candidate, overlap = findBestCandidate(target_strand, candidate_list)
    combined_strand = joinTwoStrands(target_strand, best_candidate, overlap)

    print(combined_strand)

if  __name__=='__main__':
    main()