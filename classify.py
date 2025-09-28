from processor_regex import classify_with_regex
from processor_bert import classify_with_bert
from processor_llm import classify_with_llm
import pandas as pd

def classify_log(source, log_msg):

    if(source == "LegacyCRM"):

        label = classify_with_llm(log_msg)
    else:

        label = classify_with_regex(log_msg)

        if(label is None):
            label = classify_with_bert(log_msg)

    return label

def classify(logs):
    labels = []
    for source, log_msg in logs:
        label = classify_log(source, log_msg)
        labels.append(label)

    return labels

def classify_csv(f):

    df=pd.read_csv(f)
    df["target_label"] = classify(list(zip(df["source"], df["log_message"])))

    output_file = "ressources/output.csv"
    df.to_csv(output_file, index = False)

if __name__ == "__main__":
    classify_csv("ressources/test.csv")
    '''logs = [
        ("BillingSystem", "User User231 logged in."),
        ("LegacyCRM", "Lead conversion failed for prospect ID 100 due to missing contact information."),
        ("ModernCRM", "Email service experiencing issues with sending."),
        ("LegacyCRM", "API endpoint 'getCustomerDetails' is deprecated and will be removed in version 3.2. Use 'fetchCustomerInfo' instead."),
        ("ThirdPartyAPI", "File data_300.csv uploaded successfully by user User50."),
        ("ModernHR", "User 80 made multiple failed login attempts."),
        ("AnalyticsEngine", "System component has failed: component ID Component450."),
        ("ModernCRM", "alpha.osapi_compute.wsgi.server - 12.10.11.1 - API returned 404 not found error.")
    ]

    labels = classify(logs)
    print(labels)'''


