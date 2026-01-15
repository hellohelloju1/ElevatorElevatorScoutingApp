import streamlit as st
import time as t
import json
import os
# st.set_page_config(layout="wide")
with open("data.json", "r") as f:
    data = json.load(f)
col1, col2 = st.columns([1,4], gap="small")
with col1:
    st.image("https://86832b.this-is-a.website/wp-content/uploads/2025/12/SmallLogo-300x300.png", width=150)
with col2:
    st.title("Push Back Scouting Sheet")
tab1, tab2, tab3 = st.tabs(["View Profile", "New Entry", "Edit Profiles"])
st.markdown("""
<style>
.big-font {
    font-size:30px !important;
}
</style>
""", unsafe_allow_html=True)
with tab1:

    selectedteam = st.selectbox("Select Team", options=[team["Number"] for team in data["Teams"]], key="selected_team")
    try:
        team_info = next(team for team in data["Teams"] if team["Number"] == selectedteam)
        st.header(f"{team_info['Number']} Profile")
        st.divider()
        for key, value in team_info.items():
            for key, value in team_info.items():
                globals()[key] = value
        col1, col2 = st.columns(2, gap="medium")
        with col1:
            st.subheader("Picture",divider="red")
            try:
                st.image(Picture)
            except:
                st.image("Default.png")
        with col2:
            st.subheader("Team Number",divider="red")
            st.markdown(f"<p class='big-font'>{Number}</p>", unsafe_allow_html=True)
            st.subheader("Team Name",divider="red")
            st.markdown(f"<p class='big-font'>{Name}</p>", unsafe_allow_html=True)
            st.subheader("School",divider="red")
            st.markdown(f"<p class='big-font'>{School}</p>", unsafe_allow_html=True)
            st.divider()
            st.image("lol.png",width=100)
        st.divider()
        col1, col2 = st.columns(2, gap="medium")
        with col1:
            st.subheader("Match Flaws",divider="red")
            st.write(Notes["MatchFlaws"])
        with col2:
            st.subheader("Driver Notes",divider="red")
            st.write(Notes["DriverNotes"])
        col1, col2 = st.columns(2, gap="medium")
        with col1:
            st.subheader("Add. Notes",divider="red")
            st.write(Notes["AdditionalNotes"])
        with col2:
            st.subheader("Auton Notes",divider="red")
            st.write(Notes["AutonNotes"])
        st.divider()
        st.header("Info Sheet")
        col1, col2 = st.columns(2, gap="medium",border=True)
        with col1:
            incol1, incol2 = st.columns(2, gap="small")
            with incol1:
                st.write("Left Auton:")
                st.write("Right Auton:")
                st.write("Driver:")
                st.write("Score Mech:")
                st.write("Consistency:")
                st.write("Under long goal:")
                st.write("Aligner:")
            with incol2:
                st.write(InfoSheet["LeftAuton"])
                st.write(InfoSheet["RightAuton"])
                listt = [InfoSheet["Driver"],InfoSheet["ScoreMech"],InfoSheet["Consistency"]]
                for each in listt:
                    stars = ""
                    for x in range(each):
                        stars = stars + "⭐"
                    st.write(stars)
                listt = [InfoSheet["GoUnder"],InfoSheet["Aligner"]]
                for each in listt:
                    if each:
                        st.badge(icon=":material/check:", color="green",label="")
                    else:
                        st.badge(icon=":material/cancel:", color="red",label="")
        with col2:
            incol1, incol2 = st.columns(2, gap="small")
            with incol1:
                st.write("Bot Type:")
                st.write("DT Motor Count:")
                st.write("DT Type:")
                st.write("Parking:")
                st.write("Wing:")
                st.write("Matchload:")
                st.write("Descore:")
            with incol2:
                st.write(InfoSheet["BotType"])
                st.text(InfoSheet["MotorCount"])
                st.write(InfoSheet["DriveType"])
                st.write(InfoSheet["Parking"])
                listt = [InfoSheet["Wing"],InfoSheet["Matchload"],InfoSheet["Descore"]]
                for each in listt:
                    if each:
                        st.badge(icon=":material/check:", color="green",label="")
                    else:
                        st.badge(icon=":material/cancel:", color="red",label="")

    except:
        st.warning("No Teams.")


with tab2:
    st.header("New Team Entry")
    
    # Create input fields for all team data
    col1, col2 = st.columns(2)
    
    with col1:
        uploaded_file = st.file_uploader("Choose an image")
        team_number = st.text_input("Team Number")
        team_name = st.text_input("Team Name")
        school = st.text_input("School")
        MatchFlaws = st.text_area("Match Flaws")
        DriverNotes = st.text_area("Driver Notes")
        AutonNotes = st.text_area("Auton Notes")
        AdditionalNotes = st.text_area("Additional Notes")
    with col2:
        bot_type = st.selectbox("Bot Type", options=["S Bot", "C Bot", "Ruiguan Slope", "Lever Bot", "Basket Bot", "Pushbot", "Other"])
        drive_type = st.selectbox("Drive Type", options=["Tank Drive", "H Drive", "Mecanum Drive", "X Drive", "* Drive", "Swerve Drive", "Other"])
        parking = st.selectbox("Parking", options=["None", "Single", "Double"])
        DT_motor_count = st.number_input("DT Motor Count", min_value=2, max_value=8, step=1)
        left_auton = st.selectbox("Left Auton", options=["None", "You Tried", "Inconsistent", "Decent", "Holy Shit"])
        right_auton = st.selectbox("Right Auton", options=["None", "You Tried", "Inconsistent", "Decent", "Holy Shit"])
        driver_rating = st.slider("Driver Rating", 1, 5, 3)
        score_mech = st.slider("Score Mechanism", 1, 5, 3)
        consistency = st.slider("Consistency", 1, 5, 3)  
        wing = st.checkbox("Wing")
        matchload = st.checkbox("Matchload (tongue)")
        descore = st.checkbox("Descore")
        go_under = st.checkbox("Under Long Goal:")
        aligner = st.checkbox("Aligner")
        
    
    # Save button
    if st.button("Save Team", type="primary"):
        if uploaded_file is not None:
            uploads_dir = "uploads"
            if not os.path.exists(uploads_dir):
                os.makedirs(uploads_dir)
            
            # Save the file
            file_path = os.path.join(uploads_dir, uploaded_file.name)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            # Get the full directory path
            full_path = os.path.abspath(file_path)
            st.write(f"File path: {file_path}")

            st.image(file_path, caption=uploaded_file.name)
        # Create new team entry
        new_team = {
            "Number": team_number,
            "School": school,
            "Name": team_name,
            "Picture": file_path,
            "Notes" : {"MatchFlaws" : MatchFlaws,"DriverNotes" : DriverNotes,"AutonNotes" : AutonNotes,"AdditionalNotes" : AdditionalNotes},
            "InfoSheet" : {
                "BotType": bot_type,
                "DriveType": drive_type,
                "Parking": parking,
                "MotorCount": DT_motor_count,
                "LeftAuton": left_auton,
                "RightAuton": right_auton,
                "Driver": driver_rating,
                "ScoreMech": score_mech,
                "Consistency": consistency,
                "Wing": wing,
                "Matchload": matchload,
                "Descore": descore,
                "GoUnder": go_under,
                "Aligner": aligner
            }

        }

        # Add to data and save to file
        data["Teams"].append(new_team)
        
        with open("data.json", "w") as f:
            json.dump(data, f, indent=2)
        
        st.success(f"Team {team_number} - {team_name} has been added!")
        st.rerun()  # Refresh the app to show the new team in dropdowns
with tab3:
    st.header("Edit Existing Teams")
    selectedteam_edit = st.selectbox("Select Team to Edit", options=[team["Number"] for team in data["Teams"]], key="selected_team_edit")
    def chooseteam():
        global team_info_edit, haveteams
        try:
            team_info_edit = next(team for team in data["Teams"] if team["Number"] == selectedteam_edit)
            haveteams = True
        except:
            haveteams = False
            st.warning("No Teams.")
        
    st.button("Select Team", on_click=chooseteam())
    col1, col2 = st.columns(2)
    if haveteams:
        with col1:
            picture = team_info_edit["Picture"]
            team_name = st.text_input("Team Name", value=team_info_edit["Name"], key="team_name_edit")
            school = st.text_input("School", value=team_info_edit["School"], key="school_edit")
            MatchFlaws = st.text_area("Match Flaws", value=team_info_edit["Notes"]["MatchFlaws"], key="match_flaws_edit")
            DriverNotes = st.text_area("Driver Notes", value=team_info_edit["Notes"]["DriverNotes"], key="driver_notes_edit")
            AutonNotes = st.text_area("Auton Notes", value=team_info_edit["Notes"]["AutonNotes"], key="auton_notes_edit")
            AdditionalNotes = st.text_area("Additional Notes", value=team_info_edit["Notes"]["AdditionalNotes"], key="additional_notes_edit")
        with col2:
            bot_type_options = ["S Bot", "C Bot", "Ruiguan Slope", "Lever Bot", "Basket Bot", "Pushbot", "Other"]
            bot_type = st.selectbox("Bot Type", options=bot_type_options, index=bot_type_options.index(team_info_edit["InfoSheet"]["BotType"]), key="bot_type_edit")
            
            drive_type_options = ["Tank Drive", "H Drive", "Mecanum Drive", "X Drive", "* Drive", "Swerve Drive", "Other"]
            drive_type = st.selectbox("Drive Type", options=drive_type_options, index=drive_type_options.index(team_info_edit["InfoSheet"]["DriveType"]), key="drive_type_edit")
            
            parking_options = ["None", "Single", "Double"]
            parking = st.selectbox("Parking", options=parking_options, index=parking_options.index(team_info_edit["InfoSheet"]["Parking"]), key="parking_edit")
            
            DT_motor_count = st.number_input("DT Motor Count", min_value=2, max_value=8, step=1, value=team_info_edit["InfoSheet"]["MotorCount"], key="dt_motor_count_edit")
            
            left_auton_options = ["None", "You Tried", "Inconsistent", "Decent", "Holy Shit"]
            left_auton = st.selectbox("Left Auton", options=left_auton_options, index=left_auton_options.index(team_info_edit["InfoSheet"]["LeftAuton"]), key="left_auton_edit")
            
            right_auton_options = ["None", "You Tried", "Inconsistent", "Decent", "Holy Shit"]
            right_auton = st.selectbox("Right Auton", options=right_auton_options, index=right_auton_options.index(team_info_edit["InfoSheet"]["RightAuton"]), key="right_auton_edit")
            
            driver_rating = st.slider("Driver Rating", 1, 5, value=team_info_edit["InfoSheet"]["Driver"], key="driver_rating_edit")
            score_mech = st.slider("Score Mechanism", 1, 5, value=team_info_edit["InfoSheet"]["ScoreMech"], key="score_mech_edit")
            consistency = st.slider("Consistency", 1, 5, value=team_info_edit["InfoSheet"]["Consistency"], key="consistency_edit")  
            wing = st.checkbox("Wing", value=team_info_edit["InfoSheet"]["Wing"], key="wing_edit")
            matchload = st.checkbox("Matchload (tongue)", value=team_info_edit["InfoSheet"]["Matchload"], key="matchload_edit")
            descore = st.checkbox("Descore", value=team_info_edit["InfoSheet"]["Descore"], key="descore_edit")
            go_under = st.checkbox("Under Long Goal:", value=team_info_edit["InfoSheet"]["GoUnder"], key="go_under_edit")
            aligner = st.checkbox("Aligner", value=team_info_edit["InfoSheet"]["Aligner"], key="aligner_edit")
            
    
    if st.button("Modify", type="primary"):
        # Create new team entry
        new_team = {
            "Number": team_info_edit["Number"],
            "School": school,
            "Name": team_name,
            "Picture": team_info_edit["Picture"],
            "Notes" : {"MatchFlaws" : MatchFlaws,"DriverNotes" : DriverNotes,"AutonNotes" : AutonNotes,"AdditionalNotes" : AdditionalNotes},
            "InfoSheet" : {
                "BotType": bot_type,
                "DriveType": drive_type,
                "Parking": parking,
                "MotorCount": DT_motor_count,
                "LeftAuton": left_auton,
                "RightAuton": right_auton,
                "Driver": driver_rating,
                "ScoreMech": score_mech,
                "Consistency": consistency,
                "Wing": wing,
                "Matchload": matchload,
                "Descore": descore,
                "GoUnder": go_under,
                "Aligner": aligner
            }

        }
        
        st.success(f"Team {team_number} - {team_name} modified!")
        t.sleep(2)
        st.rerun()  # Refresh the app to show the new team in dropdowns
    confi = st.text_input("Type meowmeowmeow to confirm deletion", key="delete_confirm")
    if st.button("Delete Entry"):
        if confi == "meowmeowmeow":
            team_index = next((i for i, team in enumerate(data["Teams"]) if team["Number"] == selectedteam_edit), None)
            if team_index is not None:
                team_index = next((i for i, team in enumerate(data["Teams"]) if team["Number"] == team_number), None)
                removed_team = data["Teams"].pop(team_index)
                data["Teams"].append(new_team)
                t.sleep(1)
                removed_team = data["Teams"].pop(team_index)
                with open("data.json", "w") as f:
                    json.dump(data, f, indent=2)


                
                with open("data.json", "w") as f:
                    json.dump(data, f, indent=2)

                st.success(f"Team {removed_team['Number']} - {removed_team['Name']} deleted!")
                t.sleep(1)
                st.rerun()
            else:
                st.error("Team not found!")
                st.rerun()
        else:
            st.error("please type in confirmation")
    
    # Pre-fill input fields with existing data

st.text("meow - CY")
