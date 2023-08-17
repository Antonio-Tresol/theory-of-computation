# Copyright: GNU General Public License
# Authors: 
# Antonio Badilla Olivas - B80874
# Gabriel Molina Bulgarelli - C14826
# Brandon Alonso Mora Umaña - C15179

class Record:
    """@brief: Record class to store the data of a record in the dataset
      @atribute start_date: is date of the record
      @atribute end_date: is the end date of the record
      @atribute region: is a string the region of the record
      @atribute num_visits: is the number of visits of the record
    """
    def __init__(self, start_date, end_date, region, num_visits):
        """@brief: Constructor of the class
          @param start_date: is date of the record
          @param end_date: is the end date of the record
          @param region: is a string the region of the record
          @param num_visits: is the number of visits of the record
        """
        self.start_date = start_date
        self.end_date = end_date
        self.region = region
        self.num_visits = num_visits
    # END CONSTRUCTOR

    def __str__(self):
        """@brief: Method to represent the object as a string"""
        return "-RECORD- \nstart_date: " + str(self.start_date) + " end_date: " + str(self.end_date) + " region: " + str(self.region) + " num_visits: " + str(self.num_visits)
    # END METHOD __str__
# END CLASS Record

class Site:
    """" @brief: Site class to store the data of a site in the dataset
      @atribute title: is a string with the title of the site
      @atribute url: is a string with the url of the site
      @atribute topics: is a np.array of topics of the site
      @atribute records: is a np.array of records of the site
    """
    def __init__(self, title, url, topics, records):
        """@brief: Constructor of the class
          @param title: is a string with the title of the site
          @param url: is string the url of the site
          @param topics: is a np.array of topics of the site
        @param records: is a np.array of records of the site
        """
        self.title = title
        self.topics = topics
        self.url = url
        self.records = records
    # END CONSTRUCTOR

    def __str__(self):
        """@brief: Method to represent the object as a string"""
        strSite = "\n-SITE- \ntitle: " + str(self.title) + " url: " + str(self.url) + " topics: " + str(self.topics)
        for record in self.records:
          strSite += "\n" + str(record)
        return strSite
  # END METHOD __str__
# END CLASS Site
