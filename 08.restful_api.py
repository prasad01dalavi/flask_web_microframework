from flask import Flask, jsonify, request

app = Flask(__name__)

languages = [{"name": "javascript"}, {"name": "python"}, {"name": "ruby"}]
# Creating a list of dict

@app.route('/', methods=['GET'])  # http://127.0.0.1:8080
def test():
    return jsonify({'message': 'it works!'})


@app.route('/lang', methods=['GET'])   # http://127.0.0.1:8080/lang
def my_api_view():
    return jsonify({'my_key': languages})

if __name__ == '__main__': 
    app.run(debug=True, port=8080)  
    # specify the server port otherwise by default it is 5000
