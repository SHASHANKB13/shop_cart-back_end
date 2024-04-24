import json
from flask import Flask, request, Response, jsonify, send_file, make_response
import DAO.databaseHandler as dbh
import util.configFile as conf
import Controllers.constants as constants
from flask_cors import CORS
import logging

app = Flask(__name__)
CORS(app)

config = conf.init()

app.config['SECRET_KEY'] = constants.SECRET_KEY


@app.route('/api/shopping/product/list', methods=['POST'])
def product_listing():
    try:
        req_data = request.get_json()
        category = req_data['category']
        pageNumber = req_data['pageNumber']
        pageSize = req_data['pageSize']
        pageNumber = pageNumber * 10

        fetched_products = dbh.fetch_product_listing(category)
        fetched_product_list = [
            {
                "id": item[0],
                "name": item[1],
                "price": float(item[2]),
                "category": item[3],
                "imageUrl": item[4],
                "created_date": item[5].isoformat(),
                "updated_date": item[6].isoformat()
            }
            for item in fetched_products
        ]

        message = {
            'status': 'success',
            'status_code': '200',
            'message': 'Fetched all products',
            'data': fetched_product_list
        }
        return Response(json.dumps(message), status=200, mimetype='application/json')

    except Exception as e:
        logging.error("The Error is: %s", e)
        error_message = {
            "status_code": "500",
            "error_code": "E500",
            "error_message": "Internal Server Error",
            "data": str(e)
        }
        return Response(json.dumps(error_message), status=500, mimetype='application/json')


@app.route('/api/shopping/product/details/<product_id>', methods=['GET'])
def get_product_details(product_id):
    try:
        fetched_product_details = dbh.fetch_product_with_id(product_id=product_id)
        fetched_product_list = [
            {
                "id": item[0],
                "name": item[1],
                "price": float(item[2]),
                "category": item[3],
                "imageUrl": item[4],
                "created_date": item[5].isoformat(),
                "updated_date": item[6].isoformat(),
                "description": item[7],
                # "rating": float(item[8])
                "rating": float(item[8]) if item[8] is not None else None

            }
            for item in fetched_product_details
        ]

        message = {
            'status': 'success',
            'status_code': '200',
            'message': 'Fetched product details successfully.',
            'data': fetched_product_list
        }
        return Response(json.dumps(message), status=200, mimetype='application/json')

    except Exception as e:
        logging.error("The Error is: %s", e)
        error_message = {
            "status_code": "500",
            "error_code": "E500",
            "error_message": "Internal Server Error",
            "data": str(e)
        }
        return Response(json.dumps(error_message), status=500, mimetype='application/json')


@app.route('/api/shopping/user/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    check_user = dbh.check_user_exist(username=username)

    if not check_user:
        return jsonify({'message': 'user not found. please try with valid username',
                        'error': 'Bad request'}), 400
    # Check username and password, and if they are correct, generate a token
    else:
        if valid_login(username, password):
            # dbh.store_token_employee(username, token)
            user_details = dbh.fetch_user(username=username)
            user_id = user_details[0][0]
            first_name = user_details[0][1]
            last_name = user_details[0][2]
            user_name = user_details[0][3]
            user_phone = user_details[0][5]
            user_email = user_details[0][6]
            address = user_details[0][7]
            cart_count = dbh.get_product_count_with_userID(user_id=user_id)

            return jsonify({'message': 'Login successful',
                            # 'token': token,
                            'id': user_id,
                            'first_name': first_name,
                            'last_name': last_name,
                            'username': user_name,
                            'email': user_email,
                            'phone': user_phone,
                            'address': address,
                            'cart_count': cart_count
                            }), 200

        return jsonify({'message': 'Invalid credentials'}), 401


def valid_login(username, password):
    fetched_user = dbh.fetch_user(username=username)
    if fetched_user:
        if username == fetched_user[0][3] and password == fetched_user[0][4]:
            return True
        else:
            return False


@app.route('/api/shopping/cart/add', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    user_id = data.get('user_id')
    product_id = data.get('product_id')
    quantity = data.get('quantity')

    add_products = dbh.add_product_to_cart(user_id=user_id, product_id=product_id, quantity=quantity)

    if not add_products:
        return jsonify({'message': 'Failed to add product to cart. please try with valid user_id or product_id',
                        'error': 'Bad request'}), 400
    else:
        return jsonify({'message': 'Product added to cart successfully.',
                        'user': user_id,
                        'product': product_id,
                        'quantity': quantity
                        }), 200


@app.route('/api/shopping/cart/details/<user_id>', methods=['GET'])
def get_cart_products(user_id):
    try:
        fetched_cart_details = dbh.fetch_cart_products_with_userID(user_id=user_id)
        fetched_cart_products_list = []
        total_price = 0
        for item in fetched_cart_details:
            products_list = dbh.fetch_product_with_id(product_id=item[2])
            fetched_cart_products_list.extend([
                {
                    "id": products[0],
                    "name": products[1],
                    "price": float(products[2]),
                    "imageUrl": products[4],
                    "quantity": item[3],
                    "rating": float(products[8]) if products[8] is not None else None
                }
                for products in products_list
            ])
            # total_price += sum(
            #     float(product['price']) * int(product['quantity']) for product in fetched_cart_products_list)

        for product in fetched_cart_products_list:
            total_price += float(product['price']) * int(product['quantity'])

        message = {
            'status': 'success',
            'status_code': '200',
            'message': f'Fetched cart product details successfully for user:{user_id}.',
            'total_price': total_price,
            'data': fetched_cart_products_list
        }
        return Response(json.dumps(message), status=200, mimetype='application/json')

    except Exception as e:
        logging.error("The Error is: %s", e)
        error_message = {
            "status_code": "500",
            "error_code": "E500",
            "error_message": "Internal Server Error",
            "data": str(e)
        }
        return Response(json.dumps(error_message), status=500, mimetype='application/json')


@app.route('/api/shopping/cart/product/delete', methods=['POST'])
def delete_cart_products():
    data = request.get_json()
    user_id = data.get('user_id')
    product_id = data.get('product_id')

    try:
        new_quantity = dbh.delete_product(user_id=user_id, product_id=product_id)
        if new_quantity > 0:
            message = {
                'status': 'success',
                'status_code': '200',
                'message': f'Deleted product in cart successfully.',
                'new_quantity': new_quantity
            }
            return Response(json.dumps(message), status=200, mimetype='application/json')
        else:
            dbh.delete_product_row_from_db(user_id=user_id, product_id=product_id)
            message = {
                'status': 'success',
                'status_code': '200',
                'message': f'Deleted product in cart successfully.'
            }
            return Response(json.dumps(message), status=200, mimetype='application/json')

    except Exception as e:
        logging.error("The Error is: %s", e)
        error_message = {
            "status_code": "500",
            "error_code": "E500",
            "error_message": "Internal Server Error",
            "data": str(e)
        }
        return Response(json.dumps(error_message), status=500, mimetype='application/json')


@app.route('/api/shopping/user/update', methods=['POST'])
def user_address_update():
    data = request.get_json()
    user_id = data.get('user_id')
    phone = data.get('phone')
    email = data.get('email')
    address = data.get('address')
    try:
        dbh.update_user_address(user_id, phone, email, address)
        message = {
            'status': 'success',
            'status_code': '200',
            'message': 'user address updated successfully.',
            'data': {
                'phone_number': phone,
                'email': email,
                'address': address
            }
        }
        return Response(json.dumps(message), status=200, mimetype='application/json')
    except Exception as e:
        logging.error("The Error is: %s", e)
        error_message = {
            "status_code": "500",
            "error_code": "E500",
            "error_message": "Internal Server Error",
            "data": str(e)
        }
        return Response(json.dumps(error_message), status=500, mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=config.get('SERVER', 'debug'), port=config.get('SERVER', 'port'),
            host=config.get('SERVER', 'host'))
    # app.run(debug=True, port=3000, host='127.0.0.1')
