our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

def destination_both(our_routes, competitor_routes):
    both = our_routes.intersection(competitor_routes)
    print (f"{both} are on our and our competitors routs")


def destination_unique(our_routes, competitor_routes):
    our_routes_only = our_routes.difference(competitor_routes)
    print(f"{our_routes_only} are our routes exclusivly")
    
def exclusive(our_routes, competitor_routes):
    exclusive_routes = our_routes.symmetric_difference(competitor_routes)
    print(f"{exclusive_routes} are the routes that are not shared between us and our competitor")


destination_both(our_routes,competitor_routes)
destination_unique(our_routes, competitor_routes)
exclusive(our_routes, competitor_routes)