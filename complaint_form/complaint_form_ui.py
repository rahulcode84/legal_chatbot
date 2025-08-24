import streamlit as st
#from generate_complaint import generate_index_pdf, generate_affidavit_pdf


def complaint_form():
    st.header("📝 Automatic Consumer Complaint Form")
    st.markdown("""
    ### Welcome to the Online Consumer Complaint Filing System
    This form will help you file a formal consumer complaint against a business or service provider.
    Please fill in all details carefully. Fields marked with * are mandatory.
    
    Need help? Look for the ℹ️ icon next to each field for guidance.
    """)

    with st.form("complaint_form"):
        # Case Details Section with improved help text
        st.subheader("📌 Case Details")
        st.info("This section captures information about your complaint and the compensation you're seeking.")
        
        case_type = st.selectbox(
            "Case Type *", 
            ["Consumer Complaint", "Product Defect", "Service Issue", "Unfair Trade Practice", "Deficiency in Service"],
            help="Select the type of complaint that best describes your situation."
        )
        
        col1, col2 = st.columns(2)
        with col1:
            paid_consideration = st.number_input(
                "Amount Paid (₹) *", 
                min_value=0.0, 
                help="Enter the total amount you paid to the business or service provider (in INR)."
            )
        with col2:
            claim_consideration = st.number_input(
                "Amount Claimed (₹) *", 
                min_value=0.0, 
                help="Enter the total compensation amount you are claiming from the opposite party (in INR)."
            )
        
        date_cause = st.date_input(
            "Date of Incident/Issue *", 
            help="Select the date when the issue occurred or when you discovered the problem."
        )
        
        col1, col2 = st.columns(2)
        with col1:
            state_cause = st.text_input(
                "State where Issue Occurred *", 
                help="Enter the name of the state where the incident took place."
            )
        with col2:
            district_cause = st.text_input(
                "District where Issue Occurred *",
                help="Enter the district where the incident took place."
            )
        
        col1, col2 = st.columns(2)
        with col1:
            case_category = st.selectbox(
                "Case Category *", 
                ["Product Defect", "Service Issue", "Misleading Advertisement", "Unfair Contract Terms", "E-commerce Issue", "Other"],
                help="Select the broad category that your complaint falls under."
            )
        with col2:
            sub_category = st.text_input(
                "Sub Category *", 
                help="Further classification of your complaint (e.g., 'Defective Electronics', 'Flight Cancellation', 'Insurance Claim Rejection')."
            )

        # Complainant Details Section
        st.markdown("---")
        st.subheader("👤 Your Details (Complainant)")
        st.info("Please provide your personal information as the person filing the complaint.")
        
        comp_name = st.text_input(
            "Full Name *", 
            help="Enter your full legal name as it appears on official documents."
        )
        
        col1, col2 = st.columns(2)
        with col1:
            comp_relation = st.selectbox(
                "Relation *", 
                ["S/o", "D/o", "W/o", "H/o"],
                help="S/o = Son of, D/o = Daughter of, W/o = Wife of, H/o = Husband of"
            )
        with col2:
            comp_relative_name = st.text_input(
                "Relative's Name *",
                help="Enter name of your father/mother/spouse as per the relation selected."
            )
        
        col1, col2 = st.columns(2)
        with col1:
            comp_mobile = st.text_input(
                "Mobile Number *", 
                help="Enter your 10-digit mobile number. This will be used for communication regarding your complaint."
            )
        with col2:
            comp_email = st.text_input(
                "Email", 
                help="Enter your email address for receiving updates about your complaint."
            )
        
        comp_age_type = st.selectbox(
            "Special Category (if applicable)", 
            ["None", "Senior Citizen", "Widow", "Differently Abled", "Serious Ailments"],
            help="Select if you belong to any special category. This information may be considered during your case."
        )
        
        # Complainant Address
        st.subheader("Your Address")
        comp_address_type = st.selectbox(
            "Address Type *", 
            ["Present", "Permanent", "Present and Permanent"],
            help="Select the type of address you are providing."
        )

        col1, col2 = st.columns(2)
        with col1:
            comp_house = st.text_input(
                "House No./Building *", 
                help="Enter your house number, apartment, or building name."
            )
        with col2:
            comp_block = st.text_input(
                "Street/Area/Sector *", 
                help="Enter your street name, area, or sector."
            )
        
        comp_landmark = st.text_input(
            "Landmark", 
            help="Enter a nearby landmark for easier identification of your address (optional)."
        )
        
        col1, col2, col3 = st.columns(3)
        with col1:
            comp_country = st.text_input(
                "Country *", 
                value="India"
            )
        with col2:
            comp_state = st.text_input(
                "State *", 
                help="Enter the state of your residence."
            )
        with col3:
            comp_district = st.text_input(
                "District *", 
                help="Enter the district of your residence."
            )
        
        col1, col2 = st.columns(2)
        with col1:
            comp_pincode = st.text_input(
                "Pincode *", 
                help="Enter your 6-digit postal code."
            )
        with col2:
            comp_post_office = st.text_input(
                "Post Office", 
                help="Enter your local post office name (optional)."
            )
        
        comp_police_station = st.text_input(
            "Police Station", 
            help="Enter your local police station name (optional)."
        )

        # Opposite Party Details Section
        st.markdown("---")
        st.subheader("🏢 Opposite Party Details (Business/Service Provider)")
        st.info("Provide details of the business, company, or person against whom you are filing the complaint.")
        
        opp_name = st.text_input(
            "Name of Business/Company/Person *", 
            help="Enter the full name of the business or individual against whom you are filing the complaint."
        )
        
        col1, col2 = st.columns(2)
        with col1:
            opp_relation = st.selectbox(
                "Relation (if applicable)", 
                ["Not Applicable", "S/o", "D/o", "W/o", "H/o"],
                help="Select only if the opposite party is an individual (not a company)."
            )
        with col2:
            opp_relative_name = st.text_input(
                "Relative's Name (if applicable)",
                help="Required only if the opposite party is an individual person."
            )
        
        col1, col2 = st.columns(2)
        with col1:
            opp_mobile = st.text_input(
                "Contact Number *", 
                help="Enter the contact number of the business or person you're complaining against."
            )
        with col2:
            opp_email = st.text_input(
                "Email (if available)", 
                help="Enter the email address of the business or person."
            )
        
        opp_age_type = st.selectbox(
            "Category (if applicable)", 
            ["Not Applicable", "Corporate Entity", "Government Organization", "Individual"],
            help="Select the category that best describes the opposite party."
        )
        
        # Opposite Party Address
        st.subheader("Opposite Party Address")
        opp_address_type = st.selectbox(
            "Address Type *", 
            ["Business Address", "Registered Office", "Branch Office", "Residence"],
            help="Select the type of address you are providing for the opposite party."
        )

        col1, col2 = st.columns(2)
        with col1:
            opp_house = st.text_input(
                "Building/Office No. *", 
                help="Enter building number or office number of the opposite party."
            )
        with col2:
            opp_block = st.text_input(
                "Street/Area/Sector *", 
                help="Enter the street, area or sector of the opposite party's address."
            )
        
        opp_landmark = st.text_input(
            "Landmark (Opposite Party)", 
            help="Enter a nearby landmark for easier identification (optional)."
        )
        
        col1, col2, col3 = st.columns(3)
        with col1:
            opp_country = st.text_input(
                "Country (Opposite Party) *", 
                value="India"
            )
        with col2:
            opp_state = st.text_input(
                "State (Opposite Party) *", 
                help="Enter the state of the opposite party's address."
            )
        with col3:
            opp_district = st.text_input(
                "District (Opposite Party) *", 
                help="Enter the district of the opposite party's address."
            )
        
        col1, col2 = st.columns(2)
        with col1:
            opp_pincode = st.text_input(
                "Pincode (Opposite Party) *", 
                help="Enter the 6-digit postal code of the opposite party's address."
            )
        with col2:
            opp_post_office = st.text_input(
                "Post Office (Opposite Party)", 
                help="Enter local post office name (optional)."
            )
        
        opp_police_station = st.text_input(
            "Police Station (Opposite Party)", 
            help="Enter local police station name (optional)."
        )

        # Complaint Details Section - Added for better context
        st.markdown("---")
        st.subheader("📄 Complaint Details")
        st.info("Provide a clear description of your complaint.")
        
        complaint_description = st.text_area(
            "Description of Complaint *", 
            height=150,
            help="Provide a detailed description of your complaint. Include what happened, when it happened, and what you expect as resolution."
        )
        
        # Evidence Upload - Optional section for future implementation
        st.subheader("📎 Supporting Documents (Optional)")
        st.info("You can attach supporting documents related to your complaint.")
        
        file_upload = st.file_uploader(
            "Upload Documents (Bills, Communication, Photos, etc.)", 
            accept_multiple_files=True,
            help="Upload any documents that support your complaint such as bills, receipts, emails, or photos."
        )

        # Submit Button with confirmation checkbox
        st.markdown("---")
        terms_agree = st.checkbox(
            "I confirm that all the information provided above is true to the best of my knowledge *",
            help="You must confirm this to submit the form."
        )
        
        submitted = st.form_submit_button("Submit Complaint")

        if submitted:
            if terms_agree:
                st.success("Form submitted successfully! Your complaint is now being processed...")
                st.info("Your complaint reference number will be sent to your mobile and email shortly.")
                # You can call your automation function here and pass the collected values
                return {
                    "case_type": case_type,
                    "paid_consideration": paid_consideration,
                    "claim_consideration": claim_consideration,
                    "date_cause": str(date_cause),
                    "state_cause": state_cause,
                    "district_cause": district_cause,
                    "case_category": case_category,
                    "sub_category": sub_category,
                    "complaint_description": complaint_description,
                    "complainant": {
                        "name": comp_name,
                        "relation": comp_relation,
                        "relative_name": comp_relative_name,
                        "mobile": comp_mobile,
                        "email": comp_email,
                        "age_type": comp_age_type,
                        "address_type": comp_address_type,
                        "house": comp_house,
                        "block": comp_block,
                        "landmark": comp_landmark,
                        "country": comp_country,
                        "pincode": comp_pincode,
                        "state": comp_state,
                        "district": comp_district,
                        "post_office": comp_post_office,
                        "police_station": comp_police_station
                    },
                    "opposite_party": {
                        "name": opp_name,
                        "relation": opp_relation,
                        "relative_name": opp_relative_name,
                        "mobile": opp_mobile,
                        "email": opp_email,
                        "age_type": opp_age_type,
                        "address_type": opp_address_type,
                        "house": opp_house,
                        "block": opp_block,
                        "landmark": opp_landmark,
                        "country": opp_country,
                        "pincode": opp_pincode,
                        "state": opp_state,
                        "district": opp_district,
                        "post_office": opp_post_office,
                        "police_station": opp_police_station
                    }
                }
            else:
                st.error("Please confirm that all information provided is true before submitting.")

            # Extracting data from the form_data
'''
            # Generate PDFs
            index_pdf_path = f"complaint_form/generated_index_{user_name}.pdf"
            affidavit_pdf_path = f"complaint_form/generated_affidavit_{user_name}.pdf"
                
            generate_index_pdf(user_name, complainant_name, police_station, output_file=index_pdf_path)
            generate_affidavit_pdf(user_name, complainant_name, police_station, pin_code, applicant_age, occupation, occupation_place, output_file=affidavit_pdf_path)

            st.success("PDFs generated successfully!")
            st.write("📄", index_pdf_path)
            st.write("📄", affidavit_pdf_path)'''


# if data: handle_submission(data)  # save to csv/json and call automation