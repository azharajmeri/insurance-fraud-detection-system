from django.shortcuts import render, HttpResponse
import requests

def home(request):
    return render(request, "index.html")

def fraud_detection(request):
    if request.method == 'POST':
        print(request.POST['age'], "------------------------")
    
    # NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
    API_KEY = "YnlkkR_ZgrYqWQsmbP7EFzGrzyN_Ds5j8Sgw4Vwygn-a"
    token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
    mltoken = token_response.json()["access_token"]

    header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

    # NOTE: manually define and pass the array(s) of values to be scored in the next line
    payload_scoring = {
        "input_data": [
            {
                "fields": [
                    "months_as_customer",
                    "age",
                    "policy_state",
                    "policy_csl",
                    "policy_deductable",
                    "policy_annual_premium",
                    "umbrella_limit",
                    "insured_sex",
                    "insured_education_level",
                    "insured_occupation",
                    "insured_hobbies",
                    "insured_relationship",
                    "capital-gains",
                    "capital-loss",
                    "incident_type",
                    "collision_type",
                    "incident_severity",
                    "authorities_contacted",
                    "incident_state",
                    "incident_city",
                    "incident_hour_of_the_day",
                    "number_of_vehicles_involved",
                    "property_damage",
                    "bodily_injuries",
                    "witnesses",
                    "police_report_available",
                    "total_claim_amount",
                    "injury_claim",
                    "property_claim",
                    "vehicle_claim",
                    "auto_make",
                    "auto_model",
                    "auto_year"
			    ],
                "values": [[
                    request.POST['month_as_customer'],
                    request.POST['age'],
                    request.POST['state'],
                    None,
                    None,
                    None,
                    None,
                    None,
                    request.POST['eduction_level'],
                    request.POST['occupation'],
                    request.POST['hobby'],
                    None,
                    None,
                    None,
                    None,
                    None,
                    request.POST['incident_severity'],
                    request.POST['autorities_contacted'],
                    request.POST['incident_state'],
                    None,
                    request.POST['incident_hour'],
                    None,
                    None,
                    None,
                    request.POST['witnessess'],
                    request.POST['policy_report_available'],
                    None,
                    None,
                    None,
                    None,
                    request.POST['auto_company'],
                    request.POST['auto_model'],
                    request.POST['auto_year'],
                ]]
            }
        ]
    }

    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/8d31dc0c-4cf1-4819-a6d4-f294ea7946fe/predictions?version=2021-10-21&version=2021-10-21', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
    print("Scoring response")
    print(response_scoring.json())
    x = response_scoring.json()
    return HttpResponse(x['predictions'][0]["values"][0][0] + "," + str(x['predictions'][0]["values"][0][1][0])+ "," + str(x['predictions'][0]["values"][0][1][1]))

def result(request):
    return render(request, "result.html")