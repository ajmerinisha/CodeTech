import csv
import os
import webbrowser
from collections import defaultdict
from fpdf import FPDF


def analyze_data(filename):
    department_data = defaultdict(list)
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                department = row['Department']
                salary = int(row['Salary'])
                department_data[department].append(salary)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        exit(1)
    except Exception as e:
        print(f"Error while reading the file: {e}")
        exit(1)
    return department_data


def generate_pdf_report(data, output_file):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)


    pdf.set_text_color(0, 0, 128)
    pdf.cell(200, 10, txt="Company Salary Report", ln=True, align='C')
    pdf.ln(10)

    for dept, salaries in data.items():
        total = sum(salaries)
        avg = total / len(salaries)

        pdf.set_text_color(0, 0, 0)
        pdf.set_font("Arial", style='B', size=12)
        pdf.cell(200, 10, txt=f"Department: {dept}", ln=True)

        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt=f"  Total Employees: {len(salaries)}", ln=True)
        pdf.cell(200, 10, txt=f"  Total Salary: Rs. {total}", ln=True)
        pdf.cell(200, 10, txt=f"  Average Salary: Rs. {avg:.2f}", ln=True)
        pdf.ln(5)

    try:
        pdf.output(output_file)
        print(f"\n✅ PDF report generated successfully: {os.path.abspath(output_file)}")
    except Exception as e:
        print(f"Error generating PDF: {e}")


if __name__ == "__main__":
    input_file = "data.csv"
    output_file = "salary_report.pdf"

    data = analyze_data(input_file)
    generate_pdf_report(data, output_file)

    
    webbrowser.open(output_file)
