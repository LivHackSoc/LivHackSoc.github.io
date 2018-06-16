import requests

class check_link():
    def __init__(self): 
        # generates bad responses from 400 to 409 and from 501 to 503
        self.bad_resp = list(range(400, 409)) + list(range(501, 504))
        self.badLinks = {}
    
    def __str__(self):
        # if this object is printed, print the dictionary
        return self.badLinks

    def check(self, address):   
        # method will check a link in an address
        # this method should be called with different addresses eachtime
        try:
            req = requests.get(address)
            resp = req.status_code
            if resp == 200:
                return True
            else:
                # it's possible to get HTTP 999: access denied
                # which isn't an error
                if resp in self.bad_resp:
                    self.badLinks.update({resp : address})
                    return resp
        except Exception as e:
            print ("{}{}".format(e, address))
            pass
