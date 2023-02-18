from mrjob.job import MRJob

class MovieLensRatingsCount(MRJob):
    def mapper(self, _, line):
        fields = line.split('::')
        rating = fields[2]
        yield rating, 1

    def reducer(self, rating, counts):
        yield rating, sum(counts)

if _name_ == '_main_':
    MovieLensRatingsCount.run()