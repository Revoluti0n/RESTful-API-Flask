from flask import Flask, jsonify, request
import json

app = Flask(__name__)

devs = [
    {
        'id': 1,
        'name': 'Kelvyn Xavier',
        'lang': 'Python'
    },
    {
        'id': 2,
        'name': 'Fulano',
        'lang': 'C'
    },
    {
        'id': 3,
        'name': 'Ciclano',
        'lang': 'C++'
    }
]


@app.route('/devs', methods=['GET'])
def index() -> json:
    # Serializa
    return jsonify(devs), 200


@app.route('/devs/<string:lang>', methods=['GET'])
def devs_per_language(lang: str) -> json:
    devs_per_lang = [dev for dev in devs if dev['lang'] == lang.capitalize()]
    # Serializa
    return jsonify(devs_per_lang), 200


@app.route('/devs/<int:id>', methods=['PUT'])
def change_lang(id: int) -> json:
    """
    Alterar a linguagem de programação.
    """

    for dev in devs:
        if dev['id'] == id:
            dev['lang'] = request.get_json().get('lang')
            # Serializa
            return jsonify(dev), 200

    # Serializa
    return jsonify({'Error': 'Not Found'}), 404


@app.route('/devs/<int:id>', methods=['GET'])
def devs_per_id(id: int) -> json:
    """
    Mostra o desenvolvedor com um determinado id.
    """
    for dev in devs:
        if dev['id'] == id:
            # Serializa
            return jsonify(dev), 200

    # Serializa
    return jsonify({'Error': 'Not Found'}), 404


@app.route('/devs/<int:id>', methods=['DELETE'])
def remove_dev(id: int) -> json:
    """
    Remove um desenvolvedor.
    """

    for dev in devs:
        if dev['id'] == id:
            ind = id - 1
            del devs[ind]
            # Serializa
            return jsonify({'message': 'Removido com sucesso'}), 200
    # Serializa
    return jsonify({'message': 'ID não encontrado'}), 404


@app.route('/devs', methods=['POST'])
def save_dev() -> json:
    """
    Insere um desenvolvedor.
    """

    data = request.get_json()
    devs.append(data)
    # Serializa
    return jsonify(data), 201


if __name__ == '__main__':
    app.run(debug=True)
