# Variables that are defined within a local scope are available in that local scope, and any scopes 
# nested within it. A global variable will only exist within a local scope if there's no variable 
# with the same name in the local scope. If a local variable has the same name as a global variable 
# the local variable will always take precedence.


name = "Mycroft"

def print_name_box():
    print(name)

    def smaller_box():
        # (Re)assigning a variable within a local scope
        # overwrites the same variable from an outer scope
        # You also can't use the global variable *before*
        # assigning it, if you assign it anywhere in that scope.

        # --TASK--: uncomment the print() function below
        #     and interpret the results when running the script

        # print(name)
        name = "Sherlock"

        def smallest_box():
            # Inner scopes always draw from the next-outer layer.
            # After `name` got overwritten, the name that will
            # be printed is NOT the global-scope name anymore
            print(name)

        smallest_box()

    smaller_box()

print_name_box()