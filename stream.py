import streamlit as st
#from xgboost import XGBclassifier
import pickle  

pickle_in = open("C:\\Users\\dell\\Desktop\\VS_Code\\Project\\Model\\XGBoost.pkl", 'rb')
print(pickle_in)
classifier = pickle.load(pickle_in)
st.title("Insurance Fraud Prediction")


months_as_customer = st.slider("Number of Month ",0,120)
policy_deductable = st.number_input("policy_deductable")
umbrella_limit = st.slider("umbrella_limit",0,10000000, step= 1000000)
capital_gains = st.number_input("capital-gains")
capital_loss = st.number_input("capital-loss")
incident_hour_of_the_day  = st.slider("incident_hour_of_the_day",0,24)
number_of_vehicles_involved = st.slider("number_of_vehicles_involved",0,5)
bodily_injuries = st.slider("bodily_injuries",0,5)
witnesses = st.slider("witnesses",0,5)
injury_claim = st.number_input("injury_claim")
property_claim = st.number_input("property_claim")
vehicle_claim = st.number_input("vehicle_claim")

policy_csl =  st.selectbox("policy_csl",['100/300', '250/500', '500/1000'])
if policy_csl == '100/300':
	policy_csl = 1
elif policy_csl == '250/500':
	policy_csl =2.5
else:
	insured_sex = 5

insured_sex = st.selectbox("insured_sex",['Male','Female'])
if insured_sex == 'Male':
	insured_sex = 1
else:
	insured_sex = 0

insured_education_level = st.selectbox("insured_education_level",['JD' , 'High School' ,'College','Masters','Associate','MD','PhD'])
if insured_education_level == 'JD':
	insured_education_level = 1
elif insured_education_level == 'High School' :
	insured_education_level = 2
elif insured_education_level =='College':
	insured_education_level = 3
elif insured_education_level == 'Masters':
	insured_education_level = 4
elif insured_education_level =='Associate':
	insured_education_level = 5
elif insured_education_level =='MD':
	insured_education_level = 6
else :
	insured_education_level = 7

incident_severity = st.selectbox("incident_severity",['Trivial Damage', 'Minor Damage','Major Damage','Total Loss'])
if incident_severity == 'Trivial Damage':
	incident_severity = 1
elif incident_severity == 'Minor Damage' :
	incident_severity = 2
elif incident_severity == 'Major Damage':
	incident_severity = 3
else :
	incident_severity = 4

property_damage = st.selectbox("property_damage",['Yes','No'])
if property_damage == 'Yes':
	property_damage = 1
else:
	property_damage = 0


police_report_available = st.selectbox("police_report_available",['Yes','No'])
if police_report_available == 'Yes':
	police_report_available = 1
else:
	police_report_available = 0

insured_occupation_armed_forces_1 =  st.selectbox("insured_occupation_armed_forces_1",['Yes','No'])
if insured_occupation_armed_forces_1 == 'Yes':
	insured_occupation_armed_forces_1 = 1
else:
	insured_occupation_armed_forces_1 = 0

insured_occupation_craft_repair_1 =  st.selectbox("insured_occupation_craft_repair_1",['Yes','No'])
if insured_occupation_craft_repair_1 == 'Yes':
	insured_occupation_craft_repair_1 = 1
else:
	insured_occupation_craft_repair_1 = 0

insured_occupation_exec_managerial_1 =  st.selectbox("insured_occupation_exec_managerial_1",['Yes','No'])
if insured_occupation_exec_managerial_1 == 'Yes':
	insured_occupation_exec_managerial_1 = 1
else:
	insured_occupation_exec_managerial_1 = 0
	
insured_occupation_farming_fishing_1 = st.selectbox("insured_occupation_farming_fishing_1",['Yes','No'])
if insured_occupation_farming_fishing_1 == 'Yes':
	insured_occupation_farming_fishing_1 = 1
else:
	insured_occupation_farming_fishing_1 = 0

insured_occupation_handlers_cleaners_1 = st.selectbox("insured_occupation_handlers_cleaners_1",['Yes','No'])
if insured_occupation_handlers_cleaners_1 == 'Yes':
	insured_occupation_handlers_cleaners_1 = 1
else:
	insured_occupation_handlers_cleaners_1 = 0

insured_occupation_machine_op_inspct_1 = st.selectbox("insured_occupation_machine_op_inspct_1",['Yes','No'])
if insured_occupation_machine_op_inspct_1 == 'Yes':
	insured_occupation_machine_op_inspct_1 = 1
else:
	insured_occupation_machine_op_inspct_1 = 0

insured_occupation_other_service_1 = st.selectbox("insured_occupation_other_service_1",['Yes','No'])
if insured_occupation_other_service_1 == 'Yes':
	insured_occupation_other_service_1 = 1
else:
	insured_occupation_other_service_1 = 0

insured_occupation_priv_house_serv_1 =  st.selectbox("insured_occupation_priv_house_serv_1",['Yes','No'])
if insured_occupation_priv_house_serv_1 == 'Yes':
	insured_occupation_priv_house_serv_1 = 1
else:
	insured_occupation_priv_house_serv_1 = 0

insured_occupation_prof_specialty_1 = st.selectbox("insured_occupation_prof_specialty_1",['Yes','No'])
if insured_occupation_prof_specialty_1 == 'Yes':
	insured_occupation_prof_specialty_1 = 1
else:
	insured_occupation_prof_specialty_1 = 0

insured_occupation_protective_serv_1 = st.selectbox("insured_occupation_protective_serv_1",['Yes','No'])
if insured_occupation_protective_serv_1 == 'Yes':
	insured_occupation_protective_serv_1 = 1
else:
	insured_occupation_protective_serv_1 = 0

insured_occupation_sales_1 = st.selectbox("insured_occupation_sales_1",['Yes','No'])
if insured_occupation_sales_1 == 'Yes':
	insured_occupation_sales_1 = 1
else:
	insured_occupation_sales_1 = 0

insured_occupation_tech_support_1 = st.selectbox("insured_occupation_tech_support_1",['Yes','No'])
if insured_occupation_tech_support_1 == 'Yes':
	insured_occupation_tech_support_1 = 1
else:
	insured_occupation_tech_support_1 = 0

insured_occupation_transport_moving_1 =  st.selectbox("insured_occupation_transport_moving_1",['Yes','No'])
if insured_occupation_transport_moving_1 == 'Yes':
	insured_occupation_transport_moving_1 = 1
else:
	insured_occupation_transport_moving_1 = 0

insured_relationship_not_in_family_1 = st.selectbox("insured_relationship_not_in_family_1",['Yes','No'])
if insured_relationship_not_in_family_1 == 'Yes':
	insured_relationship_not_in_family_1 = 1
else:
	insured_relationship_not_in_family_1 = 0

insured_relationship_other_relative_1 = st.selectbox("insured_relationship_other_relative_1",['Yes','No'])
if insured_relationship_other_relative_1 == 'Yes':
	insured_relationship_other_relative_1 = 1
else:
	insured_relationship_other_relative_1 = 0

insured_relationship_own_child_1 = st.selectbox("insured_relationship_own_child_1",['Yes','No'])
if insured_relationship_own_child_1 == 'Yes':
	insured_relationship_own_child_1 = 1
else:
	insured_relationship_own_child_1 = 0

insured_relationship_unmarried_1 = st.selectbox("insured_relationship_unmarried_1",['Yes','No'])
if insured_relationship_unmarried_1 == 'Yes':
	insured_relationship_unmarried_1 = 1
else:
	insured_relationship_unmarried_1 = 0

insured_relationship_wife_1 = st.selectbox("insured_relationship_wife_1",['Yes','No'])
if insured_relationship_wife_1 == 'Yes':
	insured_relationship_wife_1 = 1
else:
	insured_relationship_wife_1 = 0

incident_type_Parked_Car_1 = st.selectbox("incident_type_Parked_Car_1",['Yes','No'])
if incident_type_Parked_Car_1 == 'Yes':
	incident_type_Parked_Car_1 = 1
else:
	incident_type_Parked_Car_1 = 0

incident_type_Single_Vehicle_Collision_1 = st.selectbox("incident_type_Single_Vehicle_Collision_1",['Yes','No'])
if incident_type_Single_Vehicle_Collision_1 == 'Yes':
	incident_type_Single_Vehicle_Collision_1 = 1
else:
	incident_type_Single_Vehicle_Collision_1 = 0

incident_type_Vehicle_Theft_1 =  st.selectbox("incident_type_Vehicle_Theft_1",['Yes','No'])
if incident_type_Vehicle_Theft_1 == 'Yes':
	incident_type_Vehicle_Theft_1 = 1
else:
	incident_type_Vehicle_Theft_1 = 0

collision_type_Rear_Collision_1 = st.selectbox("collision_type_Rear_Collision",['Yes','No'])
if collision_type_Rear_Collision_1 == 'Yes':
	collision_type_Rear_Collision_1 = 1
else:
	collision_type_Rear_Collision_1 = 0

collision_type_Side_Collision_1 =  st.selectbox("collision_type_Side_Collision",['Yes','No'])
if collision_type_Side_Collision_1 == 'Yes':
	collision_type_Side_Collision_1 = 1
else:
	collision_type_Side_Collision_1 = 0

authorities_contacted_Fire_1 = st.selectbox("authorities_contacted_Fire_1",['Yes','No'])
if authorities_contacted_Fire_1 == 'Yes':
	authorities_contacted_Fire_1 = 1
else:
	authorities_contacted_Fire_1 = 0

authorities_contacted_None_1 = st.selectbox("authorities_contacted_None_1",['Yes','No'])
if authorities_contacted_None_1 == 'Yes':
	authorities_contacted_None_1 = 1
else:
	authorities_contacted_None_1 = 0

authorities_contacted_Other_1 = st.selectbox("authorities_contacted_Other_1",['Yes','No'])
if authorities_contacted_Other_1 == 'Yes':
	authorities_contacted_Other_1 = 1
else:
	authorities_contacted_Other_1 = 0

authorities_contacted_Police_1 = st.selectbox("authorities_contacted_Police_1",['Yes','No'])
if authorities_contacted_Police_1 == 'Yes':
	authorities_contacted_Police_1 = 1
else:
	authorities_contacted_Police_1 = 0

submit = st.button('Predict')

feature = ['months_as_customer', 'policy_deductable', 'umbrella_limit',
       'capital_gains', 'capital_loss', 'incident_hour_of_the_day',
       'number_of_vehicles_involved', 'bodily_injuries', 'witnesses',
       'injury_claim', 'property_claim', 'vehicle_claim', 'policy_csl',
       'insured_sex', 'insured_education_level', 'incident_severity',
       'property_damage', 'police_report_available',
       'insured_occupation_armed_forces_1',
       'insured_occupation_craft_repair_1',
       'insured_occupation_exec_managerial_1',
       'insured_occupation_farming_fishing_1',
       'insured_occupation_handlers_cleaners_1',
       'insured_occupation_machine_op_inspct_1',
       'insured_occupation_other_service_1',
       'insured_occupation_priv_house_serv_1',
       'insured_occupation_prof_specialty_1',
       'insured_occupation_protective_serv_1', 'insured_occupation_sales_1',
       'insured_occupation_tech_support_1',
       'insured_occupation_transport_moving_1',
       'insured_relationship_not_in_family_1',
       'insured_relationship_other_relative_1',
       'insured_relationship_own_child_1', 'insured_relationship_unmarried_1',
       'insured_relationship_wife_1', 'incident_type_Parked_Car_1',
       'incident_type_Single_Vehicle_Collision_1',
       'incident_type_Vehicle_Theft_1', 'collision_type_Rear_Collision_1',
       'collision_type_Side_Collision_1', 'authorities_contacted_Fire_1',
       'authorities_contacted_None_1', 'authorities_contacted_Other_1',
       'authorities_contacted_Police_1']

if submit:
    prediction = classifier.predict(feature)
	#prediction = 0
    if prediction == 0:
	    st.success("Claim is legitimate")
    else:
	    st.error("Fraudulent claim")