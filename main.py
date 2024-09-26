from flask import Flask, jsonify, request
import ibm_boto3
from ibm_botocore.client import Config

app = Flask(__name__)

# IBM Cloud Object Storage beállítások
COS_ENDPOINT = "https://s3.us-south.cloud-object-storage.appdomain.cloud"  # Public endpoint
COS_API_KEY_ID = "nXkSMheA7GT9zdnrHJwKSqmn-VCJPhXGe7XstbLvrLW2"  # API kulcs
COS_INSTANCE_CRN = "crn:v1:bluemix:public:cloud-object-storage:global:a/46c4f2c9bc554c8293a3574f4d0bee64:6208154c-1bfc-437a-8ab5-6c3088afdf56:bucket:elek-donotdelete-pr-flomvcezkdcypu"  # CRN
bucket_name = "elek-donotdelete-pr-flomvcezkdcypu"  # Bucket neve

@app.route('/')
def home():
    return "Hello, Flask alkalmazás!"

@app.route('/upload', methods=['POST'])
def upload_file():
    file_name = "output111.txt"
    
    # Kérjük be a JSON-ből a 'fileContent' értéket
    text_data = request.json.get('fileContent', 'Alapértelmezett szöveg')  # Ha nincs megadva, 'Alapértelmezett szöveg'

    # IBM COS boto3 kliens létrehozása
    cos = ibm_boto3.client('s3',
                           ibm_api_key_id=COS_API_KEY_ID,
                           ibm_service_instance_id=COS_INSTANCE_CRN,
                           config=Config(signature_version='oauth'),
                           endpoint_url=COS_ENDPOINT)

    try:
        # Fájl feltöltése az IBM Cloud Object Storage-be
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
