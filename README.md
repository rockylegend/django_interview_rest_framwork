Assignment Name: Django RestFramwork

Python - Django Assignment
Build APIs only for a Content Management System (Frontend not
required)
● The system will have 2 types of user role, admin and author. Admin users are created
using seeding
● Author should be able to register and login using email to the CMS (Refer below table for
user fields)
● Admin can view, edit and delete all the contents created by multiple authors
● Author can create, view, edit and delete contents created by him only
● Users should search content by matching terms in title, body, summary and categories.
(Refer below table for content item fields)


validation:
i have used filed based validation  for email and password as well as for content.

authentication:
Django User Modal Authentication

Api View:
i have Used generic ApiView for creating the restFramwork View, also i have used normal or deafualt ApiView of django-restframework.



Fileds used:

User fields
Content item fields
Field Validation Required
Email Std email validation yes
Password
Min 8 length, 1 uppercase, 1
lowercase yes
Full Name FirstName LastName yes
Phone Length 10, numeric yes
Address no
City no
State no
Country no
Pincode Length 6, numeric yes
