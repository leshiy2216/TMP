import csv
import re


from checksum import calculate_checksum


regular = [
    r'^[A-Za-z]+$',          
    r'^\d{1,3}$',            
    r'^\d{4}-\d{2}-\d{2}$',  
    r'^\+?\d{10,15}$',       
    r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$',  
    r'^[A-Z]{2}\d{4}[A-Z]{2}$',  
    r'^\d+\.\d{2}$',          
    r'^[A-Z][a-z]+$',        
    r'^[A-Za-z0-9]{8,}$',    
    r'^[A-Za-z\s]+$'         
]


def validate_row(row):
    errors = []
    for i, value in enumerate(row):
        if not re.match(regular[i], value):
            errors.append(i)
    return errors


def process_csv(file_path):
    invalid_row_numbers = []
    with open(file_path, newline='', encoding='latin-1') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for i, row in enumerate(reader):
            if validate_row(row):
                invalid_row_numbers.append(i)
    return invalid_row_numbers


def main():
    csv_file_path = r'E:\TMP\TMP\lab_3\4.csv'
    invalid_rows = process_csv(csv_file_path)
    checksum = calculate_checksum(invalid_rows)
    print(f"Invalid Rows: {invalid_rows}")
    print(f"Checksum: {checksum}")


if __name__ == "__main__":
    main()