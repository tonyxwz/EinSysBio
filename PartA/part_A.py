#!/usr/bin/env python2
''' Author: Weizhou Xing
    System biology module 3
    Part A
'''
import numpy as np

MATCH = 2
MISMATCH = -1
GAP = -4

def global_alignment(s="", t=""):
    m = len(s) + 1
    n = len(t) + 1
    A = np.zeros([m, n, 2])

    for ii in range(m):
        A[ii, 0, 0] = ii*GAP
    for jj in range(n):
        A[0, jj, 0] = jj*GAP

    for ii in range(m-1):
        for jj in range(n-1):
            if s[ii] == t[jj]:
                A[ii+1, jj+1, 0] = np.max([A[ii,jj,0]+MATCH, A[ii,jj+1,0]+GAP, A[ii+1,jj,0]+GAP])
                #A[ii+1, jj+1, 1] = np.argmax([A[ii,jj,0]+MATCH, A[ii,jj+1,0]+GAP, A[ii+1,jj,0]+GAP])
            else:
                A[ii+1, jj+1, 0] = np.max([A[ii,jj,0]+MISMATCH, A[ii,jj+1,0]+GAP, A[ii+1,jj,0]+GAP])
                #A[ii+1, jj+1, 1] = np.argmax([A[ii,jj,0]+MISMATCH, A[ii,jj+1,0]+GAP, A[ii+1,jj,0]+GAP])

    
    return A[m-1,n-1,0]


def semi_global_alignment(s="", t=""):
    m = len(s) + 1
    n = len(t) + 1
    A = np.zeros([m, n])

    for ii in range(m-1):
        for jj in range(n-1):
            if s[ii] == t[jj]:
                A[ii+1, jj+1] = max(A[ii,jj]+MATCH, A[ii,jj+1]+GAP, A[ii+1,jj]+GAP)
            else:
                A[ii+1, jj+1] = max(A[ii,jj]+MISMATCH, A[ii,jj+1]+GAP, A[ii+1,jj]+GAP)
    
    return max(max(A[m-1,1:]), max(A[1:,n-1]))


def local_alignment(s="", t=""):
    m = len(s) + 1
    n = len(t) + 1
    A = np.zeros([m, n])

    for ii in range(m-1):
        for jj in range(n-1):
            if s[ii] == t[jj]:
                A[ii+1, jj+1] = max(0, A[ii,jj]+MATCH, A[ii,jj+1]+GAP, A[ii+1,jj]+GAP)
            else:
                A[ii+1, jj+1] = max(0, A[ii,jj]+MISMATCH, A[ii,jj+1]+GAP, A[ii+1,jj]+GAP)
    # print A
    # print np.argmax(A)
    return np.max(A[:,:])

# # Extra
# def trace_back(A):
#     pass

# (a)
str1 = "ACAAGGA"
str2 = "ACAGG"
print global_alignment(s=str1, t=str2)
# (b)
str3 = "AGCCATTACCAATTAAGG"
str4 = "CCAATT"
print semi_global_alignment(s=str3, t=str4)
# (c)
str5 = "AGCCTTCCTAGGG"
str6 = "GCTTCGTTT"
print local_alignment(s=str5, t=str6)

# (d)
def special_semi_global_alignment(s="", t=""):
    pass


def read_fasta(path="ebolasequences-1.fasta"):
    with open(path) as f:
        fasta = f.read()

    sequence_list = fasta.split("\n>")
    for i in range(len(sequence_list)):
        start_index = sequence_list[i].find("\n")
        sequence_list[i] = sequence_list[i][start_index:]
        sequence_list[i] = sequence_list[i].replace("\n", "")

    return sequence_list


[str7,str8] = read_fasta(path="/home/joey/Work/systembiology/PartA/ebolasequences-1.fasta")

print special_semi_global_alignment(s=str7, t=str8)
