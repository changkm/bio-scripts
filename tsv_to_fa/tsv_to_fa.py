#!/usr/bin/env python3

import argparse

def main(input_file_name: str, output_file_name: str) -> None:

    with open(input_file_name) as f:
        lines = f.readlines()

    entries = []


    for line in lines:
        line = line.strip().strip("\t")
        length = len(line.split("\t"))
        header1 = seq1 = header2 = seq2 = header3 = seq3 = None
        if length == 12:
            header1, seq1, _, _, header2, seq2, _, _, header3, seq3, _, _ = line.split("\t")
        elif length == 9:
            header1, seq1, _, _, _, header2, seq2, _, _ = line.split("\t") 
        elif length == 4:
            header1, seq1, _, _ = line.split("\t")
        else:
            import pprint
            pprint.pprint(line.split("\t"))
            raise
        if header1:
            entries.append(f">{header1}")
            entries.append(seq1)
        if header2:
            entries.append(f">{header2}")
            entries.append(seq2)
        if header3:
            entries.append(f">{header3}")
            entries.append(seq3)


    with open(output_file_name, "w") as f:
        for entry in entries:
            print(entry, file=f)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Turn a TSV into fastfa.')
    parser.add_argument("input_file", type=str, help="TSV file to parse. Expects the format to be <seqID>\t<sequence>\t<other-column>\t<another-column>\t. Up to three of these sets per row")
    parser.add_argument("--output_file", type=str, default="", help="Optional output fastfa file. Defaults to same name and folder as input file")
    args = parser.parse_args()
    
    if args.output_file:
        output_file_name = args.output_file
    else:
        # Strip .tsv and replace with .fastfa
        output_file_name = ".".join(args.input_file.split(".")[:-1]) + ".fastfa"

    main(args.input_file, output_file_name)

    

