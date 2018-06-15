import requests

class check_link():
    def __init__(self): 
        # generates bad responses from 400 to 409 and from 501 to 503
        self.bad_resp = list(range(399, 410)).append(range(500, 504))
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
            # this if statement means we save the iteration of the code
            if resp.status < self.bad_resp[-1] + 1 and resp.status > self.bad_resp[0] - 1:
                if resp.status in self.bad_resp:
                    print("HTTP" + resp.status_code + " found! At address " + address)   
                    # add the badlink to a dictionary of bad links
                    self.badLinks.update({resp.status_code : address})
                    return False
            else:
                return True

        except Exception as e:
            print ("{}{}".format(e, address))
            pass
