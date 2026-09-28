class LoggingMixin:
    def log(self, message):
        print(f"LOG: {message}")


class SaveMixin:
    def save(self):
        print("Saving data...")


class User(LoggingMixin, SaveMixin):
    def __init__(self, name):
        self.name = name


user = User("Nancin")

user.log("User logged in")
user.save()

"""
MIXIN PATTERN
it's a small class that adds a certain capability or function
to another class, without being meant to stand on it's own
Use Cases:

1. Logging
   Multiple classes in an application may need the ability
   to record messages or errors. A LoggingMixin can provide
   the same logging functionality to many different classes.

2. Saving Data
   Different objects may need the ability to save information.
   A SaveMixin can provide reusable save functionality without
   rewriting the same method in every class.

3. Authentication or Permissions
   Different classes may need to check whether a user has
   permission to perform an action. A PermissionMixin can add
   permission-checking behavior to those classes.


Benefits:

1. Code Reuse
   The same behavior can be added to several different classes
   without duplicating the code.

2. Separation of Responsibilities
   Each mixin can focus on one specific behavior, which keeps
   the main classes smaller and easier to understand.

3. Flexibility
   Classes can combine only the behaviors they need by inheriting
   from different mixins.
"""