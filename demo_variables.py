#views
def views(data):
    print data, "FROM CONTROLLER"

#controllers
def controllers():

    #L. data_to_view - just a memory space
    #R. is a function that may or may not return anything...
    data_to_view = models("my_request")
    #1. invokes models
    #   a. in models request_from_controller = "my_request"
    #   b. prints out "my_request"
    #   c. sets results variable to database('data1')
    #   d. return results
    # data_to_view = results
    # but results is = database('data1')
    # therefore: data_to_view = database('data1')
    #2. invokes database
        #a. query = 'data1'
        #b. db_data = the dictionary in the function {.... : ....}
        #c. prints db_data[query]
            #i. prints db_data['data1']
            #ii. prints 'info from database, 1'
        #d. returns db_data[query]
    # data_to_view = db_data[query]
    # which is = 'info from database, 1'
    # therefore: data_to_view = 'info from database, 1'
    views(data_to_view)
    #3 Invoke views(data_to_view)
            #i. Really that means -> views('info from database, 1')
        #1 data = 'info from database, 1'
        #2 prints data
        #3 which means it prints 'info from database, 1'


#models
#def  - its a method
#models - just the name
#request_from_controller is the parameter (we can call this whatever we want)
#...When models called...(it gets called(invoked) by models(....) <-- parentheses matter)
#...When models called... 1) request_from_controller get set as memory space (ie. it becomes an L.) 2) that memory space is set to what was passed as (....) above. (e.g. models("my_request") --  request_from_controller = "my_request")
def models(request_from_controller):
    print request_from_controller
    results = database('data1')
    return results

#db
def database(query):
    db_data = {'data1': 'info from database, 1',
    'data2': 'info from database, 1',
    'data3': 'info from database, 1',
    'data4': 'info from database, 1',
    'data5': 'info from database, 1'}
    print db_data[query]
    return db_data[query]
#controllers invoked (run that function!)
controllers()
#1. invokes models
#   a. in models request_from_controller = "my_request"
#   b. prints out "my_request"
#   c. sets results variable to database('data1')
#   d. return results
# data_to_view = results
# but results is = database('data1')
# therefore: data_to_view = database('data1')
#2. invokes database
    #a. query = 'data1'
    #b. db_data = the dictionary in the function {.... : ....}
    #c. prints db_data[query]
        #i. prints db_data['data1']
        #ii. prints 'info from database, 1'
    #d. returns db_data[query]
# data_to_view = db_data[query]
# which is = 'info from database, 1'
# therefore: data_to_view = 'info from database, 1'
#views(data_to_view)
#3 Invoke views(data_to_view)
        #i. Really that means -> views('info from database, 1')
    #1 data = 'info from database, 1'
    #2 prints data
    #3 which means it prints 'info from database, 1'
