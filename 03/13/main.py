from models.all_models import Customer, Product, Reseller, User

# class

if __name__ == "__main__":
    # Create customer
    c1 = Customer('new', '123', 'new simple', 'simple1@gmail.com')
    c2 = Customer('now', '456', 'now simple', 'simple2@gmail.com')
    # c3 = Customer('jack', '987', 'jack simple', 'simple3@gmail.com')

    c1.set_enable()
    # print(c1.__wallet_amount)
    print(c1.wallet)  # True
    # print('Check password: ', c1.check_password('123'))
    print(c1.username)

    # Create Product
    p1 = Product(1, 'Product #1')
    p2 = Product(1, 'Product #2', 1000)
    p3 = Product(1, 'Product #3', 1000, 'Some description about product')

    # Product.is_free()  > Error
    # Product.upc        > Error
    # print(p1.upc, p1.is_free())
    # print(p2.upc, p2.is_free())
    # print(p3.upc, p3.is_free())
    # Product.product_list.append()   # Class attrs
    # print(Product.product_list)
    for pr in Product.product_list:
        print(pr)

    c3 = Customer(
        email='reza@mail', fullname='Nima',
        password='789', username='nima'
    )

    r1 = Reseller(
        'Brand #1', 'log/path', 'reseller', '246',
        'Reseller', 'reseller@gmail.com'
    )

    print(r1.username, c3.username)
    print(type(r1), type(c3))

    print(r1.check_password('246'), c3.check_password('789'))

    # Inheritance vs Composition

    # Reseller composition
    p2 = Product(2, 'Product #2', 1000, reseller=r1)
    # print(type(p2), type(p2.reseller))
    # print(p2.name, p2.reseller.check_password('123'))

    u2 = User.create('reseller2', '247', 'Reseller', 'reseller2@gmail.com')
    User.validate_password('123')
    if u2:
        print(u2)