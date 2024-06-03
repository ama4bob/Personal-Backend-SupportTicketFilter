from flask import Flask, request, jsonify
from utils.FilterUtil import FilterUtil
from utils.ValidateUtil import ValidateUtil

app = Flask(__name__)

# Quick test if the POST method is connecting
@app.route("/POSTconnection", methods=['POST'])
def connectionTestPOST():
    return jsonify({"response" : "Post Request Called"})

# Quick test if the server is recieving the right JSON
@app.route("/POSTjson", methods=['POST'])
def jsonReturnTestPOST():
    return request.json
    
# Validate and filter the ticket and its contents from the single json array
@app.route("/POSTrun", methods=["POST"])
def filterPOST():
    content = request.json
    # TODO: This could be optimized for faster speed and memory
    for parsedContent in content[:]:
        if ValidateUtil.validateTicket(object, parsedContent):
            content.remove(parsedContent)
        else:
            if "msg" in parsedContent:
                parsedContent["msg"] = FilterUtil.filterDescription(object, parsedContent["msg"])

    return content

if __name__ == "__main__":
    app.run(debug=True, port=8080, host="127.0.0.1")