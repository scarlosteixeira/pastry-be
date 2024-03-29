from app import app, db
from models.user import UserModel
from models.role import RoleModel
from models.product import ProductModel
from models.image import ImageModel
from models.address import AddressModel
from models.cart import CartModel
from models.cart_item import CartItemModel
from models.order import OrderModel


roles = ["Admin", "Owner", "Employee", "Customer"]

with app.app_context():

    try:
        print("Creating our database...")

        db.session.commit()
        db.drop_all()
        db.create_all()

        print("Seeding the database!")
        for role in roles:
            rolename = RoleModel(role_name=role)
            rolename.save()
            
        user = UserModel(
            email="admin@pastry.com",
            username="admin",
            password="1q2w3e4r5t6Y.",
            name="Carlos",
            surname="Teixeira",
            phone="07767668991",
            role_id=1,
        )
        user.save()
        
        user_owner = UserModel(
            email="owner@pastry.com",
            username="owner",
            password="1q2w3e4r5t6Y.",
            name="Carlos",
            surname="Teixeira",
            phone="07767668992",
            role_id=2,
        )
        user_owner.save()

        user_employee = UserModel(
            email="employee@pastry.com",
            username="employee",
            password="1q2w3e4r5t6Y.",
            name="Carlos",
            surname="Teixeira",
            phone="07767668993",
            role_id=3,
        )
        user_employee.save()
        
        user_customer = UserModel(
            email="customer@pastry.com",
            username="customer",
            password="1q2w3e4r5t6Y.",
            name="Carlos",
            surname="Teixeira",
            phone="07767668999",
        )
        user_customer.save()

        address = AddressModel(
            country = "Monaco",
            fullname = user_customer.name + " " +user_customer.surname,
            phone = user_customer.phone,
            postcode = "DT7 6LJ",
            address_line_1 = "88745 Evangeline Falls",
            address_line_2 = "Suite 496",
            town_city = "Irvingville",
            county = "West Sussex",
            delivery_instr = "Leave at door.",
            is_default = True,
            is_billing_address = True,
            user_id = user_customer.id
        )
        address.save()

        product = ProductModel(
            name="Banana Cake",
            description="Cake made of banana.",
            price=15.5,
            in_stock=True,
            created_by=user.id,
        )
        product.save()

        image = ImageModel(image_url="https://source.unsplash.com/500x500/?food-drink,Cake", product_id=product.id)
        image.save()

        product_2 = ProductModel(
            name = "Product 2",
            description= "The beautiful range of Apple Naturalé that has an exciting mix of natural ingredients. With the Goodness of 100% Natural Ingredients",
            price = 366.00,
            in_stock = True,
            created_by = user.id,
        )
        product_2.save()

        image_2 = ImageModel( image_url = "https://source.unsplash.com/500x500/?food-drink,Cake", product_id=product_2.id)
        image_2.save()

        # cart = CartModel(user_id = user_customer.id)
        # cart.save()

        # cart_item = CartItemModel(product_id= product.id, cart_id = cart.id)
        # cart_item.save()

        # cart_item_2 = CartItemModel(product_id= product_2.id, cart_id = cart.id, quantity = 3)
        # cart_item_2.save()

        # order = OrderModel(cart_id=cart.id, user_id= user_customer.id, total = (cart_item.quantity*product.price)+(cart_item_2.quantity*product_2.price) )
        # order.save()
        print("Database seeded!")
    except Exception as e:
        print("exception", e)
