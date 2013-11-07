def lookup(country, year):
    t = {'fo': ((2010, Faroe2010),)}
    try:
        for y, c in t[country][::-1]:
            if year >= y:
                return c
    except:
        pass
    raise(NotImplementedError)

class Faroe2010:
    def __init__(self):
        self.total_seats = 33
    def seats(self, votes):
        self.total_votes = sum(votes.values())
        self.abs_threshold = self.total_votes / self.total_seats
		
        # remove parties below threshold
        self.eligible = {p: v for p, v in votes.items() if v >= self.abs_threshold}
        self.eligible_votes = sum(self.eligible.values())
        
        self.quota = self.eligible_votes / self.total_seats
        self.seat_dist = {p: int(v / self.quota) for p, v in self.eligible.items()}
        self.remainder = {p: (v % self.quota) for p, v in self.eligible.items()}
        self.remaining = self.total_seats - sum(self.seat_dist.values())
        for p, r in sorted(self.remainder.items(), key=lambda x: x[1], reverse=True)[:self.remaining]:
            self.seat_dist[p] += 1
        return self.seat_dist
