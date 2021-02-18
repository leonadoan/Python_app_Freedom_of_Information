# Retrieve data from Stop & Search API
# https://data.police.uk/docs/
# Le Doan 25/11/2020


import requests
import StopAndSearch_DropBoxOption  # pylint: disable=F0401

# Create date list:
date_list_year = StopAndSearch_DropBoxOption.year_value[::-1]
date_list_month = StopAndSearch_DropBoxOption.month_value
date_list = []
for y in date_list_year:
    for m in date_list_month:
        date_list.append(y + '-' + m)


""" Create SnS class for an area in a given month """


class Stop_search_month:
    area = ''
    month = ''
    year = ''

    def __init__(self, year, month, area):
        self.year = year
        self.month = month
        self.area = area

    # Get area name:
    def get_area_name(self):
        return self.area

    # Get input month:
    def get_month(self):
        return self.month

    # Get input year:
    def get_year(self):
        return self.year

    # Get input date load:
    def date_load(self):
        return self.year + '-' + self.month

    # Replace None with N.I in dictionary counts:
    def changename_None(self, type, counts):
        try:
            x = counts[type]
            counts['No information'] = x
            del counts[type]
        except Exception:
            counts
        return counts

    # Check status retrieving data from the API, and load to data to json file
    def retrieve_data(self):
        area = self.area
        date_load = self.date_load()
        link = 'https://data.police.uk/api/stops-force?force='
        stop_query_request = requests.get(link + area + '&date=' + date_load)
        if stop_query_request.status_code == requests.codes.ok:
            self.stop_query_data = stop_query_request.json()

        return self.stop_query_data

    # Get number of SnS by age groups:
    def count_age_group(self):

        # Create age group in stop query data:
        stop_query_data = self.retrieve_data()
        age_range = []

        for stop in stop_query_data:
            age_range.append(stop['age_range'])

        # Count number in each age group:
        counts = dict()
        for i in age_range:
            counts[i] = counts.get(i, 0) + 1

        # Replace None with Undefined in dictionary counts:
        counts = self.changename_None(None, counts)
        return counts

    # Get number of SnS by gender:
    def gender_group(self):
        # Create gender list in stop query data:
        stop_query_data = self.retrieve_data()
        gender_list = []

        for stop in stop_query_data:
            gender_list.append(stop['gender'])

        # Count number in each gender group:
        counts = dict()
        for i in gender_list:
            counts[i] = counts.get(i, 0) + 1

        # Replace None with Undefined in dictionary counts:
        counts = self.changename_None(None, counts)
        return counts

    # Get number of SnS by ethnic groups:
    def ethnic_group(self):
        # Create ethnicity list in stop query data:
        stop_query_data = self.retrieve_data()
        ethnic_list = []

        for stop in stop_query_data:
            ethnic_list.append(stop['self_defined_ethnicity'])

        # Count number in each ethinic group:
        counts = dict()
        for i in ethnic_list:
            counts[i] = counts.get(i, 0) + 1

        # Replace None with Undefined in dictionary counts:
        counts = self.changename_None(None, counts)
        return counts

    # Get number of SnS by stop object groups:
    def object_of_search(self):
        # Create object of search list in stop query data:
        stop_query_data = self.retrieve_data()
        object_search_list = []

        for stop in stop_query_data:
            object_search_list.append(stop['object_of_search'])

        # Count number in each group:
        counts = dict()
        for i in object_search_list:
            counts[i] = counts.get(i, 0) + 1

        # Replace None with Undefined in dictionary counts:
        counts = self.changename_None(None, counts)
        return counts

    # Get number of SnS by outcome groups:
    def outcome(self):
        # Create result outcome list in stop query data:
        stop_query_data = self.retrieve_data()
        outcome_list = []

        for stop in stop_query_data:
            outcome_list.append(stop['outcome'])

        # Count number in each group:
        counts = dict()
        for i in outcome_list:
            counts[i] = counts.get(i, 0) + 1
        # Replace Blank with No Informationin dictionary counts:
        counts = self.changename_None('', counts)
        return counts


""" Create SnS class for an area in an given date """


class Stop_search_range:
    area = ''
    start_year = ''
    start_month = ''
    end_year = ''
    end_month = ''

    def __init__(self, start_year, start_month, end_year, end_month, area):

        self.start_year = start_year
        self.start_month = start_month
        self.end_year = end_year
        self.end_month = end_month
        self.area = area

    # Get area name:
    def get_area_name(self):
        return self.area

    # Get input start date:
    def get_start_date(self):
        return self.start_year + '-' + self.start_month

    # Get input end date:
    def get_end_date(self):
        return self.end_year + '-' + self.end_month

    # Loading the date ranged from start date to end date
    def date_load(self):
        date_start = self.start_year + '-' + self.start_month
        date_end = self.end_year + '-' + self.end_month
        index_start = date_list.index(date_start)
        index_end = date_list.index(date_end)

        self.date_query_load = [date_list[i] for i
                                in range(index_start, index_end + 1)]
        return self.date_query_load

    # Create list of request API link:
    def query_data(self):
        area = self.area
        date_query_load = self.date_load()
        self.stop_query_request_list = []

        for date_load in date_query_load:
            link = 'https://data.police.uk/api/stops-force?force='
            self.stop_query_request_list.append(requests.get(link + area
                                                             + '&date='
                                                             + date_load))
        return self.stop_query_request_list

    # Check status and retrieve data from the API
    def retrieve_data(self):
        stop_query_request_list = self.query_data()
        self.stop_query_data_list = []
        for stop_query_request in stop_query_request_list:
            if stop_query_request.status_code == requests.codes.ok:
                self.stop_query_data_list.append(stop_query_request.json())

        return self.stop_query_data_list

    # Calculate total stop and search in the chosen period:
    def total_stop_month(self):
        stop_query_data_list = self.retrieve_data()
        date_query_load = self.date_load()
        self.total_stop_by_month = dict()

        for i in range(len(date_query_load)):
            temp = len(stop_query_data_list[i])
            self.total_stop_by_month[date_query_load[i]] = temp
        return self.total_stop_by_month


# Main program
# stop_and_search_range('2019','01','2019','12')
if __name__ == "__main__":  # pragma: no cover
    check = Stop_search_month('2020', '06', 'cleveland')
    check.retrieve_data()
    print(check.count_age_group())

    # cleveland = Stop_search_range('2020', '03', '2020', '07', 'cleveland')
    # print(cleveland.retrieve_data())
    # print(cleveland.total_stop_month())
