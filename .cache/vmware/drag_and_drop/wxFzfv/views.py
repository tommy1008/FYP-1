from flask import render_template, flash
from flask.ext.appbuilder.models.sqla.interface import SQLAInterface
from flask.ext.appbuilder import ModelView, MultipleView, MasterDetailView
from app import appbuilder, db
from flask_appbuilder import AppBuilder, expose, BaseView, has_access, SimpleFormView
from flask_babel import lazy_gettext as _
from flask_appbuilder.charts.views import DirectByChartView

from wtforms import Form, StringField
from wtforms.validators import DataRequired
from flask_appbuilder.fieldwidgets import BS3TextFieldWidget
from flask_appbuilder.forms import DynamicForm

from flask_appbuilder.widgets import ListThumbnail
from flask_appbuilder.actions import action
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from flask_appbuilder.fieldwidgets import BS3TextFieldWidget, Select2Widget
from flask_appbuilder import ModelView
from flask_appbuilder.fieldwidgets import Select2Widget
from flask_appbuilder.models.sqla.interface import SQLAInterface
from .models import Employee, Department, Function, EmployeeHistory, Benefit
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from app import appbuilder, db

from .models import MyUser, Feedback, Exchange, FAQ, Place, Country, Activities, Review, Rating, Contact, Hotel, Flight, \
    Company, Invoice, Ticket, Discount, Weather, Culture, Booking, FlightTicket, CateGory, ForumPlace, Post, Comment, \
    New, ShopHistory, LoginHistory, Themes, Blog, BlogCategory, Continent, Plan


def department_query():
    return db.session.query(Department)


class MyUserView(ModelView):
    datamodel = SQLAInterface(MyUser)


class FeedbackView(ModelView):
    datamodel = SQLAInterface(Feedback)


class ExchangeView(ModelView):
    datamodel = SQLAInterface(Exchange)


class FAQView(ModelView):
    datamodel = SQLAInterface(FAQ)


class PlaceView(ModelView):
    datamodel = SQLAInterface(Place)


class CountryView(ModelView):
    datamodel = SQLAInterface(Country)


class ActivitiesView(ModelView):
    datamodel = SQLAInterface(Activities)


class ReviewView(ModelView):
    datamodel = SQLAInterface(Review)


class RatingView(ModelView):
    datamodel = SQLAInterface(Rating)


class ContactView(ModelView):
    datamodel = SQLAInterface(Contact)


class HotelView(ModelView):
    datamodel = SQLAInterface(Hotel)


class FlightView(ModelView):
    datamodel = SQLAInterface(Flight)


class CompanyView(ModelView):
    datamodel = SQLAInterface(Company)


class InvoiceView(ModelView):
    datamodel = SQLAInterface(Invoice)


class TicketView(ModelView):
    datamodel = SQLAInterface(Ticket)


class DiscountView(ModelView):
    datamodel = SQLAInterface(Discount)


class WeatherView(ModelView):
    datamodel = SQLAInterface(Weather)


class CultureView(ModelView):
    datamodel = SQLAInterface(Culture)


class BookingView(ModelView):
    datamodel = SQLAInterface(Booking)


class FlightTicketView(ModelView):
    datamodel = SQLAInterface(FlightTicket)


class CateGoryView(ModelView):
    datamodel = SQLAInterface(CateGory)


class ForumPlaceView(ModelView):
    datamodel = SQLAInterface(ForumPlace)


class PostView(ModelView):
    datamodel = SQLAInterface(Post)


class CommentView(ModelView):
    datamodel = SQLAInterface(Comment)


class NewView(ModelView):
    datamodel = SQLAInterface(New)


class ShopHistoryView(ModelView):
    datamodel = SQLAInterface(ShopHistory)


class LoginHistoryView(ModelView):
    datamodel = SQLAInterface(LoginHistory)


class ThemesView(ModelView):
    datamodel = SQLAInterface(Themes)


class BlogView(ModelView):
    datamodel = SQLAInterface(Blog)


class BlogCategoryView(ModelView):
    datamodel = SQLAInterface(BlogCategory)


class ContinentVaiew(ModelView):
    datamodel = SQLAInterface(Continent)


class PlanView(ModelView):
    datamodel = SQLAInterface(Plan)


class EmployeeHistoryView(ModelView):
    datamodel = SQLAInterface(EmployeeHistory)
    # base_permissions = ['can_add', 'can_show']
    list_columns = ['department', 'begin_date', 'end_date']


class EmployeeView(ModelView):
    datamodel = SQLAInterface(Employee)

    list_columns = ['full_name', 'department.name', 'employee_number']
    edit_form_extra_fields = {'department': QuerySelectField('Department',
                                                             query_factory=department_query,
                                                             widget=Select2Widget(extra_classes="readonly"))}

    related_views = [EmployeeHistoryView]
    show_template = 'appbuilder/general/model/show_cascade.html'


class FunctionView(ModelView):
    datamodel = SQLAInterface(Function)
    related_views = [EmployeeView]


class DepartmentView(ModelView):
    datamodel = SQLAInterface(Department)
    related_views = [EmployeeView]


class BenefitView(ModelView):
    datamodel = SQLAInterface(Benefit)
    add_columns = ['name']
    edit_columns = ['name']
    show_columns = ['name']
    list_columns = ['name']


db.create_all()

appbuilder.add_view(MyUserView, "MyUser", icon="gear", category='Manage', )
appbuilder.add_view(FeedbackView, "Feedback", icon="gear", category='Manage', )
appbuilder.add_view(ExchangeView, "Exchange", icon="gear", category='Manage', )
appbuilder.add_view(FAQView, "FAQ", icon="gear", category='Manage', )
appbuilder.add_view(PlaceView, "Place", icon="gear", category='Manage', )
appbuilder.add_view(CountryView, "Country", icon="gear", category='Manage', )
appbuilder.add_view(ActivitiesView, "Activities", icon="gear", category='Manage', )
appbuilder.add_view(ReviewView, "Review", icon="gear", category='Manage', )
appbuilder.add_view(RatingView, "Rating", icon="gear", category='Manage', )
appbuilder.add_view(ContactView, "Contact", icon="gear", category='Manage', )
appbuilder.add_view(HotelView, "Hotel", icon="gear", category='Manage', )
appbuilder.add_view(FlightView, "Flight", icon="gear", category='Manage', )
appbuilder.add_view(CompanyView, "Company", icon="gear", category='Manage', )
appbuilder.add_view(InvoiceView, "Invoice", icon="gear", category='Manage', )
appbuilder.add_view(TicketView, "Ticket", icon="gear", category='Manage', )
appbuilder.add_view(DiscountView, "Discount", icon="gear", category='Manage', )
appbuilder.add_view(WeatherView, "Weather", icon="gear", category='Manage', )
appbuilder.add_view(CultureView, "Culture", icon="gear", category='Manage', )
appbuilder.add_view(BookingView, "Booking", icon="gear", category='Manage', )
appbuilder.add_view(FlightTicketView, "FlightTicket", icon="gear", category='Manage', )
appbuilder.add_view(CateGoryView, "CateGory", icon="gear", category='Manage', )
appbuilder.add_view(ForumPlaceView, "ForumPlace", icon="gear", category='Manage', )
appbuilder.add_view(PostView, "Post", icon="gear", category='Manage', )
appbuilder.add_view(CommentView, "Comment", icon="gear", category='Manage', )
appbuilder.add_view(NewView, "New", icon="gear", category='Manage', )
appbuilder.add_view(ShopHistoryView, "ShopHistory", icon="gear", category='Manage', )
appbuilder.add_view(LoginHistoryView, "LoginHistory", icon="gear", category='Manage', )
appbuilder.add_view(ThemesView, "Themes", icon="gear", category='Manage', )
appbuilder.add_view(BlogView, "Blog", icon="gear", category='Manage', )
appbuilder.add_view(BlogCategoryView, "BlogCategory", icon="gear", category='Manage', )
appbuilder.add_view(ContinentVaiew, "Continent", icon="gear", category='Manage', )
appbuilder.add_view(PlanView, "Plan", icon="gear", category='Manage', )

appbuilder.add_view(EmployeeView, "Employees", icon="gear", category="Manage")
appbuilder.add_view(DepartmentView, "Departments", icon="gear", category="Manage")
appbuilder.add_view(FunctionView, "Functions", icon="gear", category="Manage")
appbuilder.add_view(BenefitView, "Benefits", icon="gear", category="Manage")
