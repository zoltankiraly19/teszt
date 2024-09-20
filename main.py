from flask import Flask, jsonify
import ibm_boto3
from ibm_botocore.client import Config

app = Flask(__name__)

COS_ENDPOINT = "https://s3.us-south.cloud-object-storage.appdomain.cloud"
COS_API_KEY_ID = "cC326fk6u3sRdRsIGE_gyleGM24gynn__WeDyMoqQ52M"
COS_INSTANCE_CRN = "crn:v1:bluemix:public:cloud-object-storage:global:a/e4dcac9c25e9473485989a3a05ee4ec1:04e94adb-84d3-42d2-ad14-3e0ca6eb4af5::"

@app.route('/upload', methods=['POST'])
def upload_file():
    bucket_name = "elek-donotdelete-pr-tpbfrekjccp3nj"
    file_name = "output222.txt"
    text_data = "Ez egy teszt szöveg."

    cos = ibm_boto3.client('s3',
                           ibm_api_key_id=COS_API_KEY_ID,
                           ibm_service_instance_id=COS_INSTANCE_CRN,
                           config=Config(signature_version='oauth'),
                           endpoint_url=COS_ENDPOINT)

    try:
        # Fájl feltöltése a bucketbe
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
    app.run(host='0.0.0.0', port=8080)
