from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app import db, app


class Category(db.Model):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    products = relationship('Product', backref='category',lazy=True)

class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    price = Column(Float, default=0)
    image = Column(String(100))
    category_id = Column(Integer, ForeignKey(Category.id),nullable=False)


if __name__ == '__main__':
    with app.app_context():
        # c1 = Category(name='Mobile')
        # c2 = Category(name='Tablet')
        #
        # db.session.add(c1)
        # db.session.add(c2)
        # db.session.commit()

        p1 = Product(name='Xiaomi', price=2000007, category_id=1,
             image='https://cdn-v2.didongviet.vn/files/products/2023/3/22/1/1682146244776_iphone_13_xanh_didongviet.jpg'        )
        p2 = Product(name='Redmi', price=2000707, category_id=1,
                     image='https://cdn-v2.didongviet.vn/files/products/2023/3/22/1/1682146244776_iphone_13_xanh_didongviet.jpg')
        p3 = Product(name='Ipad pro', price=2000407, category_id=2,
                     image='https://cdn-v2.didongviet.vn/files/products/2023/3/22/1/1682146244776_iphone_13_xanh_didongviet.jpg')
        p4 = Product(name='Xiaomi Note7', price=3000007, category_id=1,
                     image='https://cdn-v2.didongviet.vn/files/products/2023/3/22/1/1682146244776_iphone_13_xanh_didongviet.jpg')
        p5 = Product(name='Galaxy Tab', price=2050007, category_id=2,
                     image='https://cdn-v2.didongviet.vn/files/products/2023/3/22/1/1682146244776_iphone_13_xanh_didongviet.jpg')

        db.session.add_all([p1,p2,p3,p4, p5])
        db.session.commit()

        # db.create_all()
