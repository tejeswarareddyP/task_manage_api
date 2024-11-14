from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)  # Registers routes for TaskViewSet

urlpatterns = [
    path('', include(router.urls)),  # Includes all routes from the router
]

'''
{"refresh":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTczMTY2MDYzNCwiaWF0IjoxNzMxNTc0MjM0LCJqdGkiOiI4OTZlMWEyOGMwYzc0NGEyYjU5ZTEyNTVjN2NiOTZiMSIsInVzZXJfaWQiOjF9.RT7xrzKDBdKQdO_tIsdaKMekfDfDbl8dnaNDkRY3r0g",
"access":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMxNTc3ODM0LCJpYXQiOjE3MzE1NzQyMzQsImp0aSI6IjkzODQ4YzQxN2I3MTRlYWM4YmJiYmMwNDQ4ZWMxZDg1IiwidXNlcl9pZCI6MX0.IkXSAOOb5McjWzxdJh7PxHfAz9F2zPEDq6VLUPNpOwE"}
'''