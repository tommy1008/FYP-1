from flask.ext.appbuilder import Model
from flask.ext.appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn
from sqlalchemy import Table, Column, Integer, String, ForeignKey, Date, Float, Text, DateTime
from sqlalchemy.orm import relationship
from flask_appbuilder.models.decorators import renders
from flask_appbuilder.models.sqla.filters import FilterStartsWith, FilterEqualFunction
import datetime


class Feedback(Model):
    __tablename__ = 'feedback'
    id = Column(Integer, primary_key=True)
    email = Column(String(50))
    name = Column(String(50))
    company = Column(Text(50))
    content = Column(Text(1000))

    def __repr__(self):
        return self.email


class Exchange(Model):
    __tablename__ = 'exchange'
    id = Column(Integer, primary_key=True)
    price = Column(Float)
    currency = Column(Float)
    payment = Column(String(20))

    def __repr__(self):
        return self.price


class FAQ(Model):
    __tablename__ = 'faq'
    id = Column(Integer, primary_key=True)
    title = Column(Text(50))
    content = Column(Text(200))

    def __repr__(self):
        return self.title


class MyUser(Model):
    __tablename__ = 'myuser'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    birth = Column(Date)
    email = Column(String(100), nullable=False, unique=True)
    phone = Column(String(20))
    nation = Column(String(20))

    def __repr__(self):
        return self.username


class Place(Model):
    __tablename__ = 'place'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    country_id = Column(Integer, ForeignKey('country.id'))
    country = relationship("Country")

    def __repr__(self):
        return self.name


class Continent(Model):
    __tablename__ = 'continent'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

    def __repr__(self):
        return self.name


class Country(Model):
    __tablename__ = 'country'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    continent_id = Column(Integer, ForeignKey('continent.id'))
    continent = relationship('Continent')

    def __repr__(self):
        return self.name


class Activities(Model):
    __tablename__ = 'activities'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    countent = Column(Text(200), nullable=False)
    price = Column(Float, nullable=False)
    place_id = Column(Integer, ForeignKey('place.id'))
    place = relationship("Place")

    def __repr__(self):
        return self.title


class Review(Model):
    __tablename__ = 'review'
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    content = Column(Text(200))
    rating_id = Column(Integer, ForeignKey('rating.id'))
    rating = relationship("Rating")
    user_id = Column(Integer, ForeignKey('myuser.id'))
    user = relationship("MyUser")
    activities_id = Column(Integer, ForeignKey('activities.id'))
    activities = relationship('Activities')
    def __repr__(self):
        return self.title


class Rating(Model):
    __tablename__ = 'rating'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))

    def __repr__(self):
        return self.name


class Contact(Model):
    __tablename__ = 'contact'
    id = Column(Integer, primary_key=True)
    title = Column(Text(100))
    content = Column(Text(300))
    user_id = Column(Integer, ForeignKey('myuser.id'))
    user = relationship("MyUser")

    def __repr__(self):
        return self.title


class Hotel(Model):
    __tablename__ = 'hotel'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    countent = Column(Text(200))
    place_id = Column(Integer, ForeignKey('place.id'))
    place = relationship("Place")

    def __repr__(self):
        return self.name


class Flight(Model):
    __tablename__ = 'flight'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    time = Column(DateTime)
    company_id = Column(Integer, ForeignKey('company.id'))
    company = relationship('Company')
    place_id = Column(Integer, ForeignKey('place.id'))
    place = relationship("Place")
    def __repr__(self):
        return self.name


class Company(Model):
    __tablename__ = 'company'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    place_id = Column(Integer, ForeignKey('place.id'))
    place = relationship("Place")

    def __repr__(self):
        return self.name


class Invoice(Model):
    __tablename__ = 'invoice'
    id = Column(Integer, primary_key=True)
    price = Column(Integer)
    quantity = Column(Integer)
    payment = Column(String(20))
    user_id = Column(Integer, ForeignKey('myuser.id'))
    user = relationship("MyUser")

    def __repr__(self):
        return self.price


class Ticket(Model):
    __tablename__ = 'ticket'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    quantity = Column(Integer)
    type = Column(String(20))
    price = Column(Float)
    place_id = Column(Integer, ForeignKey('place.id'))
    place = relationship("Place")

    def __repr__(self):
        return self.name


class Discount(Model):
    __tablename__ = 'discount'
    id = Column(Integer, primary_key=True)
    percentage = Column(Float)
    hotel_id = Column(Integer, ForeignKey('hotel.id'))
    hotel = relationship("Hotel")
    flight_id = Column(Integer, ForeignKey('flight.id'))
    flight = relationship("Flight")

    def __repr__(self):
        return self.percentage


class Weather(Model):
    __tablename__ = 'weather'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    time = Column(DateTime)
    place_id = Column(Integer, ForeignKey('place.id'))
    place = relationship("Place")

    def __repr__(self):
        return self.name


class Culture(Model):
    __tablename__ = 'culture'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    content = Column(String(200))
    place_id = Column(Integer, ForeignKey('place.id'))
    place = relationship("Place")

    def __repr__(self):
        return self.name


class Booking(Model):
    __tablename__ = 'booking'
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer)
    check_in_date = Column(Date)
    check_out_date = Column(Date)

    hotel_id = Column(Integer, ForeignKey('hotel.id'))
    hotel = relationship("Hotel")

    invoice_id = Column(Integer, ForeignKey('invoice.id'))
    invoice = relationship("Invoice")

    place_id = Column(Integer, ForeignKey('place.id'))
    place = relationship("Place")

    user_id = Column(Integer, ForeignKey('myuser.id'))
    user = relationship("MyUser")


class FlightTicket(Model):
    __tablename__ = 'flight_ticket'
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer)
    check_in_date = Column(Date)
    check_out_date = Column(Date)

    flight_id = Column(Integer, ForeignKey('flight.id'))
    flight = relationship("Flight")

    invoice_id = Column(Integer, ForeignKey('invoice.id'))
    invoice = relationship("Invoice")

    place_id = Column(Integer, ForeignKey('place.id'))
    place = relationship("Place")

    user_id = Column(Integer, ForeignKey('myuser.id'))
    user = relationship("MyUser")



class CateGory(Model):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    group_title = Column(String(20))
    forum_place_id = Column(Integer, ForeignKey('forum_place.id'))
    forum_place = relationship('ForumPlace')

    def __repr__(self):
        return self.group_title


class ForumPlace(Model):
    __tablename__ = 'forum_place'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))

    def __repr__(self):
        return self.name


class Post(Model):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    title = Column(String(20))
    post_date = Column(DateTime)
    user_id = Column(Integer, ForeignKey('myuser.id'))
    user = relationship("MyUser")
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship("CateGory")

    def __repr__(self):
        return self.title


class Comment(Model):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    title = Column(String(20))
    content = Column(String(100))
    user_id = Column(Integer, ForeignKey('myuser.id'))
    user = relationship("MyUser")
    post_id = Column(Integer, ForeignKey("post.id"))
    post = relationship("Post")

    def __repr__(self):
        return self.title


class New(Model):
    __tablename__ = 'new'
    id = Column(Integer, primary_key=True)
    title = Column(String(20))
    content = Column(String(100))
    date = Column(Date)
    place_id = Column(Integer, ForeignKey('place.id'))
    place = relationship("Place")

    def __repr__(self):
        return self.title


class ShopHistory(Model):
    __tablename__ = 'shop_history'
    id = Column(Integer, primary_key=True)
    data = Column(Date)
    invoice_id = Column(Integer, ForeignKey('invoice.id'))
    invoice = relationship("Invoice")
    user_id = Column(Integer, ForeignKey('myuser.id'))
    user = relationship("MyUser")

    def __repr__(self):
        return self.invoice


class LoginHistory(Model):
    __tablename__ = 'login_history'
    id = Column(Integer, primary_key=True)
    data = Column(DateTime)
    user_id = Column(Integer, ForeignKey('myuser.id'))
    user = relationship("MyUser")

    def __repr__(self):
        return self.data


class Themes(Model):
    __tablename__ = 'themes'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    content = Column(Text)
    place_id = Column(Integer, ForeignKey('place.id'))
    place = relationship("Place")

    def __repr__(self):
        return self.name


class Blog(Model):
    __tablename__ = 'blog'
    id = Column(Integer, primary_key=True)
    title = Column(Text)
    data = Column(Date)
    views = Column(Integer)
    content = Column(Text)
    user_id = Column(Integer, ForeignKey('myuser.id'))
    user = relationship("MyUser")
    blog_category_id = Column(Integer, ForeignKey('blog_category.id'))
    blog_category = relationship("BlogCategory")

    def __repr__(self):
        return self.title


class BlogCategory(Model):
    __tablename__ = 'blog_category'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))

    def __repr__(self):
        return self.name


class Plan(Model):
    __tablename__ = 'plan'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    content = Column(Text)
    activities_id = Column(Integer, ForeignKey('activities.id'))
    activities = relationship('Activities')
    themes_id = Column(Integer, ForeignKey('themes.id'))
    themes = relationship('Themes')
    place_id = Column(Integer, ForeignKey('place.id'))
    place = relationship("Place")

    def __repr__(self):
        return self.name


class Department(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class Function(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class Benefit(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name

assoc_benefits_employee = Table('benefits_employee', Model.metadata,
                                  Column('id', Integer, primary_key=True),
                                  Column('benefit_id', Integer, ForeignKey('benefit.id')),
                                  Column('employee_id', Integer, ForeignKey('employee.id'))
)


def today():
    return datetime.datetime.today().strftime('%Y-%m-%d')


class EmployeeHistory(Model):
    id = Column(Integer, primary_key=True)
    department_id = Column(Integer, ForeignKey('department.id'), nullable=False)
    department = relationship("Department")
    employee_id = Column(Integer, ForeignKey('employee.id'), nullable=False)
    employee = relationship("Employee")
    begin_date = Column(Date, default=today)
    end_date = Column(Date)


class Employee(Model):
    id = Column(Integer, primary_key=True)
    full_name = Column(String(150), nullable=False)
    address = Column(Text(250), nullable=False)
    fiscal_number = Column(Integer, nullable=False)
    employee_number = Column(Integer, nullable=False)
    department_id = Column(Integer, ForeignKey('department.id'), nullable=False)
    department = relationship("Department")
    function_id = Column(Integer, ForeignKey('function.id'), nullable=False)
    function = relationship("Function")
    benefits = relationship('Benefit', secondary=assoc_benefits_employee, backref='employee')

    begin_date = Column(Date, default=datetime.date.today(), nullable=True)
    end_date = Column(Date, default=datetime.date.today(), nullable=True)

    def __repr__(self):
        return self.full_name