#Program to merge PDF's

import os
from PyPDF2 import PdfWriter

merger = PdfWriter()
pdfs = []

n = int(input("Enter the number of PDF's to be merged: "))

for i in range(n):
  while True:
    name = input(f"Enter the name of PDF {i+1} (with .pdf ): ").strip()
    if os.path.exists(name):
      pdfs.append(name)
      break
    else:
      print("File not found")

for pdf in pdfs:
  merger.append(pdf)

output_name = input("\nEnter a name for the merged PDF (without .pdf): ").strip()
if not output_name:
  output_name = "merged_output"
output_name += ".pdf"

merger.write(output_name)
merger.close()

print(f"\nMerging complete.")
print(f"Saved as '{output_name}'")
