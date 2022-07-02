# Each Python session that you start, for example by running a script or an interpreter session, has 
# a global scope.

# Any variable that you define in the global scope is accessible within any of the inner scopes you 
# might create in that session.

# Even a function within a function within a function (etc.) can still use a variable that has been 
# defined in the global scope without needing to pass it as an argument. Nested scopes have access to 
# anything defined in their outer scopes:

name = "Mycroft"

def print_name_box():
    print(name)

    def smaller_box():
        print(name)

        def smallest_box():
            print(name)

        smallest_box()

    smaller_box()

print_name_box()
