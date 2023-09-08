class DependenciesEntityBaseClass:

    """ Use this object to store any dependencies. """

    def __init__(self):
        # REMOVED




class ScraperLogEntityBaseClass:

    NOT_NULLABLE = [
        # REMOVED
    ]

    def __init__(self, scraper_id):
        # REMOVED



class ValidatedEntityBaseClass:

    NOT_NULLABLE = [
        # REMOVED
    ]

    def __init__(self):
        # REMOVED



    def create_new_validated_entity(self):
        return ValidatedEntityBaseClass()