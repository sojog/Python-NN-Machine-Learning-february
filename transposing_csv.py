import csv

def transpose_csv(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        rows = list(reader)
        print("rows:", rows)
        print("*rows:", *rows)
        print("zip(*rows)", zip(*rows))

        transposed_rows = list(zip(*rows))
        print(transposed_rows)

        writer.writerows(transposed_rows)

input_file = 'Annex2PRUDENT002.csv'
output_file = 'Annex2PRUDENT002_output.csv'
transpose_csv(input_file, output_file)



import pandas as pd

def transpose_csv_pandas(input_file, output_file):

    df = pd.read_csv(input_file, header=None)  # header=None because your input has no header row

    # Transpunerea DataFrame-ului
    df_transposed = df.T

    # Scrierea DataFrame intr-un nou CSV file
    df_transposed.to_csv(output_file, index=False, header=False)  #


# Example usage
input_file = 'Annex2PRUDENT001.csv'
output_file = 'Annex2PRUDENT001_output_with_pandas.csv'
transpose_csv_pandas(input_file, output_file)