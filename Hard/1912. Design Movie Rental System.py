import bisect

class MovieRentingSystem(object):

    def __init__(self, n, entries):
        self.price_map = {}
        self.available = {}
        self.rented = []
        for shop, movie, price in entries:
            self.price_map[(shop, movie)] = price
            if movie not in self.available:
                self.available[movie] = []
            bisect.insort(self.available[movie], (price, shop))
        self.rented_set = set()

    def search(self, movie):
        res = []
        for price, shop in self.available.get(movie, []):
            if (shop, movie) not in self.rented_set:
                res.append(shop)
            if len(res) == 5:
                break
        return res

    def rent(self, shop, movie):
        self.rented_set.add((shop, movie))
        price = self.price_map[(shop, movie)]
        bisect.insort(self.rented, (price, shop, movie))

    def drop(self, shop, movie):
        self.rented_set.remove((shop, movie))
        price = self.price_map[(shop, movie)]
        idx = bisect.bisect_left(self.rented, (price, shop, movie))
        self.rented.pop(idx)

    def report(self):
        res = []
        for price, shop, movie in self.rented:
            if (shop, movie) in self.rented_set:
                res.append([shop, movie])
            if len(res) == 5:
                break
        return res
