import mysql.connector
import mysql
import logging
import Controllers.constants as constants
import json


def db_engine():
    try:
        mydb = mysql.connector.connect(host=constants.DB_HOST, user=constants.DB_USER,
                                       password=constants.DB_PASSWORD,
                                       port=constants.DB_PORT,
                                       database=constants.DB_NAME)
        return mydb
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        logging.error(f"Error Database connection : {str(e)}")
        return None


def fetch_product_listing(category):
    query = f"SELECT * FROM product WHERE category = '{category}';"
    try:
        cnx = db_engine()
        cursor = cnx.cursor()
        cursor.execute(query)
        jobs_data = cursor.fetchall()
        cursor.close()
        cnx.close()
        # print(jobs_data)
        return jobs_data

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        logging.error(f"Error occurred in fetch_product_listing: {str(e)}")
        return []


def fetch_product_with_id(product_id):
    query = f"SELECT * FROM product WHERE id = '{product_id}';"
    try:
        cnx = db_engine()
        cursor = cnx.cursor()
        cursor.execute(query)
        jobs_data = cursor.fetchall()
        cursor.close()
        cnx.close()
        # print(jobs_data)
        return jobs_data

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        logging.error(f"Error occurred in fetch_product_listing: {str(e)}")
        return []


def fetch_user(username):
    fquery = f"SELECT * FROM users WHERE username = '{username}';"
    with db_engine() as cnx:
        cursor = cnx.cursor()
        cursor.execute(fquery)
        fetched_user_details = cursor.fetchall()
        cnx.commit()
        cursor.close()
        # print(fetched_user_details)
        if fetched_user_details:
            return fetched_user_details
        else:
            return None


def check_user_exist(username):
    query = "SELECT COUNT(*) FROM users WHERE username = %s"

    try:
        with db_engine() as cnx:
            cursor = cnx.cursor()
            cursor.execute(query, (username,))
            result = cursor.fetchone()
            cnx.close()

            # If the count is greater than 0, the username exists
            if result[0] > 0:
                return True
            else:
                return False

    except Exception as e:
        # Handle any database connection or query errors
        print("Error:", str(e))
        return False


def add_product_to_cart(user_id, product_id, quantity):
    try:
        cnx = db_engine()
        cursor = cnx.cursor()

        # Check if the combination of user_id and product_id already exists
        cursor.execute("SELECT * FROM CartDetails WHERE user_id = %s AND product_id = %s", (user_id, product_id))
        existing_row = cursor.fetchone()

        if existing_row:
            # If the combination exists, update the quantity
            new_quantity = existing_row[3] + quantity  # Assuming quantity is in the third column
            cursor.execute("UPDATE CartDetails SET quantity = %s WHERE user_id = %s AND product_id = %s",
                           (new_quantity, user_id, product_id))
            print("Quantity updated for existing product in the cart.")
        else:
            # If the combination does not exist, insert a new row
            cursor.execute("INSERT INTO CartDetails (user_id, product_id, quantity) VALUES (%s, %s, %s)",
                           (user_id, product_id, quantity))
            print("Product added to cart.")

        cnx.commit()  # Committing changes to the database
        cursor.close()
        cnx.close()
        return True

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        logging.error(f"Error occurred in add_product_to_cart: {str(e)}")
        return False


def fetch_cart_products_with_userID(user_id):
    query = f"SELECT * FROM CartDetails WHERE user_id = '{user_id}';"
    try:
        cnx = db_engine()
        cursor = cnx.cursor()
        cursor.execute(query)
        jobs_data = cursor.fetchall()
        cursor.close()
        cnx.close()
        # print(jobs_data)
        return jobs_data

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        logging.error(f"Error occurred in fetch_cart_products_with_userID: {str(e)}")
        return []


def get_product_quantity(user_id, product_id):
    query = f"SELECT quantity FROM CartDetails WHERE user_id = '{user_id}' AND product_id ={product_id};"
    try:
        cnx = db_engine()
        cursor = cnx.cursor()
        cursor.execute(query)
        jobs_data = cursor.fetchall()
        cursor.close()
        cnx.close()
        # print(jobs_data[0][0])
        return jobs_data[0][0]

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        logging.error(f"Error occurred in get_product_quantity: {str(e)}")
        return []


def delete_product(user_id, product_id):
    current_quantity = get_product_quantity(user_id, product_id)
    if current_quantity > 0:
        new_quantity = current_quantity - 1
    else:
        new_quantity = 0
    query = f"UPDATE CartDetails SET quantity = {new_quantity} WHERE user_id = {user_id} AND product_id = {product_id};"
    try:
        cnx = db_engine()
        cursor = cnx.cursor()
        cursor.execute(query)
        cnx.commit()
        cursor.close()
        cnx.close()
        # print(new_quantity)
        return new_quantity

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        logging.error(f"Error occurred in delete_product: {str(e)}")
        return []


def delete_product_row_from_db(user_id, product_id):
    query = f"DELETE FROM CartDetails WHERE user_id = {user_id} AND product_id = {product_id};"
    try:
        cnx = db_engine()  # Assuming db_engine() returns a database connection
        cursor = cnx.cursor()
        cursor.execute(query)
        cnx.commit()
        cursor.close()
        cnx.close()
        return True
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        logging.error(f"Error occurred in delete_product_row_from_db: {str(e)}")
        return False


def get_product_count_with_userID(user_id):
    query = f"SELECT quantity FROM CartDetails WHERE user_id = {user_id};"
    try:
        cnx = db_engine()  # Assuming db_engine() returns a database connection
        cursor = cnx.cursor()
        cursor.execute(query)
        quantities = cursor.fetchall()
        total_quantity = sum(qty[0] for qty in quantities)
        cnx.commit()
        cursor.close()
        cnx.close()
        # print(total_quantity)
        return total_quantity
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        logging.error(f"Error occurred in get_product_count_with_userID: {str(e)}")
        return 0  # Return 0 in case of an error or no quantities found


def update_user_address(user_id, phone, email, address):
    query = f"UPDATE users SET phone = '{phone}', email = '{email}', address = '{address}' WHERE id = {user_id};"
    try:
        cnx = db_engine()
        cursor = cnx.cursor()
        cursor.execute(query)
        cnx.commit()
        cursor.close()
        cnx.close()
        return True
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        logging.error(f"Error occurred in update_user_address: {str(e)}")
        return False

