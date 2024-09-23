from flask import Flask, jsonify
import ibm_boto3
from ibm_botocore.client import Config

app = Flask(__name__)

# Gyökér útvonal ("/") kezelése
@app.route('/')
def home():
    return "Hello, Flask alkalmazás!"

# IBM Cloud Object Storage beállítások
COS_ENDPOINT = "https://s3.us-south.cloud-object-storage.appdomain.cloud"  # Public endpoint
COS_API_KEY_ID = "Pzvf_TUf9ie3MG7qncE7uWqd6CNX35etCldmmorZ2vvZ"  # API kulcs
COS_INSTANCE_CRN = "crn:v1:bluemix:public:cloud-object-storage:global:a/4ce442c9be554c829a35744d0bbee4:62081540-1bf6-437a-8ab5-6c308a8adf56::"  # CRN
bucket_name = "elek-donotdelete-pr-flomvcezkdcypu"  # Bucket neve

@app.route('/upload', methods=['POST'])
def upload_file():
    file_name = "output111.txt"
    text_data = "Ez egy teszt szöveg."

    # IBM COS boto3 kliens létrehozása
    cos = ibm_boto3.client('s3',
                           ibm_api_key_id=COS_API_KEY_ID,
                           ibm_service_instance_id=COS_INSTANCE_CRN,
                           config=Config(signature_version='oauth'),
                           endpoint_url=COS_ENDPOINT)

    try:
        # Fájl feltöltése az IBM Cloud Object Storage-ba
        cos.put_object(
            Bucket=bucket_name,
            Key=file_name,
            Body=text_data
        )
        download_url = f"{COS_ENDPOINT}/{bucket_name}/{file_name}"
        return jsonify({"message": "Fájl sikeresen feltöltve!", "url": download_url})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
