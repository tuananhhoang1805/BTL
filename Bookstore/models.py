from sqlalchemy import Column, Integer, String, Float, Boolean, Enum, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from Bookstore import db
from datetime import datetime
from enum import Enum as UserEnum
from flask_login import UserMixin


class BaseModel(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)


class UserRole(UserEnum):
    ADMIN = 1
    USER = 2


class User(BaseModel, UserMixin):
    name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    active = Column(Boolean, default=True)
    email = Column(String(100))
    joined_date = Column(DateTime, default=datetime.now())
    avatar = Column(String(100), default='images/avatar.jpg')
    user_role = Column(Enum(UserRole), default=UserRole.USER)
    receipts = relationship('Receipt', backref='user', lazy=True)

    def __str__(self):
        return self.name


class Category(BaseModel):
    __tableName__ = 'category'

    name = Column(String(50), nullable=False)
    products = relationship('Product',
                            backref='category', lazy=True)


class Author(BaseModel):
    __tableName__ = 'author'

    name = Column(String(50), nullable=False)
    book = relationship('Product',
                        backref='author', lazy=True)


class Product(BaseModel):
    __tableName__ = 'product'

    name = Column(String(50), nullable=False)
    description = Column(String(255))
    price = Column(Float, default=0)
    image = Column(String(100))
    active = Column(Boolean, default=True)
    created_date = Column(DateTime, default=datetime.now())
    quantity = Column(Integer, nullable=False)
    category_id = Column(Integer, ForeignKey(Category.id),
                         nullable=False)
    receipt_details = relationship('ReceiptDetail', backref='product', lazy=True)
    author_id = Column(Integer, ForeignKey(Author.id), nullable=True)

    def __str__(self):
        return self.name


class Receipt(BaseModel):
    created_date = Column(DateTime, default=datetime.now())
    customer_id = Column(Integer, ForeignKey(User.id), nullable=False)
    details = relationship('ReceiptDetail',
                           backref='receipt', lazy=True)


class ReceiptDetail(db.Model):
    receipt_id = Column(Integer, ForeignKey(Receipt.id), nullable=False, primary_key=True)
    product_id = Column(Integer, ForeignKey(Product.id), nullable=False, primary_key=True)
    quantity = Column(Integer, default=0)
    price = Column(Float, default=0)


if __name__ == '__main__':
    db.create_all()
    # categories = [{
    #     "id": 1,
    #     "name": "Sách Kinh Tế - Kĩ Năng"
    # }, {
    #     "id": 2,
    #     "name": "Sách Văn Học Việt Nam"
    # }, {
    #     "id": 3,
    #     "name": "Sách Văn Học Nước Ngoài"
    # }, {
    #     "id": 4,
    #     "name": "Sách Thiếu Nhi"
    # }, {
    #     "id": 5,
    #     "name": "Sách Giáo Dục Gia Đình"
    # }, {
    #     "id": 6,
    #     "name": "Sách Lịch Sử"
    # }, {
    #     "id": 7,
    #     "name": "Sách Văn Hóa Nghệ Thuật"
    # }, {
    #     "id": 8,
    #     "name": "Sách Khoa Học - Triết Học"
    # }, {
    #     "id": 9,
    #     "name": "Sách Tâm Linh Tôn Giáo"
    # }, {
    #     "id": 10,
    #     "name": "Sách Y học- Thực Dưỡng"
    # }]
    #
    # for c in categories:
    #     cate = Category(id=c['id'], name=c['name'])
    #     db.session.add(cate)
    #
    # db.session.commit()
    #
    # authors = [{
    #     "id": 1,
    #     "name": "Max"
    # }, {
    #     "id": 2,
    #     "name": "John"
    # }, {
    #     "id": 3,
    #     "name": "Kid"
    # }]
    #
    # for a in authors:
    #     author = Author(id=a['id'], name=a['name'])
    #     db.session.add(author)
    #
    # db.session.commit()
    #
    # products = [{
    #     "id": 1,
    #     "name": "Lập Kế Hoạch Kinh Doanh Hiệu Quả",
    #     "description": "Lập Kế Hoạch Kinh Doanh Hiệu Quả",
    #     "price": 120000,
    #     "image": "images/lap-ke-hoach-kinh-doanh-hieu-qua.jpg",
    #     "created_date": "2015-12-12",
    #     "quantity": 200,
    #     "category_id": 1,
    #     "author_id": 1
    # }, {
    #     "id": 2,
    #     "name": "Ma Bùn Lưu Manh",
    #     "description": "Ma Bùn Lưu Manh",
    #     "price": 150000,
    #     "image": "images/ma-bun-luu-manh.jpg",
    #     "created_date": "2015-12-12",
    #     "quantity": 600,
    #     "category_id": 2,
    #     "author_id": 2
    # }, {
    #     "id": 3,
    #     "name": "Giao dịch mọi nơi , không chỉ là ngân hàng",
    #     "description": "Giao Dịnh mọi nơi , không chỉ là ngân hàng",
    #     "price": 100000,
    #     "image": "images/bank-4.0.jpg",
    #     "created_date": "2015-12-12",
    #     "quantity": 300,
    #     "category_id": 3,
    #     "author_id": 3
    # }]
    #
    # for p in products:
    #     pro = Product(name=p['name'], price=p['price'], image=p['image'], quantity=p['quantity'],
    #                   created_date=p['created_date'],
    #                   description=p['description'], category_id=p['category_id'], author_id=p['author_id'])
    #     db.session.add(pro)
    #
    # db.session.commit()
