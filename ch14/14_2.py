def sed(pat_str, rep_str, file1, file2):
    
    try:
        fin = open(file1)
        fout = open(file2, 'w')

        Words = []
        for line in fin:
            word = line.strip()
            Words.append(word)

            while pat_str in Words:
                Words[Words.index(pat_str)] = rep_str

            out_str = '\n'.join(Words)
            fout.write(out_str)
            fin.close()
            fout.close()
    except:
        "Useless error message"



sed("xxx", "yyy", "infile.o", "outfile.o")
