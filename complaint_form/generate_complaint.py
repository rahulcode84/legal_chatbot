from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime

def generate_index_pdf(user_name, complainant_name, police_station, output_file="index_output.pdf"):
    c = canvas.Canvas(output_file, pagesize=A4)
    width, height = A4
    
    # Title
    c.setFont("Helvetica-Bold", 12)
    c.drawCentredString(width / 2, height - 50, "BEFORE THE HON’BLE ADDITIONAL DISTRICT")
    c.drawCentredString(width / 2, height - 70, "CONSUMER DISPUTES REDRESSAL COMMISSION,")
    c.drawCentredString(width / 2, height - 90, police_station.upper())
    
    # Case Number
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 130, "CC/24/")
    
    # Complainant and Opponent
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, height - 160, f"{user_name} ....Complainant")
    c.drawString(50, height - 180, "V/s.")
    c.drawString(50, height - 200, f"{complainant_name} ....Opponents")
    
    # Index Title
    c.setFont("Helvetica-Bold", 12)
    c.drawCentredString(width / 2, height - 240, "INDEX")
    
    # Table Header
    c.setFont("Helvetica-Bold", 10)
    c.drawString(50, height - 270, "Sr. No.")
    c.drawString(150, height - 270, "Particulars")
    c.drawString(350, height - 270, "Date")
    c.drawString(450, height - 270, "Page Nos.")
    
    # Table Entries
    entries = [
        "Synopsis",
        "Complaint of the Complainant",
        "Affidavit in support of Complaint",
        "Statement of Claim",
        "Vakalatnama",
        "Address Purshis"
    ]
    
    c.setFont("Helvetica", 10)
    y = height - 290
    for i, entry in enumerate(entries, 1):
        c.drawString(50, y, str(i))
        c.drawString(150, y, entry)
        c.drawString(350, y, "")  # Empty Date Column
        c.drawString(450, y, "")  # Empty Page Nos Column
        y -= 20
    
    c.save()
    print(f"Index PDF generated successfully: {output_file}")

def generate_affidavit_pdf(user_name, complainant_name, police_station, pin_code, applicant_age, occupation, occupation_place, output_file="affidavit_output.pdf"):
    c = canvas.Canvas(output_file, pagesize=A4)
    width, height = A4
    current_date = datetime.now().strftime("%B %d, %Y")
    
    # Title
    c.setFont("Helvetica-Bold", 12)
    c.drawCentredString(width / 2, height - 50, "AFFIDAVIT")
    c.drawCentredString(width / 2, height - 70, "BEFORE THE HON’BLE ADDITIONAL DISTRICT")
    c.drawCentredString(width / 2, height - 90, "CONSUMER DISPUTES REDRESSAL COMMISSION,")
    c.drawCentredString(width / 2, height - 110, police_station.upper())
    
    # Case Number
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 150, "CC/25/")
    
    # Complainant and Opponent
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, height - 180, f"{user_name} ....Complainant")
    c.drawString(50, height - 200, "V/s.")
    c.drawString(50, height - 220, f"{complainant_name} ....Opponents")
    
    # Affidavit Content
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 260, f"I, {user_name} Age: {applicant_age} years, Occupation: {occupation} at {occupation_place}")
    c.drawString(50, height - 280, f"R/at- {user_name}, {police_station}, {pin_code},")
    c.drawString(50, height - 300, "the complainant, do hereby state and declare on")
    c.drawString(50, height - 320, "oath as under:")
    
    affidavit_content = [
        "1. I am the Complainant in the above matter and as",
        "such fully conversant with facts of the case and",
        "competent to swear this affidavit.",
        "",
        "2. I say that I have read and understood the contents of",
        "the complaint filed under the Consumer Protection",
        "Act 2019.",
        "",
        "3. I say that the contents of the complaint filed by me",
        "are true and correct to the best of my knowledge and",
        "belief.",
        "",
        f"The contents and averments above are true and",
        f"correct to the best of my knowledge, belief and",
        f"information and I have signed hereunder on this {current_date}, at {police_station}."
    ]
    
    y = height - 340
    for line in affidavit_content:
        c.drawString(50, y, line)
        y -= 20
    
    # Affiant Signature
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y - 20, "Affiant")
    c.drawString(50, y - 40, "(Complainant)")
    
    c.save()
    print(f"Affidavit PDF generated successfully: {output_file}")

if __name__ == "__main__":
    user_name = input("Enter User Name: ")
    complainant_name = input("Enter Complainant Name: ")
    police_station = input("Enter Police Station Name: ")
    pin_code = input("Enter Pin Code: ")
    applicant_age = input("Enter Applicant Age: ")
    occupation = input("Enter Your Occupation: ")
    occupation_place = input("Enter Your Occupation Place: ")
    
    generate_index_pdf(user_name, complainant_name, police_station)
    generate_affidavit_pdf(user_name, complainant_name, police_station, pin_code, applicant_age, occupation, occupation_place)
