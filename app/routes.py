from turtle import update
from django.urls import path
from app.Apis.api_controllers.bikeapi import BikeView
from app.Apis.api_controllers.bookapi import BookView
from app.Apis.api_controllers.carapi import CarView
from app.Apis.api_controllers.employeeapi import EmployeeView
from app.Apis.api_controllers.userapi import PersonView
from app.views.api_views.bike_api import delete_bike_data, get_bike_data, post_bike_data, update_bike_data
from app.views.api_views.book_api import delete_book_data, get_book_data, post_book_data, update_book_data
from app.views.api_views.car_api import delete_car_data, get_car_data, post_car_data, update_car_data
from app.views.api_views.employee_api import delete_employee_data, get_employee_data, post_employee_data, update_employee_data
from app.views.api_views.user_api import delete_api_data, get_api_data, post_api_data, update_api_data
from app.views.home import home
from app.views.bike import AddBike, BikeObject, DeleteBike, UpdateBike
from app.views.books import AddBook, BookObject, DeleteBook, UpdateBook
from app.views.car import AddCar, CarObject, DeleteCar, UpdateCar
from app.views.user import AddPerson, User, Delete, Update
from app.views.employee import AddEmployee, DeleteEmployee, EmpUser, UpdateEmployee
# from app.views.user import User

urlpatterns = [
    path('', home, name='base-page'),

# **********for User crud***********

    path("user/", User, name="user-page"),
    path("add/", AddPerson, name="add-page"),
    path("delete/<id>", Delete, name="delete-page"),
    path("update/<id>", Update, name="update-page"),

# ***************for Employee Crud**************

    path("employee/", EmpUser, name="employee-page"),
    path("addemployee/", AddEmployee, name="addemployee-page"),
    path("deleteemployee/<id>", DeleteEmployee, name="deleteemployee-page"),
    path("updateemployee/<id>", UpdateEmployee, name="updateemployee-page"),

# *****************for Car Crud***************
 
    path("car/", CarObject, name="car-page"),
    path("addcar/", AddCar, name="addcar-page"),
    path("deletecar/<id>", DeleteCar, name="deletecar-page"),
    path("updatecar/<id>", UpdateCar, name="updatecar-page"),

# *****************for Book Crud***************
    path("book/", BookObject, name="book-page"),
    path("addbook/", AddBook, name="addbook-page"),
    path("deletebook/<id>", DeleteBook, name="deletebook-page"),
    path("updatebook/<id>", UpdateBook, name="updatebook-page"),

# ********************for Bike Crud************
    path("bike/", BikeObject, name="bike-page"),
    path("addbike/", AddBike, name="addbike-page"),
    path("deletebike/<id>", DeleteBike, name="deletebike-page"),
    path("updatebike/<id>", UpdateBike, name="updatebike-page"),

]


# ?/********************Api urls*********************

urlpatterns += [
    
# # ********************User urls************
    path("api/user/list/", PersonView.as_view({ "get": "list", "post": "create"})),
    path("api/user/<int:pk>/", PersonView.as_view({"get":"retrieve", "put":"edit", "delete": "destroy"})),

# # ********************employee urls************
    path("api/employee/list/", EmployeeView.as_view({ "get": "list", "post": "create"})),
    path("api/employee/<int:pk>/", EmployeeView.as_view({"get":"retrieve", "put":"edit", "delete": "destroy"})),

# # ********************car urls************
    path("api/car/list/", CarView.as_view({ "get": "list", "post": "create"})),
    path("api/car/<int:pk>/", CarView.as_view({"get":"retrieve", "put":"edit", "delete": "destroy"})),

# # ********************books urls************
    path("api/book/list/", BookView.as_view({ "get": "list", "post": "create"})),
    path("api/book/<int:pk>/", BookView.as_view({"get":"retrieve", "put":"edit", "delete": "destroy"})),

# # ********************bike urls************
    path("api/bike/list/", BikeView.as_view({ "get": "list", "post": "create"})),
    path("api/bike/<int:pk>/", BikeView.as_view({"get":"retrieve", "put":"edit", "delete": "destroy"})),



# ?]********************Api Templates************

# todo:********************User Api Templates************
    path("api_user_data/", get_api_data, name="user_api_data"),
    path("api_add_User_data/", post_api_data, name="user_add_api_data"),
    path("api_delete_User_data/<int:id>/", delete_api_data, name="user_delete_api_data"),
    path("api_update_User_data/<int:id>/", update_api_data, name="user_update_api_data"),

# todo:********************employee Api Templates************
    path("api_employee_data/", get_employee_data, name="employee_api_data"),
    path("api_add_employee_data/", post_employee_data, name="employee_add_api_data"),
    path("api_delete_employee_data/<int:id>/", delete_employee_data, name="employee_delete_api_data"),
    path("api_update_employee_data/<int:id>/", update_employee_data, name="employee_update_api_data"),

# todo:********************Car Api Templates************
    path("api_car_data/", get_car_data, name="car_api_data"),
    path("api_add_car_data/", post_car_data, name="car_add_api_data"),
    path("api_delete_car_data/<int:id>/", delete_car_data, name="car_delete_api_data"),
    path("api_update_car_data/<int:id>/", update_car_data, name="car_update_api_data"),

# todo:********************books Api Templates***************
    path("api_book_data/", get_book_data, name="book_api_data"),
    path("api_add_book_data/", post_book_data, name="book_add_api_data"),
    path("api_delete_book_data/<int:id>/", delete_book_data, name="book_delete_api_data"),
    path("api_update_book_data/<int:id>/", update_book_data, name="book_update_api_data"),

# todo:********************bike Api Templates************
    path("api_bike_data/", get_bike_data, name="bike_api_data"),
    path("api_add_bike_data/", post_bike_data, name="bike_add_api_data"),
    path("api_delete_bike_data/<int:id>/", delete_bike_data, name="bike_delete_api_data"),
    path("api_update_bike_data/<int:id>/", update_bike_data, name="bike_update_api_data"),

]
  
    

