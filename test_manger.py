



#Service manger test case
if(True):
    try:
        from modules.service_manager import service_manager
        obj = service_manager()

        # Add service
        service_id = obj.add_service('test_name', 'test_type', 'test_address', 0, 0, 'test_email', 'test_phone_number')

        # Check if service is in DB
        service = obj.retrieve_service_by_id(service_id)
        if(service == None):
            raise Exception('Service was not added to DB!')

        # Delete the service
        obj.del_service(service_id)

        #Check if service was deleted
        service = obj.retrieve_service_by_id(service_id)
        if(service != None):
            raise Exception('Service was not deleted from DB!')



    except Exception as e:
        print(e)
        print('modules/service_manger.py has failed test case!')
